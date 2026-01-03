<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atom="http://www.w3.org/2005/Atom">
<xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<xsl:variable name="title"><xsl:value-of select="/rss/channel/title"/></xsl:variable>
<xsl:variable name="description"><xsl:value-of select="/rss/channel/description"/></xsl:variable>
<xsl:variable name="link"><xsl:value-of select="/rss/channel/link"/></xsl:variable>
<html class="scroll-smooth">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title><xsl:value-of select="$title"/></title>
<style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;color:#1a202c;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);min-height:100vh;padding:20px}@media(max-width:640px){body{padding:10px}}.container{max-width:900px;margin:0 auto;background:#fff;border-radius:12px;box-shadow:0 20px 60px rgba(0,0,0,.3);overflow:hidden}.header{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff;padding:40px 30px;text-align:center}.header h1{margin:0 0 10px;font-size:32px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:10px}.rss-icon{width:32px;height:32px;fill:currentColor}.header p{margin:0 0 20px;font-size:16px;opacity:.95}.header .btn{display:inline-block;color:#fff;text-decoration:none;padding:12px 24px;border:2px solid #fff;border-radius:8px;font-weight:600;transition:all .3s ease}.header .btn:hover{background:#fff;color:#667eea}.info-box{background:#f7fafc;border-left:4px solid #667eea;padding:24px 30px;margin:30px;border-radius:8px}.info-box h2{margin:0 0 12px;font-size:20px;color:#2d3748}.info-box p{margin:0 0 12px;color:#4a5568;line-height:1.7}.info-box a{color:#667eea;font-weight:600;text-decoration:none}.info-box a:hover{text-decoration:underline}.subscribe-btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:15px}@media(max-width:640px){.subscribe-btns{flex-direction:column}}.subscribe-btn{display:inline-block;padding:10px 18px;background:#fff;border:1px solid #cbd5e0;border-radius:6px;color:#4a5568;text-decoration:none;font-size:14px;font-weight:500;transition:all .2s ease;text-align:center}.subscribe-btn:hover{background:#667eea;color:#fff;border-color:#667eea}.content{padding:30px}@media(max-width:640px){.content,.info-box{padding:20px}}.content>h2{margin:0 0 30px;font-size:26px;color:#2d3748;border-bottom:3px solid #667eea;padding-bottom:12px}.post{margin-bottom:40px;padding-bottom:40px;border-bottom:1px solid #e2e8f0}.post:last-child{border-bottom:none}.post h3{margin:0 0 10px;font-size:24px;line-height:1.4}.post h3 a{color:#2d3748;text-decoration:none;transition:color .2s}.post h3 a:hover{color:#667eea}.post-meta{color:#718096;font-size:14px;margin-bottom:12px}.post-tags{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}.tag{display:inline-block;padding:5px 14px;background:#edf2f7;color:#4a5568;border-radius:16px;font-size:13px;font-weight:500}.post-desc{color:#4a5568;line-height:1.7;margin-top:12px}.post-desc p{margin:0 0 12px}.post-desc h1,.post-desc h2,.post-desc h3{color:#2d3748;margin:20px 0 10px;font-weight:600}.post-desc a{color:#667eea;text-decoration:none}.post-desc a:hover{text-decoration:underline}.post-desc img{max-width:100%;height:auto;border-radius:8px;margin:15px 0;box-shadow:0 4px 6px rgba(0,0,0,.1)}.post-desc ul,.post-desc ol{margin:12px 0;padding-left:25px}.post-desc code{background:#edf2f7;padding:2px 6px;border-radius:3px;font-size:.9em;font-family:Consolas,Monaco,monospace;color:#d73a49}.post-desc pre{background:#2d3748;color:#e2e8f0;padding:16px;border-radius:6px;overflow-x:auto;margin:15px 0}.post-desc blockquote{border-left:4px solid #667eea;padding-left:20px;margin:15px 0;color:#4a5568;font-style:italic}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>
<svg class="rss-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
<path d="M6.18 15.64a2.18 2.18 0 0 1 2.18 2.18C8.36 19 7.38 20 6.18 20C5 20 4 19 4 17.82a2.18 2.18 0 0 1 2.18-2.18M4 4.44A15.56 15.56 0 0 1 19.56 20h-2.83A12.73 12.73 0 0 0 4 7.27V4.44m0 5.66a9.9 9.9 0 0 1 9.9 9.9h-2.83A7.07 7.07 0 0 0 4 12.93V10.1z"/>
</svg>
<xsl:value-of select="$title"/>
</h1>
<p><xsl:value-of select="$description"/></p>
<a class="btn" href="{$link}" target="_blank" rel="noopener noreferrer">Visit Website →</a>
</div>

<div class="info-box">
<h2>📡 What is this?</h2>
<p>This is an <strong>RSS feed</strong>. Subscribe to get new posts delivered automatically to your RSS reader app.</p>
<p>New to RSS? <a href="https://aboutfeeds.com/" target="_blank">Learn more about RSS feeds</a></p>
<strong>Subscribe with:</strong>
<div class="subscribe-btns">
<a class="subscribe-btn" href="https://feedly.com/i/subscription/feed/{/rss/channel/atom:link[@rel='self']/@href}" target="_blank">Feedly</a>
<a class="subscribe-btn" href="https://www.inoreader.com/feed/{/rss/channel/atom:link[@rel='self']/@href}" target="_blank">Inoreader</a>
<a class="subscribe-btn" href="https://feedbin.com/?subscribe={/rss/channel/atom:link[@rel='self']/@href}" target="_blank">Feedbin</a>
</div>
</div>

<div class="content">
<h2>Recent Posts</h2>
<xsl:for-each select="/rss/channel/item">
<article class="post">
<h3>
<a href="{link}" target="_blank" rel="noopener noreferrer">
<xsl:value-of select="title"/>
</a>
</h3>
<div class="post-meta">
Published: <xsl:value-of select="pubDate"/>
</div>
<xsl:if test="category">
<div class="post-tags">
<xsl:for-each select="category">
<span class="tag"><xsl:value-of select="."/></span>
</xsl:for-each>
</div>
</xsl:if>
<div class="post-desc">
<xsl:value-of select="description" disable-output-escaping="yes"/>
</div>
</article>
</xsl:for-each>
</div>
</div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
