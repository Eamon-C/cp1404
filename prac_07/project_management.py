"""
CP1404 prac, week 7
project_management.py
estimated time: 3 hours
actual: 12:00
"""

import datetime
from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit\n>>> "


def main():
    """main function"""
    choice = input(MENU).upper()
    filename = "projects.txt"   # sets default filename
    projects = []
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            print(f"{filename} loaded.")
            choice = input(MENU).upper()
        # elif choice == "S":
        #
        elif choice == "D":
            extract_data(filename, projects)
            projects.sort()
            display_projects(projects)
        # elif choice == "F":
        #
        # elif choice == "A":
        #
        # elif choice == "U":
        break
    print("Thank you for using custom-built project management software.")


def display_projects(projects):
    """displays projects separated by completion status and ordered by priority"""
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"    {project.name}, start: {project.start_date}, priority {project.priority}, estimate: "
                  f"${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")
    print("Complete projects:")
    for project in projects:
        if project.is_complete():
            print(f"    {project.name}, start: {project.start_date}, priority {project.priority}, estimate: "
                  f"${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")


def extract_data(filename, projects):
    """extracts data from chosen file and stores as objects in a list"""
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("	")
        projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))


main()
