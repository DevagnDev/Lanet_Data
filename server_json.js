const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");

const app = express();
const port = 3000;

app.get("/scrape", async (req, res) => {
  // Get the URL from query parameters
  const { url } = req.query;
  if (!url) {
    return res
      .status(400)
      .json({ error: 'The "url" query parameter is required.' });
  }

  try {
     const response = await axios.get(url);
    const html = response.data;
    const $ = cheerio.load(html);

   $(".chart").remove();

    let companyName = $("h1").first().text().trim() || "Not found";

    let currentPrice = "Not found";
    $("*").each((i, el) => {
      const text = $(el).text().trim();
      if (text.includes("₹") && /\d/.test(text)) {
        currentPrice = text;
        return false; // break out of loop once found
      }
    });

    // Get the cleaned HTML (with chart elements removed)
    const cleanedHtml = $.html();

    // Return the scraped data as JSON
    res.json({
      company_name: companyName,
      current_price: currentPrice,
      cleaned_html: cleanedHtml,
    });
  } catch (error) {
    res
      .status(500)
      .json({ error: `Failed to fetch or process page: ${error.toString()}` });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
