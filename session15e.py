from session15c import Patient
from session15d  import Database
from  tabulate   import tabulate 
from session15f   import Consultation
def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO Doctor's App")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     
    db=Database()

    while True:
        print("1:Add New Patient")
        print("2:Update existing  Patient")
        print("3:Delete existing Patient")
        print("4:view Patient by pid")
        print("5:view all Patients")
        print("6:Add consulations for patient")
        print("7:view consulation for patient")
        print("8:view all consultations")
        print("9:view all follow_ups")

        print("0:Quit app")

        choice=int(input("enter your choice:"))

        if choice == 1:
            patient = Patient()
            patient.add_pateint_details()
            sql="insert into Patient values(null,'{name}','{phone}','{email}','{dob}','{gender}','{created_on}')".format_map(vars(patient))
            db.write(sql)
            print("[doc  app]",patient.name,"saved in database")
        elif choice == 2:

            pid=int(input("Enter the patient pid to update the Pateint details:"))
            sql="select * from Patient where pid={}".format(pid)
            rows=db.read(sql)
            print(rows)
            patient = Patient(pid=rows[0][0],name=rows[0][1],phone=rows[0][2],email=rows[0][3],dob=rows[0][4],gender=rows[0][5])
            #columns =["cid","name","phone","email","age","gender","created_on"]
            #print(tabulate(rows,headers=columns,tablefmt='grid'))
            print("patient to update....")
            patient.show()      
            patient.update_Patient_details()    

            sql="update Patient set name='{name}',phone='{phone}',email='{email}',dob='{dob}',gender='{gender}',created_on='{created_on}' where pid={pid}".format_map(vars(patient))
            db.write(sql)
            patient.show()  

        elif choice == 3:
            pid=int(input("Enter the  patient id"))
            sql="delete from Patient where pid={}".format(pid)
            ask = input("Are you sure to delete ? (yes/no)")
            if ask== "yes":

              db.write(sql)
              print("[doc app]",pid,"delete from database")
            else:
                print("delete operation skipped....")
        

        elif choice == 4:
            pid=int(input("Enter the patient pid"))
            sql="select * from Patient where pid={}".format(pid)
            rows= db.read(sql)
            columns =["cid","name","phone","email","ward_on","age","gender","created_on"]
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            
        elif choice == 5:
            sql="select * from Patient"
            #customers =db.read(sql) this customers are rows in db language
            rows =db.read(sql) 
            columns =["pid","name","phone","email","dob","gender","created_on"]
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            #for customer in customers:
             #  print(customer)
        elif choice == 6:
            consultation =  Consultation()
            consultation.add_consultation_details()
            sql="insert into Consultation values(null,{pid},'{remarks}','{medicines}','{next_followup}','{created_on}')".format_map(vars(consultation))
            db.write(sql)
            print("consultation created...........")

        elif choice == 7:
            pid=int(input("Enter the patient pid"))
            sql="select * from Consultation where pid={}".format(pid)
            rows= db.read(sql)
            columns =["cid","pid","remarks","medicines","next_followup","created_on"]
            print(tabulate(rows,headers=columns,tablefmt='grid'))


        elif choice == 8:
            sql="select * from Consultation"
            rows =db.read(sql) 
            columns =["cid","pid","remarks","medicines","next_followup","created_on"]
            print(tabulate(rows,headers=columns,tablefmt='grid'))


        elif choice == 9:
            start_date=input("enter the start date:")
            end_date=input("enter the end date")
            sql = "select * from Consultation where next_followup >= '{}' and next_followup <= '{}'".format(start_date, end_date)
            rows = db.read(sql)

            columns = ["cid", "pid", "remarks", "medicines", "next_followup", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))     

            
        elif choice == 0:
            break
        else:
            print("[doc app]inavlid choice")


if __name__=="__main__":
    main()