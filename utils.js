const fs = require("fs");

// Function to save data
function saveToFile(filename, data) {
  fs.writeFileSync(`./output/${filename}.json`, JSON.stringify(data, null, 2));
  console.log(`✅ Data saved to output/${filename}.json`);
}

module.exports = { saveToFile };
