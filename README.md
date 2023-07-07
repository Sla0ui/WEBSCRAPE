# WEBSCRAPE

<img width="960" alt="Capture d'écran 2023-06-18 194820" src="https://github.com/Sla0ui/WEBSCRAPE/assets/136838832/25b13a56-87e4-4752-86b0-8ec6b0f59c66">

Web Links Scraper

This Python script allows you to scrape web links from a specified domain using the Wayback Machine's web archive. It utilizes the Selenium library to interact with a web browser and retrieve the links.

Features:
- Scrape links from the specified domain within the Wayback Machine's web archive.
- Supports scraping multiple pages.
- Provides options to sort the results based on the date of capture.
- Filters out duplicate and irrelevant links.
- Writes the scraped links to a text file.

Usage:
1. Enter the domain for which you want to scrape links.
2. Specify the number of pages to scrape (maximum of 200).
3. Choose the sorting order for the results.
4. The script will launch a headless Chrome browser and start scraping the links.
5. The scraped links will be saved in the "Scraped_output.txt" file.

Optimizations and Improvements:
- Implemented explicit waits to ensure elements are loaded before interacting with them.
- Used URL parsing and manipulation functions for cleaner link handling.
- Added colorama library for colorful console output.
- Improved filtering of links to exclude irrelevant and duplicate entries.

Future Enhancements:
- Implement multi-threading or asynchronous processing to scrape multiple pages concurrently, thereby improving the scraping speed.
- Implement a progress indicator to display the status of the scraping process.
- Add error handling and logging to handle any exceptions during scraping.

Note: This script requires the Selenium, colorama, and Chrome WebDriver libraries to be installed.

Feel free to contribute, provide feedback, or suggest improvements!

Author: Sla0ui

