import tkinter as tk
import customtkinter as ctk
from subprocess import call
import time
import math
import serial
import json
#------------------------------------------------------------------------------------------------#
#------------------------------------Nastavenie main okna----------------------------------------#
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")
        
app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("1220x700")
app.resizable(False, False)
app.title("Robotická ruka ")

font_name = "Calibri"

#------------------------------------------------------------------------------------------------#
#------------------------------------------Menu frame--------------------------------------------#
menu_frame = ctk.CTkFrame(master=app, width=180, height=680)
menu_frame.place(x=10, y=10)
def ulozit_nastavenia():
    print("Nastavenia Button")
    call(["python3", "nastavenia.py"])

nastavenia_button = ctk.CTkButton(master=menu_frame, text="Nastavenia" ,width=160, command=ulozit_nastavenia, font = (font_name, 15))
nastavenia_button.place(x=10, y=640)

#------------------------------------------------------------------------------------------------#
#-------------------------------------Hlavne stredne okno----------------------------------------#
menu_tabview = ctk.CTkTabview(master= app, width=820, height=680)
menu_tabview.place(x=200, y=10)
menu_tabview.add("Domov")
menu_tabview.add("Ovládanie(X,Y,Z)")

motor1max = 100

#---Okno Domov---#

#---Okno Ovládanie(X,Y,Z)---#
 
#----------OS x GUI----------#
osXlable = ctk.CTkLabel(master=menu_tabview.tab("Ovládanie(X,Y,Z)"),text=0, width=50, font = (font_name, 15))
osXlable.place(x=630, y= 40)

def showXdata(osXslider: int):
    osXstr= (round(osXslider, 2))
    osXlable.configure(text= osXstr)

osXslider = ctk.CTkSlider(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), from_=0.1, to=360, width= 600, command=showXdata)
osXslider.place(x=20, y=50)

osXentry = ctk.CTkEntry(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), width=100, font = (font_name, 15))
osXentry.place(x=25, y= 90)

def dataosXfromEntry():
    osxfromentryint= (float(osXentry.get()))
    osXslider.set(osxfromentryint)
    osXlable.configure(text= osXentry.get())

ulozitosX = ctk.CTkButton(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), text="Uložiť os X" ,width=250, command=dataosXfromEntry, font = (font_name, 15))
ulozitosX.place(x=180, y=90)

#----------OS y GUI----------#
osylable = ctk.CTkLabel(master=menu_tabview.tab("Ovládanie(X,Y,Z)"),text=0, width=50, font = (font_name, 15))
osylable.place(x=630, y= 140)

def showYdata(osXslider: int):
    osystr= (round(osXslider, 2))
    osylable.configure(text= osystr)

osyslider = ctk.CTkSlider(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), from_=0.1, to=360, width= 600, command=showYdata)
osyslider.place(x=20, y=150)

osyentry = ctk.CTkEntry(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), width=100, font = (font_name, 15))
osyentry.place(x=25, y= 190)

def dataosYfromEntry():
    osyfromentryint= (float(osyentry.get()))
    osyslider.set(osyfromentryint)
    osylable.configure(text= osyentry.get())

ulozitosY = ctk.CTkButton(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), text="Uložiť os Y" ,width=250, command=dataosYfromEntry, font = (font_name, 15))
ulozitosY.place(x=180, y=190)

#----------OS Z GUI----------#
osZlable = ctk.CTkLabel(master=menu_tabview.tab("Ovládanie(X,Y,Z)"),text=0, width=50, font = (font_name, 15))
osZlable.place(x=630, y= 240)

def showZdata(osZslider: int):
    osZstr= (round(osZslider, 2))
    osZlable.configure(text= osZstr)

osZslider = ctk.CTkSlider(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), from_=0.1, to=360, width= 600, command=showZdata)
osZslider.place(x=20, y=250)

osZentry = ctk.CTkEntry(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), width=100, font = (font_name, 15))
osZentry.place(x=25, y= 290)

def dataosZfromEntry():
    osZfromentryint= (float(osZentry.get()))
    osZslider.set(osZfromentryint)
    osZlable.configure(text= osZentry.get())

ulozitosZ = ctk.CTkButton(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), text="Uložiť os Z" ,width=250, command=dataosZfromEntry, font = (font_name, 15))
ulozitosZ.place(x=180, y=290)

#----------SERVO GUI----------#
servolable = ctk.CTkLabel(master=menu_tabview.tab("Ovládanie(X,Y,Z)"),text=0, width=50, font = (font_name, 15))
servolable.place(x=630, y= 340)

def showservodata(servoslider: int):
    servostr= (round(servoslider, 2))
    servolable.configure(text= servostr)

servoslider = ctk.CTkSlider(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), from_=0, to=100, width= 600, command=showservodata)
servoslider.place(x=20, y=350)

servoentry = ctk.CTkEntry(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), width=100, font = (font_name, 15))
servoentry.place(x=25, y= 390)

def dataservofromEntry():
    servofromentryint= (float(servoentry.get()))
    servoslider.set(servofromentryint)
    servolable.configure(text= servoentry.get())

ulozitservo = ctk.CTkButton(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), text="Uložiť Servo" ,width=250, command=dataservofromEntry, font = (font_name, 15))
ulozitservo.place(x=180, y=390)

#--------------Switches--------------
switch_save=ctk.CTkSwitch(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), text="Uložiť dáta do ruky.", font = (font_name, 13))
switch_save.place(x=20, y=470)
switch_save.select()

switch_run=ctk.CTkSwitch(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), text="Spustiť chod ruky hned po prijatí dát.", font = (font_name, 13))
switch_run.place(x=20, y=500)
switch_run.select()

#---------speed, accel inputs--------

