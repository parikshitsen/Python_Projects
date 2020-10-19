import pickle as p
import re
import os
import time
from prettytable import PrettyTable
################### MAIN MENU #######################
def menu():
	os.system('cls')
	n=input('''	
				MAIN MENU
		1 Dealer Registation
		2 Dealer Login
		3 User Registstion
		4 User Login
		5 Admin Login
		6 Exit
		Enter your choice :
		''')
	if n=='1':
		D_reg()
	elif n=='2':
		D_login()
	elif n=='3':
		u_reg()
	elif n=='4':
		u_login()
	elif n=='5':
		admin_login()
	elif n=='6':
		exit()
	else:
		print("Invalid Input")
		time.sleep(.5)
		menu()

############# DEALER REGISTERTION  ################################
def D_reg():
	os.system('cls')
	print("		DEALER REGISTERTION")
	file = open('delar.txt','rb')
	d=p.load(file)
	file.close()
	
	while True:
		flag = 0
		D_id=input("Enter Dealer Id : ")
		for a in d:
			if(d[a][0]==D_id):
				print("This Dealer ID already exist")
				flag = 1
		if flag==0:
			break		
	D_pass=input("Enter Password : ")
	D_name=input("Enter Name :")
	while True:
		D_email=input("Enter E-mail : ")
		ck=check(D_email)
		if ck == 1:
			break		
		else:
			print("Invalid Email")
	while True:
		D_phone=input("Enter Phone No. : ")
		k=check_p(D_phone)
		if k == 1:
			break		
		else:
			print("Invalid Phone No. ")
	
	D_address=input("Enter Address : ")
	file = open('delar.txt','wb')
	d[len(d)+1]=[D_id,D_pass,D_name,D_email,D_phone,D_address]
	p.dump(d,file)
	file.close()
	print("Registstion Successfully :)")
	time.sleep(.3)
	menu()

####################### DEALER LOGIN ##################################
def D_login():
	os.system('cls')
	print("		DEALER LOGIN")
	D_id=input("Enter Dealer Id : ")
	D_pass=input("Enter Password : ")

	file = open('delar.txt','rb')
	d=p.load(file)
	file.close()
	flag=0
	for a in d:
		if(d[a][0]==D_id and d[a][1]==D_pass):
			flag=1
			a=d[a][2]
			break	
	if flag==1:
		print("Login Successfully :)")
		print("Hello,",a)
		c_menu(D_id)
	else:
		print("Invalid Dealer Id and Password :(")
		time.sleep(.3)
		menu()

####################### CAB MENU #####################
def c_menu(D_id):
		ch=input('''
					CAB MENU
			1 Add Cab
			2 View Cab
			3 Delete Cab
			4 Change Password
			5 See All Request
			6 Logout 
			''')
		if ch=='1':
			add_cab(D_id)
		elif ch=='2':
			view_cab(D_id)
		elif ch=='3':
			del_cab(D_id)
		elif ch=='4':
			change_p(D_id)
		elif ch=='5':
			see_request(D_id)
		elif ch=='6':
			menu()
		else:
			print('Invalid Input')
			c_menu(D_id)

################# ADD CAB #################################
def add_cab(D_id):
	os.system('cls')
	print("		ADD CAB")
	file = open('cab.txt','rb')
	d=p.load(file)
	file.close()
	while True:
		flag = 0
		c_id=input("Enter Cab Id : ")
		for a in d:
			if(d[a][0]==c_id):
				print("This Cab ID already exist")
				flag = 1
		if flag==0:
			break		
	c_name=input("Enter Cab name : ")
	c_type=input("Enter Cab type : ")
	c_from=input("From : ")
	c_to=input("To : ")
	while True:
		c_status=input("Cab status (1-Enable/0-Disable) : ")
		if c_status=='1' or c_status=='0':
			break
		else:
			print("Inavlid Input")
	file = open('cab.txt','wb')
	d[len(d)+1]=[c_id,c_name,c_type,c_from,c_to,c_status,D_id]
	p.dump(d,file)
	file.close()
	print("Cab Added Successfully :)")
	time.sleep(.3)
	c_menu(D_id)

################## VIEW CAB ###############################
def view_cab(D_id):
	os.system('cls')
	print("			ALL CAB")
	file = open('cab.txt','rb')
	d=p.load(file)
	file.close()
	flag = 1
	x=PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To","Status"]
	for a in d:
		if(D_id==d[a][-1]):
			x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4],d[a][5]])
			flag=0
	print(x)
	if flag==1:
		print("No cab registered ")
	time.sleep(.3)
	c_menu(D_id)

