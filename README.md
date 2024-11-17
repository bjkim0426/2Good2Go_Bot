# TooGoodToGo Bot

This project automates the process of reserving meals on the TooGoodToGo app. The bot is designed to minimize the time required to reserve meals, especially for popular restaurants where availability is limited. The program interacts with the app using Appium and automates the reservation process.

## Features
- **Favorites Tab Automation**: The program navigates to the "Favorites" tab of the app, ensuring the desired restaurant is pre-selected by the user as a favorite.
- **Rapid Availability Check**: Checks for the availability of the "Reserve" button up to 25 times per second.
- **Customizable Quantity**: Automates the process of increasing the meal quantity during checkout.
- **Apple Pay Integration**: Automatically proceeds to the Apple Pay screen for final confirmation.

---

## Prerequisites

1. **Appium**:
   - Install Appium globally using npm:
     ```bash
     npm install -g appium
     ```

2. **Python Environment**:
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On MacOS/Linux
     venv\Scripts\activate     # On Windows
     ```
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **WebDriverAgent**:
   - Ensure WebDriverAgent is correctly installed and configured on your device.
   - The WebDriverAgentRunner app must be installed on your iOS device to enable automation.
  
4. **TooGoodToGo App**:
   - Download the TooGoodToGo app from the App Store.
   - Sign in using a valid TooGoodToGo account.
  
---

# Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/bjkim0426/TooGoodToGo-Bot.git
   cd TooGoodToGo-Bot
   ```
2. **Configure Your Device:**
   - Replace `os.getenv("myUdid")` in the code with your own device's UDID:
     ```python
     "udid": "your-device-udid-here",
     ```
   - To find your device's UDID, connect your iPhone to your Mac, and run:
     ```bash
     idevice_id -l
     ```
3. **Mark Your Restaurant as a Favorite:**
   - The bot navigates to the "Favorites" tab in the TooGoodToGo app.
   - Mark your desired restaurant as a favorite for the program to work effectively.
     
4. **Run the Program:**
   - Ensure the Appium server is running:
     ```bash
     appium
     ```
   - Run the program:
     ```bash
     python3 main.py
     ```
---

## Usage

1. Start the Appium server locally (default: `http://127.0.0.1:4723`).
2. Run the Python script to automate the reservation process.
3. The program will:
   - Navigate to the "Favorites" tab.
   - Select the first restaurant marked as a favorite.
   - Continuously check for the availability of the "Reserve" button.
   - Proceed to the checkout process once the item is available.

---

## Notes

- **Apple Developer Account**: Ensure you have the proper Apple developer account setup to install WebDriverAgent on your device.
- **Device Integrity**: Verify that your iPhone allows running apps installed from Xcode.
- **Custom Automation**: Adjust the quantity of meals or favorite restaurant selection by modifying the script as needed.

---

## Troubleshooting

- **Connection Refused (Port 8100)**:
  - Ensure `WebDriverAgentRunner` is installed and running on your device.
  - Open Xcode, build, and run the `WebDriverAgentRunner` scheme on your connected device.
  
- **UDID Not Found**:
  - Verify that the correct UDID is set in the script.
  - Run `idevice_id -l` to confirm your device is connected.
  
- **Integrity Verification Error**:
  - On your iPhone, navigate to `Settings > General > VPN & Device Management` and trust the developer profile associated with WebDriverAgent.

---

## Contributing

If you encounter issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## Disclaimer

Use this bot responsibly.

  

