
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of a month (1-12): "))

if month in [12, 1, 2]:
    season = seasons[0]  # Winter
elif month in [3, 4, 5]:
    season = seasons[1]  # Spring
elif month in [6, 7, 8]:
    season = seasons[2]  # Summer
elif month in [9, 10, 11]:
    season = seasons[3]  # Autumn
else:
    season = "Invalid month"

print(f"The corresponding season is: {season}")
