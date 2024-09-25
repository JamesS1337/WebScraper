from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Set the path to your geckodriver
geckodriver_path = r"C:\Users\themi\AppData\Local\Programs\Microsoft VS Code\bin\geckodriver.exe"

# Set the path to your Firefox binary
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Adjust this path as needed

# Configure the WebDriver service and options
service = Service(geckodriver_path)
options = Options()
options.binary_location = firefox_binary_path

# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Open the Wikipedia page for Particle Physics
driver.get('https://en.wikipedia.org/wiki/Particle_physics')

# Allow the page to load completely
time.sleep(5)

# Scrape the main content from the Wikipedia page (excluding sidebars and footers)
content = driver.find_element(By.ID, 'mw-content-text').text

# Write the content to a text file
with open("particle_physics_wikipedia.txt", "w", encoding="utf-8") as file:
    file.write(content)

# Close the browser
driver.quit()

print("Scraping complete. Content saved to particle_physics_wikipedia.txt")
