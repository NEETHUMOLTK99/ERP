import  teams as t
import org as o
import employee as emp
from empstore import employees
from empstore import teams
from empstore import org
while True:
	print("Press 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for search employee")
	print("Press 4 for display  employee")
	print("Press 5 for change employee details")
	print("Press 6 manage all teams")
	print("Press 7 for Quit")
	ch = int(input("Enter choice:"))
	
	o.org_details()
	#first organization details 
	emp.main_menu()
	ch=int(input("enter your choice: "))
	if ch == 1:
	#adding employee
		emp.add_employee()
			
	elif ch == 2:
	#delete
		emp.delete_employee()
	elif ch == 3:
	#search
		emp.search_employee()
	elif ch == 4:
	#display employee
		emp.display_employee()
	elif ch== 5:
	#change employee details
		emp.change_employee()
	elif ch == 6:
	
		t.manage_all_teams()
	elif ch == 7:
		break
	else:
		print("Invalid Choice")

    

