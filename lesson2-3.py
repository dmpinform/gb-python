season = {"winter": [12, 1, 2], "spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11]}
month = input("Enter the month number: ")
select_season = "".join(key for key, val in season.items() if int(month) in val)
print(select_season)
