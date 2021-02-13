import Latitude_Longtitude
'''This data cleaner takes each row and labels with the appropriate 
latitude longtitude pair to identify its location. '''

read = open("First_Cleaned_Data.txt","r")
location_labeled_file = open("Second_Cleaned_Data.txt", "w+")
i = 0
for old_line in read:
    location_labeled_file.write(f"{Latitude_Longtitude.list_of_locations[i]};{old_line}")
    i += 1