#################### DELETE CAB ######################
def del_cab(D_id):
	os.system('cls')
	flag=0
	file = open('cab.txt','rb')
	d=p.load(file)
	file.close()
	print("			Delete CAB")
	flag = 1
	x=PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To","Status"]
	for a in d:
		if(D_id==d[a][-1]):
			x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4],d[a][5]])
			flag=0
	print(x)
	if flag==1:
		print("No cab registered ")
	else:
		print()
		c_id=input("Enter cab id which u want to delete : ")
		for a in d:
			if(c_id==d[a][0] and D_id==d[a][-1]):
				d.pop(a)
				flag=1
				break
		file = open('cab.txt','wb')
		p.dump(d,file)
		file.close()
		if flag==1:
			del_cab_req(c_id)
			print("Delete Cab Successfully :)")
		else:
			print("Cab Not Found!!!!")
	time.sleep(.3)
	c_menu(D_id)

######################### VIEW REQUEST #####################
def see_request(D_id):
	os.system('cls')
	print("				VIEW ALL REQUEST")
	file = open('request.txt','rb')
	l=p.load(file)
	file.close()
	file = open('cab.txt','rb')
	c=p.load(file)
	file.close()
	file = open('user.txt','rb')
	u=p.load(file)
	file.close()
	flag=0
	x=PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To","Dealar ID","User Name"]
	for a in l:
		u1=l[a][0]
		for udata in u.values():
					if udata[0]==u1:
						u_name=udata[2]
						break
		for i in c:
			if l[a][1]==c[i][0] and c[i][-1]==D_id:
				x.add_row([c[i][0],c[i][1],c[i][2],c[i][3],c[i][4],c[i][6],u_name])
				flag=1
	print(x)
	if flag==0:
		print("No cab is booked")
	input()
	os.system('cls') 
	c_menu(D_id)

############## CHANGE DEALER PASSWORD ###################
def change_p(D_id):
	os.system('cls')
	print("		DEALER PASSWORD CHANGE")
	file = open('delar.txt','rb')
	d=p.load(file)
	file.close()
	o_pas=input("Enter old Password :")
	pas=input("Enter new Password : ")
	flag=0
	for a in d:
		if(D_id==d[a][0] and o_pas==d[a][1]):
			d[a][1]=pas
			print("Password Changed Successfully :)")
			file = open('delar.txt','wb')
			p.dump(d,file)
			file.close()
			flag=1
			break
	if flag==0:
		print("Old Password did not match ")
	time.sleep(.3)
	menu()

################ USER REGISTERATION ####################
def u_reg():
	os.system('cls')
	print("		USER REGISTERATION")
	file = open('user.txt','rb')
	d=p.load(file)
	file.close()
	while True:
		flag = 0
		u_id=input("Enter User Id : ")
		for a in d:
			if(d[a][0]==u_id):
				print("This Dealer ID already exist")
				flag = 1
		if flag==0:
			break	
	u_pass=input("Enter Password : ")
	u_name=input("Enter User Name : ")
	while True:
		u_email=input("Enter E-mail : ")
		ck=check(u_email)
		if ck == 1:
			break		
		else:
			print("Invalid Email")
	while True:
		u_phone=input("Enter Phone No. : ")
		k=check_p(u_phone)
		if k == 1:
			break		
		else:
			print("Invalid Phone No. ")
	u_address=input("Enter Address : ")
	file = open('user.txt','wb')
	d[len(d)+1]=[u_id,u_pass,u_name,u_email,u_phone,u_address]
	p.dump(d,file)
	file.close()
	print("Registstion Successfully :)")
	time.sleep(.3)
	menu()

################# USER LOGIN ######################
def u_login():
	os.system('cls')
	print("		USER LOGIN")
	u_id=input("Enter User Id : ")
	u_pass=input("Enter Password : ")
	file = open('user.txt','rb')
	d=p.load(file)
	file.close()
	flag=0
	for a in d:
		if(d[a][0]==u_id and d[a][1]==u_pass):
			flag=1
			a=d[a][2]
			break	
	if flag==1:
		print("Login Successfully :)")
		print("Hello,",a)
		u_menu(u_id)
	else:
		print("Invalid User Id and Password :(")
		time.sleep(.5)
		menu()

