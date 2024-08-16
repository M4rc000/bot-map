# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import random
# import time
# import faker

# # Function to initialize WebDriver
# def initialize_driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
#     driver = webdriver.Chrome()
#     return driver

# # Initialize Faker for generating random names
# fake = faker.Faker()

# # Success counter and data storage
# success = 0
# successful_registrations = []

# # Define the maximum number of attempts
# max_attempts = 5
# attempts = 0

# while attempts < max_attempts:
#     attempts += 1
#     driver = None
#     try:
#         # Initialize WebDriver
#         driver = initialize_driver()

#         # Open the URL
#         driver.get('https://www.mapclub.com/en/user/signup?store=KSO8')

#         # Generate random phone numbers
#         def generate_phone_numbers(num):
#             base = "8"
#             return [base + ''.join(random.choices('0123456789', k=10)) for _ in range(num)]

#         phone_numbers = generate_phone_numbers(60)

#         def generate_phone_numbers_input(num):
#             base = "0877"
#             return [base + ''.join(random.choices('0123456789', k=8)) for _ in range(num)]

#         phone_numbers_input = generate_phone_numbers_input(60)

#         # Pick a random phone number
#         phone_number = random.choice(phone_numbers)

#         #phone input
#         phone_number_input = random.choice(phone_numbers_input)


#         time.sleep(4)

#         # Find the input element and enter the phone number
#         input_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone number"]')
#         input_element.clear()
#         input_element.send_keys(phone_number)

#         # Find and click the "Check" button
#         check_button = driver.find_element(By.CSS_SELECTOR, 'span.check')
#         check_button.click()

#         # Wait for the "Apply MAPCLUB Member" button to be present and clickable
#         wait = WebDriverWait(driver, 10)
#         apply_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.confirm__form-submit')))
#         apply_button.click()

#         # Wait for the form to load
#         time.sleep(5)

#         # Generate random personal data
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"

#         # Generate a random date from 1970 to 2000
#         start_year = 1970
#         end_year = 2000
#         random_year = random.randint(start_year, end_year)
#         random_month = random.randint(1, 12)
#         random_day = random.randint(1, 28)  # To avoid invalid dates like February 30

#         date = f"{random_day:02d}/{random_month:02d}/{random_year}"

#         # Fill out the additional form fields
#         first_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]')
#         last_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]')
#         phone_element = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
#         email_element = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
#         date_element = driver.find_element(By.CSS_SELECTOR, 'input[name="date"]')

#         first_name_element.clear()
#         first_name_element.send_keys(first_name)

#         last_name_element.clear()
#         last_name_element.send_keys(last_name)

#         phone_element.clear()
#         phone_element.send_keys(phone_number_input)

#         email_element.clear()
#         email_element.send_keys(email)

#         date_element.clear()
#         date_element.send_keys(date)

#         # Close any open date picker (if needed)
#         try:
#             # Find and click a place outside of the date picker to close it
#             outside_date_picker = driver.find_element(By.CSS_SELECTOR, 'body')  # Adjust selector if needed
#             outside_date_picker.click()
#         except:
#             pass  # Date picker might not always be present

#         # Wait to ensure date picker is closed
#         time.sleep(2)

#         # Select a radio button (male or female)
#         gender_choice = random.choice(['male', 'female'])

#         try:
#             gender_radio = driver.find_element(By.XPATH, f"//span[contains(text(), '{gender_choice}')]")
#             driver.execute_script("arguments[0].click();", gender_radio)
#         except Exception as e:
#             print(f"Error selecting gender radio button: {e}")

#         # Fill the select option input for Domicile (city)
#         city_dropdown = driver.find_element(By.CSS_SELECTOR, 'div.dropdown.content__form-select-input')
#         city_dropdown.click()

#         # Wait for the dropdown items to be visible and select a random city
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.dropdown-item')))
#         city_options = driver.find_elements(By.XPATH, "//ul[@class='dropdown-item']/li")
#         random_city = random.choice(city_options)
#         random_city_text = random_city.text
#         random_city.click()

