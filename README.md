This Python script checks the upcoming weather forecast for a specified location and sends a text notification if rain is predicted. It utilizes the OpenWeatherMap API and Twilio API for data retrieval and communication.

## Key Features

* Checks the weather forecast for the next four hours
* Alerts the user if rain is predicted
* Uses the OpenWeatherMap API for weather data
* Uses the Twilio API for SMS notifications

## Requirements

* Python 3.x
* Requests library
* Twilio API account with credentials (account_sid and auth_token)
* OpenWeatherMap API key

## Installation

1. Install the required libraries:

```bash
pip install requests


2. Create a Twilio account and obtain your account_sid and auth_token.

3. Acquire an OpenWeatherMap API key from their website.

4. Replace the placeholders for account_sid, auth_token, and api_key in the code with your credentials.

5. Save the code as a Python file (e.g., weather_alert.py) and run it using your preferred Python interpreter.

## Usage

bash
python weather_alert.py


The script will check the weather forecast for the next four hours and send a text notification if rain is predicted.