speedLable = ctk.CTkLabel(master=menu_tabview.tab("Ovládanie(X,Y,Z)"),text="Maximálna rýchlosť: ", width=50, font = (font_name, 15))
speedLable.place(x=25, y= 540)

speedEntry = ctk.CTkEntry(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), width=100, font = (font_name, 15), placeholder_text="4000")
speedEntry.place(x=170, y= 540)
speedEntry.insert(0, "4000")

accelLable = ctk.CTkLabel(master=menu_tabview.tab("Ovládanie(X,Y,Z)"),text="Maximálna akcelerácia: ", width=50, font = (font_name, 15))
accelLable.place(x=25, y= 580)

accelEntry = ctk.CTkEntry(master=menu_tabview.tab("Ovládanie(X,Y,Z)"), width=100, font = (font_name, 15), placeholder_text="2000")
accelEntry.place(x=195, y= 580)
accelEntry.insert(0, "2000")

#-----------------------MATH------------------------
xP = 365
yP = 0
zP = 100
L1 = 228.0  # L1 = 228mm
L2 = 136.5  # L2 = 136.5mm
theta1, theta2, phi, z = None, None, None, None 

def tvorbaSerialDat(x, y, L1, L2):

    xsqr =math.pow(x, 2)
    ysqr= math.pow(y, 2)
    L1sqr = math.pow(L1, 2)
    L2sqr = math.pow(L2, 2)

    theta2 = math.acos((xsqr + ysqr - L1sqr - L2sqr) / (2 * L1 * L2))

    if x < 0 and y < 0:
        theta2 = (-1) * theta2

    theta1 = math.atan2(x, y) - math.atan2((L2 * math.sin(theta2)), (L1 + L2 * math.cos(theta2)))

    theta2 = (-1) * theta2 * 180 / math.pi
    theta1 = theta1 * 180 / math.pi

    # Angles adjustment depending on which quadrant the final tool coordinate (x, y) is
    if x >= 0 and y >= 0:       # 1st quadrant
        theta1 = 90 - theta1
    if x < 0 and y > 0:        # 2nd quadrant
        theta1 = 90 - theta1
    if x < 0 and y < 0:        # 3rd quadrant
        theta1 = 270 - theta1
        phi = 270 - theta1 - theta2
        phi = (-1) * phi
    if x > 0 and y < 0:        # 4th quadrant
        theta1 = -90 - theta1
    if x < 0 and y == 0:
        theta1 = 270 + theta1

    # Calculate "phi" angle so gripper is parallel to the X-axis
    phi = 90 + theta1 + theta2
    phi = (-1) * phi

    # Angle adjustment depending on which quadrant the final tool coordinate (x, y) is
    if x < 0 and y < 0:       # 3rd quadrant
        phi = 270 - theta1 - theta2
    if abs(phi) > 165:
        phi = 180 + phi

    theta1 = round(theta1)
    theta2 = round(theta2)
    phi = round(phi)

    return theta1, theta2, phi

#------------------------------------------------------------------------------------------------#
#--------------------------------------comunication----------------------------------------------#
comunication_menu_frame = ctk.CTkFrame(master=app, width=180, height=680)
comunication_menu_frame.place(x=1030, y=10)

ruka_vykonava_zadanie_progressbar = ctk.CTkProgressBar(master=comunication_menu_frame, width=160 )
ruka_vykonava_zadanie_progressbar.place(x=10, y= 600)
ruka_vykonava_zadanie_progressbar.configure(mode="indeterminnate")

konzola_komunikacia=ctk.CTkTextbox(master= comunication_menu_frame, width=160, height= 100)
konzola_komunikacia.place(x= 10, y=490)

def odoslat():
    L1 = 228.0  # Replace with your actual value for L1
    L2 = 136.5  # Replace with your actual value for L2
    x_value = osXslider.get()  # Replace with your actual value for x
    y_value = osyslider.get()  # Replace with your actual value for y
    z_value = round(osZslider.get())
    servo_value=round(servoslider.get())
    run_value = switch_run.get()
    save_value = switch_save.get()

    speed_value= speedEntry.get()
    accel_value = accelEntry.get()



    theta1_result, theta2_result, phi_result = tvorbaSerialDat(x_value, y_value, L1, L2)
    print(f"Theta1: {theta1_result}, Theta2: {theta2_result}, Phi: {phi_result}, zP: {z_value}")
    USBdata=(f"{save_value},{run_value},{theta1_result},{theta2_result},{phi_result},{z_value},{servo_value},{speed_value},{accel_value}")
    print(USBdata)
    odosielam_data(USBdata)
    

def odosielam_data(data_string):
    print("Odosielam data")
    ruka_vykonava_zadanie_progressbar.start()
    konzola_komunikacia.insert("0.0", "Loading......\n" + (f"Data: {data_string}\n" + "---------------------\n"))

    # Nacitanie dat zo suboru
    with open('setup.json') as f:
        data = json.load(f)

    # Vytiahnutie hodnot 'port' a 'bits_rate'
    port = data.get('port')
    bits_rate = int(data.get('bits_rate'))

    # Kontrola, ci boli hodnoty uspesne ziskane
    if port is not None and bits_rate is not None:
        print(f'Port: {port}, Bits rate: {bits_rate}')
    else:
        print('Chyba pri ziskavani hodnot z json suboru.')

    ser = serial.Serial(port, bits_rate, timeout=None)
    ser.write(b""+(data_string))
    ser.close()
    ruka_vykonava_zadanie_progressbar.stop()

odoslat_button = ctk.CTkButton(master=comunication_menu_frame, text="Odoslať" ,width=160, command=odoslat, font = (font_name, 15))
odoslat_button.place(x=10, y=640)



if __name__ == '__main__':
    app.mainloop()
