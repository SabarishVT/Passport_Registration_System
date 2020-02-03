from tkinter import *
import sqlite3

window = Tk()
window.geometry('625x650')
window.configure(bg='LightCyan2')
window.title("Personal Details Registration System")


Fullname=StringVar()
gender = StringVar()
address = StringVar()
postcode = IntVar()
nation = StringVar()
mobile = IntVar()
email = StringVar()
aadhar = IntVar()
c=StringVar()
d = IntVar()
m = IntVar()
y = IntVar()

def insert():
    
    Ful= Fullname.get()
    gen = gender.get()
    add = address.get()
    pos = postcode.get()
    nat = nation.get()
    mob = mobile.get()
    ema = email.get()
    aad = aadhar.get()
    caa=c.get()
    daa = d.get()
    maa= m.get()
    yaa = y.get()
    conn = sqlite3.connect('personal_info.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('INSERT INTO Personal_registry (id,name,gender,address,postcode,nationality,mobile,dob,email,aadhar,education) VALUES (NULL,?,?,?,?,?,?,?,?,?,?)',(Ful,gen,add,pos,nat,mob,daa,ema,aad,caa))
        conn.commit()
    from tkinter import messagebox as mb
    mb.showinfo('success',"information have been added successfully")
def clear():                                                                                                                                             
        entry_1.delete(0, END)

label_1 = Label(window, text = "Name", width = 20,font=("bold",12),bg='LightCyan2')
label_1.place(x=11,y=33)

entry_1 = Entry(window,textvar=Fullname,width=35,font=("bold",12),bg='oldlace')
entry_1.place(x=185,y=33,height=25)

label_2 = Label(window, text = "Gender", width = 20,font=("bold",12),bg='LightCyan2')
label_2.place(x=16,y=75)

Radiobutton(window, text="Male",padx = 5, variable=gender, value="Male",bg='LightCyan2').place(x=185,y=77)
Radiobutton(window, text="Female",padx = 20, variable=gender, value="Female",bg='LightCyan2').place(x=265,y=77)

label_3 = Label(window, text = "Address", width = 20,font=("bold",12),bg='LightCyan2')
label_3.place(x=18,y=115)

entry_3 = Entry(window,textvar=address,width=20,font=("bold",12),bg='oldlace')
entry_3.place(x=185,y=120,height=80)

label_4 = Label(window, text = "Post Code", width = 20,font=("bold",12),bg='LightCyan2')
label_4.place(x=26,y=220)

entry_4 = Entry(window,textvar=postcode,width=15, font=("bold",12),bg='oldlace')
entry_4.place(x=185,y=220,height=25)

label_5 = Label(window, text = "Nationality", width = 20,font=("bold",12),bg='LightCyan2')
label_5.place(x=29,y=265)

Radiobutton(window, text="Indian",padx = 5, variable=nation, value="Indian",bg='LightCyan2').place(x=185,y=265)
Radiobutton(window, text="Other",padx = 5, variable=nation, value="Other",bg='LightCyan2').place(x=272,y=265)

label_6 = Label(window, text = "Mobile No", width = 20,font=("bold",12),bg='LightCyan2')
label_6.place(x=26,y=310)

entry_6 = Entry(window,textvar=mobile,width=35,font=("bold",12),bg='oldlace')
entry_6.place(x=185,y=310,height=25)

label_7 = Label(window, text = "Date of birth", width = 20,font=("bold",12),bg='LightCyan2')
label_7.place(x=37,y=355)

day = ['1', '2', '3', '4', '5' ,'6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

droplist=OptionMenu(window,d, *day)
droplist.config(width=5)
d.set('Day') 
droplist.place(x=210,y=355)

month = ['1', '2', '3', '4', '5' ,'6','7','8','9','11','12']

droplist=OptionMenu(window,m, *month)
droplist.config(width=5)
m.set('month') 
droplist.place(x=310,y=355)

year = ['1980','1981','1982','1983','1983','1984','1985','1986','1987','1988','1989',
        '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','1990',
        '2000','2001','2001','2002','2003','2004','2005','2006','2007','2008','2009',
        '2010']

droplist=OptionMenu(window,y, *year)
droplist.config(width=5)
y.set('year') 
droplist.place(x=410,y=355)

label_8 = Label(window, text = "Email", width = 20,font=("bold",12),bg='LightCyan2')
label_8.place(x=8,y=410)

entry_8 = Entry(window,textvar=email,width=35,font=("bold",12),bg='oldlace')
entry_8.place(x=185,y=410,height=25)

label_9 = Label(window, text = "Aadhar No", width = 20,font=("bold",12),bg='LightCyan2')
label_9.place(x=28,y=455)

entry_9 = Entry(window,textvar=aadhar,width=35,font=("bold",12),bg='oldlace')
entry_9.place(x=185,y=455,height=25)

label_10 = Label(window, text = "Educational qualification", width = 20,font=("bold",12),bg='LightCyan2')
label_10.place(x=83,y=500)

list1 = ['Post Graduate', 'Under Graduate', 'Higher Sec', 'SSLC', 'Other' ]

droplist=OptionMenu(window,c, *list1)
droplist.config(width=11)
c.set('Graduation') 
droplist.place(x=300,y=500)

var1 = IntVar()
Checkbutton(window, text="Accept terms and Conditions", variable=var1).place(x=87,y=560)

Button(window, text="Reset", command=clear).place(x=385,y=600)
Button(window, text="Submit", command=insert).place(x=465,y=600)

window.mainloop()
