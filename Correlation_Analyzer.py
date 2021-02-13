from scipy.stats.stats import pearsonr
final_data = {}
list_of_locations = []
with open("Third_Cleaned_Data.txt","r") as file:
    for line in file:
        location_string = line.split(";")[0][2:-2].split("', '")
        location = list(map(float, location_string))
        location = tuple(location)
        list_of_locations.append(location)
        data_string = line.split(";")[1][1:-2].split(", ")
        data = list(map(int, data_string))
        final_data[location] = data

stats = open("Correlation_Data.txt", "w+")
w = 0
for i in range(0,len(list_of_locations)):
    for j in range(i+1,len(list_of_locations)):
        first_list = final_data[list_of_locations[i]]
        second_list = final_data[list_of_locations[j]]
        stats.write(f"Correlation of {list_of_locations[i]}, {list_of_locations[j]}: {pearsonr(first_list, second_list)[0]}\n")
        print(f"Correlation of {list_of_locations[i]}, {list_of_locations[j]}: {pearsonr(first_list, second_list)[0]}")