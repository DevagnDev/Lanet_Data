const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const urlLib = require("url"); // Used to resolve relative URLs

const app = express();
const port = process.env.PORT || 3000;

async function scrapeWebsite(targetUrl) {
    try {
        console.log(`🔍 Fetching data from: ${targetUrl}`);

        // Fetch the HTML from the target website
        const { data } = await axios.get(targetUrl, {
            headers: { "User-Agent": "Mozilla/5.0" },
        });

        // Load HTML into Cheerio
        const $ = cheerio.load(data);

        // Get the base URL from the provided target URL
        const baseUrl = new URL(targetUrl).origin;

        // For <link> tags:
        $("link[href]").each((_, el) => {
            let href = $(el).attr("href");
            if (href && !href.startsWith("http")) {
                $(el).attr("href", urlLib.resolve(baseUrl, href));
            }
        });

        // For <script> tags:
        $("script[src]").each((_, el) => {
            let src = $(el).attr("src");
            if (src && !src.startsWith("http")) {
                $(el).attr("src", urlLib.resolve(baseUrl, src));
            }
        });

        // For <img> tags:
        $("img[src]").each((_, el) => {
            let src = $(el).attr("src");
            if (src && !src.startsWith("http")) {
                $(el).attr("src", urlLib.resolve(baseUrl, src));
            }
        });

        // For <a> tags (buttons or links):
        $("a[href]").each((_, el) => {
            let href = $(el).attr("href");
            if (href && !href.startsWith("http")) {
                $(el).attr("href", urlLib.resolve(baseUrl, href));
            }
            // Optional: open all links in a new tab
            $(el).attr("target", "_blank");
        });

        // Remove unwanted elements:
        $("form.flex,section#chart,section#peers,section#analysis, section#documents, footer, nav, div.flex-row div h2, p.sub").remove();
        $("button.a,button.button-secondary").remove();
        $("div.flex.text-align-center, div.company-ratios,div.flex.flex-gap-8,div.sub-nav-holder").remove();
        // Return the modified HTML
        return $.html();
    } catch (error) {
        console.error("❌ Error scraping website:", error.message);
        return null;
    }
}

app.get("/scrape", async (req, res) => {
    const url = req.query.url;
    if (!url) {
        return res.status(400).json({ error: "Please provide a valid URL using ?url=YOUR_URL" });
    }

    const modifiedHtml = await scrapeWebsite(url);
    if (!modifiedHtml) {
        return res.status(500).json({ error: "Failed to scrape website." });
    }

    // Send the modified HTML as the response.
    res.send(modifiedHtml);
});

app.listen(port, () => {
    console.log(`🚀 Server running at http://localhost:${port}`);
});
