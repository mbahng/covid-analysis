import Latitude_Longtitude
number_of_locations_completed, location = 0, Latitude_Longtitude.list_of_locations       #len(location) = 3950
g = open("Testing.txt","r")
for lat_long in location:
    number_of_locations_completed += 1
    confirmed_cases = []
    for month in Latitude_Longtitude.list_of_months:
        for day in Latitude_Longtitude.list_of_days:
            try:
                with open(f"/Users/mbahng/PycharmProjects/Coronavirus_Analysis/Data_by_Date/{month}{day}20.txt") as f:
                    for line in f:
                        if line.split(",")[1:3] == lat_long:
                            confirmed_cases.append(int(line.split(",")[3]))
            except:
                confirmed_cases.append("-")
                continue
    #Doing this so that the data from March 1st ~ March 22nd, which was not collected, are deleted.
    confirmed_cases = confirmed_cases[21:]

    #The next loop converts each list such that all the "-" are either averaged out by the other 2 variables or gone.
    for i in range(len(confirmed_cases)):
        if type(confirmed_cases[i]) is str:
            try:
                confirmed_cases[i] = (int(confirmed_cases[i - 1]) + int(confirmed_cases[i + 1])) // 2
            except:
                confirmed_cases[i] = 0
    g.write(str(confirmed_cases) + "\n")
    print(confirmed_cases)
    print(f"number_of_locations_completed: {number_of_locations_completed}")
g.close()
