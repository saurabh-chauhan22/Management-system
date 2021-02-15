from tkinter import *
import sqlite3
import time


class Welcome():
    def __init__(self, master):
        self.master = master
        self.master.geometry('1600x800+0+0')
        self.master.title("Starting Page")

        self.label1 = Label(self.master, font=('arial', 30, 'bold'), text='Competition Management System',
                            fg='red', bd=10, anchor='w').grid(row=0, column=0)
        self.label2 = Label(self.master, font=('arial', 30, 'bold'), text='Game:-Boxing', fg='#8B008B', bd=10,
                            anchor='w').grid(row=1, column=0)

        self.but = Button(self.master, padx=12, pady=12, bd=6, fg='Black', font=('arial', 12, 'bold'),
                          text='Get Started', bg='#4169E1', command=self.gotohome).place(x=300, y=450)
        self.butext = Button(self.master, padx=12, pady=12, bd=6, fg='Black', font=('arial', 12, 'bold'),
                             text='Exit', bg='#4169E1', command=self.gotoext).place(x=325, y=550)

    def gotohome(self):
        root1 = Toplevel(self.master)
        window2 = Home(root1)

    def gotoext(self):
        self.master.destroy()


class Home():
    def __init__(self, master):
        self.master = master
        self.master.geometry('1600x800+0+0')
        self.master.title("Home Page")

        self.label1 = Label(self.master, font=('arial', 30, 'bold'), text='Home', fg='red', bd=10, anchor='w').pack()
        self.label2 = Label(self.master, font=('arial', 30, 'bold'), text='Menu', fg='#8B008B', bd=10,
                            anchor='w').pack()

        self.btnrf = Button(self.master, padx=8, pady=8, bd=4, fg='Black', font=('arial', 12, 'bold'),
                            text='Registration',
                            bg='#4169E1',
                            command=self.gotorege)

        self.btnrf.place(x=620, y=200)


        self.btnsrch = Button(self.master, padx=8, pady=8, bd=4, fg='Black', font=('arial', 12, 'bold'), text='Search',
                              bg='#4169E1',
                              command=self.gotosearch)

        self.btnsrch.place(x=640, y=300)

        self.btnrslt = Button(self.master, padx=8, pady=8, bd=4, fg='Black', font=('arial', 12, 'bold'), text='Result',
                              bg='#4169E1',
                              command=self.gotoresult)

        self.btnrslt.place(x=640, y=400)

        self.btnext = Button(self.master, padx=8, pady=8, bd=4, fg='Black', font=('arial', 12, 'bold'), text='Back',
                             bg='#4169E1',
                             command=self.gotoexit)

        self.btnext.place(x=645, y=500)

    def gotorege(self):
        root5 = Toplevel(self.master)
        window2 = Rege(root5)

    def gotoclassify(self):
        root2 = Toplevel(self.master)
        window3 = Classification(root2)

    def gotosearch(self):
        root4 = Toplevel(self.master)
        window4 = Search(root4)

    def gotoresult(self):
        root6 = Toplevel(self.master)
        windowrslt = Result(root6)

    def gotoexit(self):
        self.master.destroy()


