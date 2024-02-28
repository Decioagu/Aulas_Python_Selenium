from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Replace 'PATH_TO_YOUR_CHROME_DRIVER' with the actual path
driver = webdriver.Chrome(ChromeDriverManager().install(executable_path='PATH_TO_YOUR_CHROME_DRIVER'))
