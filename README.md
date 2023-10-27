# Python-code
from selenium import webdriver

# Create a WebDriver instance (you can choose your preferred browser driver)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://example.com")

# Use JavaScript to find the element with the highest z-index
highest_z_index_element = driver.execute_script(
    "var elements = document.querySelectorAll('*'); "
    "var maxZ = -1; "
    "var highestElement = null; "
    "for (var i = 0; i < elements.length; i++) { "
    "    var zIndex = window.getComputedStyle(elements[i]).getPropertyValue('z-index'); "
    "    if (!isNaN(zIndex) && zIndex > maxZ) { "
    "        maxZ = zIndex; "
    "        highestElement = elements[i]; "
    "    } "
    "} "
    "return highestElement;")

# Now, you can click on the element with the highest z-index
highest_z_index_element.click()

# Close the WebDriver when done
driver.quit()
