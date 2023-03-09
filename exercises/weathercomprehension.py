def cel_to_faren(temp):
    faren = (temp * 9 / 5) + 32
    return faren


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_c_faren = {f'{day}': cel_to_faren(temp) for (day, temp) in weather_c.items()}

print(weather_c_faren)
