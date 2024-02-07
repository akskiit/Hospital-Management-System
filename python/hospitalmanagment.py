import mysql.connector as msc
import os
import time
import pandas as pd










def AdminMenu():
    print("1: Add a patient or Doctor\n")
    print("----------------------------------------------------------------------\n")
    print("3: KNOW AVAIALBLE DOCTORS\n")
    print("----------------------------------------------------------------------\n")
    print("4: to calculate bill\n")
    print("----------------------------------------------------------------------\n")
    print("5: Change patient or doctor details\n")
    print("----------------------------------------------------------------------\n")
    
    print("7: Search for a particular patient on pid basis\n")
    print("----------------------------------------------------------------------\n")
    print("8: Search for a particular doctor on d_id basis\n")
    print("----------------------------------------------------------------------\n")
    print("9: Search patients on the basis of some other column\n")
    print("----------------------------------------------------------------------\n")
    print("10: Search patients on the basis of some other column\n" )
    print("----------------------------------------------------------------------\n")
    print("11: Run Query of your choice on patient table\n")
    print("----------------------------------------------------------------------\n")
    print("12: Run Query of your choice on doctor table\n")
    print("----------------------------------------------------------------------\n")
    print("13: to delete patient details\n")
    print("----------------------------------------------------------------------\n")
    print("14: to delete doctor details\n")
    print("----------------------------------------------------------------------\n")
    print("16:  names of patient with a paricular disease\n")
    print("----------------------------------------------------------------------\n")
    print("17: to display the detail of doctor  who are male or female\n")
    print("----------------------------------------------------------------------\n")
    print("15: to display the detail of,  who are male or female\n")
    print("----------------------------------------------------------------------\n")
    print("18: Exit\n")
    print("----------------------------------------------------------------------\n")
                             












def UserMenu():
    print("1: Search for a  patient OR doctor on ID basis")
    print("----------------------------------------------------------------------\n")
    print("3: Search patients on the basis of some other column\n")
    print("----------------------------------------------------------------------\n")
    print("4: to know available doctors\n")
    print("----------------------------------------------------------------------\n")
    print("5: display details of doctor OR patient \n")
    print("----------------------------------------------------------------------\n")
    print("7: know bills\n")
    print("----------------------------------------------------------------------\n")
    print("8: to display the detail of patient who are male or female\n")
    print("----------------------------------------------------------------------\n")
    print("9: to display the detail of doctor  who are male or female\n")
    print("----------------------------------------------------------------------\n")
    print("10: Exit")
    print("----------------------------------------------------------------------\n")

                                                  #1
    









def Add_details():
 conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
 cur=conn.cursor()
 os.system('cls')
 h=int(input("press 1 to add patient details\npress 2 to add doctor details\n\n"))
 if h==1:
     
    r=int(input("enter patient id::  "))
    nm=input("enter name::  ")
    s=int(input("enter age::  "))
    q=input("enter sex:: ")
    fs=input("enter date of admission  in (DD-MM-YYYY)::  ")
    g=input("enter disease::  ")
    a=int(input("enter phone number::  "))
    c=input("enter address::  ")
    b=input("enter doctor consulting:: ")
    cur.execute("insert into PATIENT values(%s,'%s',%s,'%s','%s','%s',%s,'%s','%s')" %(r,nm,s,q,fs,g,a,c,b,))
    conn.commit()
    conn.close()
    print("patient added successfully")
    time.sleep(2)
    os.system('cls')
 elif h==2:
    t=int(input("enter d_id::  "))
    m=input("enter name:: ")
    nm=input("enter sex:: ")
    s=int(input("enter age:: "))
    g=input("enter department:: ")
    sa=input("enter shift (morning , afternoon, night, emergengy):: ")
    d=input("enter adress::  ")
    p=int(input("enter phone no.::  "))
    a=input("enter date of joining in (yyyy-mm-dd) form:: ")
    cur.execute("insert into doctor values(%s,'%s','%s',%s,'%s','%s','%s',%s,'%s')" %(t,m,nm,s,g,sa,d,p,a))
    conn.commit()
    conn.close()
    print("doctor added successfully\n\n")
    time.sleep(2)
    os.system('cls')
 else:
     print("\n\ninvalid choice !!!!\n\nTRY AGAIN")
     time.sleep(2)
     os.system('cls')    

 



                                              #2
 