class Result():
    def __init__(self, master):
        self.master = master
        self.master.geometry("1600x800+0+0")
        self.master.title("Result")

        self.gold = StringVar()
        self.silver = StringVar()
        self.bronze1 = StringVar()
        self.bronze2 = StringVar()

        Tops = Frame(master, width=1600, height=30, relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(master, width=1600, height=800, relief=SUNKEN)
        f1.pack(side=TOP)

        self.label1 = Label(Tops, font=('arial', 32, 'bold'), text='Result', fg='red', bd=10, anchor='w').grid(
            row=2, column=2)

        self.lblet = Label(f1, font=('arial', 15, 'bold'), text="          Event          ", fg="Steel Blue", bd=10,
                           anchor='w')
        self.lblet.grid(row=1, column=2)
        self.optionList1 = (
            '                       SELECT                    ', 'Point Fighting', 'Light Contact', 'Kick Light',
            'Low Kick', 'K1 Rules', 'Musical Form');
        self.v = StringVar()
        self.v.set(self.optionList1[0])
        self.om = OptionMenu(f1, self.v, *self.optionList1)
        self.om.grid(row=1, column=3)

        self.lblwt = Label(f1, font=('arial', 15, 'bold'), text="         Weight          ", fg="Steel Blue", bd=10,
                           anchor='w')
        self.lblwt.grid(row=2, column=2)
        self.optionList2 = (
            '                       SELECT                    ', '15-18', '19-22', '22-25', '26-30', '31-35', '36-40',
            '41-45', '46-50', '51-55', '56-60', '61-65', '66-70', '71-75', '75 and Above')
        self.v = StringVar()
        self.v.set(self.optionList2[0])
        self.om = OptionMenu(f1, self.v, *self.optionList2)
        self.om.grid(row=2, column=3)

        self.lblage = Label(f1, font=('arial', 15, 'bold'), text="          Age          ", fg="Steel Blue", bd=10,
                            anchor='w')
        self.lblage.grid(row=3, column=2)
        self.optionList3 = (
            '                       SELECT                    ', ' 4 - 5 - 6 ', ' 7 - 8 - 9 ', ' 10 - 11 - 12 ',
            ' 13 - 14 - 15 ', ' 16 - 17 - 18 ', '19 and Above');
        self.v = StringVar()
        self.v.set(self.optionList3[0])
        self.om = OptionMenu(f1, self.v, *self.optionList3)
        self.om.grid(row=3, column=3)

        self.lblet = Label(f1, font=('arial', 15, 'bold'), text="          Gold Medal          ", fg="Steel Blue",
                           bd=10,
                           anchor='w')
        self.lblet.grid(row=4, column=2)
        txtname = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.gold, bd=10, insertwidth=8, bg='white',
                        justify='right')
        txtname.grid(row=4, column=3)

        self.lblet = Label(f1, font=('arial', 15, 'bold'), text="          Silver Medal          ", fg="Steel Blue",
                           bd=10,
                           anchor='w')
        self.lblet.grid(row=5, column=2)
        txtname = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.silver, bd=10, insertwidth=8, bg='white',
                        justify='right')
        txtname.grid(row=5, column=3)

        self.lblet = Label(f1, font=('arial', 15, 'bold'), text="          1st Bronze Medal          ", fg="Steel Blue",
                           bd=10,
                           anchor='w')
        self.lblet.grid(row=6, column=2)
        txtname = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.bronze1, bd=10, insertwidth=8, bg='white',
                        justify='right')
        txtname.grid(row=6, column=3)

        self.lblet = Label(f1, font=('arial', 15, 'bold'), text="          2nd Bronze Medal          ", fg="Steel Blue",
                           bd=10,
                           anchor='w')
        self.lblet.grid(row=7, column=2)
        txtname = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.bronze2, bd=10, insertwidth=8, bg='white',
                        justify='right')
        txtname.grid(row=7, column=3)

        self.btnsbmt = Button(f1, padx=8, pady=8, bd=4, fg='Black', font=('arial', 12, 'bold'), text='Submit',
                              bg='#4169E1', command=self.submit)

        self.btnsbmt.grid(row=8, column=2)

        self.btnhm = Button(f1, padx=8, pady=8, bd=4, fg='Black', font=('arial', 12, 'bold'), text='Home',
                            bg='#4169E1',
                            command=self.gotohome)

        self.btnhm.grid(row=8, column=3)

        self.sbox = Text(self.master, height=6, width=60, bg="white")
        self.sbox.place(x=480, y=500)
        self.sbox.focus_set()

    def gotohome(self):
        root3 = Toplevel(self.master)
        window2 = Home(root3)
        self.master.destroy()

    def submit(self):
        self.g = self.gold.get()
        self.s = self.silver.get()
        self.b1 = self.bronze1.get()
        self.b2 = self.bronze2.get()

        con = sqlite3.connect('kb.db')
        with con:
            c = con.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS Result (Gold text,Silver text,Bronze1 text,Bronze2 text)")
        c.execute("INSERT INTO Result (Gold,Silver,Bronze1,Bronze2) VALUES (?,?,?,?)",(self.g, self.s, self.b1, self.b2))
        print(self.g)
        con.commit()
        count = c.execute('SELECT * FROM Result WHERE Gold=?',(self.g,))
        data = c.fetchall()
        print(data)
        for self.row in data:
            if self.row == None:
                # messagebox.showinfo("Not Found", "Sorry, No such player found.")
                self.sbox.insert(END, "No Such player found in the database.")
            else:
                self.sbox.insert(END, ("Gold    =   "+self.row[0]))
                self.sbox.insert(END, ("\nSilver    =   "+self.row[1]))
                self.sbox.insert(END, ("\nBronze 1  =       "+self.row[2]))
                self.sbox.insert(END, ("\nBronze 2  =   "+self.row[3]))
        for row in c.fetchall():
            print()


        con.commit()


