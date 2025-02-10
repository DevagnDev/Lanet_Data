const axios = require("axios");
const cheerio = require("cheerio");
const fs = require("fs");
const chalk = require("chalk");

async function scrapeWebsite(url) {
  try {
    console.log(chalk.blue(`Fetching data from ${url}...`));
    
    // Fetch the HTML from the website
    const { data } = await axios.get(url, {
      headers: { "User-Agent": "Mozilla/5.0" } // Prevent blocking
    });

    const $ = cheerio.load(data);
    const fullData = $.html(); // This returns the entire parsed HTML

    fs.writeFileSync("./output/scrapedData.json", JSON.stringify({ html: fullData }, null, 2));
    
    console.log(chalk.green("✅ Data successfully scraped and saved!"));
    return fullData;
  } catch (error) {
    console.error(chalk.red("❌ Error scraping website:", error.message));
    return null;
  }
}

module.exports = { scrapeWebsite };
