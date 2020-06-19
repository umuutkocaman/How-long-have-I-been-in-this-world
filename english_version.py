import datetime as dt
control = True
while control:
    birthDate = input("Enter your date of birth with '/' at intervals of day / month / year. Press 'q' to exit: ")
    if birthDate.lower == "q":
        break
    else:
        date = birthDate.split('/') # day, month, year separation
        #control whether or not the user entered the date with /. If it separates with something different, split will return 1 value. returns 3 values if entered correctly.
        if len(date) == 3: 
            day = date[0]
            month = date[1]
            year = date[2]

            now = dt.datetime.now() # taking today's date
            now2 = str(now) #converting day, month and year values to string type to get them separately
            thisYear = now2[:4]
            thisMonth = now2[5:7]
            today = now2[8:10]
 
            if int(year) > int(thisYear): # check whether the year after the current year has been entered
                print(f"You entered the wrong year information. Please enter {thisYear} or less.")
                continue
            elif int(month) <= 0 or int(month) > 12 : # check whether month information is entered from 1 to 12
                print("You have entered incorrect month information. Please enter a month between 1-12")
                continue
            elif int(day) <= 0: # check whether the day information is entered less than 0
                print("You cannot enter a day value of 0 or less.")
                continue

            #day control by day of the month
            elif (int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12) and int(day) > 31:
                print(f"The {month} month is 31 days. You cannot enter a higher value.")
                continue
            elif (int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11) and int(day) > 30:
                print(f"The {month} month is 30 days. You cannot enter a higher value.")
                continue

            #February day control according to leap year
            elif int(month) == 2:
                if int(year) % 4 == 0:
                    if int(year) % 100 == 0:
                        if int(year) %400 == 0 :
                            if int(day) > 29:
                                print(f"The {month}. month is 29 days this year. You cannot enter a higher value.")
                                continue
                        else:
                            if int(day) > 28:
                                print(f"The {month}. month is 28 days this year. You cannot enter a higher value.")
                                continue
                    else:
                        if int(day) > 29:
                            print(f"The {month}. month is 29 days this year. You cannot enter a higher value.")
                            continue
                else:
                    if int(day) > 28:
                        print(f"The {month}. month is 28 days this year. You cannot enter a higher value.")
                        continue

            # Month check if birthday is entered in the current year        
            elif int(year) == int(thisYear):
                if int(month) > int(thisMonth):
                    print(f"You have entered wrong month information. We're in {thisMonth}. months now. Please enter a previous date.")
                    continue
                
                #day control if the current year and month are entered as the date of birth
                elif int(month) == int(thisMonth) and int(day) > int(today):
                    print(f"You entered the wrong day information. We're on {today}. day now. Please enter a previous date.")
                    continue  
                
            while True:
                try:
                    birthTime = int(input("Do you know your birthday? Press 1 for Yes, 0 for No: "))
                    if birthTime == 1:
                        birthTime = input("Please enter your birth time in the form of 00:00 with colons between: ")
                        s = birthTime.split(':') # splitting into hours and minutes
                        hour = s[0]
                        minute = s[1]
                        detailedBirthDate = dt.datetime(int(year), int(month), int(day), int(hour), int(minute)) #converting the entered date of birth into datetime to find the date difference
                        passingTime = now - detailedBirthDate #accounts of type timedelta
                        
                        #The result of type timedelta returns data of days and seconds. Calculation of hours, minutes and seconds according to these
                        passingHour = (passingTime.days * 24 +  passingTime.seconds // 3600 ) % 24 
                        passingMinute = (passingTime.seconds % 3600) // 60
                        passingSecond = passingTime.seconds % 60
                        
                        #Printing on the screen in the type of day, hour, minute and second from birth to today
                        print(f"\nYou are in this world for {passingTime.days} days, {passingHour} hours, {passingMinute} minutes, {passingSecond} seconds.")
                        #The time passed from birth to today is different from day type, hour type, minute type, second type.
                        print(f"\nDay: {passingTime.days} \nHour: {(passingTime.days * 24 +  passingTime.seconds // 3600 )} \nMinute: {passingTime.days * 1440 + passingMinute} \nSecond: {passingTime.days * 86400 + passingTime.seconds}\n")
                        control = False
                        break

                    elif birthTime == 0:
                        detailedBirthDate = dt.datetime(int(year), int(month), int(day), 23, 59)#converting the entered date of birth into datetime to find the date difference
                        passingTime2 = now - detailedBirthDate #accounts of type timedelta 
                        
                        #The result of type timedelta returns data of days and seconds. Calculation of hours, minutes and seconds according to these
                        passingHour = (passingTime2.days * 24 +  passingTime2.seconds // 3600 ) % 24
                        passingMinute = (passingTime2.seconds % 3600) // 60
                        passingSecond = passingTime2.seconds % 60
                        
                        #Printing on the screen in the type of day, hour, minute and second from birth to today
                        #The time of birth was accepted as 23:59 and calculated accordingly. Thus, even if it is not clear, the minimum time it lives is calculated.
                        print(f"\nYou are in this world for {passingTime2.days} days and at least {passingHour} hours, {passingMinute} minutes, {passingSecond} seconds.")
                        print("\nThe hours, minutes and seconds are not exact because you have not entered your birth time. The minimum time was calculated by accepting your birth time as 23:59..\n")
                        control = False
                        break

                    else:
                        print("You entered an incorrect value.")
                        continue
                except ValueError:
                    print("You entered an incorrect value. You can only enter 0 or 1 values.")      
        else:
            print("Enter your date of birth with '/' at intervals of day / month / year.")
            continue       
