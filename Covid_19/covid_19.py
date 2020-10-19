import requests
from prettytable import PrettyTable
import os

def menu():
	os.system('cls')
	ch=input('''
			COVID-19
			1) WORLD DETALIS
			2) INDIA DETALIS
			3) EXIT
			Enter your choice :  ''')
	if ch=='1':
		world()
	elif ch=='2':	
		india()
	elif ch=='3':
		exit()
	else:
		print("INVALID INPUT....")
		input("PLEASE ENTER TO CONT....")
		menu()
def ke():
	return "285f01e1d4msh918404bc322548fp1e8764jsncb116ffbdf11"


def india():
	os.system('cls')
	ch=input("Enter State name which u want to see : ")
	response = requests.get(f"https://corona-virus-world-and-india-data.p.rapidapi.com/api_india",
	 headers={
	   "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com",
	   "X-RapidAPI-Key": ke()}
	   )
	q='state_wise'
	d=response.json()
	if ch=='all':
		x=PrettyTable()
		x.field_names=['STATE','CASES','ACTIVE','DEATHS','RECOVERY','LAST UPDATE']
		for a in d[q]:
			if a !='Unknown':
				x.add_row([a,d[q][a]['confirmed'],d[q][a]['active'],d[q][a]['deaths'],d[q][a]['recovered'],d[q][a]['lastupdatedtime']])
		print(x)
	else:
		x=PrettyTable()
		x.field_names=['STATE','CASES','ACTIVE','DEATHS','RECOVERY','LAST UPDATE']
		for a in d['state_wise']:
			if a==ch:
				x.add_row([a,d[q][a]['confirmed'],d[q][a]['active'],d[q][a]['deaths'],d[q][a]['recovered'],d[q][a]['lastupdatedtime']])
		print(x)
	input("PLEASE ENTER TO CONT....")
	menu()

def world():
	os.system('cls')
	ch=input("Enter Country name which u want to see : ")
	response = requests.get(f"https://corona-virus-world-and-india-data.p.rapidapi.com/api",
	 headers={
	   "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com",
	   "X-RapidAPI-Key": ke()}
	   )
	d=response.json()
	q='countries_stat'
	if ch=='all':
		x=PrettyTable()
		x.field_names=['COUNTRY','CASES','ACTIVE','DEATHS','RECOVERY','NEW CASES','NEW DEATHS']
		for a in d[q]:
			x.add_row([a['country_name'],a['cases'],a['active_cases'],a['deaths'],a['total_recovered'],a['new_cases'],a['new_deaths']])
		print(x)
	else:
		x=PrettyTable()
		x.field_names=['COUNTRY','CASES','ACTIVE','DEATHS','RECOVERY','NEW CASES','NEW DEATHS']
		for a in d[q]:
			if a['country_name']==ch:
				x.add_row([a['country_name'],a['cases'],a['active_cases'],a['deaths'],a['total_recovered'],a['new_cases'],a['new_deaths']])
		print(x)
	input("PLEASE ENTER TO CONT....")
	menu()

menu()
