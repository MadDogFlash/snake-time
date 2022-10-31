def tempCheck(temp):
    
    strSeason="?"

    

    if (temp<=40):

        strSeason="w"

    elif (temp>=41 and temp<66):

        strSeason="f"

    elif (temp>=66 and temp<=80):

        strSeason="sp"

    else:

        strSeason="s"

    

    return(strSeason)



####################################################

cities = ["Moscow","London", "Seoul","Tokyo","Mumbai","Dubai","Toronto","Stockholm","Oslo","Wellington"]

temperature = [65, 68, 90, 25, 82, 67, 70, 30, 91, 72]

season = ["s", "sp", "f", "w", "w", "s", "sp", "s", "f", "w"]







for i in range(10):

    print(cities[i] + " " + str(temperature[i]) + " " + str(season[i]))

    

    strSeason = tempCheck(temperature[i])

    if (season[i]!=strSeason):

        print(" should be " + strSeason )

    print("------------------------------------------")