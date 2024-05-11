from methods import *
if __name__=="__main__":
    while True:
        try: 
            print(f"\n{yel_in}{decor_equal}{out}\U0001F3AC{mag_in} Welcome To YASH CINEMAS{out}\U0001F3AC{yel_in}{decor_equal}{out}")
            print(f"\n{tab5}| 1. Login as ADMIN     |       2. Continue as User     |       3. Close Terminal  |")
            print(f"{tab5}+{decor_hyphen}----+")
            choice=0
            choice=int(input(f"\t{tab7} Please Enter Your Choice : "))
            if choice<=0 or choice>3 :
                raise InvalidChoiceError 
        except ValueError as v:
            print(f"\n{red_in}Please Enter Numeric choice{out}")
        except InvalidChoiceError as i:
            print(i)

        print(f"\t{tab7}{decor_ticket}")

        if choice==1:
            t.adminLogin()
            while True:
                try:
                    print(f"\n{tab7}\t\t{decor_underscore3} : {yel_in}Please make a choice from below{out} :\U0001F447 {decor_underscore3}")
                    print(f"\n{tab7}\t\t1. Show Seats Available          |           2. Show Ticket Prices\n")
                    print(f"\t{tab7}\t3. Show Movie Details            |           4. Show Bookings\n")
                    print(f"\t{tab7}\t5. Update Movies                 |           6. LogOut\n")
                    print(f"\t{tab7}\t{decor_underscore}")
                    choice=int(input('Enter Your Choice : '))
                    if choice==1:
                        print(f"\n\t\t{tab7}{decor_underscore3} : {yel_in}Please make a choice from below{out} :\U0001F447 {decor_underscore3}")
                        print(f"\n\t{tab7}1. SCREEN:1-SLOT:1     |       2. SCREEN:1-SLOT:2      |       3. SCREEN:1-SLOT:3\n\n\t{tab7}4. SCREEN:2-SLOT:1     |       5. SCREEN:2-SLOT:2      |       6. SCREEN:2-SLOT:3")
                        print(f"\t\t{tab7}{decor_underscore}")
                        while True:
                            try:
                                choice=int(input("\nSelect Screen & Slot to check Seat Availability : "))
                                if choice==1:
                                    t.availableTicketsscr1sl1()
                                    break
                                elif choice==2:
                                    t.availableTicketsscr1sl2()
                                    break
                                elif choice==3:
                                    t.availableTicketsscr1sl3()
                                    break
                                elif choice==4:
                                    t.availableTicketsscr2sl1()
                                    break
                                elif choice==5:
                                    t.availableTicketsscr2sl2()
                                    break
                                elif choice==6:
                                    t.availableTicketsscr2sl3()
                                    break
                                else:
                                    print(f"\n{red_in}Please Enter correct Option{out}")
                            except ValueError as v:
                                print(f"{red_in}Please choose a Numeric option{out}")
                    elif choice==2:
                        t.showPrice()
                    elif choice==3:
                        t.showMovieDetails()
                    elif choice==4:
                        print(f"\n\t\t{tab7}{decor_underscore3} : {yel_in}Please make a choice from below{out} :\U0001F447 {decor_underscore3}")
                        print(f"\n\t\t{tab7}1. Check Todays Bookings  |  2. Check Overall Booking | 3. << Back ")
                        print(f"\t\t{tab7}{decor_underscore}")
                        while True:
                            try:
                                ch=int(input("Enter Your Choice : "))
                                if ch==1:
                                    t.showTodaysbooking()
                                    break
                                elif ch==2:
                                    t.showoverallBooking()
                                    break
                                elif ch==3:
                                    break
                                else:
                                    print(f"\n{red_in}Please Enter Valid Choice{out}")
                            except ValueError as v:
                                print(f"{red_in}Please choose a Numeric option{out}")

                    elif choice==5:
                        print(f"\t\t{tab7}{decor_underscore}")
                        print(f"\n\t\t{tab7}1. Remove a Movie      |     2. Add New Movie     |     3.<< Back \n")
                        print(f"\t\t{tab7}{decor_underscore}")
                        while True:
                            try:
                                choice=int(input('Enter Your Choice : '))
                                if choice==1:
                                    t.delmovie()
                                    break
                                elif choice==2:
                                    t.addMovie()
                                    break
                                elif choice==3:
                                    break
                                else:
                                    print(f"{red_in}Please choose option between 1 / 2 / 3{out}")
                            except ValueError as v:
                                print(f"{red_in}Please choose a Numeric option{out}")
                    elif choice==6:
                        print(f"{grn_in}Logged Out Successfully !{out}")
                        break
                    else:
                        raise InvalidChoiceError
                except ValueError as v:
                    print(f"\n{red_in}Please Enter Numeric choice{out}")
                except InvalidChoiceError as i:
                    print(i)
        elif choice==2:
            while True:
                
                print(f"\n{tab7}{decor_underscore3} : {yel_in}Please make a choice from below{out} :\U0001F447 {decor_underscore3}")
                print(f"\n{tab7}1. Show Movie Details          |           2. Show Ticket Prices\n")
                print(f"{tab7}3. Book Ticket                 |           4. EXIT")
                print(f"{tab7}{decor_underscore}")
                try:
                    choice=int(input('Enter Your Choice : '))
                    if choice==1:
                        t.showMovieDetails()
                    elif choice==2:
                        t.showPrice()
                    elif choice==3:
                        t.bookTicket()
                    elif choice==4:
                        print(f"{grn_in}Exited Succesfully{out}")
                        break
                    else:
                        raise InvalidChoiceError
                except ValueError as v:
                    print(f"\n{red_in}Please Enter a Numeric choice{out}")
                except InvalidChoiceError as i:
                    print(i)
        elif choice==3:
            print(f"\n\n{tab7}\U0001F4FD \U0001F3AC  '{cyn_in}Hum hai rahi pyar ke'...'fir milenge'...'chalte chalte{out}'  \U0001F3AC \U0001F4FD")
            print(f"\n\n\t{mag_in}{decor_equal}::: GOOD BYE :::{decor_equal}{out}\n\n\n")
            break
