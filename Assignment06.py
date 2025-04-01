# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Adam Packer, 3/26/25, Updated the starter file to add the functionality required by the assignment.
# ------------------------------------------------------------------------------------------ #

import json  # Imports the JSON module for working with .json files
import os  # Imports the OS module to check if the file exists

# Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''  # Menu shown to the user
FILE_NAME: str = "Enrollments.json"  # The name of the file used to read/write student data

# Data variables
menu_choice: str = ""  # Holds the user menu choice
students: list = []  # List to hold student registration data (list of dictionaries)

# Class Definitions
class IO:
    """Handles Input and Output"""

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu to the user"""
        print(menu)  # Prints the provided menu text

    @staticmethod
    def input_menu_choice():
        """Gets the user's menu selection"""
        return input("What would you like to do: ")  # Asks user for menu choice and returns it

    @staticmethod
    def input_student_data(student_data: list):
        """Prompts the user to enter student data and appends it to the list"""
        try:
            first = input("Enter the student's first name: ")  # Get first name
            if not first.isalpha():  # Validate name is alphabetic
                raise ValueError("First name must contain only letters.")
            last = input("Enter the student's last name: ")  # Get last name
            if not last.isalpha():  # Validate name is alphabetic
                raise ValueError("Last name must contain only letters.")
            course = input("Enter the course name: ")  # Get course name
            student_data.append({"FirstName": first, "LastName": last, "CourseName": course})  # Add to list
            print(f"You have registered {first} {last} for {course}.")  # Confirmation message
        except Exception as e:
            IO.output_error_messages("Error: Invalid student data.", e)  # Show formatted error

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays all student records"""
        print("-" * 50)  # Visual separator
        for student in student_data:  # Loop through all records
            print(f'{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')  # Print each
        print("-" * 50)  # Visual separator

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays error messages in a standardized format"""
        print(message)  # Show custom error message
        if error:  # If exception provided, show technical details
            print("-- Technical Error Message --")
            print(error.__doc__)  # Print documentation for the error
            print(error.__str__())  # Print string version of the error


class FileProcessor:
    """Handles reading and writing data to and from a JSON file"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a JSON file into the student_data list"""
        try:
            if not os.path.exists(file_name):  # Check if file exists
                with open(file_name, "w") as file:
                    json.dump([], file)  # Create empty file if not present
            with open(file_name, "r") as file:
                student_data.extend(json.load(file))  # Load file contents into list
        except Exception as e:
            IO.output_error_messages("Error reading from file.", e)  # Show error if read fails

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes student data to a JSON file"""
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)  # Save data to JSON
            print("The following data was saved to file:")  # Confirmation message
            IO.output_student_courses(student_data)  # Show what was saved
        except Exception as e:
            IO.output_error_messages("Error writing to file.", e)  # Show error if write fails


# Main Body of the Script
if __name__ == "__main__":
    FileProcessor.read_data_from_file(FILE_NAME, students)  # Load initial data from file

    while True:
        IO.output_menu(MENU)  # Show the menu to the user
        menu_choice = IO.input_menu_choice()  # Get the user's selection

        if menu_choice == "1":
            IO.input_student_data(students)  # Let the user add a student
        elif menu_choice == "2":
            IO.output_student_courses(students)  # Display current student records
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)  # Save student records to file
        elif menu_choice == "4":
            break  # Exit the loop
        else:
            IO.output_error_messages("Please only choose option 1, 2, 3, or 4.")  # Handle invalid input

    print("Program Ended.")  # Final message after loop exits

