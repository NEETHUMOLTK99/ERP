from employee import Emp
from empstore import emp
import change_employee as cemp
import search_employee as semp

def main_menu():
    print("1. Add employee")
    print("2. Delete employee")
    print("3. Search employee")
    print("4. Display all employee")
    print("5. Change a employee's data")
    print("6. exit")


def add_employee():
    emp_id = input("\tEnter employee id : ")
    name = input("\tEnter employee name : ")
    age = input("\tEnter employee's age : ")
    gender = input("\tEnter employee's gender : ")
    place = input("\tEnter employee's place : ")
    salary = input("\tEnter employee's salary : ")
    previous_company = input("\tEnter employee's previous company name : ")
    joining_date = input("\tEnter employee's joining date : ")

    emp_temp = Emp(emp_id, name, age, gender, place,
                   salary, previous_company, joining_date)
    emp.append(emp_temp)


def delete_employee():
    name = input("Enter name :")
    emp_l = list(filter(lambda a: a.name == name, emp))
    if len(emp) == 0:  # not st #st
        print("No employee found")
    else:
        pass



def display_employee():
    for i in emp:
        print(
            f'{i.name} |{i.age} | {i.gender}|{i.place} |{i.salary} | {i.previous_company} | {i.joining_date} ')




while True:
    main_menu()
    ch = int(input("Enter choice : "))
    if ch == 1:
        # add employee
        add_employee()

    elif ch == 2:
        # delete employee
        delete_employee()

    elif ch == 3:
        # search employee
        semp.search_employee()
    elif ch == 4:
        display_employee()
    elif ch == 5:
        cemp.change_emp_data()
    elif ch == 6:
        break
    else:
        print("Invalid option")
