<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:atom="http://www.w3.org/2005/Atom"
                xmlns:dc="http://purl.org/dc/elements/1.1/">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
      <head>
        <title><xsl:value-of select="/rss/channel/title"/> - RSS Feed</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
        <style type="text/css">
          * {
            box-sizing: border-box;
          }

          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #1a202c;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
          }

          .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
          }

          .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
          }

          .header h1 {
            margin: 0 0 10px 0;
            font-size: 28px;
            font-weight: 700;
          }

          .header p {
            margin: 0 0 20px 0;
            font-size: 16px;
            opacity: 0.95;
          }

          .header a {
            display: inline-block;
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border: 2px solid white;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s ease;
          }

          .header a:hover {
            background: white;
            color: #667eea;
          }

          .info-box {
            background: #f7fafc;
            border-left: 4px solid #667eea;
            padding: 20px 30px;
            margin: 30px;
            border-radius: 6px;
          }

          .info-box h2 {
            margin: 0 0 10px 0;
            font-size: 18px;
            color: #2d3748;
          }

          .info-box p {
            margin: 0 0 15px 0;
            color: #4a5568;
          }

          .info-box a {
            color: #667eea;
            font-weight: 600;
            text-decoration: none;
          }

          .info-box a:hover {
            text-decoration: underline;
          }

          .subscribe-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
          }

          .subscribe-btn {
            display: inline-block;
            padding: 8px 16px;
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            color: #4a5568;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.2s ease;
          }

          .subscribe-btn:hover {
            background: #667eea;
            color: white;
            border-color: #667eea;
          }

          .content {
            padding: 30px;
          }

          .content h2 {
            margin: 0 0 25px 0;
            font-size: 24px;
            color: #2d3748;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 10px;
          }

          .post {
            margin-bottom: 40px;
            padding-bottom: 40px;
            border-bottom: 1px solid #e2e8f0;
          }

          .post:last-child {
            border-bottom: none;
          }

          .post h3 {
            margin: 0 0 8px 0;
            font-size: 22px;
            line-height: 1.4;
          }

          .post h3 a {
            color: #2d3748;
            text-decoration: none;
            transition: color 0.2s ease;
          }

          .post h3 a:hover {
            color: #667eea;
          }

          .post-meta {
            color: #718096;
            font-size: 14px;
            margin-bottom: 12px;
          }

          .post-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 12px 0;
          }

          .tag {
            display: inline-block;
            padding: 4px 12px;
            background: #edf2f7;
            color: #4a5568;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 500;
          }

          .post-description {
            color: #4a5568;
            line-height: 1.7;
          }

          .post-description p {
            margin: 0 0 12px 0;
          }

          .post-description h1,
          .post-description h2,
          .post-description h3 {
            color: #2d3748;
            margin: 20px 0 10px 0;
          }

          .post-description a {
            color: #667eea;
            text-decoration: none;
          }

          .post-description a:hover {
            text-decoration: underline;
          }

          .post-description img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 15px 0;
          }

          .post-description ul,
          .post-description ol {
            margin: 12px 0;
            padding-left: 25px;
          }

          .post-description code {
            background: #edf2f7;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.9em;
            font-family: 'Consolas', 'Monaco', monospace;
          }

          .post-description pre {
            background: #2d3748;
            color: #e2e8f0;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 15px 0;
          }

          .post-description blockquote {
            border-left: 4px solid #667eea;
            padding-left: 20px;
            margin: 15px 0;
            color: #4a5568;
            font-style: italic;
          }

          .rss-icon {
            width: 24px;
            height: 24px;
            display: inline-block;
            vertical-align: middle;
            margin-right: 8px;
          }

          @media (max-width: 640px) {
            body {
              padding: 10px;
            }

            .header {
              padding: 30px 20px;
            }

            .header h1 {
              font-size: 24px;
            }

            .info-box,
            .content {
              padding: 20px;
            }

            .subscribe-buttons {
              flex-direction: column;
            }

            .subscribe-btn {
              text-align: center;
            }

            .post h3 {
              font-size: 20px;
            }
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <h1>
              <svg class="rss-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path d="M6.18 15.64a2.18 2.18 0 0 1 2.18 2.18C8.36 19 7.38 20 6.18 20C5 20 4 19 4 17.82a2.18 2.18 0 0 1 2.18-2.18M4 4.44A15.56 15.56 0 0 1 19.56 20h-2.83A12.73 12.73 0 0 0 4 7.27V4.44m0 5.66a9.9 9.9 0 0 1 9.9 9.9h-2.83A7.07 7.07 0 0 0 4 12.93V10.1z"/>
              </svg>
              <xsl:value-of select="/rss/channel/title"/>
            </h1>
            <p><xsl:value-of select="/rss/channel/description"/></p>
            <a>
              <xsl:attribute name="href">
                <xsl:value-of select="/rss/channel/link"/>
              </xsl:attribute>
              Visit Website →
            </a>
          </div>

          <div class="info-box">
            <h2>📡 What is this?</h2>
            <p>This is an <strong>RSS feed</strong> - a way to follow this blog without visiting the website. When new posts are published, they'll automatically appear in your RSS reader.</p>
            <p>New to RSS? <a href="https://aboutfeeds.com/" target="_blank">Learn more about RSS feeds</a></p>

            <strong>Subscribe with:</strong>
            <div class="subscribe-buttons">
              <a class="subscribe-btn" target="_blank">
                <xsl:attribute name="href">
                  <xsl:text>https://feedly.com/i/subscription/feed/</xsl:text>
                  <xsl:value-of select="/rss/channel/atom:link[@rel='self']/@href"/>
                </xsl:attribute>
                Feedly
              </a>
              <a class="subscribe-btn" target="_blank">
                <xsl:attribute name="href">
                  <xsl:text>https://www.inoreader.com/feed/</xsl:text>
                  <xsl:value-of select="/rss/channel/atom:link[@rel='self']/@href"/>
                </xsl:attribute>
                Inoreader
              </a>
              <a class="subscribe-btn" target="_blank">
                <xsl:attribute name="href">
                  <xsl:text>https://feedbin.com/?subscribe=</xsl:text>
                  <xsl:value-of select="/rss/channel/atom:link[@rel='self']/@href"/>
                </xsl:attribute>
                Feedbin
              </a>
              <a class="subscribe-btn" target="_blank">
                <xsl:attribute name="href">
                  <xsl:value-of select="/rss/channel/atom:link[@rel='self']/@href"/>
                </xsl:attribute>
                Copy URL
              </a>
            </div>
          </div>

          <div class="content">
            <h2>Recent Posts</h2>
            <xsl:for-each select="/rss/channel/item">
              <article class="post">
                <h3>
                  <a target="_blank">
                    <xsl:attribute name="href">
                      <xsl:value-of select="link"/>
                    </xsl:attribute>
                    <xsl:value-of select="title"/>
                  </a>
                </h3>
                <div class="post-meta">
                  Published: <xsl:value-of select="pubDate"/>
                </div>

                <xsl:if test="category">
                  <div class="post-tags">
                    <xsl:for-each select="category">
                      <span class="tag">
                        <xsl:value-of select="."/>
                      </span>
                    </xsl:for-each>
                  </div>
                </xsl:if>

                <div class="post-description">
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
