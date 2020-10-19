import sqlite3
import random
import datetime
import os	
from prettytable import PrettyTable
con=sqlite3.connect("bank.db")
cus=con.cursor()

################## CREATING TABLE ####################
	
cus.execute(''' CREATE TABLE if not exists user(
acc_no TEXT PRIMARY KEY, 
name TEXT,
f_name TEXT,
DOB DATE,
phone INTEGER,
balance REAL  ) ''')

cus.execute(''' CREATE TABLE if not exists history(
h_id INTEGER PRIMARY KEY autoincrement, 
acc_no TEXT,
td TEXT,
purpose TEXT,
balance REAL,
total REAL,
a_id TEXT,
FOREIGN KEY (acc_no) REFERENCES user(acc_no) 
FOREIGN KEY (a_id) REFERENCES admin(a_id) ) ''')

###################### CREATE ACCOUNT ########################

def create_acc(a_id):
	os.system('cls')
	print("		CREATE ACCOUNT")
	
	while True:
		name=input("ACCOUNT HOLDER NAME : ")
		if check_name(name)==1:
			break
		else:
			print("INVALID INPUT !!!!")

	while True:
		f_name=input("ACCOUNT HOLDER'S FATHER NAME : ")
		if check_name(f_name)==1:
			break
		else:
			print("INVALID INPUT !!!!")

	while True:
		DOB=input("DATE OF BIRTH (DD/MM/YYYY) : ")
		if (check_dob(DOB))==1:
			break
		else:
			print("INVALID INPUT !!!!")
	
	while True:
		phone=input("PHONE NUMBER : ")
		if (check_phone(phone))==1:
			break
		else:
			print("INVALID INPUT !!!!")
	
	while True:
		balance=input("STARTING BALANCE : ")
		if (check_amt(balance))==1:
			break
		else:
			print("INVALID INPUT !!!!")
	while True:
		acc="ACCNO"+str(random.randrange(10000,99999))
		cus.execute("select * from user where acc_no=='"+acc+"'")		
		d=cus.fetchall()
		if len(d)==0:
			break
	
	t=(acc,name,f_name,DOB,phone,balance) 
	cus.execute(''' INSERT into user (acc_no,name,f_name,DOB,phone,balance) values (?,?,?,?,?,?) ''',t)
	con.commit()
	t=(acc,td(),"INITIAL",balance,balance,a_id) 
	cus.execute(''' INSERT into history (acc_no,td,purpose,balance,total,a_id) values (?,?,?,?,?,?) ''',t)
	con.commit()
	print("CONGRATULATIONS, ACCOUNT SUCCESSFULLY :) ")
	print("ACCOUNT NO. : ",acc)
	print("TOTAL AMOUNT : ",balance)
	input("PRESS ENTER TO CONTINUE.....")
	menu2(a_id)

############################# ADMIN LOGIN ####################

def admin_login():
	os.system('cls')
	print("		ADMIN LOGIN")
	n=input("USERNAME : ")
	p=input("PASSWORD : ")
	t=(n,p)
	cus.execute("SELECT * from admin where name=? and password=? ",t)		
	d=cus.fetchall()
	if d==[]:
		print("INVALID USERNAME OR PASSWORD !!!! PLEASE TRY AGAIN.....")
		input("PRESS ENTER TO CONTINUE.....")
		menu()
	else:
		menu2(d[0][0])

######################## MAIN MENU #########################

def menu():
	os.system('cls')
	ch=input('''
		MAIN MENU
		1) ADMIN LOGIN 
		2) EXIT
		ENTER YOUR CHOICE : ''')
	if ch=='1':
		admin_login()
	elif ch=='2':
		exit()
	else:
		print("INVALID CHOICE !!!! PLEASE TRY AGAIN.....")
		input("PRESS ENTER TO CONTINUE.....")
		menu()

###################### MENU 2 ######################

def menu2(a_id):
	os.system('cls')
	ch=input(''' 
				ADMIN PANEL
				1) CREATE NEW ACCOUNT
				2) DEPOSIT AMOUNT
				3) WITHDRAWAL AMOUNT
				4) VIEW ALL TRANSACTION
				5) VIEW ALL LOGS
				6) LOGOUT
				ENTER YOUR CHOICE : ''')
	if ch=='1':
		create_acc(a_id)
	elif ch=='2':
		deposit_amt(a_id)
	elif ch=='3':
		withdrawal_amt(a_id)
	elif ch=='6':
		menu()
	elif ch=='5':
		log(a_id)
	elif ch=='4':
		history(a_id)
	else:
		print("INVALID CHOICE !!!! PLEASE TRY AGAIN.....")
		input("PRESS ENTER TO CONTINUE.....")
		menu2(a_id)

########################## DEPOSIT AMOUNT #########################

