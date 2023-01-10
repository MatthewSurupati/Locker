from kink import inject, di
from mylocker.services.generator import Generator
from mylocker.services.arduinoservo import ArduinoServo
from mylocker.services.locker_service import MessageBox, LockerService


class MockPasswordGenerator(Generator):
    def generate(self):
        return "1234"


@inject
class MockArduino(ArduinoServo):
    def rotate_locker_to_0(self, pin):
        return pin

    def rotate_locker_to_90(self, pin):
        return pin


class MockMessageBox(MessageBox):
    def showinfo(self, title, message):
        return title, message

    def showerror(self, title, message):
        return title, message


dbtest = r"box_test"
di["db_file"] = dbtest
di["dbinit"] = True
di["password_"] = MockPasswordGenerator()
di["arduino_"] = MockArduino()
di["message_"] = MockMessageBox()


def test_should_return_true_when_register_new_user():
    di.clear_cache()
    service = LockerService()

    id, name, email = "Aaa01", "Matthew", "danielmatthew170@gmail.com"
    current = service.add_user(id, name, email)
    expected = True
    assert current == expected


def test_should_return_false_when_registered():
    di.clear_cache()
    service = LockerService()

    id, name, email = "Aaa02", "Daniel", "danielmatthew170@gmail.com"
    current = service.add_user(id, name, email)
    expected = False
    assert current == expected


def test_should_return_true_when_delete_user():
    di.clear_cache()
    service = LockerService()

    id = "Aaa01"
    current = service.remove_user(id)
    expected = True
    assert current == expected


def test_should_return_false_when_user_not_registered():
    di.clear_cache()
    service = LockerService()

    id = "Aaa05"
    current = service.remove_user(id)
    expected = False
    assert current == expected


def test_should_return_true_when_user_are_registered():
    di.clear_cache()
    service = LockerService()

    id, size, type = "Aaa01", "Small", "item01"
    current = service.drop_package(id, size, type)
    expected = True
    assert current == expected


def should_return_():
    pass
