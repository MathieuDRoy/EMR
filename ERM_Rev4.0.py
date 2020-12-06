import tkinter as tk
from tkinter import messagebox
import time
import csv

import mysql.connector

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.geometry("800x600")
        self.parent.title("Electronic Medical Record")
        
        #variable for db

        self.permissions = False
        self.userName = ""
        
        self.start_up()

    def start_up(self):
    #standard input buttons
        self.search_button       = tk.Button(self.parent, text="Search Student", width = 25, state=tk.DISABLED, command = self.search_func)
        self.search_button.grid(row = 0, column = 0)

        self.edit_button         = tk.Button(self.parent, text="Edit Information", width = 25, state=tk.DISABLED, command = self.edit_func)
        self.edit_button.grid(row = 1, column = 0)

        self.add_student_button = tk.Button(self.parent, text="Add Student", width = 25, state=tk.DISABLED, command = self.add_student_func)
        self.add_student_button.grid(row = 2, column = 0)
        
        self.add_faculty_button  = tk.Button(self.parent, text="Add Faculty", width = 25, state=tk.DISABLED, command = self.add_faculty_func)
        self.add_faculty_button.grid(row = 3, column = 0)

        self.covid_button       = tk.Button(self.parent, text="Covid-19", width = 25, state=tk.DISABLED, command = self.covid_func)
        self.covid_button.grid(row = 4, column = 0)

        self.list_staff_button   = tk.Button(self.parent, text="List Staff", width = 25, state=tk.DISABLED, command = self.list_staff_func)
        self.list_staff_button.grid(row = 5, column = 0)

        self.list_student_button = tk.Button(self.parent, text="List Student", width = 25, state=tk.DISABLED, command = self.list_student_func)
        self.list_student_button.grid(row = 6, column = 0)

        self.search_faculty_button = tk.Button(self.parent, text="Search Faculty", width = 25, state=tk.DISABLED, command = self.search_faculty_func)
        self.search_faculty_button.grid(row = 7, column = 0)

        self.add_covid_button = tk.Button(self.parent, text="Add Covid-19 Result", width = 25, state=tk.DISABLED, command = self.covid_add_func)
        self.add_covid_button.grid(row = 8, column = 0)

        self.add_medical_button = tk.Button(self.parent, text="Add Medical Information", width = 25, state=tk.DISABLED, command = self.medical_add_func)
        self.add_medical_button.grid(row = 9, column = 0)

        self.search_medical_button = tk.Button(self.parent, text="Search/DeleteMedical Information", width = 25, state=tk.DISABLED, command = self.search_medical_func)
        self.search_medical_button.grid(row = 10, column = 0)

        self.transfer_student_button = tk.Button(self.parent, text="Transfer Students", width = 25, state=tk.DISABLED, command = self.transfer_student_func)
        self.transfer_student_button.grid(row = 11, column = 0)

        self.isolate_button = tk.Button(self.parent, text="Isolate Student", width = 25, state=tk.DISABLED, command = self.isolate_func)
        self.isolate_button.grid(row = 12, column = 0)

        self.testing_history = tk.Button(self.parent, text="Testing History", width = 25, state=tk.DISABLED, command = self.testing_history_func)
        self.testing_history.grid(row = 13, column = 0)

        self.schedule = tk.Button(self.parent, text="Schedule evaluation", width = 25, state=tk.DISABLED, command = self.schedule_func)
        self.schedule.grid(row = 14, column = 0)
        


        #class switches
        #all covid results

        self.start = [self.search_button, self.edit_button, self.add_student_button, self.add_faculty_button, self.covid_button, self.list_staff_button, self.list_student_button,  self.search_faculty_button, self.add_covid_button, self.add_medical_button, self.search_medical_button, self.transfer_student_button, self.isolate_button, self.testing_history, self.schedule]

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

    #search student environment        
        self.search_number_label    = tk.Label(self.parent, text = "Student Number:")
        self.search_number_entry    = tk.Entry(self.parent)

        self.search_name_label      = tk.Label(self.parent, text = "  Student Name:")
        self.search_name_entry      = tk.Entry(self.parent)

        self.search_year_label      = tk.Label(self.parent, text = " Student Grade:")
        self.search_year_entry      = tk.Entry(self.parent)

        self.search_student_button  = tk.Button(self.parent, text = "Search", command = self.search_action)

        self.search_delete_button   = tk.Button(self.parent, text = "Delete", command = self.delete_action)

        self.search_text            = tk.Text(self.parent, height = 10, width = 50)

        self.search = [self.search_number_label, self.search_number_entry,
                       self.search_name_label, self.search_name_entry,
                       self.search_year_label, self.search_year_entry,
                       self.search_student_button, self.search_text,
                       self.search_delete_button]

    #search faculty environment
        self.search_faculty_number_label            = tk.Label(self.parent, text = "Faculty Number:")
        self.search_faculty_number_entry            = tk.Entry(self.parent)

        self.search_faculty_name_label              = tk.Label(self.parent, text = "  Faculty Name:")
        self.search_faculty_name_entry              = tk.Entry(self.parent)

        self.search_faculty_position_label          = tk.Label(self.parent, text = " Faculty Position:")
        self.search_faculty_position_entry          = tk.Entry(self.parent)

        self.search_faculty_search_button           = tk.Button(self.parent, text = "Search", command = self.search_faculty_action)

        self.delete_faculty_button                  = tk.Button(self.parent, text = "Delete", command = self.delete_faculty_action)

        self.search_faculty_text                    = tk.Text(self.parent, height = 10, width = 50)

        self.search_faculty = [self.search_faculty_number_label,    self.search_faculty_number_entry,
                       self.search_faculty_name_label,              self.search_faculty_name_entry,
                       self.search_faculty_position_label,          self.search_faculty_position_entry,
                       self.search_faculty_search_button,                  self.search_faculty_text,
                       self.delete_faculty_button]

    #edit student environement
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

        self.edit_update_button         = tk.Button(self.parent, text = "Update", command = self.edit_update)

        self.edit = [self.edit_number_label,        self.edit_number_entry,
                     self.edit_find_button,
                     self.edit_name_label,          self.edit_name_entry,
                     self.edit_grade_label,         self.edit_grade_entry,
                     self.edit_address_label,       self.edit_address_entry,
                     self.edit_eContactName_label,  self.edit_eContactName_entry,     
                     self.edit_eContactNumber_label,self.edit_eContactNumber_entry,
                     self.edit_update_button]

    #list staff demographics
        self.list_staff_label           = tk.Label(self.parent, text = "Faculty Members:")
        self.list_staff_text            = tk.Text(self.parent, height = 10, width = 80)

        self.list_staff = [self.list_staff_label,    self.list_staff_text]

    #list student demographics
        self.list_student_label           = tk.Label(self.parent, text = "Student Body:")
        self.list_student_text            = tk.Text(self.parent, height = 10, width = 80)

        self.list_student = [self.list_student_label,    self.list_student_text]
        
        

    #add student environment
        self.add_student_name_label             = tk.Label(self.parent, text = "Name:")
        self.add_student_name_entry             = tk.Entry(self.parent)

        self.add_student_grade_label            = tk.Label(self.parent, text = "Grade:")
        self.add_student_grade_entry            = tk.Entry(self.parent)

        self.add_student_address_label          = tk.Label(self.parent, text = "Address:")
        self.add_student_address_entry          = tk.Entry(self.parent)

        self.add_student_eContactName_label    = tk.Label(self.parent, text = "Emergancy Contact Name:")
        self.add_student_eContactName_entry    = tk.Entry(self.parent)

        self.add_student_eContactNumber_label  = tk.Label(self.parent, text = "Emergancy Contact Number:")
        self.add_student_eContactNumber_entry  = tk.Entry(self.parent)

        self.add_student_data_button            = tk.Button(self.parent, text = "Add", command = self.add_student_action)

        self.add_student = [self.add_student_name_label,            self.add_student_name_entry,
                            self.add_student_grade_label,           self.add_student_grade_entry,
                            self.add_student_address_label,         self.add_student_address_entry,
                            self.add_student_eContactName_label,    self.add_student_eContactName_entry,
                            self.add_student_eContactNumber_label,  self.add_student_eContactNumber_entry,
                            self.add_student_data_button]

    #add faculty environment
        self.add_faculty_name_label             = tk.Label(self.parent, text = "Name:")
        self.add_faculty_name_entry             = tk.Entry(self.parent)

        self.add_faculty_possition_label        = tk.Label(self.parent, text = "Possiton:")
        self.add_faculty_possition_entry        = tk.Entry(self.parent)

        self.add_faculty_sickDays_label         = tk.Label(self.parent, text = "Sick Days")
        self.add_faculty_sickDays_entry         = tk.Entry(self.parent)

        self.add_faculty_hireDate_label         = tk.Label(self.parent, text = "Hire Date")
        self.add_faculty_hireDate_entry         = tk.Entry(self.parent)

        self.add_faculty_password_label         = tk.Label(self.parent, text = "Password")
        self.add_faculty_password_entry         = tk.Entry(self.parent)

        self.add_faculty_data_button            = tk.Button(self.parent, text = "Add", command = self.add_faculty_action)

        self.add_faculty = [self.add_faculty_name_label,        self.add_faculty_name_entry,
                            self.add_faculty_possition_label,   self.add_faculty_possition_entry,
                            self.add_faculty_sickDays_label,    self.add_faculty_sickDays_entry,
                            self.add_faculty_hireDate_label,    self.add_faculty_hireDate_entry,
                            self.add_faculty_password_label,    self.add_faculty_password_entry,
                            self.add_faculty_data_button]
   

    #covid results environment
        self.covid_reselts_text     = tk.Text(self.parent, height = 15, width = 80)
        

        #delete

        self.delete_covid_entry     = tk.Entry(self.parent)
        self.delete_covid_button    = tk.Button(self.parent, text = "Delete test", command = self.delete_covid)

        self.covid = [self.covid_reselts_text, self.delete_covid_entry, self.delete_covid_button]

    #covid add environment
        self.add_covid_studentID_label      = tk.Label(self.parent, text = "Student Identification:")
        self.add_covid_studentID_entry      = tk.Entry(self.parent)

        self.add_covid_testDate_label       = tk.Label(self.parent, text = "Date of test (yyyy-mm-dd):")
        self.add_covid_testDate_entry       = tk.Entry(self.parent)
        
        self.add_covid_result_label         = tk.Label(self.parent, text = "Result")
        self.add_covid_result_entry         = tk.Entry(self.parent)

        self.add_covid_isolationBegin_label = tk.Label(self.parent, text = "Isolation begining date (yyyy-mm-dd)")
        self.add_covid_isolationBegin_entry = tk.Entry(self.parent)

        self.add_covid_isolationEnd_label   = tk.Label(self.parent, text = "Isolation ending date (yyyy-mm-dd)")
        self.add_covid_isolationEnd_entry   = tk.Entry(self.parent)

        self.covid_add_button               = tk.Button(self.parent, text = "Add", command = self.covid_add_action)

        self.add_covid = [self.add_covid_studentID_label,       self.add_covid_studentID_entry,
                          self.add_covid_testDate_label,        self.add_covid_testDate_entry,
                          self.add_covid_result_label,          self.add_covid_result_entry,
                          self.add_covid_isolationBegin_label,  self.add_covid_isolationBegin_entry,
                          self.add_covid_isolationEnd_label,    self.add_covid_isolationEnd_entry,
                          self.covid_add_button]

    #add medical environment
        self.add_medical_studentID_label        = tk.Label(self.parent, text = "Student Identification:")
        self.add_medical_studentID_entry        = tk.Entry(self.parent)        

        self.add_medical_medication_label       = tk.Label(self.parent, text = "Medication (only 1):")
        self.add_medical_medication_entry       = tk.Entry(self.parent)

        self.add_medical_dosage_label           = tk.Label(self.parent, text = "Dosage for Medication (in mg):")
        self.add_medical_dosage_entry           = tk.Entry(self.parent)

        self.add_medical_vaccine_label          = tk.Label(self.parent, text = "Vaccine list:")
        self.add_medical_vaccine_entry          = tk.Entry(self.parent)

        self.add_medical_variedCondition_label  = tk.Label(self.parent, text = "Conditons:")
        self.add_medical_variedCondition_entry  = tk.Entry(self.parent)

        self.add_medical_currentStatus_label    = tk.Label(self.parent, text = "Current Status:")
        self.add_medical_currentStatus_entry    = tk.Entry(self.parent)

        self.medical_add_button                 = tk.Button(self.parent, text = "Add", command = self.medical_add_action)

        self.medical = [self.add_medical_studentID_label,       self.add_medical_studentID_entry,
                        self.add_medical_medication_label,      self.add_medical_medication_entry,
                        self.add_medical_dosage_label,          self.add_medical_dosage_entry,
                        self.add_medical_vaccine_label,         self.add_medical_vaccine_entry,
                        self.add_medical_variedCondition_label, self.add_medical_variedCondition_entry,
                        self.add_medical_currentStatus_label,   self.add_medical_currentStatus_entry ,
                        self.medical_add_button]

    #medical results environment
        self.medical_text     = tk.Text(self.parent, height = 15, width = 80)
        

        #delete

        self.delete_medical_entry     = tk.Entry(self.parent)
        self.delete_medical_button    = tk.Button(self.parent, text = "Delete Entry", command = self.delete_medical)

        #output medication
        self.search_medication_entry    = tk.Entry(self.parent)
        self.search_medication_label    = tk.Label(self.parent, text = "Search For Student's Medications:")
        self.search_medication_button   = tk.Button(self.parent, text = "Search Medication", command = self.medication_lookup)

        self.medical_search = [self.medical_text,               self.delete_medical_entry,
                               self.delete_medical_button,      self.search_medication_entry,
                               self.search_medication_label,    self.search_medication_button]


    #transfer class environment
        self.studentID_label = tk.Label(self.parent, text = "Student Identification:")
        self.studentID_entry = tk.Entry(self.parent)

        self.current_class_label = tk.Label(self.parent, text = "Current Class:")
        self.current_class_entry = tk.Entry(self.parent)

        self.target_class_label = tk.Label(self.parent, text = "Target Class:")
        self.target_class_entry = tk.Entry(self.parent)

        self.transfer_button = tk.Button(self.parent, text = "Transfer", command = self.transfer_action)

        self.drop_button = tk.Button(self.parent, text = "Drop this class", command = self.drop_class)
        self.enter_button = tk.Button(self.parent, text = "Enter this class", command = self.enter_class)


        self.transfer = [self.studentID_label,      self.studentID_entry,
                         self.current_class_label,  self.current_class_entry,
                         self.target_class_label,   self.target_class_entry,
                         self.transfer_button,      self.drop_button,
                         self.enter_button]

    #isolate environemt

        self.isolate_studentID_label = tk.Label(self.parent, text = "Student Identification:")
        self.isolate_studentID_entry = tk.Entry(self.parent)        
        self.isolate_text = tk.Text(self.parent, height = 15, width = 80)
        self.isolate_student_go = tk.Button(self.parent, text = "Compromise Classes", command = self.isolate_action)
        self.view_conditions = tk.Button(self.parent, text = "View Outbreak Status", command = self.view_condition_status)

        self.isolate= [self.isolate_studentID_label,    self.isolate_studentID_entry,
                       self.isolate_text,               self.isolate_student_go,
                       self.view_conditions]

    #testing history environment

        self.testing_label = tk.Label(self.parent, text = "testing type:")
        self.testing_entry = tk.Entry(self.parent)
        self.testing_text = tk.Text(self.parent, height = 15, width = 80)
        self.testing_go = tk.Button(self.parent, text = "Testing History", command = self.testing_action)
        self.testing = [self.testing_label, self.testing_entry, self.testing_go, self.testing_text]

    #schedule environement
        self.schedule_studentID_label = tk.Label(self.parent, text = "Student Identification:")
        self.schedule_studentID_entry = tk.Entry(self.parent)

        self.schedule_test_type_lable = tk.Label(self.parent, text = "Test Type:")
        self.schedule_test_type_entry = tk.Entry(self.parent)

        self.schedual_test_date_label = tk.Label(self.parent, text = "Date (yyyy-mm-dd):")
        self.schedule_test_date_entry = tk.Entry(self.parent)

        self.schedule_go  = tk.Button(self.parent, text = "Schedule", command = self.schudule_action)

        self.schedule_text = tk.Text(self.parent, height = 15, width = 80)

        self.schedule_view = tk.Button(self.parent, text = "View Scheduled Evenets", command = self.schudule_view)

        self.schedule = [self.schedule_studentID_label, self.schedule_studentID_entry,
                         self.schedule_test_type_lable, self.schedule_test_type_entry,
                         self.schedual_test_date_label, self.schedule_test_date_entry,
                         self.schedule_go, self.schedule_text, self.schedule_view]
        

    def schedule_func(self):
        self.schedule_studentID_label.grid(row = 0, column = 2) 
        self.schedule_studentID_entry.grid(row = 1, column = 2)

        self.schedule_test_type_lable.grid(row = 2, column = 2)
        self.schedule_test_type_entry.grid(row = 3, column = 2)

        self.schedual_test_date_label.grid(row = 4, column = 2)
        self.schedule_test_date_entry.grid(row = 5, column = 2)

        self.schedule_go.grid(row = 7, column = 2)
        self.schedule_view.grid(row = 8, column = 2)

        self.schedule_text.grid(row = 6, column = 2)

    def schudule_action(self):

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()
        sql = "INSERT INTO results (studentID, test, diagnosis, resultDate) VALUES (%s, %s, 'TBD', %s)"
        fettch_them = (self.schedule_studentID_entry.get(), self.schedule_test_type_entry.get(), self.schedule_test_date_entry.get(), )

       
        mycursor.execute(sql,fettch_them, )
        db.commit()

    def schudule_view(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()
        sql = "select * from results where cast(resultDate as Date) > cast(now() as Date)"
        mycursor.execute(sql,)


        self.schedule_text.delete('1.0', 'end')
        records = mycursor.fetchall()
        for x in records:
            strng = str(list(x))
            self.schedule_text.insert(tk.END, strng)
            self.schedule_text.insert(tk.END, "\n\n")
        

    def testing_history_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.testing_history['state'] = 'disabled'

        self.clear()

        self.testing_label.grid(row = 0, column = 2)
        self.testing_entry.grid(row = 1, column = 2)
        self.testing_text.grid(row = 3, column = 2)
        self.testing_go.grid(row = 2, column = 2)
        self.testing_go.grid(row = 2, column = 2)

    def testing_action(self):

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()
        sql = "SELECT student.studentName, results.resultDate, results.test FROM results INNER JOIN student ON results.studentID = student.StudentID WHERE results.test = %s"
        fettch_them = (self.testing_entry.get(),)

        mycursor.execute(sql,fettch_them, )
        records = mycursor.fetchall()
        for x in records:
            strng = str(list(x))
            self.testing_text.insert(tk.END, strng)
            self.testing_text.insert(tk.END, "\n\n")        

    def isolate_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.isolate_button['state'] = 'disabled'

        self.clear()

        self.isolate_studentID_label.grid(row = 0, column = 2)
        self.isolate_studentID_entry.grid(row = 1, column = 2)
        self.isolate_text.grid(row = 3, column = 2)
        self.view_conditions.grid(row = 4, column = 2)
        self.isolate_student_go.grid(row = 2, column = 2)

    def isolate_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "CREATE TEMPORARY TABLE temp (SELECT classID  FROM class AS temp WHERE studentID = %s)"
        fettch_them = (self.isolate_studentID_entry.get(),)

        mycursor.execute(sql,fettch_them, )

        sql = "UPDATE class SET compromized = 1 WHERE classID in (select * from temp)"
        mycursor.execute(sql, )

        sql = "DROP TABLE temp"
        mycursor.execute(sql, )

    def view_condition_status(self):

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()
        sql = "select student.studentName, class.classID from class INNER JOIN student ON student.studentID = class.studentID where compromized = 1"
        mycursor.execute(sql, )
        records = mycursor.fetchall()
        for x in records:
            strng = str(list(x))
            self.isolate_text.insert(tk.END, strng)
            self.isolate_text.insert(tk.END, "\n\n")
        
    def transfer_student_func(self):

        for x in self.start:
            x.configure(state="normal")
        self.search_button['state'] = 'disabled'

        self.clear()

        self.studentID_label.grid(row = 0, column = 2)
        self.studentID_entry.grid(row = 1, column = 2)

        self.current_class_label.grid(row = 2, column = 2)
        self.current_class_entry.grid(row = 3, column = 2)

        self.target_class_label.grid(row = 4, column = 2)
        self.target_class_entry.grid(row = 5, column = 2)

        self.drop_button.grid(row = 3, column = 3)
        self.enter_button.grid(row = 5, column = 3)

        self.transfer_button.grid(row = 6, column =2)

    def transfer_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "UPDATE class SET classID = %s, classSize = %s WHERE classID = %s AND studentID = %s"
        fetch_name = (self.target_class_entry.get(), targetClassSize, self.current_class_entry.get(), self.studentID_entry.get(),)

        mycursor.execute(sql, fetch_name,)

        sql = "UPDATE class SET classSize = classSize + 1 WHERE classID = %s"
        fetch = (self.target_class_entry.get(), )

        mycursor.execute(sql, fetch,)

        sql = "UPDATE class SET classSize = classSize - 1 WHERE classID = %s"
        fetch_it = (self.current_class_entry.get(), )

        mycursor.execute(sql, fetch_it,)
        
        db.commit()

    def drop_class(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "DELETE FROM class WHERE studentId = %s AND classID = %s"
        fetch_it = (self.studentID_entry.get(), self.current_class_entry.get(), )
        mycursor.execute(sql, fetch_it,)


        sql = "UPDATE class SET classSize = classSize - 1 WHERE classID = %s"
        fetch_it = (self.current_class_entry.get(), )
        mycursor.execute(sql, fetch_it,)
        
        db.commit()

    def enter_class(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        size = 0

        sql = "SELECT classSize FROM class WHERE classID = %s"
        fetch = (self.target_class_entry.get(), )
        mycursor.execute(sql, fetch,)

        records = mycursor.fetchall()
        for x in records:
            size = x[0]



        sql = "INSERT INTO class (classID, studentID, classSize, compromized) values (%s, %s, %s, %s)"
        fetch_it = (self.target_class_entry.get(), self.studentID_entry.get(), size, 0, )
        mycursor.execute(sql, fetch_it,)


        sql = "UPDATE class SET classSize = classSize + 1 WHERE classID = %s"
        fetch_it = (self.target_class_entry.get(), )
        mycursor.execute(sql, fetch_it,)
        
        db.commit()
        
                          
    def search_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.search_button['state'] = 'disabled'

        self.clear()

        self.search_number_label.grid(row = 0, column = 2)
        self.search_number_entry.grid(row = 0, column = 3)
        
        self.search_name_label.grid(row = 1, column = 2)
        self.search_name_entry.grid(row = 1, column = 3)

        self.search_year_label.grid(row = 2, column = 2)
        self.search_year_entry.grid(row = 2, column = 3)

        self.search_student_button.grid(row = 3, column = 2)
        self.search_delete_button.grid(row = 3, column = 3)

        self.search_text.grid(row = 5, column = 4)

    def search_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()
        sql = "SELECT * FROM student WHERE studentID = %s OR studentName = %s OR grade = %s"
        fetch_name = (self.search_number_entry.get(),  self.search_name_entry.get(), self.search_year_entry.get(), )
        mycursor.execute(sql, fetch_name,)
        records = mycursor.fetchall()
        self.search_text.delete('1.0', 'end')
        
        for x in records:
            strng = str(list(x))
            self.search_text.insert(tk.END, strng)
            self.search_text.insert(tk.END, "\n\n")
            
    def delete_action(self):
        sql = "DELETE FROM student where studentID = %s"
        fetch_name = (self.search_number_entry.get(),)

        mycursor.execute(sql, fetch_name,)
        db.commit()

    def search_faculty_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.search_faculty_button['state'] = 'disabled'

        self.clear()

        self.search_faculty_number_label.grid(row = 0, column = 2)
        self.search_faculty_number_entry.grid(row = 0, column = 3)
        
        self.search_faculty_name_label.grid(row = 1, column = 2)
        self.search_faculty_name_entry.grid(row = 1, column = 3)

        self.search_faculty_position_label.grid(row = 2, column = 2)
        self.search_faculty_position_entry.grid(row = 2, column = 3)

        self.search_faculty_search_button.grid(row = 3, column = 2)
        self.delete_faculty_button.grid(row = 3, column = 3)

        self.search_faculty_text.grid(row = 5, column = 4)

    def search_faculty_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "SELECT * FROM faculty WHERE facultyID = %s OR facultyName = %s OR position = %s"
        fetch_name = (self.search_faculty_number_entry.get(),  self.search_faculty_name_entry.get(), self.search_faculty_position_entry.get(), )

        mycursor.execute(sql, fetch_name,)

        records = mycursor.fetchall()

        self.search_text.delete('1.0', 'end')
        
        for x in records:
            strng = str(list(x))
            self.search_faculty_text.insert(tk.END, strng)
            self.search_faculty_text.insert(tk.END, "\n\n")
            
    

    def edit_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.edit_button['state'] = 'disabled'        

        self.clear()

        self.edit_number_label.grid(row = 0, column = 2)
        self.edit_number_entry.grid(row = 0, column = 3)

        self.edit_find_button.grid(row = 1, column = 3)

        self.edit_name_label.grid(row = 2, column = 2)
        self.edit_name_entry.grid(row = 3, column = 2)
        
        self.edit_grade_label.grid(row = 2, column = 3)
        self.edit_grade_entry.grid(row = 3, column = 3)

        self.edit_address_label.grid(row = 6, column = 2)
        self.edit_address_entry.grid(row = 7, column = 2)

        self.edit_eContactName_label.grid(row = 4, column = 2)
        self.edit_eContactName_entry.grid(row = 5, column = 2)

        self.edit_eContactNumber_label.grid(row = 4, column = 3)
        self.edit_eContactNumber_entry.grid(row = 5, column = 3)

        self.edit_update_button.grid(row = 7, column = 3)

    def edit_find_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "SELECT * FROM student WHERE studentID = %s"
        fetch = (self.edit_number_entry.get(), )

        mycursor.execute(sql, fetch,)

        records = mycursor.fetchall()

        self.edit_name_entry.delete(0, 'end')
        self.edit_grade_entry.delete(0, 'end')
        self.edit_address_entry.delete(0, 'end')
        self.edit_eContactName_entry.delete(0, 'end')
        self.edit_eContactNumber_entry.delete(0, 'end')

        for x in records:
            self.edit_name_entry.insert(0, x[1])
            self.edit_grade_entry.insert(0, x[5])
            self.edit_address_entry.insert(0, x[2])
            self.edit_eContactName_entry.insert(0, x[3])
            self.edit_eContactNumber_entry.insert(0, x[4])  

    def edit_update(self):

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "UPDATE student SET studentName = %s, grade = %s, adress = %s, contactName = %s, contactNumber = %s,  WHERE studentID = %s"
        fetch = (self.edit_name_entry.get(), self.edit_grade_entry.get(), self.edit_address_entry.get(), self.edit_eContactName_entry.get(), self.edit_eContactNumber_entry.get(), self.edit_number_entry.get(), )

        mycursor.execute(sql, fetch,)
        db.commit()

        print(done)

    
    def list_student_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.list_student_button['state'] = 'disabled'
        
        self.clear()

        self.list_student_label.grid(row = 0, column = 2)
        self.list_student_text.grid(row = 1, column = 2)

        
        sql = "SELECT * FROM student"
        mycursor.execute(sql)

        records = mycursor.fetchall()

        for x in records:
            strng = str(list(x))
            self.list_student_text.insert(tk.END, strng)
            self.list_student_text.insert(tk.END, "\n\n")

    def add_student_func(self):
        
        for x in self.start:
            x.configure(state="normal")
        self.add_student_button['state'] = 'disabled'        

        self.clear()

        self.add_student_name_label.grid(row = 0, column = 2)
        self.add_student_name_entry.grid(row = 1, column = 2)

        self.add_student_address_label.grid(row = 2, column = 2)
        self.add_student_address_entry.grid(row = 3, column = 2)
        
        self.add_student_eContactName_label.grid(row = 4, column = 2)
        self.add_student_eContactName_entry.grid(row = 5, column = 2)

        self.add_student_eContactNumber_label.grid(row = 4, column = 3)
        self.add_student_eContactNumber_entry.grid(row = 5, column = 3)

        self.add_student_grade_label.grid(row = 0, column = 3)
        self.add_student_grade_entry.grid(row = 1, column = 3)

        self.add_student_data_button.grid(row = 6, column = 3)

    def add_student_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "INSERT INTO student (studentName, adress, contactNumber, contactName, grade) VALUES (%s, %s, %s, %s, %s)"
        fetch = (self.add_student_name_entry.get(), self.add_student_address_entry.get(), self.add_student_eContactName_entry.get(), self.add_student_eContactNumber_entry.get(), self.add_student_grade_entry.get(), )

        mycursor.execute(sql, fetch,)
        db.commit()

    def search_faculty_func(self):
         
        for x in self.start:
            x.configure(state="normal")
        self.search_faculty_button['state'] = 'disabled'

        self.clear()

        self.search_faculty_number_label.grid(row = 0, column = 2)
        self.search_faculty_number_entry.grid(row = 0, column = 3)
        
        self.search_faculty_name_label.grid(row = 1, column = 2)
        self.search_faculty_name_entry.grid(row = 1, column = 3)

        self.search_faculty_position_label.grid(row = 2, column = 2)
        self.search_faculty_position_entry.grid(row = 2, column = 3)

        self.search_faculty_search_button.grid(row = 3, column = 2)
        self.delete_faculty_button.grid(row = 3, column = 3)

        self.search_faculty_text.grid(row = 5, column = 4)

    def search_faculty_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "SELECT * FROM faculty WHERE facultyID = %s OR facultyName = %s OR position = %s"
        fetch_name = (self.search_faculty_number_entry.get(),  self.search_faculty_name_entry.get(), self.search_faculty_position_entry.get(), )

        mycursor.execute(sql, fetch_name,)

        records = mycursor.fetchall()

        self.search_text.delete('1.0', 'end')
        
        for x in records:
            strng = str(list(x))
            self.search_faculty_text.insert(tk.END, strng)
            self.search_faculty_text.insert(tk.END, "\n\n")

    def add_faculty_func(self):
        
        for x in self.start:
            x.configure(state="normal")
        self.add_faculty_button['state'] = 'disabled'        

        self.clear()                         

        self.add_faculty_name_label.grid(row = 0, column = 2)
        self.add_faculty_name_entry.grid(row = 1, column = 2)

        self.add_faculty_possition_label.grid(row = 2, column = 2)
        self.add_faculty_possition_entry.grid(row = 3, column = 2)
        
        self.add_faculty_sickDays_label.grid(row = 4, column = 2)
        self.add_faculty_sickDays_entry.grid(row = 5, column = 2)

        self.add_faculty_hireDate_label.grid(row = 4, column = 3)
        self.add_faculty_hireDate_entry.grid(row = 5, column = 3)

        self.add_faculty_password_label.grid(row = 0, column = 3)
        self.add_faculty_password_entry.grid(row = 1, column = 3)

        self.add_faculty_data_button.grid(row = 6, column = 3)

    def add_faculty_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "INSERT INTO faculty (facultyName, position, sickDaysLeft, hireDate, password) VALUES (%s, %s, %s, %s, %s)"
        fetch = (self.add_faculty_name_entry.get(), self.add_faculty_possition_entry.get(), self.add_faculty_sickDays_entry.get(), self.add_faculty_hireDate_entry.get(), self.add_faculty_password_entry.get(), )

        mycursor.execute(sql, fetch,)
        db.commit()


    def list_staff_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.list_staff_button['state'] = 'disabled'
        
        self.clear()

        self.list_staff_label.grid(row = 0, column = 2)
        self.list_staff_text.grid(row = 1, column = 2)

        
        sql = "SELECT * FROM faculty"
        mycursor.execute(sql)

        records = mycursor.fetchall()

        for x in records:
            strng = str(list(x))
            self.list_staff_text.insert(tk.END, strng)
            self.list_staff_text.insert(tk.END, "\n\n")

    def delete_faculty_action(self):
        sql = "DELETE FROM faculty where facultyID = %s"
        fetch_name = (self.search_faculty_number_entry.get(),)

        mycursor.execute(sql, fetch_name,)
        db.commit()


    def covid_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.covid_button['state'] = 'disabled'        

        self.clear()

        self.covid_reselts_text.grid(row = 4, column = 1)
        self.delete_covid_entry.grid(row = 6, column = 1)
        self.delete_covid_button.grid(row = 7, column = 1)

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "SELECT * FROM covid ORDER BY testDate DESC"

        mycursor.execute(sql, )

        records = mycursor.fetchall()
        
        for x in records:
            strng = str(list(x))
            self.covid_reselts_text.insert(tk.END, strng)
            self.covid_reselts_text.insert(tk.END, "\n\n")

    def covid_add_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.add_student_button['state'] = 'disabled'        

        self.clear()

        self.add_covid_studentID_label.grid(row = 0, column = 2)
        self.add_covid_studentID_entry.grid(row = 1, column = 2)

        self.add_covid_testDate_label.grid(row = 2, column = 2)
        self.add_covid_testDate_entry.grid(row = 3, column = 2)
        
        self.add_covid_result_label.grid(row = 4, column = 2)
        self.add_covid_result_entry.grid(row = 5, column = 2)

        self.add_covid_isolationBegin_label.grid(row = 4, column = 3)
        self.add_covid_isolationBegin_entry.grid(row = 5, column = 3)

        self.add_covid_isolationEnd_label.grid(row = 0, column = 3)
        self.add_covid_isolationEnd_entry.grid(row = 1, column = 3)

        self.covid_add_button.grid(row = 6, column = 3)

    def covid_add_action(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "INSERT INTO covid (studentID, testDate, results, isolationBegin, isolationEnd) VALUES (%s, %s, %s, %s, %s)"
        fetch = (self.add_covid_studentID_entry.get(), self.add_covid_testDate_entry.get(), self.add_covid_result_entry.get(), self.add_covid_isolationBegin_entry.get(), self.add_covid_isolationEnd_entry.get(), )

        mycursor.execute(sql, fetch,)
        db.commit()

    def delete_covid(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "DELETE FROM covid WHERE testID =  %s"
        fetch = (self.delete_covid_entry.get(), )

        mycursor.execute(sql, fetch,)
        db.commit()


        self.covid_reselts_text.delete('1.0', 'end')

        sql = "SELECT * FROM covid ORDER BY testDate DESC"

        mycursor.execute(sql, )

        records = mycursor.fetchall()
        
        for x in records:
            strng = str(list(x))
            self.covid_reselts_text.insert(tk.END, strng)
            self.covid_reselts_text.insert(tk.END, "\n\n")


    def medical_add_func(self):
        for x in self.start:
            x.configure(state="normal")
        self.add_medical_button['state'] = 'disabled'

        self.clear()
        
        self.add_medical_studentID_label.grid(row = 0, column = 2)
        self.add_medical_studentID_entry.grid(row = 1, column = 2)        

        self.add_medical_medication_label.grid(row = 2, column = 2)
        self.add_medical_medication_entry.grid(row = 3, column = 2)

        self.add_medical_dosage_label.grid(row = 4, column = 2)
        self.add_medical_dosage_entry.grid(row = 5, column = 2)

        self.add_medical_vaccine_label.grid(row = 4, column = 3)
        self.add_medical_vaccine_entry.grid(row = 5, column = 3)

        self.add_medical_variedCondition_label.grid(row = 0, column = 3)
        self.add_medical_variedCondition_entry.grid(row = 1, column = 3)

        self.add_medical_currentStatus_label.grid(row = 2, column = 3)
        self.add_medical_currentStatus_entry.grid(row = 3, column = 3)

        self.medical_add_button.grid(row = 6, column = 3)

    def medical_add_action(self):         
        
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        sql = "INSERT INTO medicalInfo (studentID, medication, dosage, vaccines, variedCondition, currentStatus) VALUES (%s, %s, %s, %s, %s, %s)"
        fetch = (self.add_medical_studentID_entry.get(), self.add_medical_medication_entry.get(), self.add_medical_dosage_entry.get(), self.add_medical_vaccine_entry.get(), self.add_medical_variedCondition_entry.get(),self.add_medical_currentStatus_entry.get(), )

        mycursor.execute(sql, fetch,)
        db.commit()

    def search_medical_func(self):

        for x in self.start:
            x.configure(state="normal")
        self.search_medical_button['state'] = 'disabled'        

        self.clear()

        self.medical_text.grid(row = 4, column = 1)
        self.delete_medical_entry.grid(row = 6, column = 1)
        self.delete_medical_button.grid(row = 7, column = 1)

        self.search_medication_label.grid(row = 8, column = 1)
        self.search_medication_entry.grid(row = 9, column = 1)
        self.search_medication_button.grid(row = 10, column = 1)

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        self.covid_reselts_text.delete('1.0', 'end')

        sql = "SELECT * FROM medicalInfo GROUP BY studentID ORDER BY recordID DESC"

        mycursor.execute(sql, )

        records = mycursor.fetchall()
        
        for x in records:
            strng = str(list(x))
            self.medical_text.insert(tk.END, strng)
            self.medical_text.insert(tk.END, "\n\n")



    def delete_medical(self):
        sql = "DELETE FROM medicalInfo WHERE studentID = %s"
        fetch_name = (self.delete_medical_entry.get(),)

        mycursor.execute(sql, fetch_name,)
        db.commit()

        self.medical_text.delete('1.0', 'end')

        sql = "SELECT * FROM medicalInfo GROUP BY studentID ORDER BY recordID DESC"

        mycursor.execute(sql, )

        records = mycursor.fetchall()
        
        for x in records:
            strng = str(list(x))
            self.medical_text.insert(tk.END, strng)
            self.medical_text.insert(tk.END, "\n\n")

    def medication_lookup(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()

        self.medical_text.delete('1.0', 'end')

        sql = "SELECT student.studentName, medicalInfo.medication, SUM(medicalInfo.dosage) FROM medicalInfo INNER JOIN student ON student.studentID = medicalInfo.studentID WHERE medicalInfo.studentID = %s"
        fetch = (self.search_medication_entry.get(),)
        mycursor.execute(sql, fetch,)

        records = mycursor.fetchall()
        
        for x in records:
            strng = str(list(x))
            self.medical_text.insert(tk.END, strng)
            self.medical_text.insert(tk.END, "\n\n")

    def clear(self):
        for x in self.edit:
            x.grid_forget()
        for x in self.search:
            x.grid_forget()
        for x in self.list_staff:
            x.grid_forget()
        for x in self.list_student:
            x.grid_forget()
        for x in self.add_student:
            x.grid_forget()
        for x in self.add_faculty:
            x.grid_forget()
        for x in self.search_faculty:
            x.grid_forget()
        for x in self.covid:
            x.grid_forget()
        for x in self.add_covid:
            x.grid_forget()
        for x in self.medical:
            x.grid_forget()
        for x in self.medical_search:
            x.grid_forget()
        for x in self.transfer:
            x.grid_forget()
        for x in self.isolate:
            x.grid_forget()
        for x in self.testing:
            x.grid_forget()
        for x in self.schedule:
            x.grid_forget()
        

    def login_validate(self):
        user = self.login_user_entry.get()
        passwd = self.login_passwd_entry.get()

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="testdatabase")

        mycursor = db.cursor()
        sql = "SELECT facultyName, position FROM faculty where facultyName = %s AND password = %s"
        fetch = (self.login_user_entry.get(), self.login_passwd_entry.get(), )

        mycursor.execute(sql, fetch)

        records = mycursor.fetchall()
        for row in records:
            self.userName = row[0]
            validity = row[1]
        if(records):
            if validity == 'Executive':
                self.permissions = True
            for x in self.login:
                x.grid_forget()

            for x in self.start:
                x.configure(state="normal")
        print(self.permissions)

if __name__ == '__main__':
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase")

    mycursor = db.cursor()

    #with open('results.csv', 'r') as csvfile:
    #    reader = csv.reader(csvfile, delimiter=',')
    #    for row in reader:
    #        mycursor.execute(
    #        'INSERT \
    #        \INTO results(studentID, test, diagnosis, resultDate) \
    #        \VALUES (%s, %s, %s, %s)', row)

    #db.commit()

    root = tk.Tk()
    run = App(root)
    root.mainloop()











    