################## USER MENU ###################
def u_menu(u_id):
	c_id=0
	c=input('''
					USER MENU
			1 View and book Cab
			2 Search and book Cab
			3 Change Password
			4 Logout 
			''')
	if c=='1':
		u_view(u_id)
	elif c=='2':
		u_search(u_id)
	elif c=='3':
		change_u(u_id)
	elif c=='4':        	
		menu()
	else:
		print("Invalid Input")
		u_menu(u_id)

############## USER CAB VIEW ################
def u_view(u_id):
	os.system('cls')
	file = open('cab.txt','rb')
	d=p.load(file)
	file.close()
	print("		VIEW ALL CAB AND BOOK")
	flag=0
	x=PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To"]
	for a in d:
		if(d[a][5]=='1'):
			x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4]])
			flag=1
	print(x)
	if flag==1:
		ch=input("U want to book cab (Y/N) : ")
		if ch=='y' or ch=='Y':
			f=0
			c_id=input("Enter Cab Id which u want to book : ")
			for a in d:
				if d[a][0]==c_id and d[a][5]=='1':
					f=1
					book_cab(u_id,c_id)
			if f==0:
				print("Invalid cab ID")
				time.sleep(.3)
				u_menu(u_id)
		else:
			u_menu(u_id)
	else:
		print("No cab registered")
		time.sleep(.3)
		u_menu(u_id)

#################### CAB SEARCH #####################
def u_search(u_id):
	file = open('cab.txt','rb')
	d=p.load(file)
	file.close()
	os.system('cls')
	print("		CAB SEARCH AND BOOK")
	f=input("From : ")
	t=input("To : ")
	flag=0
	x=PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To"]
	for a in d:
		if(d[a][3]==f and d[a][4]==t):
			x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4]])
			flag=1
	print(x)
	if flag==1:
		ch=input("U want to book cab (Y/N) : ")
		if ch=='y' or ch=='Y':
			f=0
			c_id=input("Enter Cab Id which u want to book : ")
			for a in d:
				if d[a][0]==c_id and d[a][5]=='1':
					f=1
					book_cab(u_id,c_id)
			if f==0:
				print("Invalid cab ID")
				time.sleep(.3)
				u_menu(u_id)
		else:
			u_menu(u_id)
	else:
		print("No cab found")
		time.sleep(.3)
		u_menu(u_id)

####################### CHANGE USER PASSWORD ##################
def change_u(u_id):
	os.system('cls')
	print("		USER PASSWORD CHANGE")
	file = open('user.txt','rb')
	d=p.load(file)
	file.close()
	o_pas=input("Enter old Password :")
	pas=input("Enter new Password : ")
	flag=0
	for a in d:
		if(pas==d[a][0] and o_pas==d[a][0]):
			d[a][1]=pas
			print("Password Changed Successfully :)")
			file = open('user.txt','wb')
			p.dump(d,file)
			file.close()
			flag=1
			break
	if flag==0:
		print("Old Password did not match ")
	time.sleep(.3)
	menu()

##################### BOOK CAB ####################
def book_cab(u_id,c_id):
	file = open('request.txt','rb')
	l=p.load(file)
	file.close()
	file = open('request.txt','wb')
	l[len(l)+1]=[u_id,c_id]
	p.dump(l,file)
	file.close()
	print("Cab Booked Successfully :)")
	u_menu(u_id)

############# ADMIN LOGIN ##################
def admin_login():
	os.system('cls')
	print("		ADMIN LOGIN")
	a_id=input("Enter User Id : ")
	a_pass=input("Enter Password : ")
	file = open('admin.txt','rb')
	l=p.load(file)
	file.close()
	flag=0
	if (l[1]==a_id and l[2]==a_pass):
		flag=1	
	if flag==1:
		print("Login Successfully :)")
		print("Hello")
		a_menu()
	else:
		print("Invalid Admin Id and Password :(")
		time.sleep(.5)
		menu()

################# ADMIN MENU ################
def a_menu():
	n=input('''
				Admin Menu
		1 View Dealer
		2 Delete Dealer 
		3 View User 
		4 Delete User 
		5 View Cabs
		6 Delete Cabs
		7 Disable Cabs
		8 View Request
		9 Change Password
		10 Exit
		Enter your choice :
		''')
	if n=='1':
		view_alldealer()
	elif n=='2':
		del_dealer()
	elif n=='3':
		view_alluser()
	elif n=='4':
		del_user()
	elif n=='5':
		view_a_cab()
	elif n=='6':
		del_a_cab()
	elif n=='7':
		change_status()
	elif n=='8':
		view_all_request()
	elif n=='9':
		p_change()
	elif n=='10':
		menu()
	else:
		print("Invalid Inputut")
		a_menu()

