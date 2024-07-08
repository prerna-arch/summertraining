"""
create table consultation(
            cid int primary key auto_increment,
            pid int,
            remarks varchar(256),
            medicines varchar(256),
            next_followup datetime,
            created_on datetime,
            FOREIGN KEY (pid) REFERENCES Patient(pid)

);


"""

import datetime
class Consultation:
    def __init__(self,cid=0,pid=0,remarks="",medicines="",next_followup=""):
        self.cid= cid
        self.pid=pid
        self.remarks=remarks
        self.medicines=medicines
        self.next_followup=next_followup
        self.created_on=datetime.datetime.now()


    def add_consultation_details(self):
          self.pid=int(input("enter the Pateint id:"))
          self.remarks=input("enter the Pateint remarks:")
          self.medicines=input("enter the Pateint medicines:")
          self.next_followup=input("enter next follow up:")
          #we will not take input for created_on
          #created_on is a system date time stamp


    def show(self):
         Consultation="""
          {cid} | {pid} | 
          {remarks} | {medicines} 
           {created_on} | {next_followup}
          
          """ .format(vars(self))
         print(Consultation)     