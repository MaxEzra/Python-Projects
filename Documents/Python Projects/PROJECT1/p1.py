"""
File: p1.py
Author: Ezra Enchill
Date: 11/4/2022
Lab Section: 42
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''

def list_students_not_in_class(group, present):
    students_missing = []
    roster_list = []

    for i in range(len(group)):
        for j in range(len(present)):
            if group[i] in present[j]:
                roster_list.append(i)
    for i in range(len(group)):
        if i not in roster_list:
            students_missing.append(group[i])
    return students_missing


def list_all_times_checking_in_and_out(student, attendance):
    individual = []
    
    for i in range(len(attendance)): 
        if student in attendance[i]: 
            individual.append(attendance[i])
    return individual


def list_all_times_checked_in(attendance):
    roster = []
    individuals = []
    for student in attendance:
        names = student.split(",")[0]+","+student.split(",")[1]
        if names not in individuals: 
            roster.append(student)
        individuals.append(names)
    return roster


def list_students_late_to_class(time,checkind):
    present = []
    late = []
    for roster in checkind: 
        fname = roster.split(",")[0]
        lname = roster.split(",")[1]
        names = (fname, ",", lname)
        cutoff_seconds = int(time.split(":")[0])*3600 + int(time.split(":")[1])*60 + int(time.split(":")[2])
        checkedin_seconds = int(roster.split(",")[2].split(":")[0])*3600 + int(roster.split(",")[2].split(":")[1])*60 + int(roster.split(",")[2].split(":")[2])
        if names not in present and checkedin_seconds > cutoff_seconds:
            late.append(roster)
        present.append(names)
    return late


def get_first_student_to_enter(attendData):
    theFirst = None
    earliest = 100000
    for roster in attendData: 
        fname = roster.split(",")[0]
        lname = roster.split(",")[1]
        names = (fname, lname)
        checkedin_seconds = int(roster.split(",")[2].split(":")[0])*3600 + int(roster.split(",")[2].split(":")[1])*60 + int(roster.split(",")[2].split(":")[2])
        if checkedin_seconds < earliest: 
            theFirst = names
            earliest = checkedin_seconds
    return theFirst



def printList(function):
    for x in function:
        print(x)





''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class    
    
    # load class roster here into a list
    classRoster = fill_roster()

    #figure out which attendance data file to load here
    
    #load data
    attendData = fill_attendance_data()
    
    #use different tests 
    # make sure roster was filled 
    #printList(classRoster)
    # make sure attendance data was loaded
    #printList(attendData)
    
    #list all those missing
    print("****** Students missing in class *************")    
    printList(list_students_not_in_class(classRoster, attendData))
    #list signin/out times for a student
    
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))  
    #display when students first signed in (and in attendance)

    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData)) 
    
    #display all of those students late to class
    print("****** Students that arrived late ********************")
    print(list_students_late_to_class("09:00:00", attendData))

    #display first student to enter class
    print("******* Get 1st student to enter class ****************")    
    print(get_first_student_to_enter(attendData))
    
''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''