################## VIEW DEALER ##################
def view_alldealer():
	os.system('cls')
	file = open('delar.txt','rb')
	d=p.load(file)
	file.close()
	flag=0
	x = PrettyTable()
	print("			VIEW ALL DEALER")
	x.field_names = ["Dealer ID","Dealer Password","Dealer Name","Dealer Email","Dealer Phone no.","Dealer Address"]
	for a in d:
		x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4],d[a][5]])
		flag=1
	print(x)
	if(flag==0):
		print("No Dealer registered")
	input()	
	os.system('cls')
	a_menu()

########################### DELETE DEALER ############################
def del_dealer():
	os.system('cls')
	f=0
	file = open('delar.txt','rb')
	d=p.load(file)
	file.close()
	flag=0
	print("			Delete DEALER")
	x = PrettyTable()
	print("			VIEW ALL DEALER")
	x.field_names = ["Dealer ID","Dealer Password","Dealer Name","Dealer Email","Dealer Phone no.","Dealer Address"]
	for a in d:
		x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4],d[a][5]])
		flag=1
	print(x)
	if(flag==0):
		print("No Dealer registered")
	else:
		print()
		d_id=input("Enter Dealer id which u want to delete : ")
		for a in d:
			if(d_id==d[a][0]):
				d.pop(a)
				del_dealer_cab(d_id)
				f=1
				break
		file = open('delar.txt','wb')
		p.dump(d,file)
		file.close()
		if f==1:
			print("Dealer Delete Successfully :)")
		else:
			print("Dealer Not Found!!!!")
	time.sleep(.3)
	os.system('cls')
	a_menu()

###################### VIEW ALL USER ##############
def view_alluser():
	os.system('cls')
	print("			VIEW ALL USER")
	flag=0
	file = open('user.txt','rb')
	d=p.load(file)
	file.close()
	x = PrettyTable()
	x.field_names=["User ID","User Password","User Name","User Email","User Address"]
	for a in d:
		x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4]])
		flag=1
	print(x)
	if(flag==0):
		print("No User registered")
	input()	
	os.system('cls')
	a_menu()

########################## DELETE USER ######################
def del_user():	
	f=0
	flag=0
	os.system('cls')
	print("			Delete USER")
	file = open('user.txt','rb')
	d=p.load(file)
	file.close()
	x = PrettyTable()
	x.field_names=["User ID","User Password","User Name","User Email","User Address"]
	for a in d:
		x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4]])
		flag=1
	print(x)
	if(flag==0):
		print("No user registered")
	else:
		print()
		u_id=input("Enter User id which u want to delete : ")
		for a in d:
			if(u_id==d[a][0]):
				del_u_cab_req(u_id)
				d.pop(a)
				f=1
				break
		file = open('user.txt','wb')
		p.dump(d,file)
		file.close()
		if f==1:
			print("User Delete Successfully :)")
		else:
			print("User Not Found!!!!")
	time.sleep(.3)
	os.system('cls')
	a_menu()

####################### VIEW ALL CAB ##############
def view_a_cab():
	flag=0
	os.system('cls')
	print("			VIEW ALL CAB")
	file = open('cab.txt','rb')
	d=p.load(file)
	file.close()
	x = PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To","Status","Dealer ID"]
	for a in d:
		x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4],d[a][5],d[a][6]])
		flag=1
	print(x)
	if(flag==0):
		print("No cab registered")
	input()	
	os.system('cls')
	a_menu()

######################### DELETE CAB ######################
def del_a_cab():
	f=0
	flag=0
	os.system('cls')
	print("			Delete CAB")
	file = open('cab.txt','rb')
	d=p.load(file)
	file.close()
	x = PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To","Status","Dealer ID"]
	for a in d:
		x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4],d[a][5],d[a][6]])
		flag=1
	print(x)
	if(flag==0):
		print("No cab registered")
	else:
		c_id=input("Enter cab id which u want to delete : ")
		for a in d:
			if(c_id==d[a][0]):
				del_cab_req(c_id)
				d.pop(a)
				f=1
				break
		file = open('cab.txt','wb')
		p.dump(d,file)
		file.close()
		if f==1:
			print("Cab Delete Successfully :)")
		else:
			print("Cab Not Found!!!!")
	time.sleep(.3)
	os.system('cls')
	a_menu()

