# Travel-time-calculator
Python script used to calculate travel time from point A to point B and add it to a Google Sheets file. It also sends a notification via PushBullet to the user's phone/PC.


# Concept

The idea came from my curiosity as to how traffic conditions differ based on day of the week, weather and how strong of a correlation there is between these.

# How to run it yourself

All you have to do to run it is to rename the SAMPLE-config.json file to config.json and add the following in this file : starting point and destination, city (for weather and the push notification) and API keys for Dark Sky Weather, Google Maps and Pushbullet as well as a Sheet id for the Google sheets sheet that the script will be writing to.

Google Sheets template : [here](https://docs.google.com/spreadsheets/d/1VKMkeDPqdf1fYtbxRYg-TMH5dkeqJb6f0bHPmTf7Re8/edit?usp=sharing)

The script is currently configured to be run every half hour. At 8AM it sends a notification to the user's PushBullet registered devices with yesterday's travel time average.

Travel time is calculated by Google Maps based on current traffic and the route chosen can differ if an alternative is faster (shortest route is not always chosen).

Powered by Dark Sky