class Search():
    def __init__(self, master):

        self.master = master
        self.master.geometry("1600x800+0+0")
        self.master.title("Search")

        Tops = Frame(master, width=1600, height=30, relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(master, width=1600, height=800, relief=SUNKEN)
        f1.pack(side=TOP)

        self.label1 = Label(Tops, font=('arial', 30, 'bold'), text='Search Player', fg='red', bd=10, anchor='w').grid(
            row=2, column=2)

        self.name = StringVar()
        self.DOB = StringVar()

        self.lblet = Label(f1, font=('arial', 15, 'bold'), text="          Name          ", fg="Steel Blue", bd=10,
                           anchor='w')
        self.lblet.grid(row=1, column=2)
        txtname = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.name, bd=10, insertwidth=8, bg='white',
                        justify='right')
        txtname.grid(row=1, column=3)

        self.lblet = Label(f1, font=('arial', 15, 'bold'), text="          DOB          ", fg="Steel Blue", bd=10,
                           anchor='w')
        self.lblet.grid(row=2, column=2)
        txtname = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.DOB, bd=10, insertwidth=8, bg='white',
                        justify='right')
        txtname.grid(row=2, column=3)

        self.btnsrch = Button(f1, padx=8, pady=8, bd=4, fg='Black', font=('arial', 12, 'bold'), text='Search',
                              bg='#4169E1', command=self.search)

        self.btnsrch.grid(row=5, column=3)

        self.btnhm = Button(f1, padx=8, pady=8, bd=4, fg='Black', font=('arial', 12, 'bold'), text='Home',
                            bg='#4169E1',
                            command=self.gotohome)

        self.btnhm.grid(row=5, column=2)

        self.sbox = Text(self.master, height=14, width=60, bg="white")
        self.sbox.place(x=430, y=250)
        self.sbox.focus_set()

    def gotohome(self):
        root3 = Toplevel(self.master)
        window2 = Home(root3)
        self.master.destroy()

    def search(self):
        self.nm = self.name.get()
        self.dob = self.DOB.get()

        con = sqlite3.connect('kb.db')
        with con:
            c = con.cursor()

        count = c.execute('SELECT * FROM Player WHERE name=? and DOB=?', (self.nm, self.dob))
        data = c.fetchall()
        print(data)
        for self.row in data:
            if self.row == None:
                # messagebox.showinfo("Not Found", "Sorry, No such player found.")
                self.sbox.insert(END, "No Such player found in the database.")
            else:
                self.sbox.insert(END, ("Name    =   " + self.row[0]))
                self.sbox.insert(END, ("\nClub Name    =   " + self.row[1]))
                self.sbox.insert(END, ("\nSchool Name  =       " + self.row[2]))
                self.sbox.insert(END, ("\nDate of Birth   =   " + self.row[3]))
                self.sbox.insert(END, "\nAge    =   ")
                self.sbox.insert(END, self.row[4])
                self.sbox.insert(END, "\nWeight    =   ")
                self.sbox.insert(END, self.row[5])
                self.sbox.insert(END, "\nEvent  =       ")
                self.sbox.insert(END, self.row[6])
                self.sbox.insert(END, "\nMobile Number  =       ")
                self.sbox.insert(END, self.row[7])

        for row in c.fetchall():
            print()

        con.commit()