########################  Change Cab Status ######################
def change_status():
	os.system('cls')
	print("		CHANGE CAB STATUS")
	f=0
	flag=0
	file = open('cab.txt','rb')
	d=p.load(file)
	file.close()
	x = PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To","Status","Dealer ID"]
	for a in d:
		x.add_row([d[a][0],d[a][1],d[a][2],d[a][3],d[a][4],d[a][5],d[a][6]])
		flag=1
	print(x)
	if(flag==0):
		print("No cab registered")
	else:
		c_id=input("Enter cab id which u want to change status : ")
		for a in d:
			if(c_id==d[a][0]):
				while True:
					s=input("Cab status (1/0) : ")
					if s=='1' or s=='0':
						break
					else:
						print("Inavlid Input")
				d[a][5]=s
				f=1
				break
		file = open('cab.txt','wb')
		p.dump(d,file)
		file.close()
		if f==1:
			print("Cab Status change Successfully :)")
		else:
			print("Cab Not Found!!!!")
	time.sleep(.5)
	os.system('cls')
	a_menu()

######################## VIEW ALL REQUEST #####################	
def view_all_request():
	os.system('cls')
	print("				VIEW ALL REQUEST")
	file = open('request.txt','rb')
	l=p.load(file)
	file.close()
	file = open('cab.txt','rb')
	c=p.load(file)
	file.close()
	file = open('user.txt','rb')
	u=p.load(file)
	file.close()
	file = open('delar.txt','rb')
	d=p.load(file)
	file.close()
	flag=0
	x= PrettyTable()
	x.field_names=["Cab ID","Cab Name","Cab Type","From","To","Dealar ID","Dealar Name","User Name"]
	for a in l:
		u1=l[a][0]
		for udata in u.values():
					if udata[0]==u1:
						u_name=udata[2]
						break
		for i in c:
			if l[a][1]==c[i][0]:
				d1=c[i][-1]
				for ddata in d.values():
					if ddata[0]==d1:
						d_name=ddata[2]
						break
				x.add_row([c[i][0],c[i][1],c[i][2],c[i][3],c[i][4],c[i][6],d_name,u_name])
				flag=1
	print(x)
	if flag==0:
		print("No cab is booked")
	input()
	os.system('cls')
	a_menu()

####################### ADMIN PASSWORD CHANGE #################
def p_change():
	os.system('cls')
	print("		ADMIN PASSWORD CHANGE")
	file = open('admin.txt','rb')
	d=p.load(file)
	file.close()
	o_pas=input("Enter Old Password : ")
	pas=input("Enter new Password : ")
	if d[2]==o_pas:
		d[2]=pas
		file = open('admin.txt','wb')
		p.dump(d,file)
		file.close()
		print("Password Changed Successfully :)")
	else:
		print("Old Password did not match")
	time.sleep(.3)
	os.system('cls')
	menu()

################# CHECK EMAIL ###################
def check(email):
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	if(re.search(regex,email)):  
		return 1         
	else:  
		return 0  

##################### CHECK PHONE NO. ##################
def check_p(phone):
	if phone.isdigit() and len(phone) == 10:
		return 1
	else:
		return 0

################## DELETE CAB ################
def del_cab_req(c_id):
	while True:
		flag=0
		file = open('request.txt','rb')
		r=p.load(file)
		file.close()
		for a in r:
			if r[a][1]==c_id:
				r.pop(a)
				flag=1
				break
		file = open('request.txt','wb')
		p.dump(r,file)
		file.close()
		if flag==0:
			break
		
################# DELETE DEALER CAB REQUEST ################		
def del_dealer_cab(d_id):
	while True:	
		flag=0
		file = open('cab.txt','rb')
		d=p.load(file)
		file.close()
		for a in d:
			if d[a][-1]==d_id:
				c_id=d[a][0]
				d.pop(a)
				flag=1
				del_cab_req(c_id)
				break
		file = open('cab.txt','wb')
		p.dump(d,file)
		file.close()
		if flag==0:
			break
		
################### DELETE USER REQUEST ###############		
def del_u_cab_req(u_id):
	while True:
		flag=0
		file = open('request.txt','rb')
		r=p.load(file)
		file.close()
		for a in r:
			if r[a][0]==u_id:
				r.pop(a)
				flag=1
				break
		file = open('request.txt','wb')
		p.dump(r,file)
		file.close()
		if flag==0:
			break

######################## MAIN ######################
menu()
