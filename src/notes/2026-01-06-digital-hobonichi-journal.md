---
title: 'I Built a Digital Version of My Favorite 5-Year Journal'
slug: digital-hobonichi-journal
added: 2026-01-06 00:00
updated: 2026-01-06 00:00
tags: [projects, technology, writing]
excerpt: I love the Hobonichi 5-Year book but wanted it digital. Here's how I created a version for Notesnook that you can use too.
note: publish
---

![Pixel art illustration of a 5-year calendar journal transitioning from paper to digital](/images/digital-hobonichi.png)

# I Built a Digital Version of My Favorite 5-Year Journal

I'm a big fan of two things: [Notesnook](https://notesnook.com/) for private, encrypted note-taking, and the Hobonichi 5-Year Techo—a brilliant paper journal where you see the same date across five years on one page.

The problem? I wanted both. I wanted the format of the Hobonichi, but in Notesnook.

So I built it.

## What Is the Hobonichi 5-Year Book?

If you've never seen a [Hobonichi 5-Year Techo](https://www.1101.com/store/techo/en/5year/), here's the concept:

Each page shows one date across five consecutive years. January 1st has five rows—one for each year. You write a brief entry for that day, and next year, when you open to January 1st again, you see what you wrote last year. And the year before. And the year before that.

It's a simple idea that creates something powerful: **you can see your life in patterns.**

You notice how you felt on your birthday across multiple years. You see seasonal patterns in your mood. You track changes in what matters to you.

It's not just a journal. It's a time machine.

## Why Digital?

I love paper journals. But I also love:

- **Searchability**: finding what I wrote about something specific
- **Backup**: never losing years of entries
- **Privacy**: encrypted, synced across devices
- **Accessibility**: writing from anywhere without carrying a physical book

Notesnook gives me all of that. But there was no 5-year journal template for it.

So I created one.

## How It Works

I wrote a Python script that generates a complete 5-year journal as a single markdown file.

The file includes:

- **366 daily entries** (including Feb 29 for leap years)
- Each date shows **five years** with space to write
- **Automatic day-of-week calculation** for every year
- A **memo section** for each day
- Bonus sections: yearly overview, lists, favorite things tracker, gift log, personal notes

You import it into Notesnook, and you have a complete 5-year journal ready to use.

## The Structure

Each day looks like this:

```markdown
### January 1

**2026** (Wednesday)

[Your writing space]

**2027** (Friday)

[Your writing space]

... (continues for all 5 years)

**Memo**

[Extra notes for this date]
```

Simple. Clean. Functional.

## Why I Made This

Because I wanted it. And if I wanted it, maybe someone else does too.

The Hobonichi 5-Year book costs around $40–50, and you have to buy a new one when it's full. This digital version is free, customizable, and lasts forever.

You can generate it for any 5-year period. Starting in 2025? Done. Want 2030–2034? Easy. The script handles it.

And because it's just a markdown file, it works with Notesnook, Obsidian, or any markdown-compatible app.

## How You Can Use It

Two options:

**Option 1: Use the pre-generated file**
1. Download the [2026-2030 journal file](https://github.com/jaal/hobonichi-digital-journal)
2. Import it into Notesnook (Settings → Notesnook Importer)
3. Start writing

**Option 2: Generate your own**
1. Download the Python script from [the repository](https://github.com/jaal/hobonichi-digital-journal)
2. Run it with your preferred start year
3. Import the generated file into your app

That's it.

## What I Learned

Building this took about an hour. But the process taught me something valuable:

**If you want a tool that doesn't exist, you can build it.**

I didn't need to wait for someone else to create a digital Hobonichi template. I didn't need to compromise with half-solutions. I just made exactly what I wanted.

Here's the honest part: I created this entire project using [Claude Code](https://claude.com/claude-code) through a series of prompts. I described what I wanted, asked for adjustments when something wasn't quite right, and Claude Code handled the Python scripting, file generation, documentation, and even the Git repository setup.

I didn't write the code myself. I didn't need to. I just needed to know what problem I was solving and communicate it clearly.

The script handles leap years, calculates days of the week for every date, and generates 69,000 characters of structured markdown automatically. Once it was done, I had a tool I'll use for the next five years.

## The Repository

I made this open source under the MIT License. That means you can:

- Use it for free
- Modify it however you want
- Share it with others
- Generate journals for any year range
- Adapt it for other apps

Everything you need is in the [GitHub repository](https://github.com/jaal/hobonichi-digital-journal):
- The Python script
- A pre-generated 2026-2030 journal
- Full documentation
- Development log (if you're curious about the process)

## Try It For Yourself

If you're a Notesnook user, or if you use any markdown app, this might be exactly what you've been looking for.

If you love the idea of seeing your life across multiple years on one page, this gives you that—with all the benefits of digital note-taking.

And if you've ever wished a tool existed but couldn't find it, maybe this will inspire you to build it yourself.

---

**Using Notesnook or another markdown app?** I'd love to hear how this works for you.

---

**Resources:**
- [Hobonichi Digital Journal - GitHub Repository](https://github.com/jaal/hobonichi-digital-journal)
- [Notesnook - Private Note-Taking](https://notesnook.com/)
- [Hobonichi 5-Year Techo Official](https://www.1101.com/store/techo/en/5year/)
