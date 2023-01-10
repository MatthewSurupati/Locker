import sqlite3
from sqlite3 import Error
from mylocker.repository.dto import *
from kink import inject, di
import uuid

@inject
class LockerRepository:
    def __init__(self, db_file, dbinit):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.dbinit(dbinit)

    def dbinit(self, dbinit = False):
        if dbinit == True:
            c = self.conn.cursor()
            drop_table_member = """
            drop table if exists member
            """
            c. execute(drop_table_member)

            create_table_member = """
            create table member(
            id      text not null primary key,
            name    text,
            email   text
            );
            """
            c.execute(create_table_member)

            drop_table_arduino = """
            drop table if exists arduino
            """
            c.execute(drop_table_arduino)

            create_table_arduino = """
            create table arduino(
            arduino_pin     integer not null primary key,
            arduino_port    text not null default COM3,
            states          text not null default "TRUE",
            size            text not null,
            is_open         text not null default "FALSE"
            );
            """
            c.execute(create_table_arduino)

            insert_into_arduino = """
            insert into arduino(arduino_pin, size) values
            (1, "Large"),
            (2, "Large"),
            (3, "Medium"),
            (4, "Small");
            """
            c.execute(insert_into_arduino)
            self.conn.commit()

            drop_table_locker = """
            drop table if exists locker
            """
            c.execute(drop_table_locker)

            create_table_locker = """
            create table locker(
            arduino_pin     integer not null,
            id              text not null,
            capacity        text not null,
            password        text not null 
            );
            """
            c.execute(create_table_locker)

            drop_table_history = """
            drop table if exists history
            """
            c.execute(drop_table_history)

            create_table_history = """
            create table history(
            id              text,
            arduino_pin     text,
            id_item         text,
            capacity        text,
            time_in         text default (datetime('now', 'localtime')),
            time_out        text default (datetime('now', 'localtime'))
            );
            """
            c.execute(create_table_history)

            drop_table_item = """
            drop table if exists item
            """
            c.execute(drop_table_item)

            create_table_item = """
            create table item(
            id_item     text not null primary key,
            type        text not null
            );
            """
            c.execute(create_table_item)

            insert_into_item = """
            insert into item values
            ('item01', 'Electronic'),
            ('item02', 'Foods'),
            ('item03', 'Drinks'),
            ('item04', 'Health and Care');
            """
            c.execute(insert_into_item)
            self.conn.commit()
            return True
        return False

    #Insert Data
    def insert_user(self, id, name, email):
        c = self.conn.cursor()

        insert_user = """
        insert into member
              value (?, ?, ?)
        """
        c.execute(insert_user, (id, name, email,))
        self.conn.commit()

    #Remove Data User
    def remove_user(self, id):
        c = self.conn.cursor()

        remove_student = """
        delete from member
              where id = ?
        """
        c.execute(remove_student, (id,))
        self.conn.commit()

    #Get All User Data
    def get_all_user(self):
        c = self.conn.cursor()

        gel_all_user = """
        select * from member
        """

        c.execute(gel_all_user)
        rows = c.fetchall()

        returned_user_dto = []
        for id_, name, email in rows:
            dto = UserDTO(id_, name, email)
            returned_user_dto.append(dto)
        return returned_user_dto

    #Arduino
    def arduino(self, arduiono_pin):
        c = self.conn.cursor()

        open_locker = """
        select *
          from arduino
         where arduino_pin = ?
        """

        c.execute(open_locker, (arduiono_pin,))
        rows = c.fetchall()

        returned_arduino_dto = []
        for pin, port, state, size, status in rows:
            dto = ArduinoDTO(pin, port, state, size, status)
            returned_arduino_dto.append(dto)
        return returned_arduino_dto

    def get_all_empty(self):
        c = self.conn.cursor()
        get_all_box = """
        select *
          from arduino
         where states = "TRUE"
        """
        c.execute(get_all_box)
        rows = c.fetchall()

        returned_arduino_dto = []
        for pin, port, state, size, status in rows:
            dto = ArduinoDTO(pin, port, state, size, status)
            returned_arduino_dto.append(dto)
        return returned_arduino_dto

    def get_all_data_arduino(self):
        c = self.conn.cursor()

        get_info_locker = """
        select * from arduino
        """
        c.execute(get_info_locker)
        rows = c.fetchall()

        returned_arduino_dto = []
        for pin, port, state, size, status in rows:
            dto = ArduinoDTO(pin, port, state, size, status)
            returned_arduino_dto.append(dto)
        return returned_arduino_dto

    def get_all_locker_open(self):
        c = self.conn.cursor()

        get_all_box = """
        select * from arduino
        where is_open = "TRUE"
        """
        c.execute(get_all_box)
        rows = c.fetchall()

        returned_arduino_dto = []
        for pin, port, state, size, status in rows:
            dto = ArduinoDTO(pin, port, state, size, status)
            returned_arduino_dto.append(dto)
        return returned_arduino_dto

    def update_statement_when_locker_open(self, arduino_pin):
        c = self.conn.cursor()

        change_statement = """
        update arduino
           set is_open = 'TRUE'
         where arduino_pin = ?
        """
        c.execute(change_statement, (arduino_pin,))
        self.conn.commit()

    def update_statement_when_lcoker_close(self, arduino_pin):
        c = self.conn.cursor()

        change_statement = """
                update arduino
                   set is_open = 'FALSE'
                 where arduino_pin = ?
                """
        c.execute(change_statement, (arduino_pin,))
        self.conn.commit()

    def update_statement_when_drop_package(self, arduino_pin):
        c = self.conn.cursor()
        change_statement = """
        update arduino
           set states = "FALSE"
         where arduino_pin = ?
        """
        c.execute(change_statement, (arduino_pin,))
        # print(date)
        self.conn.commit()

    def update_statement_when_take_package(self, arduino_pin):
        c = self.conn.cursor()
        change_statement = """
        update arduino
           set states = 'TRUE'
         where arduino_pin = ?
        """
        c. execute(change_statement, (arduino_pin,))
        self.conn.commit()

    def insert_into_table_locker(self, arduino_pin, id, capacity, password):
        c = self.conn.cursor()
        insert_into_locker = """
        insert into locker values(?, ?, ?, ?)
        """
        c.execute(insert_into_locker, (arduino_pin, id, capacity,password,))
        self.conn.commit()

    def delete_from_table_locker(self, password):
        c = self.conn.cursor()
        delete_from_locker = """
        delete from locker
              where password = ?
        """
        c.execute(delete_from_locker, (password,))
        self.conn.commit()

    def get_all_data_from_locker(self):
        c = self.conn.cursor()
        get_all_data_from_locker = """
        select * from locker
        """

        c.execute(get_all_data_from_locker)
        rows = c.fetchall()

        returned_locker_dto = []
        for pin, id, capacity, password in rows:
            dto = LockerDTO(pin, id, capacity,password)
            returned_locker_dto.append(dto)
        return returned_locker_dto

    def insert_into_history(self, id, arduino_pin, id_item, capacity):
        c = self.conn.cursor()

        insert_inot_history = """
        insert into history(id, arduino_pin, id_item, capacity)
             values (?, ?, ?, ?)
        """

        c.execute(insert_inot_history, (id, arduino_pin, id_item, capacity,))
        self.conn.commit()

    def update_time_history_table(self, arduino_pin):
        c = self.conn.cursor()
        update_time_history = """
        update  history
           set  time_out = (datetime('now', 'localtime'))
         where  time_in = time_out and arduino_pin = ?
        """
        c.execute(update_time_history, (arduino_pin,))
        self.conn.commit()

    def get_history_info(self):
        c = self.conn.cursor()

        get_history_info = """
        select * from history
        """
        c.execute(get_history_info)
        rows = c.fetchall()

        returned_history_dto = []
        for (id, pin, type, capacity, in_, out) in rows:
            dto = HistoryDTO(id, pin, type, capacity, in_, out)
            returned_history_dto.append(dto)
        return returned_history_dto

    #Create Query for Show some data to operator
    def create_query_duration_by_item_type(self):
        c = self.conn.cursor()

        duration_by_type = """
           SELECT type, ROUND((julianday(time_out) - julianday(time_in)) * 1440) AS duration
             FROM item INNER JOIN history ON item.id_item = history.id_item
           """
        c.execute(duration_by_type)
        rows = c.fetchall()

        returned_query_dto = []
        for i, j in rows:
            dto = QueryItemDTO(i, j)
            returned_query_dto.append(dto)

        return returned_query_dto

    def create_query_duration_by_size(self):
        c = self.conn.cursor()

        duration_by_size = """
           SELECT size, ROUND((julianday(time_out) - julianday(time_in)) * 1440) AS duration
             FROM arduino INNER JOIN history ON arduino.arduino_pin = history.arduino_pin
           """
        c.execute(duration_by_size)
        rows = c.fetchall()

        returened_query_dto = []
        for i, j in rows:
            dto = QuerySizeDTO(i, j)
            returened_query_dto.append(dto)

        return returened_query_dto

    def create_query_duration_by_item_type_and_by_size(self):
        c = self.conn.cursor()

        duration_by_item_and_size = """
           SELECT type, size, ROUND((julianday(time_out) - julianday(time_in)) * 86400)/60 AS duration
             FROM item INNER JOIN history ON item.id_item = history.id_item
            INNER JOIN arduino ON arduino.arduino_pin = history.arduino_pin
           """

        c.execute(duration_by_item_and_size)
        rows = c.fetchall()

        returened_query_dto = []
        for i, j, k in rows:
            dto = QueryDTO(i, j, k)
            returened_query_dto.append(dto)

        return returened_query_dto