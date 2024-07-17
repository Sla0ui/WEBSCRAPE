# WEBSCRAPE

<img width="960" alt="Web Links Scraper Screenshot" src="https://github.com/Sla0ui/WEBSCRAPE/assets/136838832/25b13a56-87e4-4752-86b0-8ec6b0f59c66">

## Web Links Scraper

This Python script allows you to scrape web links from a specified domain using the Wayback Machine's web archive (Archive.org). It utilizes the Selenium library to interact with a web browser and retrieve the links.

### Features:
- Scrape links from the specified domain within the Wayback Machine's web archive.
- Supports scraping multiple pages.
- Provides options to sort the results based on the date of capture.
- Filters out duplicate and irrelevant links.
- Writes the scraped links to a text file.
- Option to save links as archived versions from the Wayback Machine or as original URLs.

### Usage:
1. **Enter the domain** for which you want to scrape links.
2. **Specify the number of pages** to scrape (maximum of 200).
3. **Choose the sorting order** for the results.
4. **Choose the link format**: 
   - Save as archived versions from the Wayback Machine.
   - Save as original URLs.
5. The script will launch a headless Chrome browser and start scraping the links.
6. The scraped links will be saved in the `Scraped_output.txt` file.

### Optimizations and Improvements:
- Implemented explicit waits to ensure elements are loaded before interacting with them.
- Used URL parsing and manipulation functions for cleaner link handling.
- Added colorama library for colorful console output.
- Improved filtering of links to exclude irrelevant and duplicate entries.

### Requirements:
- Selenium
- colorama
- progress
- Chrome WebDriver

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/Sla0ui/WEBSCRAPE.git
   cd WEBSCRAPE
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and install the [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your version of Chrome.

### Running the Script:
1. Execute the script:
   ```bash
   python3 WebScrape.py
   ```
2. Follow the on-screen prompts to input the domain, number of pages, sorting order, and link format.


### Author:
[Sla0ui](https://github.com/Sla0ui)
```

### Additional Notes:
- Make sure to include a `requirements.txt` file with the necessary libraries (Selenium, colorama, progress).
- You may want to update the script filename (`WebScrape.py` in this example) if your script has a different name.