#         # Check the Terms & Conditions checkbox
#         tnc_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="tnc"]')
#         if not tnc_checkbox.is_selected():
#             tnc_checkbox.click()

#         # Check the consent checkbox
#         consent_checkbox = driver.find_element(By.XPATH, "//div[@class='content__form-group content__form-group-tnc'][2]/div/input")
#         if not consent_checkbox.is_selected():
#             consent_checkbox.click()

#         # Click the Register button
#         register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn-black")))
#         if register_button:
#             print("Ada", success)

#         register_button.click()

#         # Increment success counter and add data to list
#         success += 1
#         successful_registrations.append({
#             'first_name': first_name,
#             'last_name': last_name,
#             'email': email,
#             'phone': phone_number,
#             'date_of_birth': date,
#             'gender': gender_choice,
#             'city': random_city_text
#         })

#         # Wait to see the result
#         time.sleep(3)

#     except Exception as e:
#         print(f"Attempt {attempts} failed: {e}")
#         time.sleep(2)  # Wait a bit before the next attempt

#     finally:
#         if driver:
#             # Close the WebDriver
#             driver.quit()

# print(f"Total successful registrations: {success}")
# print("Successful registrations data:")
# for registration in successful_registrations:
#     print(registration)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import random
# import time
# import faker

# # Function to initialize WebDriver
# def initialize_driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
#     driver = webdriver.Chrome()
#     return driver

# # Initialize Faker for generating random names
# fake = faker.Faker()

# # Success counter and data storage
# success = 0
# successful_registrations = []

# # Define the maximum number of attempts
# max_attempts = 5
# attempts = 0

# while attempts < max_attempts:
#     driver = None
#     try:
#         # Initialize WebDriver
#         driver = initialize_driver()

#         # Open the URL
#         driver.get('https://www.mapclub.com/en/user/signup?store=KSO8')

#         # Generate random phone numbers
#         def generate_phone_numbers(num):
#             base = "8"
#             return [base + ''.join(random.choices('0123456789', k=10)) for _ in range(num)]

#         phone_numbers = generate_phone_numbers(60)

#         def generate_phone_numbers_input(num):
#             base = "0877"
#             return [base + ''.join(random.choices('0123456789', k=8)) for _ in range(num)]

#         phone_numbers_input = generate_phone_numbers_input(60)

#         # Pick a random phone number
#         phone_number = random.choice(phone_numbers)

#         # phone input
#         phone_number_input = random.choice(phone_numbers_input)

#         time.sleep(4)

#         try:
#             # Find the input element and enter the phone number
#             input_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone number"]')
#             input_element.clear()
#             input_element.send_keys(phone_number)

#             # Find and click the "Check" button
#             check_button = driver.find_element(By.CSS_SELECTOR, 'span.check')
#             check_button.click()

#             # Wait for the "Apply MAPCLUB Member" button to be present and clickable
#             wait = WebDriverWait(driver, 10)
#             apply_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.confirm__form-submit')))
#             apply_button.click()

#         except Exception as e:
#             # If an error occurs in the phone number section, retry without incrementing attempts
#             print(f"Error in phone number section: {e}")
#             time.sleep(2)  # Wait a bit before retrying
#             continue

#         # Wait for the form to load
#         time.sleep(5)

#         # Generate random personal data
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"

#         # Generate a random date from 1970 to 2000
#         start_year = 1970
#         end_year = 2000
#         random_year = random.randint(start_year, end_year)
#         random_month = random.randint(1, 12)
#         random_day = random.randint(1, 28)  # To avoid invalid dates like February 30

#         date = f"{random_day:02d}/{random_month:02d}/{random_year}"

#         # Fill out the additional form fields
#         first_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]')
#         last_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]')
#         phone_element = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
#         email_element = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
#         date_element = driver.find_element(By.CSS_SELECTOR, 'input[name="date"]')