def Update():
 conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
 cur=conn.cursor()
 os.system('cls')
 h=int(input("press 1 to change patient details\npress 2 to change doctor details\n\n"))
 if h==1:
     
    r=int(input("enter pid of the patient to be modified:: "))
    print("column names are ::['pid','pname','age','sex','dao','disease','phone_no','address','consultant_DR']\n")
    nm=input("enter column name whose value you want to change:: ")
    v=input("enter the new value:: ")
    if nm in ['PID','AGE']:
        s=("update patient set %s = %s where PID = %s" %(nm,eval(v),r))
        print("updation successful")
        time.sleep(2)
        os.system('cls')
 else:
     s=("update patient set %s = '%s' where PID = %s" %(nm,v,r))
     cur.execute(s)
     conn.commit()
     conn.close()
     print("updation successful")
     time.sleep(2)
     os.system('cls')











     
def Search():
 conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
 cur=conn.cursor()
 os.system('cls')
 g=int(input("press 1 for patient details\npress 2 for doctor details\n\n"))
 if g==1:
      t=int(input("enter patient's id to be searched:: "))
      cur.execute("select * from patient where pid = %s" %(t,))
      p=cur.fetchall()
      if p==None:
           print("no such patient present")
    
      else:
        i=p
        f=pd.DataFrame(i,columns = ['pid','pname','age','sex','dao','disease','phone','adress','consultant_DR'])
        print(f)
 elif g==2:
      y=int(input("enter doctor's id  to be searched:: "))
      cur.execute("select * from doctor where D_ID = %s" %(y,))
      d=cur.fetchall()
      if d==None:
         print("no such doctor present")
     
    
      else:
         j=d
         w=pd.DataFrame(j,columns = ['D_id', 'Dname',  'sex','age', '   Department', ' Shift', '      address', '     phone_no', '  doj'])
         print(w)
    
     
         




def available_DR():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    os.system('cls')
    t=int(input("PRESS 1:  FOR MORNING\n\nPRESS 2:    FOR AFTERNOON\n\nPRESS 3: FOR NIGHT \n\nPRESS 4 : FOR EMERGENGY\n\n--->"))
    d=input("enter department ::   ")
    if t==1:
         cur.execute(("select dname from doctor where shift='morning' and department='%s' ")%(d,))
         f=cur.fetchall()
         if f==[]:
             print(" no doctor available")
             time.sleep(2)
             os.system('cls')
             
         else:
            for i in f:
                 print("\ndr.",i," is available")
                 print()
                 time.sleep(2)
               
                 
    elif t==2:
        cur.execute("select dname from doctor where shift='afternoon' and department='%s' "%(d,))
        f=cur.fetchall()
        if f==[]:
            
            print(" no doctor available")
            time.sleep(2)
            os.system('cls')
        else:
            for i in f:
                
                print(i)
                print()
                time.sleep(2)
  
                 
    elif t==3:
             cur.execute("select dname from doctor where shift='night' and department='%s' "%(d,))
             f=cur.fetchall()
             if f==[]:
                  print(" no doctor available")
             else:
                 for i in f:
                     print(i)
                     print()
                     time.sleep(2)

                     
    elif t==4:
            cur.execute("select dname from doctor where shift='emergengy';")
            f=cur.fetchall()
            if f==[]:
                print(" no doctor available")
            else:
                for i in f:
                   print(i)
                   print()
                   time.sleep(2)
     
    else:
        print('invaild choise')  
        time.sleep(2)
     
                                                # 6











def delete_DR():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    print(" column names are ::['D_id', 'Dname',  'sex', 'age', '   Department', ' Shift', '      address', '     phone_no', '  doj']")
    nm=input("enter a column name on the basis of which you want to delete the doctor:")
    v=input("enter its value:")
    if nm in ['D_id','age','phone_no']:
        cur.execute("delete from doctor where %s = %s" %(nm,eval(v)))
        print("doctor removed successfully")
        time.sleep(2)
        os.system('cls')
        
    else:
        cur.execute("delete from doctor where %s = '%s'" %(nm,v))
        conn.commit()
        conn.close()
        print("doctor removed successfully")
        time.sleep(2)
        os.system('cls')






                                        #7
        














def delete_patient():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    print("column names are ::['pid','pname','age','sex','dao','disease','phone_no','address','consultant_DR']\n")
    nm=input("enter a column name on the basis of which you want to delete the patient:")
    v=input("enter its value:")
    if nm in ['PID','age']:
        cur.execute("delete from patient where %s = %s" %(nm,eval(v)))
        print(" removed\n")
        time.sleep(2)
        os.system('cls')
    elif nm in ['pname','sex','dao','disease','address','consultant_dr']:
        cur.execute("delete from patient where %s = '%s'" %(nm,v))
        conn.commit()
        conn.close()
        print("PATIENT  removed successfully")
        time.sleep(2)
        os.system('cls')
    else:
        conn.close()
        print("no such patient")
        time.sleep(2)
        os.system('cls')

           
                                            #8





