#  convention
import smtplib
from abc import abstractmethod
from typing import List

from kink import inject


class Message:
    pass


class Observer:
    @abstractmethod
    def notified(self, message: Message):
        pass


class Observer_Register:  # FOR REGISTER
    @abstractmethod
    def notified(self, message: Message):
        pass


class Observer_Unregis:  # FOR UNREGISTER
    @abstractmethod
    def notified(self, message: Message):
        pass


class ObserverArrived:  # FOR PACKAGE ARRIVED
    @abstractmethod
    def notified(self, message: Message):
        pass


class Observer_WrongPassword5Times:  # FOR WRONG PASS 5 TIMES
    @abstractmethod
    def notified(self, message: Message):
        pass


class Observer_PostmanWrongPassword5Times:  # FOR POSTMAN WRONG PASS 5 TIMES
    @abstractmethod
    def notified(self, message: Message):
        pass


class Observer_Lockernearlyfull:  # FOR LOCKER NEARLY FULL
    @abstractmethod
    def notified(self, message: Message):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def subscribed(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message: Message):
        for n in self.observers:
            n.notified(message)


#  message
class Data_email(Message):  # DATA TYPE FOR REGISTER AND UNREGISTER
    def __init__(self, id_, email):
        self.id = id_
        self.email = email


class Arrive_email(Message):  # DATA TYPE FOR ARRIVED
    def __init__(self, id_, password, email, item_type, size):
        self.id = id_
        self.password = password
        self.email = email
        self.item_type = item_type
        self.size = size


class Customer_email(Message):  # DATA TYPE FOR CUSTOMER WRONG PASS 5 TIMES
    def __init__(self, id_, password, email):
        self.id = id_
        self.password = password
        self.email = email


#####################################################

#  Subject FOR REGISTER
@inject()
class SubjectUser_Register(Subject):
    def __init__(self, observers: List[Observer_Register]):
        self.observers = observers

    def notify(self, message: Data_email):
        for n in self.observers:
            n.notified(message)


#  observers FOR REGISTER
@inject(alias=Observer_Register)
class RegisterObserver(Observer):
    def notified(self, message: Data_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="dogolocker@gmail.com", password="DogoLock12345")
            connection.sendmail(
                from_addr="dogolocker@gmail.com",
                to_addrs=message.email,
                msg=f"Subject:Register Service "
                f"\n\n"
                f'"Konichiwa"\n'
                f"User:{message.id}\n"
                f"you have successfully registered \n"
                f"Have a nice day :)",
            )


#####################################################

#  Subject FOR UNREGISTER
@inject()
class SubjectUser_Unregister(Subject):
    def __init__(self, observers: List[Observer_Unregis]):
        self.observers = observers

    def notify(self, message: Data_email):
        for n in self.observers:
            n.notified(message)


#  observers FOR UNREGISTER
@inject(alias=Observer_Unregis)
class RegisterObserver(Observer):
    def notified(self, message: Data_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="dogolocker@gmail.com", password="DogoLock12345")
            connection.sendmail(
                from_addr="dogolocker@gmail.com",
                to_addrs=message.email,
                msg=f"Subject:Unregister Service "
                f"\n\n"
                f'"Konichiwa"\n'
                f"User:{message.id}\n"
                f"you have been unregistered \n",
            )


#####################################################

#  observers FOR ARRIVED
@inject()
class SubjectUser_PackageArrive(Subject):
    def __init__(self, observers: List[ObserverArrived]):
        self.observers = observers

    def notify(self, message: Arrive_email):
        for n in self.observers:
            n.notified(message)


#  observers FOR ARRIVED
@inject(alias=ObserverArrived)
class PCKGArrivedObserver(Observer):
    def notified(self, message: Arrive_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="dogolocker@gmail.com", password="DogoLock12345")
            connection.sendmail(
                from_addr="dogolocker@gmail.com",
                to_addrs=message.email,
                msg=f"Subject:Your Package has Arrived "
                f"\n\n"
                f'"Konichiwa"\n'
                f"User:{message.id}\n"
                f"your package has arrived \n"
                f"you can open with this password: {message.password} \n"
                f"your package type: {message.item_type} and size: {message.size}"
                f"Have a nice day :)",
            )


#####################################################

#  observers FOR WRONG PASS 5 TIMES
@inject()
class SubjectUser_WrongPassword(Subject):
    def __init__(self, observers: List[Observer_WrongPassword5Times]):
        self.observers = observers

    def notify(self, message: Customer_email):
        for n in self.observers:
            n.notified(message)


#  observers FOR WRONG PASS 5 TIMES
@inject(alias=Observer_WrongPassword5Times)
class PCKGArrivedObserver(Observer):
    def notified(self, message: Customer_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="dogolocker@gmail.com", password="DogoLock12345")
            connection.sendmail(
                from_addr="dogolocker@gmail.com",
                to_addrs=message.email,
                msg=f"Subject:Wrong password 5 times "
                f"\n\n"
                f'"Konichiwa"\n'
                f"User:{message.id}\n"
                f"You have inputed a wrong password 5 times\n"
                f"\n"
                f"Remember \n"
                f"password :{message.password} \n"
                f"Have a nice day :)",
            )


#####################################################

#  observers FOR POSTMAN WRONG PASS 5 TIMES
@inject()
class SubjectUser_PostmanWrongPassword(Subject):
    def __init__(self, observers: List[Observer_PostmanWrongPassword5Times]):
        self.observers = observers

    def notify(self, message: Message):
        for n in self.observers:
            n.notified(message)


#  observers FOR POSTMAN WRONG PASS 5 TIMES
@inject(alias=Observer_PostmanWrongPassword5Times)
class PCKGArrivedObserver(Observer):
    def notified(self, message: Message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="customersaly341@gmail.com", password="Saly12345")
            connection.sendmail(
                from_addr="customersaly341@gmail.com",
                to_addrs="dogolocker@gmail.com",
                msg=f"Subject:Wrong id 5 times "
                f"\n\n"
                f'"Konichiwa"\n'
                f" Postman have inputted a wrong id for 5 times\n",
            )


#####################################################

#  observers FOR LOCKER NEARLY FULL
@inject()
class SubjectUser_locker_nearly_full(Subject):
    def init(self, observers: List[Observer_Lockernearlyfull]):
        self.observers = observers

    def notify(self, message: Message):
        for n in self.observers:
            n.notified(message)


#  observers FOR LOCKER NEARLY FULL
@inject(alias=Observer_Lockernearlyfull)
class Locker_fullObserver(Observer):
    def notified(self, message: Message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="customersaly341@gmail.com", password="Saly12345")
            connection.sendmail(
                from_addr="customersaly341@gmail.com",
                to_addrs="dogolocker@gmail.com",
                msg=f"Subject:Your Package has Arrived "
                f"\n\n"
                f'"Konichiwa"\n'
                f"Locker is nearly full \n"
                f"Have a nice day :)",
            )