#         first_name_element.clear()
#         first_name_element.send_keys(first_name)

#         last_name_element.clear()
#         last_name_element.send_keys(last_name)

#         phone_element.clear()
#         phone_element.send_keys(phone_number_input)

#         email_element.clear()
#         email_element.send_keys(email)

#         date_element.clear()
#         date_element.send_keys(date)

#         # Close any open date picker (if needed)
#         try:
#             # Find and click a place outside of the date picker to close it
#             outside_date_picker = driver.find_element(By.CSS_SELECTOR, 'body')  # Adjust selector if needed
#             outside_date_picker.click()
#         except:
#             pass  # Date picker might not always be present

#         # Wait to ensure date picker is closed
#         time.sleep(2)

#         # Select a radio button (male or female)
#         gender_choice = random.choice(['male', 'female'])

#         try:
#             gender_radio = driver.find_element(By.XPATH, f"//span[contains(text(), '{gender_choice}')]")
#             driver.execute_script("arguments[0].click();", gender_radio)
#         except Exception as e:
#             print(f"Error selecting gender radio button: {e}")

#         # Fill the select option input for Domicile (city)
#         city_dropdown = driver.find_element(By.CSS_SELECTOR, 'div.dropdown.content__form-select-input')
#         city_dropdown.click()

#         # Wait for the dropdown items to be visible and select a random city
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.dropdown-item')))
#         city_options = driver.find_elements(By.XPATH, "//ul[@class='dropdown-item']/li")
#         random_city = random.choice(city_options)
#         random_city_text = random_city.text
#         random_city.click()

#         # Check the Terms & Conditions checkbox
#         tnc_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="tnc"]')
#         if not tnc_checkbox.is_selected():
#             tnc_checkbox.click()

#         # Check the consent checkbox
#         consent_checkbox = driver.find_element(By.XPATH, "//div[@class='content__form-group content__form-group-tnc'][2]/div/input")
#         if not consent_checkbox.is_selected():
#             consent_checkbox.click()

#         # Click the Register button
#         register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn-black")))
#         # register_button.click()

#         # Increment success counter and add data to list
#         success += 1
#         successful_registrations.append({
#             'first_name': first_name,
#             'last_name': last_name,
#             'email': email,
#             'phone': phone_number,
#             'date_of_birth': date,
#             'gender': gender_choice,
#             'city': random_city_text
#         })

#         # Wait to see the result
#         time.sleep(3)

#     except Exception as e:
#         print(f"Attempt {attempts} failed: {e}")
#         time.sleep(2)  # Wait a bit before the next attempt

#     finally:
#         if driver:
#             # Close the WebDriver
#             driver.quit()

#     # Increment the attempt count only if the entire process completes without issues
#     attempts += 1

# print(f"Total successful registrations: {success}")
# print("Successful registrations data:")
# for registration in successful_registrations:
#     print(registration)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import faker

# Function to initialize WebDriver
def initialize_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    driver = webdriver.Chrome()
    return driver

# Initialize Faker for generating random names
fake = faker.Faker()

# Success counter and data storage
success = 0
successful_registrations = []

