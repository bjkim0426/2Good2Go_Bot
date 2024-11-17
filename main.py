import os
import time
import threading
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

myUdid = os.getenv("myUdid")

# Step 1: Define desired capabilities for Appium
desired_caps = {
    "platformName": "iOS",  # Or Android for Android devices
    "deviceName": "iPhone 14 Pro Max",
    "platformVersion": "17.6.1",
    "udid": myUdid,
    "bundleId": "com.moonsted.TGTG",  # App's package ID for Android or bundle ID for iOS
    "noReset": True,
    "automationName": "XCUITest"  # Change to UiAutomator2 for Android
}

# Step 2: Initialize the Appium driver using `desired_capabilities`
server = 'http://127.0.0.1:4723'
appium_options = AppiumOptions()
appium_options.load_capabilities(desired_caps)

driver = webdriver.Remote(server, options=appium_options)
driver.implicitly_wait(0.5)  # Short implicit wait for quick element detection

reserve_button_ios_class_chain = '**/XCUIElementTypeButton[`name == "Reserve"`]'
popup_close_button_id = "close large black"
favorite_accessibility_id = "Favorites"
got_it_button_accessibility_id = "Got it!"
increase_quantity_accessibility_id = 'checkout_increase_quantity_enabled'
apple_pay_accessibility_id = 'Buy with Apple Pay'



# Start timer
start_time = time.time()

# Polling function to check for availability
def check_item_availability(driver, max_attempts):
    try:
        attempts = 0
        while attempts < max_attempts:
            attempts += 1
            try:
                # Check for popup (item is sold out)
                popup_close_button = driver.find_elements(By.ACCESSIBILITY_ID, popup_close_button_id)
                if popup_close_button and popup_close_button[0].is_displayed():
                    print("Popup detected, item is sold out.")
                    popup_close_button[0].click()  # Close the popup
                    continue

                # Try to find and click the Reserve button
                reserve_button = driver.find_element(By.IOS_CLASS_CHAIN, reserve_button_ios_class_chain)
                reserve_button.click()

                print(f"Item became available and Reserve button clicked on attempt {attempts}!")
                return  # Exit loop if button is clicked
            except NoSuchElementException:
                print(f"Item not available yet, retrying... (Attempt {attempts})")
            except Exception as e:
                print(f"Error in attempt {attempts}: {e}")
            time.sleep(0.04)  # Adjust for 25 attempts per second (1/25 = 0.04 seconds)

    except Exception as e:
        print(f"An error occurred: {e}")

# Step 3: Function to continuously check for item availability and complete checkout
def check_item_and_checkout(driver):
    try:
        # Wait for app to load (~1.1 seconds)
        print("Waiting for app to load...")
        time.sleep(1.15)

        # Click the Favorites tab (available almost immediately)
        driver.find_element(By.ACCESSIBILITY_ID, favorite_accessibility_id).click()
        print("Navigated to Favorites tab.")

        # Click the first item in the Favorites list

        driver.find_element(By.IOS_CLASS_CHAIN,
                            '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage[1]').click()
        print("Clicked item from Favorites.")


        # Start a thread to check for availability
        max_attempts = 1000
        thread = threading.Thread(target=check_item_availability, args=(driver, max_attempts))
        thread.start()
        thread.join()  # Wait for the thread to finish

        # Proceed to checkout (this function could be improved with further steps if needed)
        complete_checkout(driver)

    except Exception as e:
        print(f"An error occurred: {e}")

# Step 4: Function to complete the checkout process
def complete_checkout(driver):
    try:
        # Click the "Got it" button (available almost immediately)

        got_it_button = driver.find_element(By.ACCESSIBILITY_ID, got_it_button_accessibility_id)
        got_it_button.click()
        print("Got it button clicked.")

        # Increase quantity rapidly (batch clicking)

        for i in range(2):  # Already 1 item selected, so max increase is 2 times
            try:
                increase_quantity_button = driver.find_element(By.ACCESSIBILITY_ID, increase_quantity_accessibility_id)
                increase_quantity_button.click()
                print(f"Increased quantity to {i + 2}")
            except Exception as e:
                print(f"Error clicking increase button: {e}")
                break

        # Click the Apple Pay button and complete payment

        apple_pay_button = driver.find_element(By.ACCESSIBILITY_ID, apple_pay_accessibility_id)
        apple_pay_button.click()
        print("Apple Pay button clicked. Please confirm manually with the side button.")

    except Exception as e:
        print(f"Checkout failed: {e}")

# Main logic to call the function
check_item_and_checkout(driver)

# End timer and calculate the total time taken
end_time = time.time()
total_time = end_time - start_time
print(f"Total time taken: {total_time:.2f} seconds")

# Optional: Quit the driver after the test is done
driver.quit()
