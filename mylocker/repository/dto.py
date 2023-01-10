class ArduinoDTO:
    def __init__(self, locker_pin, locker_port, states, size, open_):
        self.arduino_pin = locker_pin
        self.arduino_port = locker_port
        self.states = states
        self.size = size
        self.is_open = open_

class UserDTO:
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

class LockerDTO:
    def __init__(self, arduino_pin, id_, capacity, password):
        self.arduino_pin = arduino_pin
        self.id = id_
        self.capacity = capacity
        self.password = password

class HistoryDTO:
    def __init__(self, id_, arduino_pin, item_type, capacity, time_in, time_out):
        self.id = id_
        self.arduino_pin = arduino_pin
        self.item_type = item_type
        self.capacity = capacity
        self.time_in = time_in
        self.time_out = time_out

class QueryItemDTO:
    def __init__(self, item_type, duration):
        self.item_type = item_type
        self.duration = duration

class QuerySizeDTO:
    def __init__(self, size, duration):
        self.size = size
        self. duration = duration

class QueryDTO:
    def __init__(self, size, item_type, duration_):
        self.size = size
        self.item_type = item_type
        self.duration = duration_