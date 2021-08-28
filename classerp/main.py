from user import User
from employee import Employee
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
    emp.append(Employee())
    emp[-1].insert()

def delete_employee():
    name = input("Enter name :")
    emp_l = list(filter(lambda a: a.name == name, emp))
    if len(emp) == 0:  # not st #st
        print("No employee found")
    else:
        pass



def display_employee():
    for i in emp:
        i.display()



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
        
