
try:
    import sqlite3  
    import requests 

except:
    print( "One of the required module is missing." )

#  creating database
domain="http://localhost:5000/api/v1"

OBJ=sqlite3.connect("students.db")    
obj=OBJ.cursor( )

#  creating tables in database

#  students table
obj.execute("""CREATE TABLE IF NOT EXISTS students(      
                      student_name text,
                      father_name text,
                      Class text,
                      date_of_birth text,
                      roll_no text PRIMARY KEY,
                      tution_fee integer,
                      annual_fee integer,
                      examination_fee integer
                      )""")

#  admins table
obj.execute("""CREATE TABLE IF NOT EXISTS ADMINS (
                  UserName text,
                  Password text
                  )""")


class overloading:
    """
    Its function is to add tuition fee and examination fee to get total fee
    """
    
    def __init__( self , fee ) :
        self.fee = fee
        
    def __add__( self , other ):        #  adding tuition fees and examination fees 
        return self.fee + other.fee


class composition:
    """
    Its function is to add tuition fee and examination fee to get total fee
    """
    
    def __init__(self,roll):
        with OBJ:
            obj.execute("SELECT * FROM students WHERE roll_no='{}'".format(roll))
        a,b,c,d,e,f,g,h=obj.fetchone()
        self.tution=overloading(f)
        self.exam=overloading(h)
        
    def total(self):                        #  adding tuition fees and examination fees
        total_fee=self.tution+self.exam
        return total_fee


# def insert ( student_name , father_name , Class , date_of_birth , roll_no , tution_fee , annual_fee , examination_fee ):
#     """
#     This function inserts record in database

#     It is called in insert function in file UserInterface
#     """
#     ""
    
#     with OBJ:
#         obj.execute("INSERT INTO  students VALUES('{}','{}','{}','{}','{}',{},{},{})".format(student_name ,father_name,Class,date_of_birth ,roll_no,tution_fee,annual_fee,examination_fee))
def insert(studentName, fatherName, Class, dateOfBirth, rollNo, tutionFee, annualFee, examinationFee):
    """
    This function inserts a record into the database by making a POST request to the Node.js endpoint.
    """
    # Prepare the data payload
    data = {
         "studentName":studentName,
         "fatherName": fatherName,
         "class": Class,
         "dateOfBirth":  dateOfBirth,
         "dateOfBirth":  dateOfBirth,
         "rollNo":rollNo,
         "tutionFee" :tutionFee,
         "annualFee":annualFee,
         "examinationFee":examinationFee
    }
    print("data",data)
    try:
        # Make a POST request to the Node.js endpoint
        response = requests.post(domain+"/insert-record", json=data)

        # Check the response status
        if response.status_code == 201:
            print("Student record inserted successfully")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error: {e}")

OBJ.commit()        
def updating( student_name  , father_name , Class , date_of_birth , roll_no , tution_fee , annual_fee , examination_fee):
    '''
    This method updates pre-existing data

    It is called in update function in file UserInterface
    '''

    with OBJ:
        obj.execute("UPDATE students SET student_name=?, father_name=?, Class=?, date_of_birth=?, tution_fee=?, annual_fee=?, examination_fee=? WHERE roll_no=?",(student_name ,father_name,Class,date_of_birth ,tution_fee,annual_fee,examination_fee,roll_no))



def search_voucher (  roll = None ):
    params = {"rollNo": roll}
    response = requests.get(domain+"/get-single-record", params=params)
    if response.status_code == 200:
            return response.json().get("singleRecord", {})
    else:
            print(f"Error fetching record: {response.status_code} - {response.text}")
            return {}

def get_students():
    '''
    This method retrieves student records from the server.
    '''
    try:
        response = requests.get(domain + "/get-student-record")
        data=response.json()
        # Check the response status
        if response.status_code == 200:
            rows = data["allStudentsRecord"]
            return rows
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None  # or raise an exception if you want to handle errors differently

    except Exception as e:
        print(f"Error: {e}")
        return None


def vouch( ):
    """
    This function fetches roll no of every student in database

    These roll no are used to generate Voucher of all the students in the database
    """
    # X=get_students()
    # roll_call=[ ]
    # for i in X:
    #     roll_call.append(i[4])
    # return roll_call

OBJ.commit()

obj.execute("INSERT INTO  ADMINS VALUES('{}','{}')".format( 'Ehsan' , '2094' ))
obj.execute("INSERT INTO  ADMINS VALUES('{}','{}')".format( 'admin' , 'admin' ))


def login( Username , password ):
    
    with OBJ :
        obj.execute("SELECT * FROM ADMINS WHERE UserName='{}' and Password='{}'".format(Username,password))
    results=obj.fetchall()
    if results:
        return True

OBJ.commit( )








