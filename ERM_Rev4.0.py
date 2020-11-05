import tkinter as tk
from tkinter import messagebox
import time

import mysql.connector

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.geometry("800x300")
        self.parent.title("Electronic Medical Recodrd")
        
        #variable for db
        
        self.start_up()

    def start_up(self):
    #standard input buttons
        self.search_button = tk.Button(self.parent, text="Search Student", width = 17, state=tk.DISABLED, command = self.search_func)
        self.search_button.grid(row = 0, column = 0)

        self.edit_button = tk.Button(self.parent, text="Edit Information", width = 17, state=tk.DISABLED, command = self.edit_func)
        self.edit_button.grid(row = 1, column = 0)

        self.add_button = tk.Button(self.parent, text="Add Student", width = 17, state=tk.DISABLED, command = self.add_func)
        self.add_button.grid(row = 2, column = 0)
        
        self.remove_button = tk.Button(self.parent, text="Remove Student", width = 17, state=tk.DISABLED, command = self.remove_func)
        self.remove_button.grid(row = 3, column = 0)

        self.covid_button = tk.Button(self.parent, text="Covid-19", width = 17, state=tk.DISABLED, command = self.covid_func)
        self.covid_button.grid(row = 4, column = 0)

        self.start = [self.search_button, self.edit_button, self.add_button, self.remove_button, self.remove_button, self.covid_button]

    #login environment
        self.login_user_label = tk.Label(self.parent, text="User Name")
        self.login_user_label.grid(row = 3, column = 2)

        self.login_user_entry = tk.Entry(self.parent)
        self.login_user_entry.grid(row = 3, column = 3)

        self.login_passwd_label = tk.Label(self.parent, text="Password")
        self.login_passwd_label.grid(row = 4, column = 2)

        self.login_passwd_entry = tk.Entry(self.parent)
        self.login_passwd_entry.grid(row = 4, column = 3)

        self.login_button = tk.Button(self.parent, text="Login", command = self.login_validate)
        self.login_button.grid(row = 5, column = 3)

        self.login = [self.login_user_label, self.login_user_entry,
                      self.login_passwd_label, self.login_passwd_entry,
                      self.login_button]

    #search environment        
        self.search_number_label    = tk.Label(self.parent, text = "Student Number:")
        self.search_number_entry    = tk.Entry(self.parent)

        self.search_name_label      = tk.Label(self.parent, text = "  Student Name:")
        self.search_name_entry      = tk.Entry(self.parent)

        self.search_year_label      = tk.Label(self.parent, text = " Student Grade:")
        self.search_year_entry      = tk.Entry(self.parent)

        self.search_student_button  = tk.Button(self.parent, text = "Search", command = self.search_action)

        self.search_text            = tk.Text(self.parent, height = 10, width = 50)

        self.search = [self.search_number_label, self.search_number_entry,
                       self.search_name_label, self.search_name_entry,
                       self.search_year_label, self.search_year_entry,
                       self.search_student_button, self.search_text]

    #edit environement
        self.edit_number_label          = tk.Label(self.parent, text = "Student Number:")
        self.edit_number_entry          = tk.Entry(self.parent)
        
        self.edit_find_button           = tk.Button(self.parent, text = "Find", command = self.edit_find_action)

        self.edit_name_label            = tk.Label(self.parent, text = "Name:")
        self.edit_name_entry            = tk.Entry(self.parent)

        self.edit_grade_label           = tk.Label(self.parent, text = "Grade:")
        self.edit_grade_entry           = tk.Entry(self.parent)

        self.edit_address_label         = tk.Label(self.parent, text = "Address:")
        self.edit_address_entry         = tk.Entry(self.parent)

        self.edit_eContactName_label    = tk.Label(self.parent, text = "Emergancy Contact Name:")
        self.edit_eContactName_entry    = tk.Entry(self.parent)
        
        self.edit_eContactNumber_label  = tk.Label(self.parent, text = "Emergancy Contact Number:")
        self.edit_eContactNumber_entry  = tk.Entry(self.parent)

        self.edit_familyDoctor_label    = tk.Label(self.parent, text = "Family Doctor:")
        self.edit_familyDoctor_entry    = tk.Entry(self.parent)

        self.edit_update_button          = tk.Button(self.parent, text = "Update", command = self.edit_update)

        self.edit = [self.edit_number_label,        self.edit_number_entry,
                     self.edit_find_button,
                     self.edit_name_label,          self.edit_name_entry,
                     self.edit_grade_label,         self.edit_grade_entry,
                     self.edit_address_label,       self.edit_address_entry,
                     self.edit_eContactName_label,  self.edit_eContactName_entry,     
                     self.edit_eContactNumber_label,self.edit_eContactNumber_entry,
                     self.edit_familyDoctor_label,  self.edit_familyDoctor_entry,
                     self.edit_update_button]

    #add environment
        #self.add_name_label
        #self.add_name_enrty

        #self.add_grade_label
        #self.add_grade_entry

        #self.add_address_label
        #self.add_address_enrty

        #self.edit_eContactName_label
        #self.edit_eContactName_label

        #self.edit_eContactNumber_label
        #self.edit_eContactNumber_label

        #self.edit_familyDoctor_label
        #self.edit_familyDoctor_entry

       

    def search_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.search_button['state'] = 'disabled'

        for x in self.edit:
            x.grid_forget()

        self.search_number_label.grid(row = 0, column = 2)
        self.search_number_entry.grid(row = 0, column = 3)
        
        self.search_name_label.grid(row = 1, column = 2)
        self.search_name_entry.grid(row = 1, column = 3)

        self.search_year_label.grid(row = 2, column = 2)
        self.search_year_entry.grid(row = 2, column = 3)

        self.search_student_button.grid(row = 3, column = 3)

        self.search_text.grid(row = 5, column = 4)

    def search_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "SELECT * FROM Student WHERE sNumber = %s OR sName = %s OR grade = %s"
        fetch_name = (self.search_number_entry.get(),  self.search_name_entry.get(), self.search_year_entry.get(), )

        mycursor.execute(sql, fetch_name,)

        records = mycursor.fetchall()

        self.search_text.delete('1.0', 'end')
        
        for x in records:
            strng = str(list(x))
            self.search_text.insert(tk.END, strng)
            self.search_text.insert(tk.END, "\n\n")

    def convertTuple(self, tup):
        strng = ''.join(tup)
        return strng

    def edit_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.edit_button['state'] = 'disabled'        

        for x in self.search:
            x.grid_forget()

        self.edit_number_label.grid(row = 0, column = 2)
        self.edit_number_entry.grid(row = 0, column = 3)

        self.edit_find_button.grid(row = 1, column = 3)

        self.edit_name_label.grid(row = 2, column = 2)
        self.edit_name_entry.grid(row = 3, column = 2)
        
        self.edit_grade_label.grid(row = 2, column = 3)
        self.edit_grade_entry.grid(row = 3, column = 3)

        self.edit_address_label.grid(row = 4, column = 2)
        self.edit_address_entry.grid(row = 5, column = 2)

        self.edit_familyDoctor_label.grid(row = 4, column = 3)
        self.edit_familyDoctor_entry.grid(row = 5, column = 3)

        self.edit_eContactName_label.grid(row = 6, column = 2)
        self.edit_eContactName_entry.grid(row = 7, column = 2)

        self.edit_eContactNumber_label.grid(row = 6, column = 3)
        self.edit_eContactNumber_entry.grid(row = 7, column = 3)

        self.edit_update_button.grid(row = 9, column = 3)

    def edit_find_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "SELECT * FROM Student WHERE sNumber = %s"
        fetch = (self.edit_number_entry.get(), )

        mycursor.execute(sql, fetch,)

        records = mycursor.fetchall()

        self.edit_name_entry.delete(0, 'end')
        self.edit_grade_entry.delete(0, 'end')
        self.edit_address_entry.delete(0, 'end')
        self.edit_eContactName_entry.delete(0, 'end')
        self.edit_eContactNumber_entry.delete(0, 'end')
        self.edit_familyDoctor_entry.delete(0, 'end')

        for x in records:
            self.edit_name_entry.insert(0, x[1])
            self.edit_grade_entry.insert(0, x[2])
            self.edit_address_entry.insert(0, x[3])
            self.edit_eContactName_entry.insert(0, x[4])
            self.edit_eContactNumber_entry.insert(0, x[5])
            self.edit_familyDoctor_entry.insert(0, x[6])  

    def edit_update(self):

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "UPDATE Student SET sName = %s, grade = %s, address = %s, eContactName = %s, eContactNumber = %s, familyDoctor = %s WHERE sNumber = %s"
        fetch = (self.edit_name_entry.get(), self.edit_grade_entry.get(), self.edit_address_entry.get(), self.edit_eContactName_entry.get(), self.edit_eContactNumber_entry.get(), self.edit_familyDoctor_entry.get(), self.edit_number_entry.get(), )

        mycursor.execute(sql, fetch,)
        db.commit()

        print(done)

    def add_func(self):
        time.sleep(0)

    def remove_func(self):
        time.sleep(0)

    def covid_func(self):
        time.sleep(0)

    def login_validate(self):

        user = self.login_user_entry.get()
        passwd = self.login_passwd_entry.get()

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()
        sql = "SELECT uName, password FROM Faculty where uName = %s AND password = %s"
        fetch = (self.login_user_entry.get(), self.login_passwd_entry.get(), )

        mycursor.execute(sql, fetch)

        records = mycursor.fetchall()

        if(records):
            for x in self.login:
                x.grid_forget()

            for x in self.start:
                x.configure(state="normal")

