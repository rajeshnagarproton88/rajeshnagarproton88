from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (assuming Chrome)
driver = webdriver.Chrome('/path/to/chromedriver')  # Replace with your chromedriver path

# Navigate to a webpage
driver.get('https://www.google.com')

# Find an element (search box)
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))  
)

# Type into the element
search_box.send_keys('Selenium automation')

# Submit the search form
search_box.submit()

# Wait for results to load (Example)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)

# Get the page title (Example)
title = driver.title
print(f"Page title after search: {title}")

# Close the browser
driver.quit()
