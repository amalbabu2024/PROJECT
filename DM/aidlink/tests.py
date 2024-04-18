# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException

# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome()

# try:
#     # Navigate to the login page
#     driver.get("http://127.0.0.1:8000/accounts/login/")  # Update with the actual URL of the login page

#     # Wait for the login form to appear
#     username_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
#     password_elem = driver.find_element(By.ID, "password")

#     # Enter username and password
#     username_elem.send_keys("milton")
#     password_elem.send_keys("Milton@123")

#     print("username and password entered successful!")

#     # Submit the login form
#     password_elem.send_keys(Keys.RETURN)

#     print("Login Button Clicked Successfully")

#     # Wait for the logout button to appear
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "logout-button")))

#     print("Login successful!")

# except TimeoutException:
#     print("Login form elements not found within the specified time.")
# except NoSuchElementException:
#     print("Login form elements not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     # Close the browser
#     driver.quit()















from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get("http://127.0.0.1:8000/accounts/login/")

    # Wait for the login form to appear
    username_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    password_elem = driver.find_element(By.ID, "password")

    # Enter username and password
    username_elem.send_keys("milton")
    password_elem.send_keys("Milton@123")

    # Submit the login form
    password_elem.send_keys(Keys.RETURN)

    # Wait for the dashboard page to load
    dashboard_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "team_leader_dashboard")))

    # Navigate to the add organization resources page
    driver.get("http://127.0.0.1:8000/add_organization_resources/")

    # Wait for the add organization resources form to appear
    resource_name_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ResourceName")))

    # Print success message
    print("Navigated to Add Organization Resources page successfully!")

except TimeoutException:
    print("Login form elements not found within the specified time.")
except NoSuchElementException:
    print("Login form elements not found.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