#mycursor.execute("INSERT INTO Faculty (uName, password, position, sickDaysLeft, hireDate) VALUES (%s, %s, %s, %s, %s)", ("root", "root", "Executive", 21, "1987-08-23 12:00:00"))
#mycursor.execute("INSERT INTO Student (sName, grade, address, allergy, eContactName, eContactNumber, familyDoctor) VALUES (%s, %s, %s, %s, %s, %s, %s)", ("Mac Peralta", 5, "2357 Valleystream Drive, Sudbury ON, P3A 6A9", "", "Amy Santiago", "(917) 099-0911", "Dr John Smith"))
#"INSERT INTO Student (sName, grade, allergy, emergencyContact) VALUES (%s, %s, %s, %s)", ("Adam West", 1, "N/A", "Regina Phalange - (917) 099-8888")
#"INSERT INTO Student (sName, grade, allergy, emergencyContact) VALUES (%s, %s, %s, %s)", ("Dylan Sprouse", 3, "N/A", "Carey Martin - (617) 011-1423")
#"INSERT INTO Student (sName, grade, allergy, emergencyContact) VALUES (%s, %s, %s, %s)", ("Cole Sprouse", 3, "N/A", "Carey Martin - (617) 011-1423")

#"Scott", "Michael", "Andrew", "Mark", "Fernando", "Faith", "Steve", "Lee", "Amani", "Liv", "Nick A", "James", "Jake", "Brett", "Graham", "Fraser", "Jacob", "Chelsea", "Phil", "George", "Charley", "Emma", "Steph"

