import os
import pandas as pd

# Read all csv files in the folder
def readCsvFiles(folder="temperatures"):
    allData = []
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder, file)) #Reading each CSV file into a pandas data frame
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


  
# Calling functions
seasonsAverage()
