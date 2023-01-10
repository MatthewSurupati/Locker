from tkinter import messagebox
import matplotlib.pyplot as plt
from mylocker.repository.locker_repository import LockerRepository
from kink import inject, di
import random
from mylocker.services.generator import RandomPasswordGenerator
from mylocker.services.observer import *
from mylocker.services.arduinoservo import *

class MessageBox:
    def showinfo(self, title, message):
        pass

    def showerror(self, title, message):
        pass


@inject
class RealMessageBox(MessageBox):
    def __init__(self):
        self.messagebox = messagebox

    def showinfo(self, title, message):
        self.messagebox.showinfo(title, message)

    def showerror(self, title, message):
        self.messagebox.showerror(title, message)


@inject
class LockerService:
    def __init__(
        self,
        _locker_repository: LockerRepository,
        subject_user_register: SubjectUser_Register,
        subject_user_unregister: SubjectUser_Unregister,
        subject_user_package_arrived: SubjectUser_PackageArrive,
        subject_user_wrong_password_5_times: SubjectUser_WrongPassword,
        subject_user_postman_wrong_id_5_times: SubjectUser_PostmanWrongPassword,
        subject_user_nearly_full: SubjectUser_locker_nearly_full,
        message_: RealMessageBox,
        password_: RandomPasswordGenerator,
        arduino_: ArduinoServo,
    ):

        self.locker_repository = _locker_repository
        self.subject_user_register = subject_user_register
        self.subject_user_unregister = subject_user_unregister
        self.subject_user_package_arrive = subject_user_package_arrived
        self.subject_user_wrong_password_5_times = subject_user_wrong_password_5_times
        self.subject_user_postman_wrong_id_5_times = (
            subject_user_postman_wrong_id_5_times
        )
        self.subject_user_nearly_full = subject_user_nearly_full
        self.password = password_
        self.arduino = arduino_
        self.messagebox = message_
        self.count = 0

    def add_user(self, id, name, email):
        complete = True
        all_user = list(member.email for member in self.get_all_user())
        if email in all_user:
            self.messagebox.showerror("ERROR", "You are registered")
            # print(messagebox.showerror("ERROR", "You are registered"))
            return not complete
        else:
            self.locker_repository.insert_user(id, name, email)
            self.subject_user_register.notify(Data_email(id, email))
            self.messagebox.showinfo("INFO", "Successfully registered")
            # print(messagebox.showinfo("INFO", "Successfully registered"))
            return complete

    def remove_user(self, id):
        complete = True
        all_user = list(member.id for member in self.get_all_user())
        if id not in all_user:
            self.messagebox.showerror("ERROR", "no id in database")
            return not complete
        else:
            EMAIL = self.get_email(id)
            self.subject_user_unregister.notify(Data_email(id, EMAIL))
            self.locker_repository.remove_user(id)
            self.messagebox.showinfo("INFO", "Successfully unregistered")
            return complete

    def get_all_user(self):
        return self.locker_repository.get_all_user()

    def get_all_password(self):
        return self.locker_repository.get_all_data_from_locker()

    # TAKE AND DROP PACKAGE
    def drop_package(self, id, capacity, item_type):
        complete = True
        EMAIL = self.get_email(id)
        password = self.password.generate()
        if id in list(member.id for member in self.get_all_user()):
            available = self.get_arduino_empty()

            if len(available) == 1:
                self.subject_user_nearly_full.notify(Message())

            if available == []:
                self.messagebox.showinfo(
                    "INFO",
                    "ALL LOCKER FULL ," "PLZ GO TO OPERATOR TO STORE THE PACKAGE",
                )
            done = False
            for available_locker in list(available):
                print(available_locker.size)

                if capacity == available_locker.size:
                    pin = available_locker.arduino_pin
                    if pin == 1 or pin == 3:
                        self.arduino.rotate_locker_to_90(pin)
                        self.locker_repository.update_statement_when_locker_open(
                            pin
                        )  # open door
                        self.locker_repository.update_statement_when_drop_package(pin)
                        self.locker_repository.insert_to_table_locker(
                            pin, id, capacity, password
                        )
                        self.locker_repository.insert_into_history(
                            id, pin, item_type, capacity
                        )
                        self.subject_user_package_arrive.notify(
                            Arrive_email(id, password, EMAIL, item_type, capacity)
                        )
                        self.messagebox.showinfo("INFO", "Package arrived")

                        self.count = 0
                        return complete

                    elif pin == 2 or pin == 4:
                        self.arduino.rotate_locker_to_0(pin)
                        self.locker_repository.update_statement_when_locker_open(pin)
                        self.locker_repository.update_statement_when_drop_package(pin)
                        self.locker_repository.insert_to_table_locker(
                            pin, id, capacity, password
                        )
                        self.locker_repository.insert_into_history(
                            id, pin, item_type, capacity
                        )
                        self.messagebox.showinfo("INFO", "Package arrived")
                        self.subject_user_package_arrive.notify(
                            Arrive_email(id, password, EMAIL, item_type, capacity)
                        )

                        self.count = 0
                        return complete

            if done == False:
                self.messagebox.showinfo("INFO", "NO LOCKER WITH THAT SIZE")
                return not complete
        else:
            self.count += 1
            self.messagebox.showerror("ERROR", "there is no member with that id")
            return not complete
        if self.count == 5:
            self.subject_user_postman_wrong_id_5_times.notify(Message())
            self.messagebox.showerror("ERROR", "WRONG ID 5 TIMES!!")
            self.count = 0

    def close_locker(self):
        is_open = self.get_arduino_locker_open()
        if is_open == []:
            self.messagebox.showinfo("INFO", "ALL LOCKER CLOSED")
        for locker_open in is_open:
            if locker_open.is_open == "TRUE":
                pin = locker_open.arduino_pin
                if pin == 1 or pin == 3:
                    # time.sleep(5)
                    self.arduino.rotate_locker_to_0(pin)
                    # self.rotate_locker_to_0(pin)
                    self.locker_repository.update_statement_when_locker_close(pin)
                    self.messagebox.showinfo("INFO", "Locker Closed")
                    break
                else:
                    # time.sleep(5)
                    self.arduino.rotate_locker_to_90(pin)
                    # self.rotate_locker_to_90(pin)
                    self.locker_repository.update_statement_when_locker_close(pin)
                    self.messagebox.showinfo("INFO", "Locker Closed")
                    break
            if is_open == "FALSE":
                self.messagebox.showerror("ERROR", "There is no locker open")

    def take_package(self, id_, password):
        complete = True
        EMAIL = self.get_email(id_)
        PASS = self.get_password(id_)
        if id_ in list(locker.id for locker in self.get_all_from_locker()):
            for pin in self.get_all_from_locker():
                print(pin)
                if password == pin.password:
                    pins = pin.arduino_pin
                    if pins == 1 or pins == 3:
                        self.arduino.rotate_locker_to_90(pins)
                        self.locker_repository.delete_from_table_locker(password)
                        self.locker_repository.update_statement_when_locker_open(pins)
                        self.locker_repository.update_statement_when_take_package(pins)
                        self.locker_repository.update_time_history_table(pins)
                        self.messagebox.showinfo(
                            "INFO", "U Have taken your package\n" "Have a nice day :)"
                        )
                        self.count = 0
                        return complete

                    elif pins == 2 or pins == 4:
                        self.arduino.rotate_locker_to_0(pins)
                        self.locker_repository.delete_from_table_locker(password)
                        self.locker_repository.update_statement_when_locker_open(pins)
                        self.locker_repository.update_statement_when_take_package(pins)
                        self.locker_repository.update_time_history_table(pins)
                        self.messagebox.showinfo(
                            "INFO", "U Have taken your package\n" "Have a nice day :)"
                        )
                        self.count = 0
                        return complete
                else:
                    return not complete
            self.count += 1
            self.messagebox.showerror("ERROR", "WRONG PASSWORD!!")
            if self.count == 5:
                self.subject_user_wrong_password_5_times.notify(
                    Customer_email(id_, PASS, EMAIL)
                )
                self.messagebox.showerror("ERROR", "WRONG PASSWORD 5 TIMES!!")
                self.count = 0
        else:
            self.messagebox.showerror("ERROR", "There is no id in locker")
            return not complete

        # ser = self.locker_repository.arduino(arduino_pin)
        # self.locker_repository.update_statement_when_take_package(arduino_pin)
        # for i in ser:
        #     print(f'{i.arduino_pin}, {i.arduino_port}, {i.states}, {i.size}')
        # if i.states == "FALSE":
        #     print('Locker Isi')
        # else:
        #     print('Locker Kosong')

    def get_email(self, id_):
        for member in self.get_all_user():
            if id_ == member.id:
                email = member.email
                return email

    def get_password(self, id_):
        for member in self.get_all_from_locker():
            if id_ == member.id:
                password_ = member.password
                return password_

    def get_arduino_empty(self):
        return self.locker_repository.get_all_empty()

    def get_arduino_locker_open(self):
        return self.locker_repository.get_all_locker_open()

    def get_arduino_info(self):
        return self.locker_repository.get_all_data_arduino()

    def get_all_from_locker(self):
        return self.locker_repository.get_all_data_from_locker()

    def query_by_item(self):
        query = self.locker_repository.create_query_duration_by_item_type()
        item = list(row.item_type for row in query)
        duration = list(row.duration for row in query)

        plt.scatter(item, duration)
        plt.title("Query by Item")
        plt.xlabel("Item")
        plt.ylabel("Duration")
        plt.show()

    def query_by_size(self):
        query = self.locker_repository.create_query_duration_by_size()
        size = list(row.size for row in query)
        duration = list(row.duration for row in query)

        plt.scatter(size, duration)
        plt.title("Query by Size")
        plt.xlabel("Size")
        plt.ylabel("Duration")
        plt.show()

    def query_by_size_and_type(self):
        query = self.locker_repository.create_query_duration_by_item_type_and_by_size()
        size = list(row.size for row in query)
        item = list(row.item_type for row in query)
        duration = list(row.duration for row in query)

        plt.scatter(item, duration)
        plt.scatter(size, duration)
        plt.show()