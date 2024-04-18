from tkinter import *
import time
#this is a basic weighing programme with a time momdule attcahed to proceed to next step of code after a specified period
#It can be employed by shop to weigh and charge for parcels

#scenario
#A shop has a fixed rate for parcels that weigh less than 10 Kgs.
#If a parcel is below 1Kg, it is eligible for free delivery.
#the fixed rate is R150
#an extra charge of R300 is applied if the parcel(s) exceed 10kgs

#Cstom Tkinter window/frame 


#New line
def new_line():
    print ( )

#sleep module function:
def sleep(x):
    time.sleep(x)

#input function

try:
    def name_entry():
        name=str(input("Please your name: "))
        sleep(2)
        print(f"Welcome, {name}")

    def weight_entry():
        weight=float(input("Enter parcel weight(Kg)"))
        if weight <= 1:
            print("please wait while we calculate your cost ...")
            time.sleep(1)
            new_line()
            print("You are eligible for free delivery")

        elif weight <= 10:
            print("This may take some time...")
            new_line()
            sleep(3)
            print("A fixed rate of R150 will  be charged")
        
        elif weight <=20:
            print("This may take some time...")
            new_line()
            sleep(3)
            print(" An extra charge of R100 will  be charged")

        elif weight >= 20:
            print("This may take some time...")
            new_line()
            time.sleep(3)
            print("An extra charge of R300 will be applied to the fixed rate")
        

        else:
            print("Please refer to kiosk")
    
    name_entry()
    weight_entry()
    
except ValueError:
    print("Please make sure your details are valid")
    print("Syntax: Name: Ontisitse Manyeneng, Weight:60.0")
    

    



