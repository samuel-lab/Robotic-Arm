import serial.tools.list_ports
import tkinter as tk
import customtkinter as ctk
import serial
import time
import json

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")

font_name = "Calibri"

window = ctk.CTk() 
window.geometry("700x700")
window.resizable(False, False)
window.title("Nastavenia")

pors_vyber_frame = ctk.CTkFrame(master=window, width=300, height=680)
pors_vyber_frame.place(x=10, y=10)


port_menu = ctk.CTkOptionMenu(master=pors_vyber_frame, width=270, values=["USB-Port:"])
port_menu.place(x=15, y= 210)

list_portov= None
def ziskaj_zariadenia_usb():
    # Získa informácie o všetkých dostupných sériových portoch
    ports = list(serial.tools.list_ports.comports())

    if not ports:
        print("Žiadne sériové porty neboli nájdené.")
    else:
        usb_ports = [port for port in ports if "usb" in port.device.lower()]
        if not usb_ports:
            print("Žiadne USB sériové porty neboli nájdené.")
        else:
            for port in usb_ports:
                #print(f"USB Port: {port.device}, Popis: {port.description}")
                list_portov = [port.device]
                print (list_portov)
                port_menu = ctk.CTkOptionMenu(master=pors_vyber_frame, width=270, values=list_portov, command=skuska_pripojenia)
                port_menu.place(x=15, y= 210)
        
            



vyhladat_button = ctk.CTkButton(master=pors_vyber_frame, text="Vyhladať zariadenia" ,width=270, command=ziskaj_zariadenia_usb, font = (font_name, 14))
vyhladat_button.place(x=15, y=50)

mainframe_main_label = ctk.CTkLabel(master=pors_vyber_frame, text="Baud rate: (odporúčaný 115200)", width= 270, font = (font_name, 14))
mainframe_main_label.place(x=15, y=100)

bits_rate_menu = ctk.CTkOptionMenu(master=pors_vyber_frame, width=270, values=["300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "31250", "38400", "57600", "115200"])
bits_rate_menu.place(x=15, y= 130)

mainframe_main_label = ctk.CTkLabel(master=pors_vyber_frame, text="USB port:", width= 270, font = (font_name, 14))
mainframe_main_label.place(x=15, y=180)


def skuska_pripojenia(port_name: str):
    print(port_name)

    ser = serial

    try:
        ser = serial.Serial(port_name, 9600, timeout=10)

        if ser.is_open:
            print ('serial open')
            print("Uložiť nastavenia")
            braudrate= bits_rate_menu.get()
            port_selected= port_name
            dictionary = {
                "port": port_selected,
                "bits_rate": braudrate,
                }
            # Serializing json
            json_object = json.dumps(dictionary, indent=4)
                
            # Writing to sample.json
            with open("setup.json", "w") as outfile:
                outfile.write(json_object)
                        
                print ('serial closed')
                ser.close()
    

    except serial.serialutil.SerialException:
        print ("exception")
    






if __name__ == '__main__':
    window.mainloop()