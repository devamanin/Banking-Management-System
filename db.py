import mysql.connector
from passlib.hash import sha256_crypt

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bms"
)
mycursor = mydb.cursor()

def userCreate(userDetails ):
    fullname = userDetails[0]
    customerId = userDetails[1]
    passHash = userDetails[2]
    MobileNo = userDetails[3]
    gender = userDetails[4]
    dob = userDetails[5]
    aadhaar = userDetails[6]
    pan = userDetails[7]
    branchId = userDetails[8]
    sql = "insert into userdetails values('{fullname}', '{customerId}', '{passHash}', {MobileNo}, '{gender}', '{dob}', {aadhaar}, '{pan}', {branchId})".format(fullname = fullname, customerId = customerId, passHash = passHash, MobileNo = MobileNo, gender = gender, dob=dob, aadhaar = aadhaar, pan = pan, branchId = branchId)
    mycursor.execute(sql)
    mydb.commit()

def userAuthenticate(loginDetails):
    sql = "select * from userdetails where customerID = '{}'".format(loginDetails[0])
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) == 1:
        if (sha256_crypt.verify(loginDetails[1], myresult[0][2])):
            return ['usrFound', myresult]
        else:
            return ["PassNotMatched"]
    else:
        return ["userNotFound"]

def check():
    print("hello world")
# print(userAuthenticate(['2343dfsd', 'aman']))