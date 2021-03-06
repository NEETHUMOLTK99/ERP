from empstore import teams
import employee as emp
from empstore import employees
def manage_all_team_menu():
	print("\t1.Create team")
	print("\t2.Display team")
	print("\t3.Manage team(Particular)")
	print("\t4.Delete team")
	print("\t5.Exit")

def manage_all_teams():
	while True:
		manage_all_team_menu()
		ch = int(input("\tEnter your choice "))
		if ch == 1:
			#Create team
			create_team()
		elif ch == 2:
			#display teams
			display_teams()
		elif ch == 3:
			#Manage group(Particular)
			manage_team()
		elif ch == 4:
			#Delete Group
			delete_team()
		elif ch == 5:
			#exit
			break
		else:
			print("\tInvalid choice")	
def create_team():
	team_name = input("\tEnter team name ")
	teams[team_name] = []

def delete_team():
	team_name = input("\tEnter team name ")
	if team_name in teams.keys():
		del teams[team_name]
		print("\tDeleted the team")
	else:
		print("\tWrong team name")

def display_teams():
	for key,value in teams.items(): #key is group_name,value is list of student serial no
		name_string = ""
		for i in value:
			name_string = name_string +"|"+emp.employees[i]["name"]
		print(f"{key} => {name_string}")
def manage_team_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
#	print("\t\t4.Exit")

def manage_team():
	team_name = input("\t\tEnter team name ")
	manage_team_menu()
	ch = int(input("\t\t Enter your Choice "))
	if ch == 1:
		#Add member
		add_member(team_name)
	elif ch == 2:
		#Delete member
		delete_member(team_name)
	elif ch == 3:
		#List member
		list_member(team_name)
	else:
		print("\tInvalid choice")

def add_member(team_name):
	display_employee()
	serial_no = input("\t\tEnter the serial no of employee ")
	if serial_no in emp.employees.keys():
		teams[team_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")

def list_member(team_name):
	name_string=""
	for i in teams[team_name]:
		name_string = name_string +"|"+i+"."+emp.employees[i]["name"]
	print(f"{name_string}")

def delete_member(team_name):
	list_member(team_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in teams[team_name]:
		groups[team_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")

