#this is a GUI version of the pywhatkit command using Tkinter
#this app performs the task of sending whatsapp text messages to the recipients phone number
#Through the WhatsApp account that is logged in the browser



from tkinter import *
from PIL import ImageTk,Image
import pywhatkit


root = Tk()
root.geometry("600x290")
root.title("WhatsApp Message Sender")
root.configure(bg="lime")
root.resizable(False,False)
#icon=PhotoImage(file="")
#root.iconphoto(False,icon)






# Function to send the message using pywhatkit's sendwhatmsg() function
def send_message():
    message = message_entry.get()
    phone_number = phone_entry.get()
    time_str = time_entry.get()
    time_list = time_str.split(":")
    hour = int(time_list[0])
    minute = int(time_list[1])
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute, 10, True)






# Create label and entry widgets for message and phone number input
message_label = Label(root, text="ENTER MESSAGE: ",font=("Helvetica",12,'bold'),bg="lime")
message_label.place(x=30,y=40)

phone_label = Label(root, text="ENTER PHONE NUMBER: ",font=("Helvetica",12,'bold'),bg="lime")
phone_label.place(x=30,y=90)

time_label = Label(root, text="TIME IN 24-HOUR FORMAT (HH:MM): ",font=("Helvetica",12,'bold'),bg="lime")
time_label.place(x=30,y=140)


#entry widgets
message_entry = Entry(root, font=("poppins",15,"bold"),bg="#404040",fg="white")
message_entry.place(x=320,y=37)

phone_entry = Entry(root,justify="center",width=20,font=("poppins",15,"bold"),bg="#404040",fg="white")
phone_entry.place(x=320,y=87)

time_entry = Entry(root,justify="center",width=20,font=("poppins",15,"bold"),bg="#404040",fg="white")
time_entry.place(x=320,y=137)


# Create a button widget that will call the send_message() function when clicked
send_button = Button(root, text="Send Message",borderwidth=9,cursor="hand2",bg="#1ab5ef",font=("Helvetica",12,'bold'), command=send_message)
send_button.place(x=200,y=190)





root.mainloop()