def deposit_amt(a_id):
	os.system('cls')
	print("		DEPOSIT PANEL")
	acc=input("ACCOUNT NO. : ")
		
	while True:
		n=input("ACCOUNT HOLDER NAME : ")
		if check_name(n)==1:
			break
		else:
			print("INVALID INPUT !!!!")
	cus.execute("SELECT * from user where name=='"+n+"' and acc_no=='"+acc+"'")		
	d=cus.fetchall()
	if d==[]:
		print("INVALID USERNAME OR PASSWORD !!!! PLEASE TRY AGAIN.....")
	else:
		while True:
			amt=input("DEPOSIT BALANCE : ")
			if (check_amt(amt))==1:
				break
			else:
				print("INVALID INPUT !!!!")
		t=(float(amt)+d[0][5],acc,n)
		cus.execute(" UPDATE user set balance=? where acc_no==? and name==? ",t)
		con.commit()
		print("TOTAL AMOUNT : ",float(amt)+d[0][5])
		t=(acc,td(),"DEBIT",amt,float(amt)+d[0][5],a_id) 
		cus.execute(''' INSERT into history (acc_no,td,purpose,balance,total,a_id) values (?,?,?,?,?,?) ''',t)
		con.commit()
		print("CONGRATULATIONS, AMOUNT DEPOSIT SUCCESSFULLY :) ")
	input("PRESS ENTER TO CONTINUE.....")
	menu2(a_id)

########################## WITHDRAWAL AMOUNT ###########################

def withdrawal_amt(a_id):
	os.system('cls')
	print("		WITHDRAWAL PANEL")
	acc=input("ACCOUNT NO. : ")
		
	while True:
		n=input("ACCOUNT HOLDER NAME : ")
		if check_name(n)==1:
			break
		else:
			print("INVALID INPUT !!!!")
	cus.execute("SELECT * from user where name=='"+n+"' and acc_no=='"+acc+"'")		
	d=cus.fetchall()
	if d==[]:
		print("INVALID USERNAME OR PASSWORD !!!! PLEASE TRY AGAIN.....")
	else:
		while True:
			amt=input("WITHDRAWAL BALANCE : ")
			if (check_amt(amt))==1:
				break
			else:
				print("INVALID INPUT !!!!")
		if(d[0][5]-float(amt)<0):
			print("INSUFFICIENT BALANCE....")
		else:
			t=(d[0][5]-float(amt),acc,n)
			cus.execute(" UPDATE user set balance=? where acc_no==? and name==? ",t)
			con.commit()
			print("CONGRATULATIONS, AMOUNT WITHDRAWAL SUCCESSFULLY :) ")
			print("TOTAL AMOUNT : ",d[0][5]-float(amt))
			t=(acc,td(),"CREDIT",amt,d[0][5]-float(amt),a_id) 
			cus.execute(''' INSERT into history (acc_no,td,purpose,balance,total,a_id) values (?,?,?,?,?,?) ''',t)
			con.commit()
	input("PRESS ENTER TO CONTINUE.....")
	menu2(a_id)

############################## HISTORY ##########################	

def history(a_id):
	os.system('cls')
	print("			TRANSACTION PANEL")
	acc=input("ACCOUNT NO. : ")
		
	while True:
		n=input("ACCOUNT HOLDER NAME : ")
		if check_name(n)==1:
			break
		else:
			print("INVALID INPUT !!!!")
	cus.execute("SELECT * from user where name=='"+n+"' and acc_no=='"+acc+"'")		
	d=cus.fetchall()
	if d==[]:
		print("INVALID USERNAME OR PASSWORD !!!! PLEASE TRY AGAIN.....")
	else:
		cus.execute("SELECT * from history where acc_no='"+acc+"' ")
		x=PrettyTable()
		x.field_names=['TRANS_ID','DATE & TIME','PURPOSE','AMOUNT','TOTAL BALANCE']
		d=cus.fetchall()
		for a in d:
			x.add_row([a[0],a[2],a[3],a[4],a[5]])
		print(x)
	input("PRESS ENTER TO CONTINUE.....")
	menu2(a_id)

############################# LOGS ################################

def log(a_id):
	os.system('cls')
	print("					LOGS PANEL")
	x=PrettyTable()
	x.field_names=['TRANS_ID','DATE & TIME','AD_ID','AD_NAME','ACC_NO','HOLDER NAME','PURPOSE','AMOUNT','TOTAL BAL']
	cus.execute("SELECT history.h_id,history.td,admin.a_id,admin.name,user.acc_no,user.name,history.purpose,history.balance,history.total from ((history inner join user on history.acc_no = user.acc_no)inner join admin on history.a_id = admin.a_id) ")
	d=cus.fetchall()
	for a in d:
		x.add_row(a)
	print(x)
	input("PRESS ENTER TO CONTINUE.....")
	menu2(a_id)

########################### SOME FUNCTION ##############################

def check_name(name):
	if ((name=='') or name.isspace()):
		return 0
	else:
		for a in name:
			if (a.isalpha() or a.isspace() or a=="."):
				pass
			else:
				return 0
		return 1

def check_dob(dob):
	l=dob.split('/')
	if len(l)==3:
		try:
			datetime.datetime(int(l[2]),int(l[1]),int(l[0]))
			if (int(l[2])<=2020):
				return 1
			else:
				return 0
		except:
			return 0
	else:
		return 0

def check_amt(amt):
	if amt=='':
		return 0
	else:
		for a in amt:
			if (a.isdigit() or a=='.'):
				pass
			else:
				return 0
		return 1

def check_phone(phone):
	if len(phone)==10:
		if phone.isdigit():
			return 1
		else:
			return 0
	else:
		return 0

def td():
	x = datetime.datetime.now()
	return x.strftime("%x %X")
###########################################################################################
 
##################### CALLING MAIN MENU ################################# 
menu()