# Flight-Deal-Notifier
OOP-based application to track flight prices using the Amadeus API, by compare them against Google Sheets thresholds via the Sheety API, and send SMS alerts via Twilio when prices drop.

## How to use

Step 1: Go to this link and make a coppy of this google sheet: https://docs.google.com/spreadsheets/d/1Zl0-HKRBXJG9PrspBegiANsW6jWSeGYFz-JhaUqDdhg/edit?gid=0#gid=0

Step 2: Connect to Sheety, https://sheety.co and add your coppy of the prices and users file then enable and get your "GET" and "PUT" api for the prices file and enable "GET" and "POST" for the users file.
  - use your own GET api in the data_manager.py file.
 
Step 3: Connect to Amadeus, https://developers.amadeus.com and get your free tokens.
  - use your own IATA_ENDPOINT, FLIGHT_ENDPOINT AND TOKEN_ENDPOINT in the flight_search.py

Step 4: Connect to Twillo and get your own free api and tokens, https://www.twilio.com/docs/messaging/quickstart/python.

Step 5: populate an .env file with your apis:

  SHEETY_USERNAME=""
  SHEETY_PASSWORD=""
  TOKEN=""
  AMADEUS_KEY=""
  AMADEUS_SECRET=""
  TWILIO_SID=""
  TWILIO_AUTH_TOKEN=""
  TWILIO_VIRTUAL_NUMBER=""
  TWILIO_VERIFIED_NUMBER=""
  TWILIO_WHATSAPP_NUMBER=""
