from tkinter import *
import time
from customtkinter import *
#this is a basic weighing programme with a time momdule attcahed to proceed to next step of code after a specified period
#It can be employed by shop to weigh and charge for parcels

#scenario
#A shop has a fixed rate for parcels that weigh less than 10 Kgs.
#If a parcel is below 1Kg, it is eligible for free delivery.
#the fixed rate is R150
#an extra charge of R300 is applied if the parcel(s) exceed 10kgs

def calculate():
    n=name_entry_box.get()
    w=weight_entry_box.get()
    print(f"Thank you for choosing ONTI COURIERS, {n} !")
    time.sleep(3)
    print(f"Your cost will calculated shortly...")

def clear():
    name_entry_box.delete(first_index=0,last_index=END)
    weight_entry_box.delete(first_index=0, last_index=END)
    

#Custom Tkinter window/frame
window=CTk()
window.geometry("500x500")
#window title 
window.title("COURIER PRO")

#label for parcel name
name_label=CTkLabel(master=window,text="Full name",
                    text_color="maroon",font=("Calibri",20,"bold"))
name_label.pack()

#entry box(name)
name_entry_box=CTkEntry(master=window,
                   width=200,
                   font=("Aerial black",15,"bold"))
name_entry_box.pack()

#label for weight entry
weight_label=CTkLabel(master=window,text="Parcel weight (Kg)",font=("Calibri",20,"bold")
                      ,text_color="green")
weight_label.pack()

#entry box(parcel weight)
weight_entry_box=CTkEntry(master=window,
                   width=50,font=("Aerial black",15,"bold"))
weight_entry_box.pack(padx=5,pady=5)



#buttons 
calculate_button=CTkButton(master=window,
                           text="Enter",
                           font=("calibri",20,"bold"),
                           command=calculate,
                           )
calculate_button.pack()

restart_button=CTkButton(master=window,
                       text="Restart",
                       font=("Calibiri",20,"bold"),
                       fg_color="Black",
                       bg_color="Green",
                       command=clear)
restart_button.pack(padx=5,pady=5)


window.mainloop()