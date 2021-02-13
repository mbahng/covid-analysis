'''Second Data Cleaner: Takes the case data from each location and determines which ones to keep based on:
     1. How many total cases there have been (to get a large sample of infected people for statistical accuracy)
     2. How many unrecorded values there are (too many unrecorded values may cause statistical inaccuracy)
'''

old_data = open("Second_Cleaned_Data.txt","r")
cleaned_data = open("Third_Cleaned_Data.txt","w+")
number_of_unclean_data = 0
number_of_clean_data = 0
for old_line in old_data:
    old_line_2 = old_line.split(";")[1]
    uncleaned_data = list(map(int, old_line_2.strip()[1:-1].split(", ")))
    #For data to be considered "clean," there must be 3 or few unrecorded cases and must have enough cases (at least 1000) and must have 289 days long.
    if uncleaned_data.count(0) < 2 and max(uncleaned_data) >= 20000 and len(uncleaned_data) == 289:
        cleaned_data.write(old_line)
        number_of_clean_data += 1
        print(old_line)
    else:
        number_of_unclean_data += 1

print(f"Number of clean data: {number_of_clean_data}")
print(f"Number of unclean data: {number_of_unclean_data}")