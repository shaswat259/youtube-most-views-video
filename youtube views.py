from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome() 

# Open a webpage
driver.get("http://youtube.com/")
driver.maximize_window()
time.sleep(5)

# Find the element by name and send keys
x = driver.find_element(By.XPATH,"//*[@name='search_query']").click()
x = driver.find_element(By.XPATH,"//*[@name='search_query']").send_keys('hello world')
driver.find_element(By.ID,"search-icon-legacy").click()
time.sleep(5)
scroll_start_time = time.time()
scroll_duration = 20  # seconds
while (time.time() - scroll_start_time) < scroll_duration:
    # Scroll down by a specific amount
    driver.execute_script("window.scrollBy(0, 100);")
    
    # Wait for a short moment to make scrolling visible
    time.sleep(0.5)  # Adjust this if needed

elements = driver.find_elements(By.XPATH,"//*[@id='metadata-line']/span[1]")

time.sleep(5)
texts = [element.text for element in elements]

print(texts)
def convert_view_count(texts):
    """ Convert view count string to a numerical value in thousands. """
    if 'K' in texts:
        return float(texts.replace('K views', '').replace(',', '')) * 1000  # in thousands
    elif 'M' in texts:
        return float(texts.replace('M views', '').replace(',', '')) * 1000000  # convert in millions
    elif 'B' in texts:
        return float(texts.replace('B views', '').replace(',', '')) * 100000000  # convert in billions
    elif 'views' in texts:
        return float(texts.replace(' views', '').replace(',', ''))  # convert to thousands if no 'K' or 'M'
    else:
        return 0

# Extract numerical values and their original indices
numerical_values = [convert_view_count(vc) for vc in texts if 'views' in vc]

# Find the maximum value and its index
max_value = max(numerical_values)
max_index = numerical_values.index(max_value)

# Retrieve the original view count with the highest value
original_view_count = texts[max_index]

# Print results
print("Original view count with highest value:", original_view_count)
print("Highest numerical value in thousands:", max_value)
print("Index of the highest value in the original array:", max_index)
time.sleep(3)
y = driver.find_element(By.XPATH,f"(//*[@id='video-title'])[{(max_index)}]")
time.sleep(3)
y.click()

time.sleep(15)



