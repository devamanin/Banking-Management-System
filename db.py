from codecs import BufferedIncrementalDecoder
from xml.dom.minidom import Document
import mysql.connector
from passlib.hash import sha256_crypt
import uuid

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bms"
)

def sqlmodify(statement):
    mycursor = mydb.cursor(buffered = True)
    mycursor.execute(statement)
    mydb.commit()
    mycursor.close()
def sqlget(statement):
    mycursor = mydb.cursor(buffered = True)
    mycursor.execute(statement)
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

def userCreate(userDetails ):
    fullname = userDetails[0]
    customerId = userDetails[1]
    passHash = sha256_crypt.encrypt(userDetails[2])
    MobileNo = userDetails[3]
    gender = userDetails[4]
    dob = userDetails[5]
    aadhaar = userDetails[6]
    pan = userDetails[7]
    branchId = userDetails[8]
    accnumber = userDetails[9]
    availbalance = userDetails[10]
    sql = "insert into userdetails values('{fullname}', '{customerId}', '{passHash}', {MobileNo}, '{gender}', '{dob}', {aadhaar}, '{pan}', {branchId}, {accnumber}, {availbalance})".format(fullname = fullname, customerId = customerId, passHash = passHash, MobileNo = MobileNo, gender = gender, dob=dob, aadhaar = aadhaar, pan = pan, branchId = branchId, accnumber = accnumber, availbalance = availbalance)
    sqlmodify(sql)

# userCreate(userDetails=["khushi singh", "123", "amankh", 23232223, 'F', '2002-9-10', 234234234, 'BAQPS4664D', 1, 6546456456457, 1200])
def userAuthenticate(loginDetails):
    sql = "select * from userdetails where customerID = '{}'".format(loginDetails[0])
    usrDetails = sqlget(sql)
    if len(usrDetails) == 1:
        if (sha256_crypt.verify(loginDetails[1], usrDetails[0][2])):
            return ['usrFound', usrDetails]
        else:
            return ["PassNotMatched"]
    else:
        return ["userNotFound"]
def LogBankEmployee(loginDetails = [1, 'aman']):
    sql = "select * from employee where emp_id={}".format(loginDetails[0])
    empDetails = sqlget(sql)
    if (len(empDetails) == 1):
        if (sha256_crypt.verify(loginDetails[1], empDetails[0][2])):
            return ['usrFound', empDetails]
        else:
            return ["PassNotMatched"]
    else:
        return ["UserNotFound"]

def fetchdetails(username):
    sql = "select * from userdetails where customerid = {}".format(username)
    myresult = sqlget(sql)
    return myresult
def fetchtrxDetails(username):
    sql = "select accnumber from userdetails where customerid = {}".format(username)
    myresult = sqlget(sql)
    sql = "select * from trandetails where accnumber = {}".format(myresult[0][0])
    return sqlget(sql)
def transfer(details):
    sql = "select availbalance from userdetails where customerid = {}".format(details[2])
    availBalance = sqlget(sql)
    if (availBalance[0][0] >= int(details[1])):
        uniqTrxNo = uuid.uuid4()
        AccoNumber = "select accnumber from userdetails where customerid = {}".format(details[2])
        AccoNumber = sqlget(AccoNumber)
        sql = "update userdetails set availbalance = {balance} where customerid = {custid}".format(balance = (availBalance[0][0] - int(details[1])), custid = details[2])
        sqlmodify(sql)
        sql = "insert into trandetails values({}, '{}', '{}', CURDATE(), {})".format(AccoNumber[0][0], 'DR', uniqTrxNo, int(details[1]))
        sqlmodify(sql)
        sql = "select availbalance from userdetails where accnumber = {}".format(details[0])
        claccountBalance = sqlget(sql)
        sql = "update userdetails set availbalance = {balance} where accnumber = {accno}".format(balance = (claccountBalance[0][0] + int(details[1])), accno = details[0])
        sqlmodify(sql)
        sql = "insert into trandetails values({}, '{}', '{}', CURDATE(), {})".format(details[0], 'CR', uniqTrxNo, int(details[1]))
        sqlmodify(sql)
        return True
    else:
        return  False



def check():
    print("hello world")
# print(userAuthenticate(['2343dfsd', 'aman']))