def UpdateDoctor():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    t=int(input("enter D_id of the doctor to be modified:"))
    print(" column names are ::['D_id', 'Dname',  'sex', 'age', '   Department', ' Shift', '      address', '     phone_no', '  doj']")
    nm=input("enter column name whose value you want to change:")
    
    v=input("enter the new value")
    if nm in ['D_id','age']:
        s="update doctor set %s = %s where d_id = %s" %(nm,eval(v),t)
        print("updation successful")
        time.sleep(2)
        os.system('cls')
        
    else:
        s="update doctor set %s = '%s' where d_id= %s" %(nm,v,t)
        cur.execute(s)
        conn.commit()
        conn.close()
        print("updation successful")
        time.sleep(2)
        os.system('cls')


                                                   
                                                # 9











def bill_ad():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    t=int(input("enter pid of the patient  who's bill you want to calculate :: "))
    cur.execute('select department from patient , doctor where pid=%s and  consultant_dr=dname' %(t,))
    p=cur.fetchone()
    for d in p:
        if d=="cardiology":
            print(" amount to pay ::  RS.1500")
        elif d=="dermatology":
            print(" amount to pay ::  RS.2000")

        elif d=="emergency":
            print(" amount to pay ::  RS.1000")
        elif d=="physiotherapy":
            print(" amount to pay ::  RS.250")
        elif d=="nephrology":
            print(" amount to pay ::  RS.1250")
        elif d=="urology":
            print(" amount to pay ::  RS.633")
        elif d=="orthopedic":
            print("amount to pay ::  rs.700")
        else:
            print(" no such patient with pid ",t)        


                                                            #10










def run_own_Query():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    print("Which type of query you want to execute ?")
    ch=int(input("Enter your choice\n:Press 1 : Select query\nPress 2 : For Non-Select query\n"))
    if ch==1:
        s=input("enter your Select command Query\n")
        cur.execute(s)
        d=cur.fetchall()
        if d==[]:
            print(" :( SORRY!!! None of the records satisfied your query ")
        else:
            for m in d:
                print(m,end="\t")
                print()
                
        time.sleep(2)

            
            
    elif ch==2:
        s=input("enter your non-select query:\n")
        cur.execute(s)
        conn.commit()
        print("CONGRATS!!! Query executed successfully")
        print("Check out the records now :)")
        a=input("enter table name on which you exicuted query")
        cur.execute("select * from "+a+";")
        p=cur.fetchall()
        if a=="patient":
            i=p
            f=pd.DataFrame(i,columns = ['pid','pname','age','sex','dao','disease','phone','adress','consultant_DR'])
            print(f)

        elif a=="doctor":
             j=p
             g=pd.DataFrame(j,columns = ['D_id', 'Dname',  'sex','age', '   Department', ' Shift', '      address', '     phone_no', '  doj'])
             print(g)
        else:
            print(" sorry , there might be a mistake in giving table name, please chech again ")
    else:
        print("invalid choice")

 
                                                            #11
        








def UserQuery():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    os.system('cls')
    print("REMEMBER!!! You can only execute Select Query")
    a=input("enter table name on which you exicuted query")
    cur.execute("select * from "+a+";")
    p=cur.fetchall()
    if a=="patient":
        i=p
        f=pd.DataFrame(i,columns = ['pid','pname','age','sex','dao','disease','phone','adress','consultant_DR'])
        print(f)

    elif a=="doctor":
        j=p
        g=pd.DataFrame(j,columns = ['D_id', 'Dname',  'sex','age', '   Department', ' Shift', '      address', '     phone_no', '  doj'])
        print(g )
    else:
        print(" sorry , there might be a mistake in giving table name, please chech again ")
  
    













def patient_gender():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    p=input("enter 'M' for male and 'F' for female ")
    if p=='m':
        print(" male patient details are  following")
    else:
        print(" female patient details are  following")
        
    cur.execute("select * from patient where sex ='%s'; " %(p,))
    f=cur.fetchall()
    if f==[]:
        print("no such record ")
    else:
        for i in f:
            print(i)
            print()
      #13
            















