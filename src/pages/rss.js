import rss from '@astrojs/rss';
import * as marked from 'marked';

const postImportResult = import.meta.globEager('../notes/**/*.md');
const posts = Object.values(postImportResult);

const postsWithContent = await Promise.all(
  posts.map(async (post) => {
    let rawContent = await post.rawContent();

    const titleEncoded = encodeURIComponent(`re: ${post.frontmatter.title}`);
    const tweetTextEncoded = encodeURIComponent(
      `re: https://olekwrites.com/${post.frontmatter.slug}`
    );

    let html = marked.parse(rawContent);

    html += `
      <hr />
      <p>Thanks for reading this post via RSS! Let me know your thoughts by sending <a href="mailto:hi@olekwrites.com?subject=${titleEncoded}">me an email</a>.</p>
      `;

    return {
      ...post,
      htmlContent: html,
    };
  })
);

postsWithContent.sort((a, b) => {
  return new Date(b.frontmatter.added) - new Date(a.frontmatter.added);
});

const postsToRender = postsWithContent.slice(0, 20);

export const get = () =>
  rss({
    title: "My name is Olek. I write what matters to me.",
    description:
      "Hi 👋🏼 I'm Olek. Here I write about what matters to me. I'm a co-founder of 2 kids 👨‍👩, married happily 💍, and 🍕 lover.",
    site: import.meta.env.SITE,
    stylesheet: '/pretty-feed-v3.xsl',
    items: postsToRender.map((post, i) => {
      const categoryTags = post.frontmatter.tags
        .map((tag) => `<category><![CDATA[${tag}]]></category>`)
        .join('');
      return {
        link: post.frontmatter.slug,
        title: post.frontmatter.title,
        pubDate: post.frontmatter.added,
        description: post.htmlContent,
        customData: categoryTags,
      };
    }),
    customData: `<atom:link href="https://olekwrites.com/rss" rel="self" type="application/rss+xml" />`,
    xmlns: {
      atom: 'http://www.w3.org/2005/Atom',
    },
  });
