""" Author: Dillon Hamman
    program: Record_Sorter.py
    Date: 5/10/2019
    Purpose: This program takes in files containing records of people
        and sorts them by 3 different categories: age, last name and
        gender (followed by last name).
"""

from datetime import datetime
import sys
from operator import itemgetter

GENDER = []
LASTNAME = []
DOB = []


class People:
    """
    This class creates instances of people with certain attributes,last name
    first name, gender, favorite color and date of birth.
    """

    def __init__(self, last_name, first_name, gender, color, dob):
        self._last_name = last_name
        self._first_name = first_name
        self._gender = gender
        self._dob = dob
        self._color = color

    def __str__(self):
        return (self._last_name + ' ~ ' + self._first_name + ' ~ ' +
                self._gender + ' ~ ' + self._color + ' ~ ' + self._dob)


def main():
    records = []  # create a list to store the objects
    file = input('File name: ')
    records = read_files(file, records)
    sort_by_last(records)
    print()
    sort_by_age(records)
    print()
    sort_by_gender(records)


def sort_by_gender(record_list):
    """This function takes in the record list and sorts it by gender first
    then by last name.
    """
    print("Records sorted by gender:")
    gender_sort = sorted(record_list, key=lambda x: \
        (x._gender, x._last_name))
    GENDER.sort(key=itemgetter("gender", "last name"))
    for record in gender_sort:  # print record list
        print(record)


def sort_by_last(record_list):
    """This function takes in the record list and then outputs the
    contents based on the last name of the person object.
    """
    print("Records sorted by last name:")
    last_name_sort = sorted(record_list, key=lambda x: x._last_name
                            , reverse=True)
    LASTNAME.sort(key=itemgetter("last name"))
    for record in last_name_sort:  # print record list
        print(str(record))


def sort_by_age(record_list):
    """ This function takes in the record list as a parameter and
    outputs the contents based on the age of the person.
    """
    print("Records sorted by age:")
    age_sort = sorted(record_list, key=lambda x: datetime.strptime
    (x._dob, '%m/%d/%Y'), reverse=True)
    DOB.sort(key=itemgetter('date of birth'), reverse=True)
    for record in age_sort:  # print record list
        print(str(record))


def read_post(contents):
    """This function takes in the contents of a [POST] request in
    record_api.py and adds it to the following sorted lists"""
    if ", " in contents:
        GENDER.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})
        LASTNAME.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})
        DOB.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})
    elif "|" in line:
        GENDER.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})
        LASTNAME.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})
        DOB.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})
    else:
        GENDER.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})
        LASTNAME.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})
        DOB.append({"last name": contents[0], "first name": contents[1], "gender":
            contents[2], "favorite color": contents[3], "date of birth": contents[4]})


def read_files(infile1, records):
    """This function reads in a file and turns its contents into an object to
    be printed in the main file. It also adds the contents of each line to each
    global list used in the API.
    These file lines can be separated by "|", "," or " ".
    """
    try:
        file = open(infile1).readlines()  # open file as file
    except FileNotFoundError:
        print("ERROR: Could not open file:", infile1)
        sys.exit()

    for line in file:  # check in line in the file
        if ", " in line:
            contents = line.strip().split(', ')  # remove \n and split by ','
            person = People(contents[0], contents[1], contents[2], contents[3]
                            , contents[4])
            records.append(person)
            # format to json for API
            GENDER.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})
            LASTNAME.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})
            DOB.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})
        elif "|" in line:
            contents = line.strip().split(' | ')  # remove \n and split by '|'
            person = People(contents[0], contents[1], contents[2], contents[3]
                            , contents[4])
            records.append(person)
            GENDER.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})
            LASTNAME.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})
            DOB.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})
        else:
            contents = line.strip().split(' ')  # remove \n and split by '|'
            person = People(contents[0], contents[1], contents[2], contents[3]
                            , contents[4])
            records.append(person)
            GENDER.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})
            LASTNAME.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})
            DOB.append({"last name": contents[0], "first name": contents[1], "gender":
                contents[2], "favorite color": contents[3], "date of birth": contents[4]})

    return records


main()