class Rege():

    def __init__(self, master):
        self.master = master
        self.master.geometry("1600x800+0+0")
        self.master.title("Competition")

        self.text_Input = StringVar()
        self.operator = ""

        # --------------------------format------------------------------------------

        Tops = Frame(master, width=1600, height=30, relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(master, width=700, height=700, relief=SUNKEN)
        f1.pack(side=LEFT)

        # --------------------------time-----------------------------------------------

        localtime = time.asctime(time.localtime(time.time()))

        # --------------------------Label---------------------------------------------

        self.lblInfo = Label(Tops, font=('arial', 30, 'bold'), text=" Pune District Boxing Championship 2019",
                             fg="#DC143C",
                             bd=10, anchor='w')
        self.lblInfo.grid(row=0, column=0)

        self.lblInfo = Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="#00FF00", bd=10, anchor='w')
        self.lblInfo.grid(row=1, column=0)

        self.lblInfo = Label(Tops, font=('arial', 25, 'bold'), text="Registration Desk", fg="black", bd=10, anchor='w')
        self.lblInfo.grid(row=2, column=0)

        self.name = StringVar()
        self.club = StringVar()
        self.school = StringVar()
        self.DOB = StringVar()
        self.age = StringVar()
        self.weight = StringVar()
        self.event = StringVar()
        self.mob_no = StringVar()

        lblname = Label(f1, font=('arial', 15, 'bold'), text="Name of Player", fg="Steel Blue", bd=10, anchor='w')
        lblname.grid(row=0, column=0)
        txtname = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.name, bd=10, insertwidth=8, bg='white',
                        justify='right')
        txtname.grid(row=0, column=1)

        lblclub = Label(f1, font=('arial', 15, 'bold'), text="Club Name", fg="Steel Blue", bd=10, anchor='w')
        lblclub.grid(row=1, column=0)
        txtclub = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.club, bd=10, insertwidth=4, bg='white',
                        justify='right')
        txtclub.grid(row=1, column=1)

        lblscl = Label(f1, font=('arial', 15, 'bold'), text="School Name", fg="Steel Blue", bd=10, anchor='w')
        lblscl.grid(row=2, column=0)
        txtscl = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.school, bd=10, insertwidth=4, bg='white',
                       justify='right')
        txtscl.grid(row=2, column=1)

        lbldob = Label(f1, font=('arial', 15, 'bold'), text="Date of Birth", fg="Steel Blue", bd=10, anchor='w')
        lbldob.grid(row=3, column=0)
        txtdob = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.DOB, bd=10, insertwidth=4, bg='white',
                       justify='right')
        txtdob.grid(row=3, column=1)

        lblage = Label(f1, font=('arial', 15, 'bold'), text="Age", fg="Steel Blue", bd=10, anchor='w')
        lblage.grid(row=4, column=0)
        txtage = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.age, bd=10, insertwidth=4, bg='white',
                       justify='right')
        txtage.grid(row=4, column=1)

        lblwt = Label(f1, font=('arial', 15, 'bold'), text="Weight", fg="Steel Blue", bd=10, anchor='w')
        lblwt.grid(row=5, column=0)
        txtwt = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.weight, bd=10, insertwidth=4, bg='white',
                      justify='right')
        txtwt.grid(row=5, column=1)

        lblet = Label(f1, font=('arial', 15, 'bold'), text="Event", fg="Steel Blue", bd=10, anchor='w')
        lblet.grid(row=6, column=0)
        txtname = Entry(f1, font=('arial',15,'bold'), textvariable=self.event, bd=10, insertwidth=4, bg='white',
                        justify='right')
        txtname.grid(row=6, column=1)

        lblmn = Label(f1, font=('arial', 15, 'bold'), text="Mobile No.", fg="Steel Blue", bd=10, anchor='w')
        lblmn.grid(row=7, column=0)
        txtmn = Entry(f1, font=('arial', 15, 'bold'), textvariable=self.mob_no, bd=10, insertwidth=4, bg='white',
                      justify='right')
        txtmn.grid(row=7, column=1)

        # -------------------------------------------f1 Button---------------------------------------

        btnRegister = Button(f1, padx=12, pady=12, bd=6, fg='Black', font=('arial', 12, 'bold'), text='Register',
                             bg='#4169E1',
                             command=self.register).grid(row=8, column=0)

        btnReset = Button(f1, padx=12, pady=12, bd=6, fg='Black', font=('arial', 12, 'bold'), text='Reset',
                          bg='#4169E1',
                          command=self.reset).grid(row=8, column=1)

        btnExit = Button(f1, padx=12, pady=12, bd=6, fg='Black', font=('arial', 12, 'bold'), text='Back', bg='#4169E1',
                         command=self.quitpg).grid(row=8, column=2)

    # ----------------------------Function------------------------------------------
        def reset(self):
            self.name.set("")
            self.club.set("")
            self.school.set("")
            self.DOB.set("")
            self.age.set("")
            self.weight.set("")
            self.event.set("")
            self.mob_no.set("")

    def register(self):
        self.nm = self.name.get()
        self.cb = self.club.get()
        self.scl = self.school.get()
        self.dob = self.DOB.get()
        self.ag = self.age.get()
        self.wt = self.weight.get()
        self.evt = self.event.get()
        self.mn = self.mob_no.get()

        con = sqlite3.connect('kb.db')
        with con:
            c = con.cursor()

        c.execute(
            "CREATE TABLE IF NOT EXISTS Player (name text,club text,school text,DOB text,age int,weight int,event text,mob_no longint)")
        c.execute("INSERT INTO Player (name,club,school,DOB,age,weight,event,mob_no) VALUES (?,?,?,?,?,?,?,?)",
                  (self.nm, self.cb, self.scl, self.dob, self.ag, self.wt, self.evt, self.mn))
        con.commit()
        self.reset()

    def quitpg(self):
        self.master.destroy()

    def reset(self):
        self.name.set("")
        self.club.set("")
        self.school.set("")
        self.DOB.set("")
        self.age.set("")
        self.weight.set("")
        self.event.set("")
        self.mob_no.set("")

def main():
    root9 = Tk()
    firstpage = Welcome(root9)
    root9.mainloop()


if __name__ == '__main__':
    main()