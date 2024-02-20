from tkinter import *
root = Tk()
root.geometry("500x300")

def submit_value():
    print("Your information has been saved successfully")

Label(root, text="python registration form", font="times 15 bold").grid(row=0, column=3)

name_user = Label(root, text="student name")
name_user.grid(row=1, column=2)

branch_user = Label(root, text="Branch")
branch_user.grid(row=2, column=2)

gender_user = Label(root, text="Gender")
gender_user.grid(row=3,column=2)

phone_user = Label(root, text="Contact no")
phone_user.grid(row=4, column=2)

country_user= Label(root, text="Country")
country_user.grid(row=5,column=2)

email_user= Label(root,text="email")
email_user.grid(row=6,column=2)

address_user = Label(root,text="address")
address_user.grid(row=7, column=2)

fathername_user = Label(root,text="fathername")
fathername_user.grid(row=8,column=2)

name_value = StringVar
branch_value = StringVar
gender_value = StringVar
phone_value = StringVar
country_value = StringVar
email_value = StringVar
address_value = StringVar
fathername_value = StringVar
check_value = IntVar


name_box = Entry(root, textvariable= name_value)
name_box.grid(row=1, column=3)
branch_box = Entry(root, textvariable=branch_value)
branch_box.grid(row=2, column=3)
gender_box = Entry(root, textvariable=gender_value)
gender_box.grid(row=3,column=3)
phone_box = Entry(root, textvariable=phone_value)
phone_box.grid(row=4, column=3)
country_box = Entry(root, textvariable=country_value)
country_box.grid(row=5, column=3)
email_box = Entry(root, textvariable=email_value)
email_box.grid(row=6,column=3)
address_box = Entry(root,textvariable=address_value)
address_box.grid(row=7,column=3)
fathername_box = Label(root, textvariable=fathername_value)
fathername_box.grid(row=8,column=3)

check_box = Checkbutton(text="Remember me ?",variable=name_value)
check_box.grid(row=9, column=3)

Button(text="submit", command=submit_value).grid(row=10, column=3)

root.mainloop()