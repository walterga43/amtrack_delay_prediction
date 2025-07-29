import requests
import pandas as pd
from datetime import datetime
import os
import json
import time


def update_train_data():
  r = requests.get("https://api-v3.amtraker.com/v3/trains")
  if r.status_code == 200:
    print("Success!")
    data = r.json()
    with open("raw_train_output.json", "w") as f:
      json.dump(data, f)
    return True
  else:
    print(f"Error: {r.status_code}")
    return False
  
  
def get_train_data():
  with open("raw_train_output.json", "r") as f:
    data = json.load(f)
  return data

if os.path.exists("raw_train_output.json"):
    file_age = time.time() - os.path.getmtime("raw_train_output.json")
    if file_age < 30 * 60:
        print("Using recently saved data.")
        data = get_train_data()
    else:
        print("Calling API for fresh data")
        update_train_data()
        data = get_train_data()
else:
  if update_train_data():
    data = get_train_data()
  else:
    print("Failed")
        