def doctor_gender():
     conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
     cur=conn.cursor()
     p=input("enter 'M' for male and 'F' for female ")
     if p=='m':
        print(" male patient details are  following")
     else:
        print(" female patient details are  following")

     cur.execute("select * from doctor where sex ='%s'; " %(p,))
     f=cur.fetchall()
     if f==[]:
        print("no such record ")
     else:
        for i in f:
            print(i)
            print()












#14
def Disease_p():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    p=input("enter disease  ")
    cur.execute("select pname from patient where disease ='%s'; " %(p,))
    f=cur.fetchall()
    if f==[]:
        print("no such record ")
    else:
        for i in f:
            print(i)
    d=0
    for i in f:
        d+=1
    print(" no. patient with disease ",p,"are",d)
    cur.execute("select * from patient;")
    m=cur.fetchall()
    g=0
    for i in m:
        g+=1
    print("total no. of patient",g)
    print((d/g)*100,"% patient are affected by ",p) 
    conn.close()


















#15
def SearchpatientColumn():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    print("column names are ::['pid','pname','age','sex','dao','disease','phone_no','address','consultant_DR']\n")
    
    nm=input("enter a column name on the basis of which you want to search the patient:")
    v=input("enter  its value  :  ")
    if nm in ['pid','age']:
        cur.execute("select * from patient where %s = %s" %(nm,eval(v)))
        r=cur.fetchall()
        for i in r:
            print(i)
    else:
        cur.execute("select * from patient where %s = '%s'" %(nm,v))
        d=cur.fetchall()
        if d==[]:
            print("no such patient present")
        else:
            for i in d:
                print(i)
    
 #16
                
















def SearchdoctorColumn():
    conn=msc.connect(host="localhost",user="root",passwd="aditya",database="hospital")
    cur=conn.cursor()
    print(" column names are ::['D_id', 'Dname',  'sex', 'age', '   Department', ' Shift', '      address', '     phone_no', '  doj']")
    nm=input("enter a column name on the basis of which you want to search the doctor:")
    v=input("enter its  value  :  "  )
    if nm in ['salary','age']:
        cur.execute("select * from doctor where %s = %s" %(nm,eval(v)))
        r=cur.fetchall()
        for i in r:
            print(i)
    else:
        cur.execute("select * from doctor where %s = '%s'" %(nm,v))
        d=cur.fetchall()
        if d==[]:
            print("no such doctor present")
        else:
            for i in d:
                print(i)
     
     











    
 #main program

print("\n\n\t\t \t\tWELCOME TO HOSPITAL MANAGEMENT SYSTEM\n\n"

       " \t\t  \t\tCREATED  BY - ADITYA KUMAR SINGH\t\t\n")
ch=int(input("Press 1:    To login as ADMIN\n\nPress 2:    To login as USER\n\n-->"))









if ch==1:
    os.system('cls')
    x=input("Enter Admin Password:")
    if x=="aa":
        print("\n\n\t\tWELCOME ADMIN : HERE IS THE MENU \n\n -> ")
        while True:
            print("\n")
            AdminMenu()
            print("\n")
            n=int(input("enter your choice::  "))
            if n==1:
                Add_details()
            
            elif n==3:
                available_DR()
                
            elif n==5:
                Update()

            elif n==6:
                Update()
                
            elif n==4:
                bill_ad()
            elif n==7:

                Search()

           
            elif n==9:
                SearchpatientColumn()

            elif n==10:
                SearchdoctorColumn()
            elif n==11:
                run_own_Query()
            elif n==12:
                run_own_Query()
            elif n==13:
                delete_patient()
            elif n==14:
                delete_DR()
            elif n==15:
                patient_gender()
            elif n==16:
                Disease_p()
            elif n==17:
                doctor_gender()
                
            elif n==18:
                break
            else:
                
                print('invaild choise')
    else:
         print("Invalid password !!\nLOGIN UNSUCCESSFUL")






















elif ch==2:
    os.system('cls')
    nm=input("Enter Username:")
    print("\n\n\t\t HI "+nm+" : HERE IS THE MENU \n\n")
    while True:
        print("\n")
        UserMenu()
        print("\n")
        n=int(input("enter your choice: "))
        if n==1:
            Search()
        
        elif n==4:
            available_DR()
            
            
        elif n==3:
            SearchpatientColumn()
            
        elif n==5:
            UserQuery()
        elif n==6:
            UserQuery()
        elif n==8:
            patient_gender()
        elif n==9:
            doctor_gender()

        elif n==7:
             bill_ad()
            
        elif n==10:                                                                                       
            break
        else:
            print('invalid choice')
else:
    print(" no other option ")