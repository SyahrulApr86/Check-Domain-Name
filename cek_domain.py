import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Automatically install the compatible ChromeDriver
chromedriver_autoinstaller.install()

# Set options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Reduce GPU usage
chrome_options.add_argument("--no-sandbox")  # Prevent permission issues
chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues

# Create a Chrome driver instance with headless options
driver = webdriver.Chrome(options=chrome_options)

# Read TLDs from the file
with open('tlds.txt', 'r') as file:
    tlds = [line.strip().lower() for line in file]

try:
    for tld in tlds:
        domain_name = f"rul.{tld}"
        print(f"Checking {domain_name}... ", end='')

        # Open the Niagahoster page
        driver.get("https://www.niagahoster.co.id/domain-murah")

        # Wait until the input element is loaded
        time.sleep(3)  # Can be replaced with explicit wait if needed

        # Find the input element for the domain name
        search_input = driver.find_element(By.ID, "h-domain-finder-header-input")

        # Enter the domain name to be checked
        search_input.send_keys(domain_name)

        # Press Enter to submit
        search_input.send_keys(Keys.RETURN)

        # Wait for a few seconds until the page is fully loaded
        time.sleep(5)

        # Check if the text indicating the domain is available is on the page
        if "Selamat! Domain yang Anda Cari Tersedia" in driver.page_source:
            print("[+] Available")
            with open('available_tlds.txt', 'a') as available_tlds_file:
                available_tlds_file.write(domain_name + '\n')
        else:
            print("[x] Not Available")
            with open('not_available_tlds.txt', 'a') as not_available_tlds_file:
                not_available_tlds_file.write(domain_name + '\n')
finally:
    # Close the browser
    driver.quit()
