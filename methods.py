from bookingdetails import *
import random
from exceptions import *
from decorations import *

class Theatre:
    def __init__(self):
        self.balprice = 450
        self.platprice = 350
        self.goldprice = 280

        self.scr1sl1_bal =80
        self.scr1sl1_plat=100
        self.scr1sl1_gold=100

        self.scr1sl2_bal =80
        self.scr1sl2_plat=100
        self.scr1sl2_gold=100

        self.scr1sl3_bal =80
        self.scr1sl3_plat=100
        self.scr1sl3_gold=100

        self.scr2sl1_bal =80
        self.scr2sl1_plat=100
        self.scr2sl1_gold=100

        self.scr2sl2_bal =80
        self.scr2sl2_plat=100
        self.scr2sl2_gold=100

        self.scr2sl3_bal =80
        self.scr2sl3_plat=100
        self.scr2sl3_gold=100

    def addMovie(self):
        title=input("Enter Movie Title : ")
        while True:
            try:
                movtable1 = PrettyTable(['SCREEN','MOVIE TITLE','DURATION','RELEASE YEAR','GENRE','TIME SLOTS'])
                screen = int(input("Enter SCREEN (1 or 2) :"))
                if screen == 1:
                    duration = input("Enter Movie Duration :")
                    while True:
                        try:
                            year = int(input("Enter release year : "))
                            break
                        except ValueError:
                            print(f"{red_in}Year must be a numeric value{out}")
                    genre = input("Enter genre : ")
                    tslot = 'SLOT-1 : 12:00PM - 03:00PM\nSLOT-2 : 05:00PM - 08:00PM\nSLOT-3 : 09:00PM - 12:00PM\n\n'
                    movtable1.add_row([screen, title, duration, year, genre, tslot])
                    print(f"\n{grn_in}New Movie Added Successfully on SCREEN:1{out}\n")
                    with open("movie1.txt", "w") as fp:
                        fp.write(title)
                    with open("newmovie1.txt", 'w') as fp:
                        fp.write(str(movtable1))
                        break
                elif screen == 2:
                    movtable2 = PrettyTable(['SCREEN','MOVIE TITLE','DURATION','RELEASE YEAR','GENRE','TIME SLOTS'])
                    duration = input("Enter Movie Duration :")
                    while True:
                        try:
                            year = int(input("Enter release year : "))
                            break
                        except ValueError:
                            print(f"{red_in}Year must be a numeric value{out}")
                    genre = input("Enter genre : ")
                    tslot = 'SLOT-1 : 12:00PM - 03:00PM\nSLOT-2 : 05:00PM - 08:00PM\nSLOT-3 : 09:00PM - 12:00PM\n\n'
                    movtable2.add_row([screen, title, duration, year, genre, tslot])
                    print(f"\n{grn_in}New Movie Added Successfully on SCREEN:2{out}\n")
                    with open("movie2.txt", "w") as fp:
                        fp.write(title)
                    with open("newmovie2.txt", 'w') as fp:
                        fp.write(str(movtable2))
                        break
                else:
                    raise InvalidChoiceError
            except ValueError as v:
                print(f"{red_in}Enter Valid Screen{out}")
            except InvalidChoiceError as i:
                print(i)
    
    def delmovie(self):
       while True: 
            try:
                screen=int(input(f"Enter SCREEN of movie you want to Remove (1/2) \n{yel_in}Enter '0' to go back{out}:"))
                if screen==1:
                        print(f"\n{grn_in}Movie removed from SCREEN:1{out}\n")
                        with open ("movie1.txt","w") as fp:
                                pass
                        with open("newmovie1.txt",'w') as fp:
                                pass
                        break
                elif screen==2:
                        print(f"\n{grn_in}Movie removed from SCREEN:2{out}\n")
                        with open ("movie2.txt","w") as fp:
                                pass
                        with open("newmovie2.txt",'w') as fp:
                                pass
                        break
                elif screen==0:
                    break
                else:
                    raise ValueError
            except ValueError as v:
                print(f"{red_in}Please Enter valid screen no.(1/2){out}")
       
    def addBooking(self, b):
        with open("bookingdetails.txt", "a") as fp:
            fp.write(str(b))

    def showPrice(self):
        print(f"\n{blu_in}{tab5}{decor_tildiz}{out}")
        print(f"\n\t{tab5}BALCONY   - ₹{self.balprice}\t~\tPLATINUM  - ₹{self.platprice}\t ~\tGOLD\t- ₹{self.goldprice}")
        print(f"\n{blu_in}{tab5}{decor_tildiz}{out}\n")
        
    def showMovieDetails(self):
        with open("newmovie1.txt",'r') as fp:
                a=fp.read()
        with open("newmovie2.txt",'r') as fp:
                b=fp.read()
        print(a)
        print(b)

    def adminLogin(self):
        while True:
            try:
                username = input(f"\n\t{tab7}Enter Username: ")
                if username == 'YASHADMIN':
                    password = int(input(f"\t{tab7}Enter Password: "))
                    if password == 12345:
                        print(f"{grn_in}Login Successful{out} \u270C")
                        break
                    else:
                        raise InvalidPasswordError 
                else:
                    raise InvalidUsernameError
            except ValueError as v:
                print(f"{red_in}Password is Numeric{out}")
            except InvalidUsernameError as v:
                print(v)
            except InvalidPasswordError as v:
                print(v)

    def bookTicket(self):
        abalbook=0
        aplatbook=0
        agoldbook=0

        custname = input("\nPlease Enter Your Name: ")
        print(f"\n\n\tHello\U0001F44B",custname,f"\nPlease select a Screen from below\n")

        while True:
            try:
                t.showMovieDetails()
                screen=int(input("Select Screen : "))
                if screen ==1:
                    with open ("movie1.txt","r") as fp:
                        for x in fp:
                            movname=x
                    bookedscreen=screen
                    while True:
                        try:
                            slot=int(input("Select Slot   : "))
                            if slot not in [1,2,3]:
                                raise InvalidChoiceError
                            break
                        except InvalidChoiceError as i:
                            print(f"{red_in}{i}{out}")
                        except ValueError as v:
                            print(f"{yel_in}Select a Time Slot between 1/2/3{out}")
                        

                    time_slots = ["12:00PM - 03:00PM", "05:00PM - 08:00PM", "09:00PM - 12:00PM"]

                    if slot==1:
                        selected_slot=time_slots[slot-1]
                        print(f"\n{tab11}__________: {yel_in}Enter Seat Class{out} :_____________\n{tab11}1. Balcony         |           2. Platinum\n{tab11}3. Gold            |           4. Exit")
                        print(f"{tab11}{decor_underscore2}")
                        while True:
                            try:
                                choice = int(input("Enter Choice: "))
                                if choice not in [1,2,3,4]:
                                    raise InvalidChoiceError
                                break
                            except ValueError as v:
                                print(f"{red_in}Please Choose from given options 1/2/3/4{out}")
                            except InvalidChoiceError as i:
                                print(f"{red_in}{i}{out}")
                        
                        if choice==1:
                            if self.scr1sl1_bal!=0:
                                t.availableTicketsscr1sl1()
                                balbook=int(input('Enter no. of tickets to Book :'))
                                if balbook<=self.scr1sl1_bal:
                                    self.scr1sl1_bal-=balbook
                                    abalbook=balbook
                                    aseattype= "BL"
                                    price=self.balprice
                                    tickets_booked=balbook
                                    break
                                else: 
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl1_bal} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Balcony in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 2:
                            if self.scr1sl1_plat!=0:
                                t.availableTicketsscr1sl1()
                                platbook = int(input("Enter Number of Tickets to Book: "))
                                if platbook<=self.scr1sl1_plat:
                                    self.scr1sl1_plat -= platbook
                                    aplatbook = platbook
                                    aseattype = "PL"
                                    tickets_booked = platbook
                                    price = self.platprice                        
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl1_plat} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Platinum in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 3:
                            if self.scr1sl1_gold!=0:
                                t.availableTicketsscr1sl1()
                                goldbook = int(input("Enter Number of Tickets to Book: "))
                                if goldbook<=self.scr1sl1_gold:
                                    self.scr1sl1_gold -= goldbook
                                    agoldbook = goldbook
                                    aseattype = "GL"
                                    tickets_booked = goldbook
                                    price = self.goldprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl1_gold} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Gold in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 4:
                            print(f"{grn_in}Booking Window Closed{out}")
                            break
                        else:
                            print(f"{red_in}Enter Valid Choice{out}")

                    elif slot==2:
                        selected_slot=time_slots[slot-1]
                        print(f"\n{tab11}__________: {yel_in}Enter Seat Class{out} :_____________\n{tab11}1. Balcony         |           2. Platinum\n{tab11}3. Gold            |           4. Exit")
                        print(f"{tab11}{decor_underscore2}")
                        while True:
                            try:
                                choice = int(input("Enter Choice: "))
                                if choice not in [1,2,3,4]:
                                    raise InvalidChoiceError
                                break
                            except ValueError as v:
                                print(f"{red_in}Please Choose from given options 1/2/3/4{out}")
                            except InvalidChoiceError as i:
                                print(f"{red_in}{i}{out}")
                        if choice==1:
                            if self.scr1sl2_bal!=0:
                                t.availableTicketsscr1sl2()
                                balbook=int(input('Enter no. of tickets to Book :'))
                                if balbook<=self.scr1sl2_bal:
                                    self.scr1sl2_bal-=balbook
                                    abalbook=balbook
                                    aseattype= "BL"
                                    price=self.balprice
                                    tickets_booked=balbook
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl2_bal} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Balcony in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 2:
                            if self.scr1sl2_plat!=0:
                                t.availableTicketsscr1sl2()
                                platbook = int(input("Enter Number of Tickets to Book: "))
                                if platbook<=self.scr1sl2_plat:
                                    self.scr1sl2_plat -= platbook
                                    aplatbook = platbook
                                    aseattype = "PL"
                                    tickets_booked = platbook
                                    price = self.platprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl2_plat} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Platinum in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 3:
                            if self.scr1sl2_gold!=0:
                                t.availableTicketsscr1sl2()
                                goldbook = int(input("Enter Number of Tickets to Book: "))
                                if goldbook<=self.scr1sl2_gold:
                                    self.scr1sl2_gold -= goldbook
                                    agoldbook = goldbook
                                    aseattype = "GL"
                                    tickets_booked = goldbook
                                    price = self.goldprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl2_gold} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Gold in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 4:
                            print(f"{grn_in}Booking Window Closed{out}")
                            break
                        else:
                            print(f"{red_in}Enter Valid Choice{out}")

                    elif slot==3:
                        selected_slot=time_slots[slot-1]
                        print(f"\n{tab11}__________: {yel_in}Enter Seat Class{out} :_____________\n{tab11}1. Balcony         |           2. Platinum\n{tab11}3. Gold            |           4. Exit")
                        print(f"{tab11}{decor_underscore2}")
                        while True:
                            try:
                                choice = int(input("Enter Choice: "))
                                if choice not in [1,2,3,4]:
                                    raise InvalidChoiceError
                                break
                            except ValueError as v:
                                print(f"{red_in}Please Choose from given options 1/2/3/4{out}")
                            except InvalidChoiceError as i:
                                print(f"{red_in}{i}{out}")
                        if choice==1:
                            if self.scr1sl3_bal!=0:
                                t.availableTicketsscr1sl3()
                                balbook=int(input('Enter no. of tickets to Book :'))
                                if balbook<=self.scr1sl3_bal:
                                    self.scr1sl3_bal-=balbook
                                    abalbook=balbook
                                    aseattype= "BL"
                                    price=self.balprice
                                    tickets_booked=balbook
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl3_bal} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Balcony in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 2:
                            if self.scr1sl3_plat!=0:
                                t.availableTicketsscr1sl3()
                                platbook = int(input("Enter Number of Tickets to Book: "))
                                if platbook<=self.scr1sl3_plat:
                                    self.scr1sl3_plat -= platbook
                                    aplatbook = platbook
                                    aseattype = "PL"
                                    tickets_booked = platbook
                                    price = self.platprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl3_plat} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Platinum in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 3:
                            if self.scr1sl3_gold!=0:
                                t.availableTicketsscr1sl3()
                                goldbook = int(input("Enter Number of Tickets to Book: "))
                                if goldbook<=self.scr1sl3_gold:
                                    self.scr1sl3_gold -= goldbook
                                    agoldbook = goldbook
                                    aseattype = "GL"
                                    tickets_booked = goldbook
                                    price = self.goldprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr1sl3_gold} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Gold in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 4:
                            print(f"{grn_in}Booking Window Closed{out}")
                            break
                        else:
                            print(f"{red_in}Enter Valid Choice{out}")
                            
                elif screen ==2:
                    with open ("movie2.txt","r") as fp:
                        for x in fp:
                            movname=x
                    bookedscreen=screen
                    while True:
                        try:
                            slot=int(input("Select Slot   : "))
                            if slot not in [1,2,3]:
                                raise InvalidChoiceError
                            break
                        except InvalidChoiceError as i:
                            print(f"{red_in}{i}{out}")
                        except ValueError as v:
                            print(f"{yel_in}Select a Time Slot between 1/2/3{out}")
                    self.slot=slot
                    time_slots = ["12:00PM - 03:00PM", "05:00PM - 08:00PM", "09:00PM - 12:00PM"]
                    if slot==1:
                        selected_slot=time_slots[slot-1]
                        print(f"\n{tab11}__________: {yel_in}Enter Seat Class{out} :_____________\n{tab11}1. Balcony         |           2. Platinum\n{tab11}3. Gold            |           4. Exit")
                        print(f"{tab11}{decor_underscore2}")
                        while True:
                            try:
                                choice = int(input("Enter Choice: "))
                                if choice not in [1,2,3,4]:
                                    raise InvalidChoiceError
                                break
                            except ValueError as v:
                                print(f"{red_in}Please Choose from given options 1/2/3/4{out}")
                            except InvalidChoiceError as i:
                                print(f"{red_in}{i}{out}")
                        if choice==1:
                            if self.scr2sl1_bal!=0:
                                t.availableTicketsscr2sl1()
                                balbook=int(input('Enter no. of tickets to Book :'))
                                if balbook<=self.scr2sl1_bal:
                                    self.scr2sl1_bal-=balbook
                                    abalbook=balbook
                                    aseattype= "BL"
                                    price=self.balprice
                                    tickets_booked=balbook
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl1_bal} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Balcony in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 2:
                            if self.scr2sl1_plat !=0:
                                t.availableTicketsscr2sl1()
                                platbook = int(input("Enter Number of Tickets to Book: "))
                                if platbook<=self.scr2sl1_plat :
                                    self.scr2sl1_plat -= platbook
                                    aplatbook = platbook
                                    aseattype = "PL"
                                    tickets_booked = platbook
                                    price = self.platprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl1_plat} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Platinum in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 3:
                            if self.scr2sl1_gold!=0:
                                t.availableTicketsscr2sl1()
                                goldbook = int(input("Enter Number of Tickets to Book: "))
                                if goldbook<=self.scr2sl1_gold:
                                    self.scr2sl1_gold -= goldbook
                                    agoldbook = goldbook
                                    aseattype = "GL"
                                    tickets_booked = goldbook
                                    price = self.goldprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl1_gold} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Gold in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 4:
                            print(f"{grn_in}Booking Window Closed{out}")
                            break
                        else:
                            print(f"{red_in}Enter Valid Choice{out}")

                    elif slot==2:
                        selected_slot=time_slots[slot-1]
                        print(f"\n{tab11}__________: {yel_in}Enter Seat Class{out} :_____________\n{tab11}1. Balcony         |           2. Platinum\n{tab11}3. Gold            |           4. Exit")
                        print(f"{tab11}{decor_underscore2}")
                        while True:
                            try:
                                choice = int(input("Enter Choice: "))
                                if choice not in [1,2,3,4]:
                                    raise InvalidChoiceError
                                break
                            except ValueError as v:
                                print(f"{red_in}Please Choose from given options 1/2/3/4{out}")
                            except InvalidChoiceError as i:
                                print(f"{red_in}{i}{out}")
                        if choice==1:
                            if self.scr2sl2_bal!=0:
                                t.availableTicketsscr2sl2()
                                balbook=int(input('Enter no. of tickets to Book :'))
                                if balbook<=self.scr2sl2_bal:
                                    self.scr2sl2_bal-=balbook
                                    abalbook=balbook
                                    aseattype= "BL"
                                    price=self.balprice
                                    tickets_booked=balbook
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl2_bal} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Balcony in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        

                        elif choice == 2:
                            if self.scr2sl2_plat!=0:
                                t.availableTicketsscr2sl2()
                                platbook = int(input("Enter Number of Tickets to Book: "))
                                if platbook<=self.scr2sl2_plat:
                                    self.scr2sl2_plat -= platbook
                                    aplatbook = platbook
                                    aseattype = "PL"
                                    tickets_booked = platbook
                                    price = self.platprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl2_plat} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Platinum in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        

                        elif choice == 3:
                            if self.scr2sl2_gold!=0:
                                t.availableTicketsscr2sl2()
                                goldbook = int(input("Enter Number of Tickets to Book: "))
                                if goldbook<=self.scr2sl2_gold:
                                    self.scr2sl2_gold -= goldbook
                                    agoldbook = goldbook
                                    aseattype = "GL"
                                    tickets_booked = goldbook
                                    price = self.goldprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl2_gold} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Gold in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        

                        elif choice == 4:
                            print(f"{grn_in}Booking Window Closed{out}")
                            break
                        else:
                            print(f"{red_in}Enter Valid Choice{out}")

                    elif slot==3:
                        selected_slot=time_slots[slot-1]
                        print(f"\n{tab11}__________: {yel_in}Enter Seat Class{out} :_____________\n{tab11}1. Balcony         |           2. Platinum\n{tab11}3. Gold            |           4. Exit")
                        print(f"{tab11}{decor_underscore2}")
                        while True:
                            try:
                                choice = int(input("Enter Choice: "))
                                if choice not in [1,2,3,4]:
                                    raise InvalidChoiceError
                                break
                            except ValueError as v:
                                print(f"{red_in}Please Choose from given options 1/2/3/4{out}")
                            except InvalidChoiceError as i:
                                print(f"{red_in}{i}{out}")
                        if choice==1:
                            if self.scr2sl3_bal!=0:
                                t.availableTicketsscr2sl3()
                                balbook=int(input('Enter no. of tickets to Book :'))
                                if balbook<=self.scr2sl3_bal:
                                    self.scr2sl3_bal-=balbook
                                    abalbook=balbook
                                    aseattype= "BL"
                                    price=self.balprice
                                    tickets_booked=balbook
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl3_bal} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Balcony in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 2:
                            if self.scr2sl3_plat!=0:
                                t.availableTicketsscr2sl3()
                                platbook = int(input("Enter Number of Tickets to Book: "))
                                if platbook<=self.scr2sl3_plat:
                                    self.scr2sl3_plat -= platbook
                                    aplatbook = platbook
                                    aseattype = "PL"
                                    tickets_booked = platbook
                                    price = self.platprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl3_plat} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Platinum in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 3:
                            if self.scr2sl3_gold!=0:
                                t.availableTicketsscr2sl3()
                                goldbook = int(input("Enter Number of Tickets to Book: "))
                                if goldbook<=self.scr2sl3_gold:
                                    self.scr2sl3_gold -= goldbook
                                    agoldbook = goldbook
                                    aseattype = "GL"
                                    tickets_booked = goldbook
                                    price = self.goldprice
                                    break
                                else:
                                    print(f"\n{red_in}Thats too much!...only {self.scr2sl3_gold} tickets are left\U0001F575. \nTry booking some less tickets or choose a different time slot{out}")
                            else:
                                print(f"{red_in}No tickets left for Gold in this Time Slot\U0001F615.\nYou can try booking in other Seat class.{out}")
                        
                        elif choice == 4:
                            print(f"{grn_in}Booking Window Closed{out}")
                            break
                        else:
                            print(f"{red_in}Enter Valid Choice{out}")
                else:
                    print(f"{red_in}Select Screen 1 or 2{out}")
            except ValueError as ve:
                print(f"{red_in}choice must be numeric{out}")

        if abalbook > 0 or aplatbook > 0 or agoldbook > 0:
            print(f"\n{aseattype}: {tickets_booked}")
            total = tickets_booked * price
            print(f"COST: \u20B9{total}")
            while True:
                try:
                    bill = int(input(f"\n{yel_in}Please Pay Bill to Get Movie Tickets:{out} \u20B9"))
                    if bill != total:
                        raise InsufficientPaymentError
                    else:
                        print(f"{tab11}: {grn_in}Please Collect Your Tickets\U0001F3AB {out}:\n")
                        break
                except ValueError as v:
                    print(f"{yel_in}Please enter billing amount carefully{out}")
                except InsufficientPaymentError as i:
                    print(i)        

            print(f"{tab11}{decor_ticket}")
            print(f"{tab11}  SCRN : {bookedscreen}")
            print(f"{tab11}  Movie: {movname}")
            print(f"{tab11}  Time : {selected_slot}")
            print(f"{tab11}  Seat : {aseattype}:{tickets_booked}")
            print(f"{tab11}{decor_ticket}")

            bid = random.randint(1000, 9999)
            time=datetime.now().strftime("%H : %M %p")
            date=datetime.now().strftime("%d-%b-%Y")
            b = Bookings(bid, custname, selected_slot, movname,aseattype,tickets_booked,time,date)
            self.addBooking(b)
            table.add_row([bid,custname,selected_slot,movname,aseattype,tickets_booked,time,date])
            with open('updated.txt','w') as fp:
                fp.write(str(table))

            print(f"\n\n{decor_popcorn} {yel_in}ENJOY THE MOVIE{out}",chr(0x1F973),f"{decor_popcorn}\n\n\n\n")
        else:
            print(f"\n{yel_in}Please Book atleast 1 ticket !{out}")    

    def availableTicketsscr1sl1(self):
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")
        print(f"\n\t\t{tab7}Available Tickets for -> Screen:1 Slot:1")
        print(f"\n{tab11}BALCONY     :   {self.scr1sl1_bal}\n{tab11}PLATINUM    :   {self.scr1sl1_plat}\n{tab11}GOLD\t    :   {self.scr1sl1_gold}")
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")

    def availableTicketsscr1sl2(self):
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")
        print(f"\n\t\t{tab7}Available Tickets for -> Screen:1 Slot:2")
        print(f"\n{tab11}BALCONY     :   {self.scr1sl2_bal}\n{tab11}PLATINUM    :   {self.scr1sl2_plat}\n{tab11}GOLD\t    :   {self.scr1sl2_gold}")
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")

    def availableTicketsscr1sl3(self):
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")
        print(f"\n\t\t{tab7}Available Tickets for -> Screen:1 Slot:3")
        print(f"\n{tab11}BALCONY     :   {self.scr1sl3_bal}\n{tab11}PLATINUM    :   {self.scr1sl3_plat}\n{tab11}GOLD\t    :   {self.scr1sl3_gold}")
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")

    def availableTicketsscr2sl1(self):
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")
        print(f"\n\t\t{tab7}Available Tickets for -> Screen:2 Slot:1")
        print(f"\n{tab11}BALCONY     :   {self.scr2sl1_bal}\n{tab11}PLATINUM    :    {self.scr2sl1_plat}\n{tab11}GOLD\t   :   {self.scr2sl1_gold}")
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")

    def availableTicketsscr2sl2(self):
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")
        print(f"\n\t\t{tab7}Available Tickets for -> Screen:2 Slot:2")
        print(f"\n{tab11}BALCONY     :   {self.scr2sl2_bal}\n{tab11}PLATINUM    :   {self.scr2sl2_plat}\n{tab11}GOLD\t    :   {self.scr2sl2_gold}")
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")
    
    def availableTicketsscr2sl3(self):
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")
        print(f"\n\t\t{tab7}Available Tickets for -> Screen:2 Slot:3")
        print(f"\n{tab11}BALCONY     :   {self.scr2sl3_bal}\n{tab11}PLATINUM    :   {self.scr2sl3_plat}\n{tab11}GOLD\t    :   {self.scr2sl3_gold}")
        print(f"\n{cyn_in}{tab7}{decor_tildiz}{out}")
    
    def showoverallBooking(self):
        fp=open("bookingdetails.txt","r")
        a=fp.read()
        print(a)

    def showTodaysbooking(self):
        with open("updated.txt","r") as fp:
            a=fp.read()
            print(a)
t=Theatre()

