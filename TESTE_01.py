from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Download and set the path for the ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Access a website
driver.get("https://www.google.com")

# Perform actions on the website
# ... (your website interaction code goes here)

# Close the browser
driver.quit()
