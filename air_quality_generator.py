# import required libraries
import os
import pandas as pd
from time import sleep
from dotenv import load_dotenv

import requests
import json
from random import randint
from datetime import datetime
from ratelimit import limits, sleep_and_retry

# set the directory for the output
output_dir = 'Output'

# set api key
load_dotenv()
airnow_api_key = os.getenv("AIR_NOW_API_KEY")

# set the base url for the airnow api
airnow_base_url = "http://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json"

air_quality = pd.read_csv(os.path.join(output_dir, 'air_quality.csv'))

# set the zip codes
zip_codes = ['12261', '14620']

CALLS = 8
PERIOD = 60

@sleep_and_retry
@limits(calls=CALLS, period=PERIOD)
def get_air_now_data(zip_code, year, month, day, distance, calls=0):
    # set the parameters for the api call
    random_hour = randint(0, 24)
    date = f"{year}-{month:02d}-{day}T00-{random_hour}00"
    params = {
        'zipCode': zip_code,
        'date': date,
        'distance':distance,
        'API_KEY': airnow_api_key
    }

    response = requests.get(airnow_base_url, params=params)
    if response.status_code != 200:
        if calls < 5:
            calls += 1
            sleep_time = randint(1, 5)
            print(f"Sleeping for {sleep_time} seconds")
            sleep(sleep_time)
            return get_air_now_data(zip_code, year, month, day, distance, calls)
        else:
            print(f"Failed to get data for {zip_code} on {date}")
            return None
    data = response.json()
    return data

miles = 100
for zip_code in zip_codes:
    for year in range(2023, 2025):
        for month in range(1, 13):
            for day in range(2):
                d = 1
                if day != 0:
                    d = 15
                response = get_air_now_data(zip_code, year, month, d, miles)
                for item in response:
                    if item['ParameterName'] in ['PM2.5', 'PM10']:
                        print(item)
                        item['CategoryNumber'] = item['Category']['Number']
                        item['CategoryName'] = item['Category']['Name']
                        air_quality = air_quality._append(item, ignore_index=True)

air_quality.to_csv(f"{output_dir}/air_quality.csv", index=False)