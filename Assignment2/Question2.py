import os
import pandas as pd

# Read all csv files in the folder
def readCsvFiles(folder="temperatures"):
    allData = []
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder, file)) #Reading each CSV file into a pandas data
            allData.append(df)
    return allData

# Finding average temperature for each season
def seasonsAverage():
    #Making a Season dictionary with the seasonal months in it
    Seasons = {
        "Summer": ["December", "January", "February"],
        "Autumn": ["March", "April", "May"],
        "Winter": ["June", "July", "August"],
        "Spring": ["September", "October", "November"]
    }

    SeasonSum = {s: 0 for s in Seasons} # For storing sum of temperatures for each season
    SeasonCount = {s: 0 for s in Seasons} # For storing count of valid temperature entries for each season


    for df in readCsvFiles():
        for season, months in Seasons.items():
            for month in months:
                if month in df.columns:
                    temps = df[month].dropna()
                    SeasonSum[season] += temps.sum()
                    SeasonCount[season] += temps.count()

    with open("average_temp.txt", "w") as f:
        for season in Seasons:
            if SeasonCount[season] > 0:
                avg = SeasonSum[season] / SeasonCount[season]
                f.write(f"{season}: {round(avg, 2)}°C\n")
            else:
                f.write(f"{season}: No data\n")

    print("Seasonal averages saved to average_temp.txt")
     
# Find the station having largest temperature range
def tempeRange():
    StationRange = {}  # Place to store temperature ranges for each station

    # Loop through all CSV files and read the tmperature data
    for df in readCsvFiles():
        for _, row in df.iterrows():
            station = row["STATION_NAME"]  
            temps = row.loc["January":"December"].dropna()  # Get the temperature data for the year

            if station not in StationRange:  
                StationRange[station] = {"max": temps.max(), "min": temps.min()}
            else:
                # Update the max and min temperature for the station
                StationRange[station]["max"] = max(StationRange[station]["max"], temps.max())
                StationRange[station]["min"] = min(StationRange[station]["min"], temps.min())

    # Calculate the temperature range  for each station
    for station, range_values in StationRange.items():
        range_values["range"] = range_values["max"] - range_values["min"]

    # Find the station with the larest temperature range
    maxRange = max(range_values["range"] for range_values in StationRange.values())  
    LargestStations = [station for station, range_values in StationRange.items() if range_values["range"] == maxRange]  

    # Write results to a file
    with open("largest_temp_range_station.txt", "w") as f:
        for station in LargestStations:
            range_values = StationRange[station]
            f.write(f"{station}: Range {round(range_values['range'],2)}°C "
                    f"(Max: {round(range_values['max'],2)}°C, Min: {round(range_values['min'],2)}°C)\n")

    print("Temperature range saved to largest_temp_range_station.txt") 


# Calling the functions
seasonsAverage()
tempeRange()
