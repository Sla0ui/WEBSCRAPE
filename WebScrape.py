import ctypes
import sys
from progress.bar import Bar
from urllib.parse import urlparse
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import tempfile

def clean_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace("www.", "")
    return domain

def extract_links(driver, domain):
    links = driver.find_elements(By.TAG_NAME, 'a')
    page_links = []
    for link in links:
        href = link.get_attribute('href')
        if href and domain in href:
            page_links.append(href)
    return page_links

def has_next_page(driver):
    try:
        next_button = driver.find_element(By.XPATH, '//*[@id="resultsUrl_next"]/a')
        return next_button.is_enabled() and next_button.is_displayed()
    except NoSuchElementException:
        return False
    
def filter_links(links):
    unique_links = set()
    filtered_links = []
    prefix = "https://web.archive.org/web/"
    for link in links:
        if link.startswith(prefix):
            modified_link = clean_link(domain, link)
        else:
            modified_link = link

        if modified_link not in unique_links:
            unique_links.add(modified_link)
            filtered_links.append(modified_link)
    
    return filtered_links

def clean_link(domain, link):
    cleaned_link = link
    if link.startswith("https://web.archive.org/web/"):
        cleaned_link = cleaned_link.replace("https://web.archive.org/web/", "")
        cleaned_link = cleaned_link.split(domain, 1)[-1].lstrip("/")
        cleaned_link = f"https://{domain}/{cleaned_link}"

    if domain in cleaned_link and len(cleaned_link.split(domain, 1)[-1].lstrip("/")) == 0:
        return None
    return cleaned_link

def write_to_file(links, save_as_archive):
    with open('Scraped_output.txt', 'w') as file:
        for link in links:
            if link is not None and "web.archive.org" not in link:
                if save_as_archive:
                    file.write(f"https://web.archive.org/web/*/{link}\n")
                else:
                    file.write(link + '\n')

ctypes.windll.kernel32.SetConsoleTitleW(f"Web Links Scraper - by Sla0ui")

init(autoreset=True)

print(Fore.CYAN+"""

    __          ________ ____   _____  _____ _____            _____  ______ 
    \ \        / /  ____|  _ \ / ____|/ ____|  __ \     /\   |  __ \|  ____|
     \ \  /\  / /| |__  | |_) | (___ | |    | |__) |   /  \  | |__) | |__   
      \ \/  \/ / |  __| |  _ < \___ \| |    |  _  /   / /\ \ |  ___/|  __|  
       \  /\  /  | |____| |_) |____) | |____| | \ \  / ____ \| |    | |____ 
        \/  \/   |______|____/|_____/ \_____|_|  \_\/_/    \_\_|    |______|
                                                                        
                                               Web Links Scraper - by Sla0ui                                                                          
                                                                t.me/slesl23
                        """)
print(Fore.LIGHTGREEN_EX + "[1] Scrape Links")
print(Fore.LIGHTGREEN_EX + "[2] Exit ")
select = int(input("\n> "))

while select <= 0 or select > 2:
    print(Fore.RED + "Incorrect value.")
    select = int(input("\n> "))

if select == 1:
    domain = clean_url(input(Fore.GREEN + "Enter The Domain: "))
    print("\n" + Fore.LIGHTGREEN_EX + "[+] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " " +domain + "\n")
    url = f'https://web.archive.org/web/*/{domain}/*'
    print(Fore.LIGHTGREEN_EX + "Enter the number of pages to scrape (max->200)")
    num_pages = int(input("\n> "))

    print(Fore.LIGHTGREEN_EX + "Save links as:\n[1] Archived version (Wayback Machine)\n[2] Original URL")
    save_option = int(input("\n> "))
    save_as_archive = save_option == 1

    log_file_path = "webdriver.log"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-logging')
    options.add_argument(f'--log-path={log_file_path}')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Exclude browser logging

    temp_stderr = tempfile.TemporaryFile()
    sys.stderr = temp_stderr
    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 10)
    all_links = []

    print(Fore.YELLOW + "\nEstablishing the connection, please wait...\n", end='', flush=True)


    driver.get(url)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
    page_links = extract_links(driver, domain)
    all_links.extend(page_links)

    print("\n" + Fore.LIGHTGREEN_EX + "[+] " + Fore.MAGENTA + ">>" + Fore.LIGHTGREEN_EX + " Connection Established !! " + "\n")

    print(Fore.LIGHTCYAN_EX + "\nSorting order ?\n\n[1] Oldest to Newest\n[2] Newest to Oldest\n[3] Default (by URL)\n")
    sort_option = input("\n> ")
    while sort_option not in ['1', '2', '3']:
        print(Fore.RED + "Incorrect value.")
        sort_option = input("\n> ")

    if sort_option == '1':
        date_sort_button = driver.find_element(By.XPATH, '//*[@id="resultsUrl"]/thead/tr/th[3]')
        date_sort_button.click()
        try:
            wait.until(EC.staleness_of(date_sort_button))
        except TimeoutException:
            pass
    elif sort_option == '2':
        date_sort_button = driver.find_element(By.XPATH, '//*[@id="resultsUrl"]/thead/tr/th[3]')
        date_sort_button.click()
        date_sort_button.click()
        try:
            wait.until(EC.staleness_of(date_sort_button))
        except TimeoutException:
            pass
    elif sort_option == '3':
        pass

    current_page = 0
    progress_bar = Bar(Fore.LIGHTCYAN_EX + 'Scraping Progress', max=num_pages)

    while has_next_page(driver) and current_page < num_pages:
        next_button = driver.find_element(By.XPATH, '//*[@id="resultsUrl_next"]/a')
        next_button.click()
        wait.until(EC.staleness_of(next_button))
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
        page_links = extract_links(driver, domain)
        all_links.extend(page_links)
        current_page += 1
        progress_bar.next()

    progress_bar.finish()
    driver.quit()

    sys.stderr = sys.__stderr__
    temp_stderr.close()

    filtered_links = filter_links(all_links)
    write_to_file(filtered_links, save_as_archive)
    print(Fore.LIGHTMAGENTA_EX + "Saved to file\n")
    print(Fore.LIGHTCYAN_EX + "Process ended. Press Enter to exit.")
    input()
    
elif select == 2:
    pass
