import requests
import pandas as pd
from datetime import datetime
import os
import json
import time

class AmtrackDataCollector:
  def __init__(self, data_path):
    self.data_path = data_path
    self.api_url = "https://api-v3.amtraker.com/v3/trains"

  def _update_train_data(self):
    r = requests.get(self.api_url)
    if r.status_code == 200:
      print("Success!")
      data = r.json()
      with open(self.data_path, "w") as f:
        json.dump(data, f)
      return True
    else:
      print(f"Error: {r.status_code}")
      return False

  def _check_data(self):
    if os.path.exists(self.data_path):
      file_age = time.time() - os.path.getmtime(self.data_path)
      if file_age < 30 * 60:
        print("Using recently saved data.")
        return True
      else:
        print("Calling API for fresh data")
        return self._update_train_data()
    else:
      print("No data file found, fetching from API")
      return self._update_train_data()

  def get_train_data(self):
    if self._check_data():
      with open(self.data_path, "r") as f:
        data = json.load(f)
      return data
    else:
      print("Could not get data.")
      return None