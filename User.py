import sqlite3
from datetime import datetime

class User:

    def __init__(self): #settings in the top
        self.payrate = 1
        self.taxrate = 1

        self.items = []#array for shifts
        self.rules = [] #array for rules
        self.startRange = datetime.now().strftime("%Y-%m-%d")
        self.endRange = datetime.now().strftime("%Y-%m-%d")
        self.Uid = 1


    def create_db(self): #create two tables for shifts and settings
        self.connection = sqlite3.connect("shifts.db", check_same_thread=False) #connect to the database
        self.cursor = self.connection.cursor() #create a cursor

        sql_command = """ CREATE TABLE IF NOT EXISTS shifts ( 
                Sid INTEGER PRIMARY KEY AUTOINCREMENT,
                Uid INTEGER NOT NULL,
                Day varchar(255) NOT NULL,
                Date INTEGER(255) NOT NULL,
                Start varchar(255) NOT NULL,
                End varchar(255) NOT NULL);"""


        sql_command2 = """ CREATE TABLE IF NOT EXISTS users ( 
                Uid INTEGER PRIMARY KEY,
                Payrate INTEGER NOT NULL,
                Taxrate INTEGER NOT NULL,
                Name varchar(255),
                FOREIGN KEY (Uid) REFERENCES shifts(uid));"""


        sql_command3 = """ CREATE TABLE IF NOT EXISTS rules (
                Rid INTEGER PRIMARY KEY AUTOINCREMENT,
                Uid INTEGER NOT NULL,
                type varchar(255) NOT NULL,
                value varchar(255) NOT NULL,
                increaseType varchar(255) NOT NULL,
                increaseValue varchar(255) NOT NULL,
                FOREIGN KEY (Uid) REFERENCES shifts(uid));"""


        #shift id, user id, date, start time, end time
        self.cursor.execute(sql_command) #create the shifts table
        self.cursor.execute(sql_command2) #create the shifts table
        self.cursor.execute(sql_command3) #create the shifts table
        self.connection.commit()
        self.cursor.close()


    def get_largest_rule_id(self):
        self.cursor = self.connection.cursor()
        sql_command = """SELECT MAX(rid) FROM rules WHERE uid = (?);"""
        self.cursor.execute(sql_command, str(self.Uid))
        max_id = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        return max_id[0][0]


    def close_db(self):
        self.cursor.close()
        self.connection.close()


    def add_rule(self, type, typeVal, increaseType, increaseValue):
        self.cursor = self.connection.cursor()
        sql_command = """INSERT INTO rules
        (Uid, type, value, increaseType, increaseValue)
        VALUES (?, ?, ?, ?, ?);"""
        data = (int(self.Uid), str(type), str(typeVal), str(increaseType), str(increaseValue))
        self.cursor.execute(sql_command, data)
        self.connection.commit()
        self.cursor.close()


    def get_rules(self):
        self.cursor = self.connection.cursor()
        sql_comand = """SELECT * FROM rules
        WHERE Uid = (?);"""
        data = str(self.Uid)
        self.cursor.execute(sql_comand, data) #get all the rules for the current user
        rules = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        if rules == []:
            self.rules = []
        else:
            self.rules = rules


    def delete_certain_rule(self, rid):
        self.cursor = self.connection.cursor()
        sql_command = """DELETE FROM rules WHERE rid = (?);"""
        self.cursor.execute(sql_command, str(rid))
        self.connection.commit()
        self.cursor.close()



    def get_all_shifts(self):
        self.cursor = self.connection.cursor()
        sql_comand = """SELECT * FROM shifts"""
        self.cursor.execute(sql_comand)
        shifts = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        if shifts == []:
            return []
        else:
            return shifts


    def get_certain_shifts(self): #get shifts from database
        self.cursor = self.connection.cursor()
        sql_comand = """SELECT * FROM shifts
        WHERE (?) <= Date AND (?) >= Date; """
        self.cursor.execute(sql_comand, (self.range_convert(self.startRange), self.range_convert(self.endRange)))
        shifts = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        if shifts == []:
            return []
        else:
            return shifts
            

    def create_shifts(self, bool):
        shift_list = []
        shifts = []
        if bool == 1:
            shifts = self.get_all_shifts()
        else:
            shift = self.get_certain_shifts()
        for shift in shifts:
            shift_list.append({"id": shift[0], "day": shift[2], "date": self.convert_date(shift[3]), "start": shift[4], "end": shift[5]})
        self.items = shift_list
        


    def add_shift(self, sid, date, day, start, end): #add a shift to the database
        self.cursor = self.connection.cursor()
        sql_command = """INSERT INTO shifts 
        (Uid, Date, Day, Start, End) 
        VALUES (?, ?, ?, ?, ?);"""
        newdate = int(date[6:10]) *10000 + int(date[3:5])*100 + int(date[0:2])
        data = (self.Uid, newdate, day, start, end)
        self.cursor.execute(sql_command, data)
        self.connection.commit()
        self.cursor.close()


    def delete_shift(self, sid): #delete a shift from the database given that the shift belongs to the current user
        self.cursor = self.connection.cursor()
        sql_commmand = """DELETE * FROM shifts WHERE sid = (?) AND uid = (?);"""
        self.cursor.execute(sql_commmand, (sid, self.Uid))
        self.connection.commit()
        self.cursor.close()
        

    def delete_all_shifts(self):
        self.items = [] #set as empty array
        self.cursor = self.connection.cursor()
        sql_commmand = """DELETE FROM shifts;"""
        self.cursor.execute(sql_commmand)
        self.connection.commit()
        self.cursor.close()


    def get_settings(self): #get the settings from database
        self.cursor = self.connection.cursor()
        sql_command = """SELECT * FROM users;"""
        self.cursor.execute(sql_command)
        settings = self.cursor.fetchall()
        self.payrate = settings["Payrate"]
        self.taxrate = settings["Taxrate"]
        self.connection.commit()
        self.cursor.close()


    def put_settings(self, payrate, taxrate): #update the settings
        self.cursor = self.connection.cursor()
        sql_command = """UPDATE users
        SET Payrate = (?), Taxrate = (?);"""
        self.cursor.execute(sql_command, (int(payrate), int(taxrate)))
        self.payrate = payrate
        self.taxrate = taxrate


    def put_range(self, startRange, endRange): #update the range
        self.startRange = startRange
        self.endRange = endRange


    def range_convert(self, date):
        return int(date[0:4]) *10000 + int(date[5:7])*100 + int(date[8:10])


    def convert_date(self, date):
        date = str(date)
        return str(date[6:8]) + "/" + str(date[4:6]) + "/" + str(date[0:4])