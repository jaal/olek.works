import 'astro/jsx-runtime';

export function postsAndTags(allPosts) {
  const posts = sortedPosts(allPosts);
  const tags = postTags(posts);
  return { allPosts: posts, allTags: tags };
}

function sortedPosts(allPosts) {
  const now = new Date();

  // Filter out posts with future dates (for scheduled publishing)
  allPosts = allPosts.filter((post) => {
    const postDate = new Date(post.frontmatter.added.replace(/-/g, '/'));
    return postDate <= now;
  });

  allPosts = allPosts.sort((a, b) => {
    return new Date(b.frontmatter.added) - new Date(a.frontmatter.added);
  });
  return allPosts;
}

function postTags(posts) {
  return posts.reduce((allTags, post) => {
    const postTags = post.frontmatter.tags;
    if (postTags) {
      postTags.forEach((tag) => {
        if (!allTags[tag]) {
          allTags[tag] = [];
        }
        allTags[tag].push(post);
      });
    }
    return allTags;
  }, {});
}
