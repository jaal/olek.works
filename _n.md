# Blog Post Creation Instructions

## Step 1: Create Blog Post

I want to create a new blogpost. Take into consideration the structure of the previous blogpost. Suggest slug, title, tags, keywords, and SEO optimization.

**Requirements:**

- Check from the gramma and syntax perspective; suggest improvements
- Analyze previous blog posts in `src/notes/` for structure and format
- Suggest multiple options for slug, title, and excerpt
- Provide SEO optimization suggestions
- Include appropriate tags
- Keep the conversational writing style
- Add clear section structure
- Include practical takeaways
- Remember to set up "added" and "updated" for the next day, at 06:00AM
- Add 1-4 tags based on the current list of tags

**Here's the text:**
[CONTENT]

## Step 2: Generate Pixel Art Image

After the blog post is created, generate a ChatGPT prompt for a pixel art cover image:

**Image Style Requirements:**

- Pixel art style 8-bit retro illustration
- Simple clean design
- Similar to retro video game graphics
- Visual metaphor related to the blog post topic

**Example prompt format:**

```
Pixel art style 8-bit retro illustration of [CONTENT], simple clean design, similar to retro video game graphics
```

## File Structure

Blog posts should follow this frontmatter format:

```markdown
---
title: 'Blog Post Title'
slug: url-slug
added: YYYY-MM-DD HH:MM
updated: YYYY-MM-DD HH:MM
tags: [en, tag1, tag2, tag3]
excerpt: Brief description under 160 characters for SEO
note: publish
---

![Image description](/images/image-name.png)

# Blog Post Title

[Content here]
```

## Scheduled Publishing

To schedule a post for future publishing:

- Set the `added` field to a future date and time
- Commit and push the post now
- The post will remain hidden until the scheduled date
- Daily automated builds will make it visible once the date arrives
