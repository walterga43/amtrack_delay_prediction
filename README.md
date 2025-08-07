# **Amtrak Delay Prediction & Route Performance Analysis**

Project Overview
Goal: Build a real time Amrtack delay tracking in order to study what makes these trains not on time
Week 2: Data exploration

#### **Data Source**
- API: Amtraker API (https://api-v3.amtraker.com/v3/)
- Data Type: Real-time Amtrak train positions, schedules, and delay information
- No API key required - free public access

#### **Current Progress**
Week 1: Data Collection & Exploration 
- Set up API data collection
- Created timezone-aware delay calculations
- Built basic data visualization
- Identified key data patterns

#### **Key Findings So Far**

- Data Quality: Overall easy to work with. Only struggle was getting the station dataframe from the train dataframe.
- Delay Patterns: Over 30% of departures are later by at least 15 minutes.
- Route Performance: 

#### **Train-Level Data**

- Route information, current location (lat/lon)
- Speed, direction headed
- Origin and destination details

#### **Station-Level Data**

- Scheduled vs actual arrival/departure times
- Station codes, names, timezones
- Train status at each station
- Delay calculations in minutes

#### **Visualizations Created**

- Delay distribution bar chart
- Average delays grouped by route

**Timezone conversion**

stations_df[col] = pd.to_datetime(stations_df[col], errors='coerce', utc=True)


Last Updated: 8/7/2025