# Define the maximum number of attempts
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    driver = None
    try:
        # Initialize WebDriver
        driver = initialize_driver()

        # Open the URL
        driver.get('https://www.mapclub.com/en/user/signup?store=KSO8')

        # Generate random phone numbers
        def generate_phone_numbers(num):
            base = "8"
            return [base + ''.join(random.choices('0123456789', k=10)) for _ in range(num)]

        phone_numbers = generate_phone_numbers(60)

        def generate_phone_numbers_input(num):
            base = "0877"
            return [base + ''.join(random.choices('0123456789', k=8)) for _ in range(num)]

        phone_numbers_input = generate_phone_numbers_input(60)

        # Pick a random phone number
        phone_number = random.choice(phone_numbers)

        # phone input
        phone_number_input = random.choice(phone_numbers_input)

        time.sleep(4)

        try:
            # Find the input element and enter the phone number
            input_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone number"]')
            input_element.clear()
            input_element.send_keys(phone_number)

            # Find and click the "Check" button
            check_button = driver.find_element(By.CSS_SELECTOR, 'span.check')
            check_button.click()

            # Wait for the "Apply MAPCLUB Member" button to be present and clickable
            wait = WebDriverWait(driver, 10)
            apply_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.confirm__form-submit')))
            apply_button.click()

        except Exception as e:
            # If an error occurs in the phone number section, retry without incrementing attempts
            print(f"Error in phone number section: {e}")
            time.sleep(2)  # Wait a bit before retrying
            continue

        # Wait for the form to load
        time.sleep(5)

        # Generate random personal data
        if random.choice([True, False]):
            # Generate male data
            first_name = fake.first_name_male()
            gender_choice = 'male'
        else:
            # Generate female data
            first_name = fake.first_name_female()
            gender_choice = 'female'

        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"

        # Generate a random date from 1970 to 2000
        start_year = 1970
        end_year = 2000
        random_year = random.randint(start_year, end_year)
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)  # To avoid invalid dates like February 30

        date = f"{random_day:02d}/{random_month:02d}/{random_year}"

        # Fill out the additional form fields
        first_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]')
        last_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]')
        phone_element = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
        email_element = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        date_element = driver.find_element(By.CSS_SELECTOR, 'input[name="date"]')

        first_name_element.clear()
        first_name_element.send_keys(first_name)

        last_name_element.clear()
        last_name_element.send_keys(last_name)

        phone_element.clear()
        phone_element.send_keys(phone_number_input)

        email_element.clear()
        email_element.send_keys(email)

        date_element.clear()
        date_element.send_keys(date)

        # Close any open date picker (if needed)
        try:
            # Find and click a place outside of the date picker to close it
            outside_date_picker = driver.find_element(By.CSS_SELECTOR, 'body')  # Adjust selector if needed
            outside_date_picker.click()
        except:
            pass  # Date picker might not always be present

        # Wait to ensure date picker is closed
        time.sleep(2)

        # Select a radio button based on the gender determined from the name
        try:
            gender_radio = driver.find_element(By.XPATH, f"//span[contains(text(), '{gender_choice}')]")
            driver.execute_script("arguments[0].click();", gender_radio)
        except Exception as e:
            print(f"Error selecting gender radio button: {e}")

        # Fill the select option input for Domicile (city)
        city_dropdown = driver.find_element(By.CSS_SELECTOR, 'div.dropdown.content__form-select-input')
        city_dropdown.click()

        # Wait for the dropdown items to be visible and select a random city
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.dropdown-item')))
        city_options = driver.find_elements(By.XPATH, "//ul[@class='dropdown-item']/li")
        random_city = random.choice(city_options)
        random_city_text = random_city.text
        random_city.click()

        # Check the Terms & Conditions checkbox
        tnc_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="tnc"]')
        if not tnc_checkbox.is_selected():
            tnc_checkbox.click()

        # Check the consent checkbox
        consent_checkbox = driver.find_element(By.XPATH, "//div[@class='content__form-group content__form-group-tnc'][2]/div/input")
        if not consent_checkbox.is_selected():
            consent_checkbox.click()

        # Click the Register button
        register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn-black")))
        # register_button.click()

        # Increment success counter and add data to list
        success += 1
        successful_registrations.append({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone_number,
            'date_of_birth': date,
            'gender': gender_choice,
            'city': random_city_text
        })

        # Wait to see the result
        time.sleep(3)

    except Exception as e:
        print(f"Attempt {attempts} failed: {e}")
        time.sleep(2)  # Wait a bit before the next attempt

    finally:
        if driver:
            # Close the WebDriver
            driver.quit()

    # Increment the attempt count only if the entire process completes without issues
    attempts += 1

print(f"Total successful registrations: {success}")
print("Successful registrations data:")
for registration in successful_registrations:
    print(registration)
