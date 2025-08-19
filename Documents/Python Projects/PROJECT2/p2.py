"""
File: p2.py
Author: Ezra Enchill
Date: 11/18/2022
Lab Section: 42
Email:  ezrae1@umbc.edu
Description:  Project 2 roster check
"""

# Comment the line below out if your have the load_dictionary function working!!
# Comment the line below out if your have the load_dictionary function working!!

# from dataEntryP2 import fillAttendanceData


# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!

def print_list(xlist):
    
    for element in xlist:
        print(element)
        

def connect_to_data_file(filename):
    infile = ""
    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file

def print_dictionary(data): 
    print(data)
    # Prints dictionary data if return pulls from dictionary

def print_count(data): 
    x = len(data)
    print("There were", x, "records for this query")
    # Prints the count for whatever query is being ran. 


def display_attendance_data_for_student(student, data):
    if student in data.keys():
        print(student, data[student]) 
        #Prints data for student if they are were in the data at any point of time. 
    if student not in data: 
        print("No student of this name in the attendance log")


def is_present(name, date, data):
    return date in data[name][1]
    # Simply returns true or false whether or not a person was in class on a specific date. 

def list_all_students_checked_in(date, data):
    test = []
    for x in data: 
        for i in data[x]:
            if date in i: 
                test.append(x)
                # Goes through the roster while searching for specific dates and appends those
                # Who match the date as present and appends them to an individual list. 
    return test

def list_all_students_checked_in_before(date, time, data):
    list = []
    
    for x in data.keys(): 
        for i in range(len(data[x])): 
            if date == data[x][i].split(",")[1].strip() and time > data[x][i].split(",")[0].strip(): 
                # Splits the time and date so that user inputted time and date can be compared to data
                # And find who came before paramters
                list.append(x)
                
    return list

def attendance_count(data):
    list = []
    for x in data: 
        if len(data[x]) == 2: 
            # Counts if individuals appear in the list of attendance data more than once
            list.append(x)
    return list

def showed_late(data):
    list = []
    for x in data: 
        if len(data[x]) == 1:
            
            list.append(x)
    return list 

def absent(data): 
    list = []
    for x in data: 
        if len(data[x]) == 0: 
            # 0 meaning the student never appears, marking them absent
            list.append(x)
    return list
          
def get_first_student_to_enter(date, data):
    firstStudent = []
    baseTime = "24:00:00"
    
    for x in data.keys(): 
        for i in range(len(data[x])): 
            
            seperate = data[x][i].split(",")[0].strip()
            if date == data[x][i].split(",")[1].strip():
                # Splits the dictionary into time and date to make it easier to evaluate.
                if seperate < baseTime: 
                    baseTime = seperate 
                    # If time is less than a base template time of 24 hours, the time given by individual is now set
                    # As the new base time. Loops continously until the smallest value is found. 
            
            if baseTime == data[i][x].split(",")[0].strip: 
                firstStudent.append[i]
                
    return firstStudent
                
                
    

            
def load_dictionary(infile):
    infile = open("dataAllShow1stAnd2ndClass.txt", "r")
    indexed = infile.read().split("\n")
    # Reads given file and splits it by white space. 
    
    dictionary = {}
    for x in indexed: 
        named_index = ",".join(x.split(",")[:2]).strip()
        td_index = ",".join(x.split(",")[2:]).strip()   
        # Seperates the First and Last name while joining them from date and time 
        if named_index not in dictionary: 
            dictionary[named_index] = [td_index]
        else: 
            dictionary[named_index].append(td_index)
            # Makes first and last name the key for the dictionary and time and date the values. 
            
    return dictionary

def load_roster(roster_file_name):
    get_roster = open("roster.txt", "r")
    list = []
    
    read_roster = get_roster.read().strip()
    
    for read_roster in get_roster: 
        list.append(read_roster.strip())
    # Simply turns roster into a list of first and last names. 
    return list
    
        

if __name__ == '__main__':

    infile = connect_to_data_file("rosters.txt")
    if(infile):
        print("connected to data file...")
    else:
        print("issue with data file... STOP")
        exit(1)

    data = load_dictionary(infile)
    # ************************
    # OR MANUALLY!!!
    # ************************

    # just making sure the data collected is good

    print_dictionary(data)
    print("********* Looking up Student Attendance Data ***********")
    display_attendance_data_for_student("Morrison, Simon", data)
    display_attendance_data_for_student("Arsenault, Al", data)


    print("********* Looking to see if Student was present on date ***********")
    print(is_present("Bower, Amy", "11/5/2022", data))
    print(is_present("Bower, Amy", "11/17/2022", data))
    

    # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/5/2022", data)
    print_list(result)
    print_count(result)

    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
    print_list(result)
    print_count(result)


    # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    result = attendance_count(data)
    print_list(result)
    print_count(result)
    
    # list the  students that showed up ONE of the days
    print("**** Those who attended ONE class ****")
    result = showed_late(data)
    print_list(result)
    
    # list the  students that have not shown up
    print("**** Those who have NOT attended a SINGLE class ****")
    result = absent(data)
    print_list(result)
    
    result = get_first_student_to_enter("11/4/2022", data)
    print(result)
    
    
    
    
    
    