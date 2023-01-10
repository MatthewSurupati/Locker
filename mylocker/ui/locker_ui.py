from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from mylocker.services.locker_service import *
from mylocker.services.generator import RandomIdGeerator
from mylocker.services.id_generator import *
from kink import inject, di

@inject
class Tkinterss:
    def __init__(self, locker_service: LockerService):

        self.locker_service = locker_service

    def open_close_window(self, x, y):
        y.deiconify()
        x.withdraw()
        self.center_window(800, 500, y)

    def clear_text(self, text):
        text.delete(0, END)

    def center_window(self, width, height, X):
        # get screen width and height
        screen_width = X.winfo_screenwidth()
        screen_height = X.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        X.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def seconds_to_time(self, seconds):
        hours = seconds // 3600
        seconds -= hours * 3600
        minutes = seconds // 60
        seconds -= minutes * 60
        # return f'Time left:{seconds:02d}'
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def create_Base(self):
        root = Tk()
        root.title("SchliessFach")
        root.iconbitmap("icon.ico")
        root.geometry("800x500")

        image = Image.open("SchliessFach.png")
        resize_image = image.resize((800, 500))
        bg = ImageTk.PhotoImage(resize_image)

        # create canvas
        my_canvas = Canvas(root, width=800, height=500, bd=0, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        # add a label
        my_canvas.create_text(
            95, 150, text="woof woof woof", font=("gothic", 13), fill="Black"
        )

        # add a button
        REGIS_ = Button(
            root,
            text="OPERATOR",
            command=lambda: self.operator(root),
            padx=39,
            pady=10,
            width=20,
        )
        LOCKER_ = Button(
            root,
            text="LOCKER",
            command=lambda: self.Locker_win(root),
            padx=36.4,
            pady=10,
            width=21,
        )
        Quit_ = Button(
            root, text="Quit", command=root.destroy, padx=0, pady=0, width=10, height=2
        )

        Regis_window = my_canvas.create_window(
            45, 180, width=100, anchor=NW, window=REGIS_
        )
        Locker_window = my_canvas.create_window(
            45, 235, width=100, anchor=NW, window=LOCKER_
        )
        QUIT_window = my_canvas.create_window(
            45, 290, width=100, anchor=NW, window=Quit_
        )

        self.center_window(800, 500, root)
        root.resizable(False, False)
        mainloop()

    def operator(self, X):
        Operator_ = Toplevel(X)
        X.withdraw()

        Operator_.iconbitmap("icon.ico")
        Operator_.geometry("800x500")

        image = Image.open("SchliessFach.png")
        resize_image = image.resize((800, 500))
        bg = ImageTk.PhotoImage(resize_image)

        # create canvas
        my_canvas = Canvas(Operator_, width=800, height=500, bd=0, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        # add a label
        my_canvas.create_text(
            95, 150, text="OPERATOR", font=("gothic", 13), fill="Black"
        )

        Register_ = Button(
            Operator_,
            text="Register",
            padx=36.4,
            pady=10,
            width=20,
            command=lambda: self.register(Operator_),
        )
        Unregister_ = Button(
            Operator_,
            text="Unregister",
            padx=39,
            pady=10,
            width=21,
            command=lambda: self.unregister(Operator_),
        )
        Report_ = Button(
            Operator_,
            text="Report",
            padx=39,
            pady=10,
            width=21,
            command=lambda: self.report_Base(Operator_),
        )
        back_button = Button(
            Operator_,
            text="<-----",
            command=lambda: self.open_close_window(Operator_, X),
        )

        Register__window = my_canvas.create_window(
            45, 180, width=100, anchor=NW, window=Register_
        )
        Unregister__window = my_canvas.create_window(
            45, 235, width=100, anchor=NW, window=Unregister_
        )
        Report__window = my_canvas.create_window(
            45, 290, width=100, anchor=NW, window=Report_
        )
        back1_window = my_canvas.create_window(
            45, 350, width=50, anchor=NW, window=back_button
        )

        self.center_window(800, 500, Operator_)
        Operator_.resizable(False, False)
        Operator_.mainloop()

    def register(self, X):
        REGIS_ = Toplevel(X)
        X.withdraw()

        REGIS_.iconbitmap("icon.ico")
        REGIS_.geometry("800x500")

        image = Image.open("SchliessFach.png")
        resize_image = image.resize((800, 500))
        bg = ImageTk.PhotoImage(resize_image)

        # create canvas
        my_canvas = Canvas(REGIS_, width=800, height=500, bd=0, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        # add a label
        my_canvas.create_text(
            95, 150, text="REGISTER", font=("gothic", 13), fill="Black"
        )

        # ID USER (dikasi)

        global ID, Name_entry, Email_entrty
        ID = Gen.combine()

        my_canvas.create_text(
            45, 180, text="ID Users: ", font=("gothic", 13), fill="Black"
        )
        my_canvas.create_text(155, 180, text={ID}, font=("gothic", 13), fill="Black")

        # #  ID USER INP
        # my_canvas.create_text(45, 180, text="ID Users: ", font=("gothic", 13), fill="Black")
        # REGIS_ID = Entry(REGIS_)
        # ID_window = my_canvas.create_window(120, 170, width=150, anchor=NW, window=REGIS_ID)

        #  Name
        my_canvas.create_text(45, 210, text="Name: ", font=("gothic", 13), fill="Black")
        Name_entry = Entry(REGIS_)
        Name_window = my_canvas.create_window(
            120, 200, width=150, anchor=NW, window=Name_entry
        )

        #  Name
        my_canvas.create_text(
            45, 240, text="Email: ", font=("gothic", 13), fill="Black"
        )
        Email_entry = Entry(REGIS_)
        Email_window = my_canvas.create_window(
            120, 230, width=150, anchor=NW, window=Email_entry
        )

        # # password
        # my_canvas.create_text(69, 220, text="Password: ", font=("gothic", 13), fill="Black")
        # password_entry = Entry(REGIS_, show="*")
        # password_window = my_canvas.create_window(120, 230, width=150, anchor=NW, window=password_entry)

        # # user type
        # my_canvas.create_text(60, 270, text="User Type: ", font=("gothic", 13), fill="Black")
        # choices = ['Staff', 'Student']
        # variable = StringVar(X)
        # variable.set('Student')
        #
        # User_Type = OptionMenu(REGIS_, variable, *choices)
        # User1_Type = my_canvas.create_window(120, 260,width=90, anchor=NW, window = User_Type)

        #  regis button

        Registration_button = Button(
            REGIS_,
            text="REGISTRATION",
            command=lambda: [
                (self.locker_service.add_user(ID, Name_entry.get(), Email_entry.get()))
            ],
        )

        Registration_button_window = my_canvas.create_window(
            180, 300, width=90, anchor=NW, window=Registration_button
        )

        back_button = Button(
            REGIS_, text="<--", command=lambda: self.open_close_window(REGIS_, X)
        )
        back1_window = my_canvas.create_window(
            120, 300, width=50, anchor=NW, window=back_button
        )

        self.center_window(800, 500, REGIS_)
        REGIS_.resizable(False, False)
        REGIS_.mainloop()

    def unregister(self, X):
        UNREGIS_ = Toplevel(X)
        X.withdraw()

        UNREGIS_.iconbitmap("icon.ico")
        UNREGIS_.geometry("800x500")

        image = Image.open("SchliessFach.png")
        resize_image = image.resize((800, 500))
        bg = ImageTk.PhotoImage(resize_image)

        # create canvas
        my_canvas = Canvas(UNREGIS_, width=800, height=500, bd=0, highlightthickness=0)
        my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        # add a label
        my_canvas.create_text(
            95, 150, text="UNREGISTER", font=("gothic", 13), fill="Black"
        )

        #  Name
        my_canvas.create_text(
            45, 180, text="ID User: ", font=("gothic", 13), fill="Black"
        )
        UNREGIS_ID = Entry(UNREGIS_)
        NIM_window = my_canvas.create_window(
            120, 170, width=150, anchor=NW, window=UNREGIS_ID
        )

        #  open back button
        DELETE_button = Button(
            UNREGIS_,
            text="DELETE",
            command=lambda: [self.locker_service.remove_user(UNREGIS_ID.get())],
        )

        DELETE1_window = my_canvas.create_window(
            180, 300, width=90, anchor=NW, window=DELETE_button
        )

        back_button = Button(
            UNREGIS_, text="<--", command=lambda: self.open_close_window(UNREGIS_, X)
        )
        back1_window = my_canvas.create_window(
            120, 300, width=50, anchor=NW, window=back_button
        )

        self.center_window(800, 500, UNREGIS_)
        UNREGIS_.resizable(False, False)
        UNREGIS_.mainloop()

    def report_Base(self, X):
        Report_base = Toplevel(X)
        X.withdraw()

        Report_base.iconbitmap("icon.ico")
        Report_base.geometry("800x500")

        image = Image.open("SchliessFach.png")
        resize_image = image.resize((800, 500))
        bg = ImageTk.PhotoImage(resize_image)

        # create canvas
        my_canvas = Canvas(
            Report_base, width=800, height=500, bd=0, highlightthickness=0
        )
        my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        # add a label
        my_canvas.create_text(95, 150, text="", font=("gothic", 13), fill="Black")

        # add a button
        REPORT_ = Button(
            Report_base,
            text="Show User",
            command=lambda: [self.report(Report_base)],
            padx=39,
            pady=10,
            width=24,
        )
        Query_item = Button(
            Report_base,
            text="Query Item",
            command=lambda: [self.query_item()],
            padx=36.4,
            pady=10,
            width=24,
        )
        Query_site = Button(
            Report_base,
            text="Query Size",
            command=lambda: [self.query_size()],
            padx=36.4,
            pady=10,
            width=24,
        )
        Query_item_site = Button(
            Report_base,
            text="Query I and S",
            command=lambda: [self.query_item_n_size()],
            padx=36.4,
            pady=10,
            width=24,
        )

        User_window = my_canvas.create_window(
            45, 180, width=100, anchor=NW, window=REPORT_
        )
        Query_item_window = my_canvas.create_window(
            45, 235, width=100, anchor=NW, window=Query_item
        )
        Query_site_window = my_canvas.create_window(
            45, 290, width=100, anchor=NW, window=Query_site
        )
        Query_item_and_site_window = my_canvas.create_window(
            45, 345, width=100, anchor=NW, window=Query_item_site
        )

        back_button = Button(
            Report_base,
            text="<--",
            command=lambda: self.open_close_window(Report_base, X),
        )
        back1_window = my_canvas.create_window(
            45, 450, width=50, anchor=NW, window=back_button
        )

        self.center_window(800, 500, Report_base)
        Report_base.resizable(False, False)
        mainloop()

    def query_item(self):
        return self.locker_service.query_by_item()

    def query_size(self):
        return self.locker_service.query_by_size()

    def query_item_n_size(self):
        return self.locker_service.query_by_size_and_type()

    def report(self, X):
        report = Toplevel(X)
        report.title("DOGE DATABASE")
        report.geometry("620x200")
        report.iconbitmap("icon.ico")

        # define columns
        columns = ("ID", "NAME", "EMAIL")
        tree = ttk.Treeview(report, columns=columns, show="headings")

        # define headings
        # tree.heading('NO', text='NO')
        tree.heading("ID", text="ID")
        tree.heading("NAME", text="NAME")
        tree.heading("EMAIL", text="EMAIL")

        # generate sample data
        rows = self.locker_service.get_all_user()

        for n in rows:
            tree.insert("", END, values=(n.id, n.name, n.email))

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item["values"]
                # show a message
                showinfo(title="Information", message=",".join(record))

        tree.bind("<<TreeviewSelect>>", item_selected)

        tree.grid(row=0, column=0, sticky="nsew")

        # add a scrollbar
        scrollbar = ttk.Scrollbar(report, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # run the app
        self.center_window(620, 240, report)
        report.resizable(False, False)
        report.mainloop()

    def Locker_win(self, X):
        new_win_locker = Toplevel(X)
        X.withdraw()
        new_win_locker.iconbitmap("icon.ico")
        new_win_locker.geometry("800x500")

        image = Image.open("SchliessFach.png")
        resize_image = image.resize((800, 500))
        bg = ImageTk.PhotoImage(resize_image)

        # create canvas
        my_canvas = Canvas(
            new_win_locker, width=800, height=500, bd=0, highlightthickness=0
        )
        my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        # add a label
        my_canvas.create_text(
            95, 150, text="SchliessFach", font=("gothic", 13), fill="Black"
        )

        Postman_ = Button(
            new_win_locker,
            text="Postman",
            padx=39,
            pady=10,
            width=20,
            command=lambda: self.open_new_win_Postman(new_win_locker),
        )
        Customers = Button(
            new_win_locker,
            text="Customer",
            padx=36.4,
            pady=10,
            width=21,
            command=lambda: self.open_new_win_Customer(new_win_locker),
        )
        # Quit_ = Button(new_win_locker, text="Quit", command=X.quit, padx=0, pady=0, width=10)
        back_button = Button(
            new_win_locker,
            text="<-----",
            command=lambda: [self.open_close_window(new_win_locker, X)],
        )

        Postman_window = my_canvas.create_window(
            45, 235, width=100, anchor=NW, window=Postman_
        )
        Customers_window = my_canvas.create_window(
            45, 180, width=100, anchor=NW, window=Customers
        )
        back1_window = my_canvas.create_window(
            45, 330, width=50, anchor=NW, window=back_button
        )
        # QUIT_window = my_canvas.create_window(45, 290, width=100, anchor=NW, window=Quit_)

        self.center_window(800, 500, new_win_locker)
        new_win_locker.resizable(False, False)
        new_win_locker.mainloop()

    def open_new_win_Postman(self, X):
        new_win_postman = Toplevel(X)
        X.withdraw()
        new_win_postman.iconbitmap("icon.ico")
        new_win_postman.geometry("800x500")

        image = Image.open("SchliessFach.png")
        resize_image = image.resize((800, 500))
        bg = ImageTk.PhotoImage(resize_image)

        # create canvas
        my_canvas = Canvas(
            new_win_postman, width=800, height=500, bd=0, highlightthickness=0
        )
        my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        # add a label
        my_canvas.create_text(
            95, 150, text="POSTMAN", font=("gothic", 13), fill="Black"
        )

        # username
        my_canvas.create_text(
            45, 180, text="ID User:", font=("gothic", 13), fill="Black"
        )
        Customer_name_entry = Entry(new_win_postman)
        CE_window = my_canvas.create_window(
            120, 170, width=150, anchor=NW, window=Customer_name_entry
        )

        countdown = StringVar()
        COUNTDOWN = countdown.set("00:00:00")

        def Close(seconds):
            global after
            if seconds >= 0:
                countdown.set(self.seconds_to_time(seconds))
                after = X.after(1000, lambda: Close(seconds - 1))
            else:
                COUNTDOWN = f'{countdown.set("00:00:00")} seconds left'
                X.after_cancel(after)
                self.locker_service.close_locker()

        size = StringVar()
        size.set("Large")
        # exp time
        my_canvas.create_text(
            65, 210, text="PACKAGE SIZE:", font=("gothic", 13), fill="Black"
        )
        exp_entry0 = Radiobutton(
            new_win_postman, text="LARGE", variable=size, value="Large", bg="light pink"
        )
        exp0_window = my_canvas.create_window(
            120, 200, width=80, anchor=NW, window=exp_entry0
        )
        exp_entry1 = Radiobutton(
            new_win_postman,
            text="MEDIUM",
            variable=size,
            value="Medium",
            bg="light green",
        )
        exp1_window = my_canvas.create_window(
            120, 230, width=80, anchor=NW, window=exp_entry1
        )
        exp_entry2 = Radiobutton(
            new_win_postman, text="SMALL", variable=size, value="Small", bg="light pink"
        )
        exp2_window = my_canvas.create_window(
            120, 260, width=80, anchor=NW, window=exp_entry2
        )
        # exp_entry3 = Checkbutton(new_win_postman, text="30 days", bg = "light green")
        # exp3_window = my_canvas.create_window(122, 290, width=80, anchor=NW, window =exp_entry3)

        #  untuk ambil dat pakai size.get()

        Item_type = StringVar()
        Item_type.set("Electronics")

        # Item Type
        my_canvas.create_text(
            65, 350, text="Item Type:", font=("gothic", 13), fill="White"
        )

        Item1_entry = Radiobutton(
            new_win_postman,
            text="Electronics",
            variable=Item_type,
            value="item01",
            bg="light green",
        )
        Item1_window = my_canvas.create_window(
            120, 340, width=90, anchor=NW, window=Item1_entry
        )

        Item2_entry = Radiobutton(
            new_win_postman,
            text="Foods",
            variable=Item_type,
            value="item02",
            bg="light pink",
        )
        Item2_window = my_canvas.create_window(
            120, 370, width=120, anchor=NW, window=Item2_entry
        )

        Item1_entry = Radiobutton(
            new_win_postman,
            text="Drinks",
            variable=Item_type,
            value="item03",
            bg="light green",
        )
        Item1_window = my_canvas.create_window(
            250, 340, width=90, anchor=NW, window=Item1_entry
        )

        Item1_entry = Radiobutton(
            new_win_postman,
            text="Health and care",
            variable=Item_type,
            value="item04",
            bg="light green",
        )
        Item1_window = my_canvas.create_window(
            250, 370, width=120, anchor=NW, window=Item1_entry
        )

        # open button
        open_button = Button(
            new_win_postman,
            text="OPEN LOCKER",
            command=lambda: [
                self.locker_service.drop_package(
                    Customer_name_entry.get(), size.get(), Item_type.get()
                )
            ],
        )
        Open1_window = my_canvas.create_window(
            180, 400, width=90, anchor=NW, window=open_button
        )

        close_button = Button(
            new_win_postman, text="CLOSE LOCKER", command=lambda: [Close(5)]
        )
        Open1_window = my_canvas.create_window(
            180, 430, width=90, anchor=NW, window=close_button
        )

        # Display
        label = Label(
            new_win_postman,
            textvariable=countdown,
            width=9,
            font=("calibri", 10, "bold"),
        )
        label.pack()
        label_v = my_canvas.create_window(150, 480, window=label)
        my_canvas.create_text(
            185,
            470,
            width=90,
            anchor=NW,
            text=":TIME LEFT",
            font=("gothic", 13),
            fill="White",
        )

        back_button = Button(
            new_win_postman,
            text="<-----",
            command=lambda: self.open_close_window(new_win_postman, X),
        )
        back1_window = my_canvas.create_window(
            120, 400, width=50, anchor=NW, window=back_button
        )

        self.center_window(800, 500, new_win_postman)
        new_win_postman.resizable(False, False)
        new_win_postman.mainloop()

    def open_new_win_Customer(self, X):
        #  customer window
        new_win_customer = Toplevel(X)
        X.withdraw()

        new_win_customer.iconbitmap("icon.ico")
        new_win_customer.geometry("800x500")

        image = Image.open("SchliessFach.png")
        resize_image = image.resize((800, 500))
        bg = ImageTk.PhotoImage(resize_image)

        # create canvas
        my_canvas = Canvas(
            new_win_customer, width=800, height=500, bd=0, highlightthickness=0
        )
        my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        # add a label
        my_canvas.create_text(
            95, 150, text="CUSTOMER LOGIN", font=("gothic", 13), fill="Black"
        )

        countdown = StringVar()
        COUNTDOWN = countdown.set("00:00:00")

        def Close(seconds):
            global after
            if seconds >= 0:
                countdown.set(self.seconds_to_time(seconds))
                after = X.after(1000, lambda: Close(seconds - 1))
            else:
                COUNTDOWN = f'{countdown.set("00:00:00")} seconds left'
                X.after_cancel(after)
                self.locker_service.close_locker()

        # ID
        my_canvas.create_text(
            45, 180, text="Id Users: ", font=("gothic", 13), fill="Black"
        )
        ID_entry = Entry(new_win_customer)
        ID_window = my_canvas.create_window(
            120, 170, width=150, anchor=NW, window=ID_entry
        )

        # password
        my_canvas.create_text(
            69, 210, text="Password: ", font=("gothic", 13), fill="Black"
        )
        password_entry = Entry(new_win_customer, show="*")
        password_window = my_canvas.create_window(
            120, 200, width=150, anchor=NW, window=password_entry
        )

        # open button
        #  di lambda masuin kalau 5 kali salah password
        open_button = Button(
            new_win_customer,
            text="OPEN LOCKER",
            command=lambda: [
                self.locker_service.take_package(ID_entry.get(), password_entry.get())
            ],
        )
        Open1_window = my_canvas.create_window(
            180, 230, width=90, anchor=NW, window=open_button
        )

        # Display
        label = Label(
            new_win_customer,
            textvariable=countdown,
            width=9,
            font=("calibri", 10, "bold"),
        )
        label.pack()
        label_v = my_canvas.create_window(150, 310, window=label)
        my_canvas.create_text(
            185,
            300,
            width=90,
            anchor=NW,
            text=":TIME LEFT",
            font=("gothic", 13),
            fill="White",
        )

        close_button = Button(
            new_win_customer, text="CLOSE LOCKER", command=lambda: [Close(5)]
        )
        close1_window = my_canvas.create_window(
            180, 260, width=90, anchor=NW, window=close_button
        )

        back_button = Button(
            new_win_customer,
            text="<--",
            command=lambda: [self.open_close_window(new_win_customer, X)],
        )
        back1_window = my_canvas.create_window(
            120, 230, width=50, anchor=NW, window=back_button
        )

        self.center_window(800, 500, new_win_customer)
        new_win_customer.resizable(False, False)
        new_win_customer.mainloop()

    def Celebration_window(self):
        pass


# di["db_file"] = r"C:\Users\hp\PycharmProjects\Locker\mylocker\Box"
# Tkinterss(LockerService(LockerRepository()), SubjectUser_Register(), SubjectUser_Unregister()
#           , SubjectUser_PackageArrive(), SubjectUser_WrongPassword(), SubjectUser_PostmanWrongPassword()).create_Base()