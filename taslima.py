print("Welcome to the Prudent Healthcare Hospital")
print("Lets start with users login process:-")

#textfile="dic.txt"  for record patient information
#textfile="data.txt"  for record payment information
#textfile="appointment.txt"  for record appointment information
#textfile="treatmentplan.txt"  for record treatment plan


def Secretarylogin():
    email=input("Enter your username:")
    passw=input("Enter your password:")
    while True:
        if (email, passw) == ("secretary", "admin"):
            print("username and password matched")
            print("\nyou are login as a secretary\n")
            break
        else:
            print("error")
            last()

def physicianlogin():
    email=input("Enter your username:")
    passw=input("Enter your password:")
    while True:
        if (email, passw) == ("physician", "admin"):
            print("username and password matched")
            print("\nyou are login as a physician\n")
            break
        else:
            print("error")
            last()

def accountantlogin():
    email=input("Enter your username:")
    passw=input("Enter your password:")
    while True:
        if (email, passw) == ("accountant", "admin"):
            print("username and password matched")
            break
        else:
            print("error")
            last()

def writes(patient_id, first_name, last_name, address, gender,DOB, contact):
    fw = open('dic.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender,DOB, contact))
    fw.close()

def registration():



    print("You are a physian\n")
    users = input("now registration of patient press Enter")
    patient_id = input("Enter patient_id:")
    first_name = input("Enter your first_name:")
    last_name = input("Enter your last name:")
    address = input("Enter your address:")
    gender = input("Enter your gender: ")
    DOB=input("Enter your DOB")
    contact = input("Enter your contact number:")
    writes(patient_id, first_name, last_name, address, gender,DOB, contact)
    print("THANK YOU!!!")
    print("\nUser created!\n")
    print("information saved in text file")
    last()


def read():
    users = open("dic.txt",'r')
    extract = input("Please input patient ID")
    for each_line in users:
        (patient_id, first_name, last_name, address, gender,DOB, contact) = each_line.split()

        if (patient_id == extract):
            print(patient_id, first_name, last_name, address, gender,DOB, contact)
    users.close()



def appointment2w(patientID,AppointmentID,status,Doctor):
    fw = open('appointment.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (patientID,AppointmentID,status,Doctor))
    fw.close()

def readappointment():
    users = open("appointment.txt",'r')
    extract = input("Please input appointment ID")
    for each_line in users:
        (patientID,AppointmentID,status,Doctor) = each_line.split()

        if (AppointmentID == extract):
            print(patientID,AppointmentID,status,Doctor)
    users.close()

def appointment2():
    readappointment()
    patientID=input("re Enter your patientID")
    AppointmentID=input("Enter your AppointmentID")
    status=input("Complete or Appointment")
    Doctor=input("Choose your doctor\n Dr.kelvin\n Dr.Scott \n Dr.Nitesh \n Dr.Richard")
    appointment2w(patientID, AppointmentID, status,Doctor)
    last()

def Treatmentwrite(TreatmentID,patientID,Complaint,Treatment):
    fw = open('treatmentplan.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (TreatmentID,patientID,Complaint,Treatment))
    fw.close()

def patientTreatmentPlan():


    TreatmentID=input("Enter your Treatment ID:")
    patientID=input("Enter your patientID:")
    Complaint=input("Enter your complaint:")
    Treatment=input("Enter given Treatment:")
    Treatmentwrite(TreatmentID,patientID,Complaint,Treatment)
    last()

def cost(extract,invoiceID,TreatmentID,name,through,recebill):
        fw = open('data.txt', "a")
        fw.write("%1s%20s%20s%20s%20s%20s\n" % (extract,invoiceID,TreatmentID,name,through,recebill))
        fw.close()


def credit(extract,invoiceID,TreatmentID, name, through, amount):
    fw = open('data.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s\n" % (extract,invoiceID,TreatmentID,name,through,amount))
    fw.close()


def cashpaid():

    extract = input("Please input patient ID")
    invoiceID=input("Enter your invoiceID:")
    TreatmentID=input("Enter your TreatmentId:")
    name=input("Enter your name")
    through=input("write through cash")
    recebill = input("Please enter the amount in Rs.:-")
    print(recebill)
    cost(extract,invoiceID,TreatmentID,name,through,recebill)
    print("Thank you")
    last()

def creditpaid():

    extract = input("Please input patient ID")
    invoiceID = input("Enter your invoiceID:")
    TreatmentID = input("Enter your TreatmentId:")
    name = input("Enter your name")
    through = input("write through credit card")
    crebill = input("Please enter the credit card number")
    amount = input("please enter total amount in Rs.")
    print(crebill)
    credit(extract,invoiceID,TreatmentID, name, through, amount)
    print("Thank you")
    last()

def logout():
    print("logout")

def last():
    print("Are you \n1.Secretary\n2.Physician\n3.Accountant\n4.logout\n")
    choose = input("Enter Choice?")
    number = int(choose)
    if (number == 1):
        print("Only Secretary can login\n")
        Secretarylogin()
        users=input("Choose your menu press Enter")
        print("1.Register Patient\n2.View Patient\n3.Exit")
        choose = input("Enter Choice?")
        number = int(choose)

        if (number == 1):
            registration()
        elif (number == 2):
            read()
            last()
        elif(number==3):
            print("exit")

            last()


        else:
            print("wrong choice")
            last()

    elif(number==2):
        post = input("only physician can login")
        print(post)
        physicianlogin()
        print("1.Appointment\n2.View Appointment\n3.Treatment Plan\n4.Exit")
        choose = input("Enter Choice?")
        number = int(choose)
        if (number == 1):
            appointment2()
        elif (number == 2):
            readappointment()
            last()
        elif (number == 3):
            patientTreatmentPlan()
            last()
        elif (number == 4):
           last()
        else:
            print("wrong choice")

    elif (number == 3):
        post = input("only accountant can login")
        print(post)
        accountantlogin()
        print("you are login as a accountant\n")

        users = input("1.By cash\n2.By Credit")
        number = int(users)
        if (number == 1):
            cashpaid()
        elif (number == 2):
            creditpaid()
        else:
            print("wrong choice")

    elif(number==4):
        logout()
    else:
        print("wrong choice")

#main part or module
last()