if __name__ == '__main__':
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase")

    mycursor = db.cursor()

    #mycursor.execute("ALTER TABLE Student DROP COLUMN allergy")

    db.commit()

    root = tk.Tk()
    run = App(root)
    root.mainloop()

#tables:
#Student (sNumber INT AUTO_INCREMENT PRIMARY KEY, sName VARCHAR(63), grade INT, address VARCHAR(255), allergy VARCHAR(255), eContactName VARCHAR(63), eContactNumber VARCHAR(15), familyDoctor VARCHAR(63))
#Faculty (uNumber INT AUTO_INCREMENT PRIMARY KEY, uName VARCHAR(63), password VARCHAR(255), position VARCHAR(63), sickDaysLeft INT, hireDate DATETIME)
#Covid (sNumber INT PRIMARY KEY, testDate DATETIME, results BOOLEAN, quarentineStartDate DATE, quarentineEndDate DATETIME)
#MedicalInfo (sNumber INT PRIMARY KEY, allergy VARCHAR(255), medication VARCHAR(255), dosage VARCHAR(255), vaccine VARCHAR(255), variedCondition VARCHAR(255), currentCase VARCHAR(255))
#Class (sNumber INT PRIMARY KEY, courseCode VARCHAR(10), teacherName VARCHAR(63), compromised BOOLEAN)
#Examiner (uNumber INT AUTO_INCREMENT PRIMARY KEY, uName VARCHAR(63), officeAddress VARCHAR(255), contactNumber VARCHAR(15), specialization VARCHAR(255))
#Result (resultIdentification VARCHAR(15) PRIMARY KEY, sName VARCHAR(63), examinerName VARCHAR(63), resultDiagnosis VARCHAR(255), resultDate DATETIME)
