
try:
    import sqlite3   

except:
    print( "One of the required module is missing." )

#  creating database

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


def insert ( student_name , father_name , Class , date_of_birth , roll_no , tution_fee , annual_fee , examination_fee ):
    """
    This function inserts record in database

    It is called in insert function in file UserInterface
    """
    
    with OBJ:
        obj.execute("INSERT INTO  students VALUES('{}','{}','{}','{}','{}',{},{},{})".format(student_name ,father_name,Class,date_of_birth ,roll_no,tution_fee,annual_fee,examination_fee))

OBJ.commit()        
def updating( student_name  , father_name , Class , date_of_birth , roll_no , tution_fee , annual_fee , examination_fee):
    '''
    This method updates pre-existing data

    It is called in update function in file UserInterface
    '''

    with OBJ:
        obj.execute("UPDATE students SET student_name=?, father_name=?, Class=?, date_of_birth=?, tution_fee=?, annual_fee=?, examination_fee=? WHERE roll_no=?",(student_name ,father_name,Class,date_of_birth ,tution_fee,annual_fee,examination_fee,roll_no))







def search_voucher (  roll = None ):
        
    with OBJ:
        obj.execute("SELECT * FROM students WHERE roll_no='{}'".format(roll))
    Voucher=obj.fetchone()
    return Voucher


def get_students( ):
    '''
    This method displays the complete Database
    '''
    
    obj.execute("SELECT * FROM students" )
    rows=obj.fetchall()
    return rows


def vouch( ):
    """
    This function fetches roll no of every student in database

    These roll no are used to generate Voucher of all the students in the database
    """
    X=get_students()
    roll_call=[ ]
    for i in X:
        roll_call.append(i[4])
    return roll_call

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








