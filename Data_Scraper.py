with open('data.txt') as f:
    g = open("test.txt", "w+")
    for line in f:
        split_line = line.split(",")
        for i in range(len(split_line)):
            if split_line[i][0:5] == "2020-" or split_line[i][3:7] == "/20 " or split_line[i][4:8] == "/20 ":
                time = split_line[i]
                latitude =  split_line[i+1]
                longtitude = split_line[i+2]
                confirmed = split_line[i+3]
                deaths = split_line[i+4]
                recovered = split_line[i+5]
                active = split_line[i+6]
                if latitude == '' or longtitude =='':
                    latitude = 0
                    longtitude = 0
                if confirmed == '':
                    confirmed = 0
                if deaths == '':
                    deaths = 0
                if recovered == '':
                    recovered = 0
                if active == '':
                    active = 0
                print([time, round(float(latitude), 3), round(float(longtitude), 3), int(confirmed), int(deaths), int(recovered), int(active)])
                g.write(time + "," + str(round(float(latitude), 3)) + ',' + str(round(float(longtitude), 3)) + ',' + str(int(confirmed)) + ',' + str(int(deaths)) + ',' + str(int(recovered)) + ',' + str(int(active)) + '\n')
                break




