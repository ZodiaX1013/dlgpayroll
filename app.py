import hashlib
import os
from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename
from PIL import Image
import os
import mysql.connector
from mysql.connector import *
import random, string
import pdfkit
import calendar
from datetime import date

# from flask_wkhtmltopdf import Wkhtmltopdf

UPLOAD_FOLDER = 'static/images/'
# WKHTMLTOPDF_PATH = "C:/Program Files/wkhtmltopdf/bin"
# WKHTMLTOPDF_PATH = f'C:\Program Files\wkhtmltopdf\bin'
WKHTMLTOPDF_PATH = f'./wkhtmltopdf.exe'


app = Flask(__name__)
app.secret_key = "asndjaheh912yeuwbqduiqasgdyq"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# wkhtmltopdf = Wkhtmltopdf(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET" , "POST"])
def home():
    print("In Home Function")
    return render_template("login.html")

@app.route('/login', methods=['GET','POST'])
def login():
    print("In Login Function Without Post")
    global connection
    if request.method == "POST" and request.form["action"] == "login":
        print("In Login Function With Post and Action As Login")
        mail = request.form["email"]
        psw = request.form["password"]

        print(mail)
        print(psw)
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            query1 = "SELECT username FROM cred"
            cursor.execute(query1)
            user = cursor.fetchall()
            user = user[0][0]
            print(user)

            query2 = "SELECT password FROM cred"
            cursor.execute(query2)
            password = cursor.fetchall()
            password = password[0][0]

            plaintext = psw.encode()
            d = hashlib.md5(plaintext)
            hash = d.hexdigest()
            print(hash)

            data = ['MCS-BS001']
            hire_date = "SELECT hire FROM employee WHERE EmployeeID= %s"
            cursor.execute(hire_date, data)
            hire_date_emp = cursor.fetchall()
            
            print(hire_date_emp)
            hire_dt = str(hire_date_emp[0][0])

            current_date = "2022-07-01"

            print(hire_dt)
            print(current_date)

            if hire_dt > current_date:
                print("Not Process")
            else:
                print("Process")


            if mail == user:
                print("User Name Is Correct")
                if hash == password:
                    print("Password is Correct Now Go To Module Function")
                    return redirect(url_for('module'))
                else:
                    print("Wrong Password - Back To Login Page")
                    msg = "Wrong Password"
                    return render_template("login.html", msg = msg)
            else:
                print("User Name Is Wrong - Back To Login page")
                msg = "Wrong Username And Password"
                return render_template("login.html", msg = msg)

        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    if request.method == "POST" and request.form["action"] == "module":
        print("In Login Function With Post and Action As Module")
        value = request.form["password"]
        user = request.form["module"]

        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            data = [user]
            query = "SELECT password FROM cred WHERE type = %s"
            cursor.execute(query,data)
            password_data = cursor.fetchall()
            password_data = password_data[0][0]

            plaintext = value.encode()
            d = hashlib.md5(plaintext)
            hash = d.hexdigest()
            print(hash)

            if hash == password_data:
                print("Password Is Correct and Now Check For Username")
                if user == "payroll":
                    print("Username is correct now go to Dashboard Of Payroll")
                    return redirect(url_for('dashboard'))
                else:
                    print("Username Is Wrong So Back To The Password Page")
                    msg = "Wrong Credentials"
                    return render_template("password.html", msg=msg)

            else:
                print("Password Is Wrong So Back To Password Page")
                msg = "Wrong Password"
                return render_template("password.html", msg=msg)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return render_template('login.html')
#     return render_template('login.html')

@app.route("/expense", methods = ["POST" , "GET"])
def expense():
    if request.method == "POST" and request.form["action"] == "esheet" :
        print("In Expense Sheet")
        return render_template("expense2.html")
    elif request.method == "POST" and request.form["action"] == "summary":
        print("In Summary")
        return render_template("expensesheet.html")
    elif request.method == "POST" and request.form["action"] == "input":
        print("In Input")
        return render_template("expense2.html")
    return render_template("expensesheet.html")


@app.route("/revenue", methods = ["POST" , "GET"])
def revenue():
    if request.method == "POST" and request.form["action"] == "rsheet" :
        return render_template("revenue2.html")
    elif request.method == "POST" and request.form["action"] == "summary":
        return render_template("revenuesheet.html")
    elif request.method == "POST" and request.form["action"] == "input":
        return render_template("revenue2.html")
    return render_template("revenuesheet.html")


@app.route("/rae", methods=["POST" , "GET"])
def rae():
    print("In RAE")
    if request.method == "POST" and request.form['action'] == 'expense':
        return redirect(url_for('expense'))
    if request.method == "POST" and request.form['action'] == 'revenue':
        return redirect(url_for('revenue'))
    if request.method == "POST" and request.form['action'] == 'main':
        return render_template("module.html")
    
    return render_template("module2.html")


@app.route("/module", methods=["GET", "POST"])
def module():
    if request.method == "POST" and request.form['action'] == 'payroll':
        value = request.form['action']
        print("User Choose Payroll Module - Goes To Password Page")
        print(value)
        return render_template("password.html", value = value)

# ===================================================================================================

    if request.method == "POST" and request.form['action'] == 'rae':  #Revenue And Expense (RAE)
        print("User Choose Revenue & Expense Module - Goes To Expense And Revenue Page")
        return redirect(url_for('rae'))

    if request.method == "POST" and request.form['action'] == 'home':
        print("In Logout")
        return render_template("login.html")
    return render_template("module.html")


@app.route("/reset", methods=["GET","POST"])
def reset():
    # global connection
    if request.method == "POST":
        old_pass = request.form["opass"]
        new_pass = request.form["npass"]
        rnew_pass = request.form["rpass"]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            query1 = "SELECT password FROM cred"
            cursor.execute(query1)
            password = cursor.fetchall()
            password = password[0][0]

            plaintext = old_pass.encode()
            d = hashlib.md5(plaintext)
            hash = d.hexdigest()

            if password == hash:
                if new_pass == rnew_pass:
                    query2 = """UPDATE cred
                    SET
                    password = %s
                    WHERE
                    username= %s
                    """
                    plaintext2 = new_pass.encode()
                    d = hashlib.md5(plaintext2)
                    hash2 = d.hexdigest()

                    data = [hash2,"admin"]
                    cursor.execute(query2,data)
                    msg = "Password updated Successfully"
                    return render_template("login.html", msg=msg)
                else:
                    msg = "New password and Re-Enter Password not match"
                    return render_template("reset.html", msg=msg)
            else:
                msg = "Old Password Wrong"
                return render_template("reset.html", msg=msg)

        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("reset.html")

@app.route("/dashboard", methods=["GET" , "POST"])
def dashboard():
    # global connection
    print("In Dashboard Without Post method")
    if request.method == "POST":
        print("In Dashboard with Post method before If")
        eid = request.form["search"]
        if eid:
            data1 = [eid]
            print("In If")
            try:
                connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
                cursor = connection.cursor(buffered=True)

                # query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'employee' AND ORDINAL_POSITION between 2 AND 4;"
                query1 = f'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "employee" AND COLUMN_NAME = "EmployeeID" OR COLUMN_NAME = "working" OR COLUMN_NAME = "FirstName" OR COLUMN_NAME = "LastName";'
                cursor.execute(query1)
                column_name = cursor.fetchall()
                print(column_name)
                heading_data = []
                data = []
                print(len(column_name))
                for i in range(len(column_name)):
                    print("i : " , i)
                    # print("j : ", j)
                    data = ''.join(column_name[i])
                    print("Data :" + data)
                    heading_data.append(data)
                
                query2 = "SELECT EmployeeID, FirstName, LastName, working FROM employee WHERE EmployeeID = %s "
                cursor.execute(query2, data1)
                table_data = cursor.fetchall()
                print(table_data)
                return render_template("dashboard.html", heading = heading_data, data = table_data)

            except Error as e:
                    print("Error While connecting to MySQL : ", e)
            finally:
                connection.commit()
                cursor.close()
                connection.close()
                print("MySQL connection is closed")                   

    else:
        print("In Else")
        # eid = request.form["search"]
        # data1 = [eid]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True) 

            # query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'employee'"
            # cursor.execute(query1)
            # column_name = cursor.fetchall()

            print("Before Query1")
            query1 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'employee' AND COLUMN_NAME = 'EmployeeID' OR COLUMN_NAME = 'working' OR COLUMN_NAME = 'FirstName' OR COLUMN_NAME = 'LastName';"
            # query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'employee' AND ORDINAL_POSITION between 2 AND 4;"
            cursor.execute(query1)
            print("Query1 Executed")
            column_name = cursor.fetchall()
            heading_data = []
            data = []
            print(len(column_name))
            for i in range(len(column_name)):
                print("i : " , i)
                # print("j : ", j)
                data = ''.join(column_name[i])
                print("Data :" + data)
                heading_data.append(data)
            
            print(column_name)
            print(heading_data)

            # query2 = "SELECT EmployeeID, FirstName, LastName FROM employee WHERE EmployeeID = %s "
            # query2 = "SELECT EmployeeID, FirstName, LastName FROM employee WHERE FirstName = %s "
            # query2 = "SELECT EmployeeID, FirstName, LastName FROM employee WHERE LastName = %s "
            # query2 = "SELECT EmployeeID, FirstName, LastName FROM employee WHERE position = %s "
            # query2 = f"SELECT EmployeeID, FirstName, LastName FROM employee"
            query2 = "SELECT EmployeeID, FirstName, LastName, working FROM employee"
            cursor.execute(query2)
            table_data = cursor.fetchall()

            print(table_data)
            return render_template("dashboard.html", heading = heading_data, data = table_data)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    print("Before Return")
    return render_template("dashboard.html")

@app.route("/employee", methods=["GET" , "POST"])
def employee():
    # global connection
    # Back To Employee Page

    if request.method == "POST" and request.form['action'] == 'back':      
        return render_template("employee.html")

    # Fetch Data

    if request.method == "POST" and request.form['action'] == 'search2': 
        
        lname = request.form["lname"]
        fname = request.form["fname"]
        position = request.form["pos"]
        eid = request.form["eid"]

        if eid:
            return render_template("dashboard.html", eid=eid)
        
# ==========================================================================================================        

    # Search Employee Page
    if request.method == "POST" and request.form['action'] == 'search':
        eid = request.form["eid"]      
        data = [eid]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            
            query1 = "SELECT FirstName From employee WHERE EmployeeID = %s"
            cursor.execute(query1, data)
            fname = cursor.fetchall()
            for i in range(len(fname)):
                fname = ''.join(fname[i])

            query2 = "SELECT LastName From employee WHERE EmployeeID = %s"
            cursor.execute(query2, data)
            lname = cursor.fetchall()
            for i in range(len(lname)):
                lname = ''.join(lname[i])
            
            query3 = "SELECT Title From employee WHERE EmployeeID = %s"
            cursor.execute(query3, data)
            title = cursor.fetchall()
            for i in range(len(title)):
                title = ''.join(title[i])

            query4 = "SELECT DOB From employee WHERE EmployeeID = %s"
            cursor.execute(query4, data)
            dob = cursor.fetchall()
            print(dob)
            if dob == []:
                dob = "0001-01-01"
            else:
                dob = dob[0][0]

            query5 = "SELECT address From employee WHERE EmployeeID = %s"
            cursor.execute(query5, data)
            add = cursor.fetchall()
            for i in range(len(add)):
                add = ''.join(add[i])

            query6 = "SELECT city From employee WHERE EmployeeID = %s"
            cursor.execute(query6, data)
            city = cursor.fetchall()
            for i in range(len(city)):
                city = ''.join(city[i])

            query7 = "SELECT country From employee WHERE EmployeeID = %s"
            cursor.execute(query7, data)
            country = cursor.fetchall()
            for i in range(len(country)):
                country = ''.join(country[i])

            query8 = "SELECT phone From employee WHERE EmployeeID = %s"
            cursor.execute(query8, data)
            phone = cursor.fetchall()
            for i in range(len(phone)):
                phone = ''.join(phone[i])

            query9 = "SELECT mobile From employee WHERE EmployeeID = %s"
            cursor.execute(query9, data)
            mobile = cursor.fetchall()
            for i in range(len(mobile)):
                mobile = ''.join(mobile[i])

            query10 = "SELECT fax From employee WHERE EmployeeID = %s"
            cursor.execute(query10, data)
            fax = cursor.fetchall()
            for i in range(len(fax)):
                fax = ''.join(fax[i])

            query11 = "SELECT email From employee WHERE EmployeeID = %s"
            cursor.execute(query11, data)
            mail = cursor.fetchall()
            for i in range(len(mail)):
                mail = ''.join(mail[i])

            query12 = "SELECT NICno From employee WHERE EmployeeID = %s"
            cursor.execute(query12, data)
            nic = cursor.fetchall()
            for i in range(len(nic)):
                nic = ''.join(nic[i])

            query13 = "SELECT TaxAC From employee WHERE EmployeeID = %s"
            cursor.execute(query13, data)
            tax = cursor.fetchall()
            for i in range(len(tax)):
                tax = ''.join(tax[i])

            query14 = "SELECT Bank From employee WHERE EmployeeID = %s"
            cursor.execute(query14, data)
            bank = cursor.fetchall()
            for i in range(len(bank)):
                bank = ''.join(bank[i])

            query15 = "SELECT BankAC From employee WHERE EmployeeID = %s"
            cursor.execute(query15, data)
            bankac = cursor.fetchall()
            for i in range(len(bankac)):
                bankac = ''.join(bankac[i])

            query16 = "SELECT Bankcode From employee WHERE EmployeeID = %s"
            cursor.execute(query16, data)
            code = cursor.fetchall()
            for i in range(len(code)):
                code = ''.join(code[i])
            
            query17 = "SELECT Carbenefit From employee WHERE EmployeeID = %s"
            cursor.execute(query17, data)
            car = cursor.fetchall()
            for i in range(len(car)):
                car = ''.join(car[i])
            
            query18 = "SELECT hire From employee WHERE EmployeeID = %s"
            cursor.execute(query18, data)
            hire = cursor.fetchall()
            if hire == []:
                hire = "0001-01-01"
            else:
                hire = hire[0][0]

            query19 = "SELECT salary From employee WHERE EmployeeID = %s"
            cursor.execute(query19, data)
            salary = cursor.fetchall()
            for i in range(len(salary)):
                salary = ''.join(salary[i])

            query20 = "SELECT position From employee WHERE EmployeeID = %s"
            cursor.execute(query20, data)
            position = cursor.fetchall()
            for i in range(len(position)):
                position = ''.join(position[i])
            
            query21 = "SELECT department From employee WHERE EmployeeID = %s"
            cursor.execute(query21, data)
            dep = cursor.fetchall()
            for i in range(len(dep)):
                dep = ''.join(dep[i])

            query22 = "SELECT Subdepartment From employee WHERE EmployeeID = %s"
            cursor.execute(query22, data)
            sdep = cursor.fetchall()
            for i in range(len(sdep)):
                sdep = ''.join(sdep[i])

            query23 = "SELECT Payescheme From employee WHERE EmployeeID = %s"
            cursor.execute(query23, data)
            payes = cursor.fetchall()
            for i in range(len(payes)):
                payes = ''.join(payes[i])

            query24 = "SELECT Payepercentage From employee WHERE EmployeeID = %s"
            cursor.execute(query24, data)
            payep = cursor.fetchall()
            for i in range(len(payep)):
                payep = ''.join(payep[i])

            query25 = "SELECT Localleave From employee WHERE EmployeeID = %s"
            cursor.execute(query25, data)
            lleave = cursor.fetchall()
            for i in range(len(lleave)):
                lleave = ''.join(lleave[i])

            query26 = "SELECT Sickleave From employee WHERE EmployeeID = %s"
            cursor.execute(query26, data)
            sleave = cursor.fetchall()
            for i in range(len(sleave)):
                sleave = ''.join(sleave[i])

            query27 = "SELECT Fixedallow From employee WHERE EmployeeID = %s"
            cursor.execute(query27, data)
            falw = cursor.fetchall()
            for i in range(len(falw)):
                falw = ''.join(falw[i])

            query28 = "SELECT Travelmode From employee WHERE EmployeeID = %s"
            cursor.execute(query28, data)
            travelmod = cursor.fetchall()
            for i in range(len(travelmod)):
                travelmod = ''.join(travelmod[i])

            query29 = "SELECT Travelallow From employee WHERE EmployeeID = %s"
            cursor.execute(query29, data)
            talw = cursor.fetchall()
            for i in range(len(talw)):
                talw = ''.join(talw[i])

            query30 = "SELECT EDF From employee WHERE EmployeeID = %s"
            cursor.execute(query30, data)
            edf = cursor.fetchall()
            for i in range(len(edf)):
                edf = ''.join(edf[i])

            query31 = "SELECT months From employee WHERE EmployeeID = %s"
            cursor.execute(query31, data)
            mon = cursor.fetchall()
            for i in range(len(mon)):
                mon = ''.join(mon[i])

            query32 = "SELECT MonthlyEDF From employee WHERE EmployeeID = %s"
            cursor.execute(query32, data)
            medf = cursor.fetchall()
            for i in range(len(medf)):
                medf = ''.join(medf[i])

            query33 = "SELECT Houseinterest From employee WHERE EmployeeID = %s"
            cursor.execute(query33, data)
            house = cursor.fetchall()
            for i in range(len(house)):
                house = ''.join(house[i])

            query34 = "SELECT Educationrel From employee WHERE EmployeeID = %s"
            cursor.execute(query34, data)
            erel = cursor.fetchall()
            for i in range(len(erel)):
                erel = ''.join(erel[i])

            query35 = "SELECT Medicalrel From employee WHERE EmployeeID = %s"
            cursor.execute(query35, data)
            mrel = cursor.fetchall()
            for i in range(len(mrel)):
                mrel = ''.join(mrel[i])

            query36 = "SELECT Paymentmode From employee WHERE EmployeeID = %s"
            cursor.execute(query36, data)
            pay = cursor.fetchall()
            for i in range(len(pay)):
                pay = ''.join(pay[i])

            query37 = "SELECT medical From employee WHERE EmployeeID = %s"
            cursor.execute(query37, data)
            med = cursor.fetchall()
            for i in range(len(med)):
                med = ''.join(med[i])

            query38 = "SELECT Specialbonus From employee WHERE EmployeeID = %s"
            cursor.execute(query38, data)
            spbns = cursor.fetchall()
            for i in range(len(spbns)):
                spbns = ''.join(spbns[i])

            query39 = "SELECT Workingdays From employee WHERE EmployeeID = %s"
            cursor.execute(query39, data)
            work = cursor.fetchall()
            for i in range(len(work)):
                work = ''.join(work[i])

            query40 = "SELECT Lastwork From employee WHERE EmployeeID = %s"
            cursor.execute(query40, data)
            last = cursor.fetchall()
            print(last)
            if last == []:
                last = "0001-01-01"
            else:
                last = last[0][0]

            query41 = "SELECT working From employee WHERE EmployeeID = %s"
            cursor.execute(query41, data)
            working = cursor.fetchall()
            for i in range(len(working)):
                working = ''.join(working[i])

            return render_template("employee2.html",eid=eid, fname=fname, lname=lname, title=title,dob=dob, add=add, city=city, country=country, phone=phone, mobile=mobile, fax=fax, mail=mail, nic=nic, tax=tax, bank=bank, bankac =bankac,code=code, car=car, hire=hire, salary=salary, position=position, dep=dep, sdep=sdep, payes=payes, payep=payep, lleave=lleave, sleave=sleave, falw=falw, travelmod = travelmod, talw=talw, edf=edf, mon=mon, medf=medf, house=house, erel=erel, mrel=mrel, pay=pay, med=med, spbns=spbns, work=work , last=last, working = working)

        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        return render_template("employee.html") 

# ==========================================================================================================

    # Update To Database

    if request.method == "POST" and request.form['action']== 'update':
        eid = request.form["eid"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        title = request.form["title"]
        dob = request.form["dob"]
        clocked = request.form["optradio"]
        address = request.form["add"]
        city = request.form["city"]
        country = request.form["con"]
        phone = request.form["phn"]
        mobile = request.form["mob"]
        fax = request.form["fax"]
        mail = request.form["mail"]
        if request.files["img"]:
            eimage = request.files["img"]
        else:
            eimage = ""
        nic = request.form["nic"]
        tax = request.form["tax"]
        bank = request.form["bank"]
        bank_ac = request.form["bac"]
        code = request.form["code"]
        # report = request.form["rpt"]
        report = ""
        nps = request.form["optradio2"]
        car = request.form["car"]
        hire = request.form["hire"]
        salary = request.form["sal"]
        position = request.form["pos"]
        dep = request.form["dep"]
        sdep = request.form["sdep"]
        paye = request.form["psch"]
        per = request.form["per"]
        lleave = request.form["lleave"]
        sleave = request.form["sleave"]
        fallow = request.form["falw"]
        tmode = request.form["tmode"]
        tallow = request.form["talw"]
        expatriate = request.form.get("chk1")
        edf = request.form["edf"]
        months = request.form["month"]  
        medf = request.form["medf"]
        house = request.form["hint"]
        erel = request.form["erel"]
        mrel = request.form["mrel"]
        payment = request.form["optradio5"]
        medical = request.form["med"]
        working = request.form["optradio3"]
        print(working)
        if working == "No":
            lwork = request.form["lwork"]
        else:
            lwork = "0001-01-01"
        spbonus = request.form["spbonus"]
        wdays = request.form["wday"]

        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            update_query = """
            UPDATE employee
            SET
            FirstName =%s ,
            LastName =%s ,
            Title =%s ,
            DOB =%s ,
            address =%s ,
            city =%s ,
            country =%s ,
            phone =%s ,
            mobile =%s ,
            fax =%s ,
            email =%s ,
            NICno =%s ,
            TaxAC =%s ,
            Bank =%s ,
            BankAC =%s ,
            Bankcode =%s ,
            Carbenefit =%s ,
            hire =%s ,
            salary =%s ,
            position =%s ,
            department =%s ,
            Subdepartment =%s ,
            Payescheme =%s ,
            Payepercentage =%s ,
            Localleave =%s ,
            Sickleave =%s ,
            Fixedallow =%s ,
            Travelmode =%s ,
            Travelallow =%s ,
            expatriate =%s ,
            EDF =%s ,
            months =%s ,
            MonthlyEDF =%s ,
            Houseinterest =%s ,
            Educationrel =%s ,
            Medicalrel =%s ,
            Paymentmode =%s ,
            medical =%s ,
            working =%s ,
            Lastwork =%s ,
            Specialbonus =%s ,
            Workingdays = %s
            WHERE
            EmployeeID = %s;
            """

            data = [fname, lname, title, dob, address, city, country, phone, mobile, fax, mail, nic, tax, bank, bank_ac, code, car, hire, salary, position, dep, sdep, paye, per, lleave, sleave, fallow, tmode, tallow, expatriate, edf, months, medf, house, erel, mrel, payment, medical, working, lwork, spbonus, wdays, eid]
            cursor.execute(update_query, data)

            msg = "Update Successfully"
            return render_template("employee.html", msg=msg)    
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        return render_template("employee.html")         
        
# Redirect

    if request.method == "POST" and request.form['action']== 'redirect':
        eid = request.form["eid"]
        return render_template("change_id.html", eid=eid)

# Change Username
    if request.method == "POST" and request.form['action']== 'change':
        eid1 = request.form["eid1"]
        eid2 = request.form["eid2"]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            query1 = "SELECT EmployeeID FROM employee WHERE EmployeeID=%s"
            data1 = [eid1]
            cursor.execute(query1, data1)

            eid = cursor.fetchall()
            for i in range(len(eid)):
                eid = ''.join(eid[i])
            
            if eid == eid1:
                update_query = """UPDATE employee
                            SET
                            EmployeeID = %s
                            WHERE
                            EmployeeID = %s;
                            """
                data = [eid2, eid1]
                cursor.execute(update_query, data)
                print("Data Updated Successfully")
                msg = "Data Updated Successfully"
                return render_template("employee.html", msg=msg)
            else:
                msg = "Employee ID Not Available"
                return render_template("change_id.html", msg=msg)
            
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        
        return render_template("change_id.html")

# ==========================================================================================================
    # Save To Database

    if request.method == "POST" and request.form['action']== 'save':
        print("in Save")
        eid = request.form["eid"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        title = request.form["title"]
        dob = request.form["dob"]
        print("dob ", dob)
        if dob == "":
            dob = "0001-01-01"
        else:
            dob = dob
        print("dob ", dob)
        clocked = request.form["optradio"]
        address = request.form["add"]
        city = request.form["city"]
        country = request.form["con"]
        phone = request.form["phn"]
        mobile = request.form["mob"]
        fax = request.form["fax"]
        mail = request.form["mail"]
        if request.files["img"]:
            eimage = request.files["img"]
        else:
            eimage = ""
        nic = request.form["nic"]
        tax = request.form["tax"]
        bank = request.form["bank"]
        bank_ac = request.form["bac"]
        code = request.form["code"]
        # report = request.form["rpt"]
        report = ""
        nps = request.form["optradio2"]
        car = request.form["car"]
        print(car)
        if car == "":
            print("In If")
            car = "0"
        else:
            print("In Else")
            car = car
        hire = request.form["hire"]
        if hire == "":
            hire = "0001-01-01"
        else:
            hire = hire
        
        salary = request.form["sal"]
        if salary == "":
            salary = "0"
        else:
            salary == salary

        position = request.form["pos"]
        dep = request.form["dep"]
        print("Dep ", dep)
        # sdep = request.form["sdep"]
        # print("Sub Dep ", sdep)
        sdep = ""
        paye = request.form["psch"]
        per = request.form["per"]

        lleave = request.form["lleave"]
        if lleave == "":
            lleave = "0"
        else:
            lleave == lleave

        sleave = request.form["sleave"]
        if sleave == "":
            sleave = "0"
        else:
            sleave == sleave

        fallow = request.form["falw"]
        if fallow == "":
            fallow = "0"
        else:
            fallow == fallow

        tmode = request.form["tmode"]
        tallow = request.form["talw"]
        if tallow == "":
            tallow = "0"
        else:
            tallow == tallow

        expatriate = request.form["optradiod4"]
        print("expatriate " , expatriate)
        if expatriate == "":
            expatriate = "No"

        edf = request.form["edf"]
        if edf == "":
            edf = "0"
        else:
            edf == edf

        months = request.form["month"]  
        medf = request.form["medf"]
        house = request.form["hint"]
        if house == "":
            house = "0"
        else:
            house == house

        erel = request.form["erel"]
        if erel == "":
            erel = "0"
        else:
            erel == erel

        mrel = request.form["mrel"]
        if mrel == "":
            mrel = "0"
        else:
            mrel == mrel

        payment = request.form["optradio5"]
        medical = request.form["med"]
        working = request.form["optradio3"]
        if working == "No":
            lwork = request.form["lwork"]
        else:
            lwork = "0001-01-01"
        spbonus = request.form["spbonus"]
        if spbonus == "":
            spbonus = "0"
        else:
            spbonus == spbonus

        wdays = request.form["wday"]
        if wdays == "":
            wdays = "0"
        else:
            wdays == wdays

        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            query2 =""" INSERT INTO employee (
                EmployeeID,
                FirstName,
                LastName,
                Title,
                DOB,
                clocked,
                address,
                city,
                country,
                phone,
                mobile,
                fax,
                email,
                image,
                NICno,
                TaxAC,
                Bank,
                BankAC,
                Bankcode,
                report,
                NPS,
                Carbenefit,
                hire,
                salary,
                position,
                department,
                Subdepartment,
                Payescheme,
                Payepercentage,
                Localleave,
                Sickleave,
                Fixedallow,
                Travelmode,
                Travelallow,
                expatriate,
                EDF,
                months,
                MonthlyEDF,
                Houseinterest,
                Educationrel,
                Medicalrel,
                Paymentmode,
                medical,
                working,
                Lastwork,
                Specialbonus,
                Workingdays
              )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
              );"""
            
            if(eimage != ""):
                # image = eimage.convert('RGB')    
                if eimage and allowed_file(eimage.filename):
                    print("In Image If")
                    filename = secure_filename(eimage.filename)
                    filename=''.join(random.choices(string.ascii_lowercase +string.digits, k=20))
                    picture = Image.open(eimage)
                    picture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename+'.jpeg'), "JPEG", optimize = True, quality = 30)
                    print(filename)
            else:
                filename = ""
            # data1 = [eid, fname, lname, title, dob, clocked, address, city, country, phone, mobile, fax, mail,filename, nic, tax, bank, bank_ac, code, report, nps, car, hire, salary, position, dep, sdep, paye, per, lleave, sleave, fallow, tmode, tallow, expatriate, edf, months, medf, house, erel, mrel, payment, medical, working, lwork, spbonus, wdays]
            data1 = [eid, fname, lname, title, dob, clocked, address, city, country, phone, mobile, fax, mail, filename, nic, tax, bank, bank_ac, code, report, nps, car, hire, salary, position, dep, sdep, paye, per, lleave, sleave, fallow, tmode, tallow, expatriate, edf, months, medf, house, erel, mrel, payment, medical, working, lwork, spbonus, wdays]
            print("Before Query")
            cursor.execute(query2, data1)
            print("Insert Query Successfully")
            msg = "New Employee Created Successfully"
            return render_template("employee.html" , msg=msg)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("employee.html")         

@app.route("/salary", methods=["GET" , "POST"])
def salary():
    # global connection
    # Search Data
    if request.method == "POST" and request.form['action'] == 'search':
        eid = request.form["eid"]
        month = request.form["mon"]
        year = request.form["year"]
        print("In If")
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True) 
            
            data1 = [eid, month]
            data2 = [eid]

            query = "SELECT LockSal FROM salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query,data1)
            lockSal = cursor.fetchall()
            for i in range(len(lockSal)):
                lockSal = ''.join(lockSal[i])

            if lockSal == "No":
                print("In If 2")
                query1 = "SELECT BasicSalary From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query1, data1)
                basic = cursor.fetchall()
                for i in range(len(basic)):
                    basic = ''.join(basic[i])

                query2 = "SELECT Fixedallow From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query2, data1)
                falw = cursor.fetchall()
                for i in range(len(falw)):
                    falw = ''.join(falw[i])

                query3 = "SELECT OtherDeduction From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query3, data1)
                otherded = cursor.fetchall()
                for i in range(len(otherded)):
                    otherded = ''.join(otherded[i])

                query4 = "SELECT Overtime From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query4, data1)
                ot = cursor.fetchall()
                for i in range(len(ot)):
                    ot = ''.join(ot[i])

                query5 = "SELECT DiscBonus From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query5, data1)
                disc = cursor.fetchall()
                for i in range(len(disc)):
                    disc = ''.join(disc[i])

                query6 = "SELECT NSFEmpee From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query6, data1)
                nsf = cursor.fetchall()
                for i in range(len(nsf)):
                    nsf = ''.join(nsf[i])

                query7 = "SELECT OtherAllow From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query7, data1)
                oalw = cursor.fetchall()
                for i in range(len(oalw)):
                    oalw = ''.join(oalw[i])

                query8 = "SELECT TaxableAllow From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query8, data1)
                tax = cursor.fetchall()
                for i in range(len(tax)):
                    tax = ''.join(tax[i])

                query9 = "SELECT Medical From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query9, data1)
                med = cursor.fetchall()
                for i in range(len(med)):
                    med = ''.join(med[i])

                query10 = "SELECT Transport From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query10, data1)
                tran = cursor.fetchall()
                for i in range(len(tran)):
                    tran = ''.join(tran[i])

                query11 = "SELECT NTaxableAllow From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query11, data1)
                ntax = cursor.fetchall()
                for i in range(len(ntax)):
                    ntax = ''.join(ntax[i])

                query12 = "SELECT EDF From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query12, data1)
                edf = cursor.fetchall()
                for i in range(len(edf)):
                    edf = ''.join(edf[i])

                query13 = "SELECT Arrears From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query13, data1)
                arr = cursor.fetchall()
                for i in range(len(arr)):
                    arr = ''.join(arr[i])

                query14 = "SELECT AttendanceBns From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query14, data1)
                att = cursor.fetchall()
                for i in range(len(att)):
                    att = ''.join(att[i])

                # query15 = "SELECT TravelAllow From OriginalData WHERE EmployeeID = %s AND Month = %s"
                # cursor.execute(query15, data1)
                # travel = cursor.fetchall()
                # for i in range(len(travel)):
                #     travel = ''.join(travel[i])

                query16 = "SELECT EOY From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query16, data1)
                eoy = cursor.fetchall()
                for i in range(len(eoy)):
                    eoy = ''.join(eoy[i])

                query17 = "SELECT Loan From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query17, data1)
                loan = cursor.fetchall()
                for i in range(len(loan)):
                    loan = ''.join(loan[i])

                query18 = "SELECT CarBenefit From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query18, data1)
                car = cursor.fetchall()
                for i in range(len(car)):
                    car = ''.join(car[i])

                query19 = "SELECT LeaveRef From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query19, data1)
                leave = cursor.fetchall()
                for i in range(len(leave)):
                    leave = ''.join(leave[i])

                query20 = "SELECT CurrentSLevy From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query20, data1)
                slevy = cursor.fetchall()
                for i in range(len(slevy)):
                    slevy = ''.join(slevy[i])

                query21 = "SELECT SpecialBns From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query21, data1)
                spebns = cursor.fetchall()
                for i in range(len(spebns)):
                    spebns = ''.join(spebns[i])

                query22 = "SELECT Lateness From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query22, data1)
                late = cursor.fetchall()
                for i in range(len(late)):
                    late = ''.join(late[i])

                query23 = "SELECT EducationRel From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query23, data1)
                edurel = cursor.fetchall()
                for i in range(len(edurel)):
                    edurel = ''.join(edurel[i])

                query24 = "SELECT SpeProBns From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query24, data1)
                speprobns = cursor.fetchall()
                for i in range(len(speprobns)):
                    speprobns = ''.join(speprobns[i])

                query25 = "SELECT NPS From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query25, data1)
                nps = cursor.fetchall()
                for i in range(len(nps)):
                    nps = ''.join(nps[i])

                query26 = "SELECT MedicalRel From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query26, data1)
                medrel = cursor.fetchall()
                for i in range(len(medrel)):
                    medrel = ''.join(medrel[i])

                query27 = "SELECT Payable From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query27, data1)
                payable = cursor.fetchall()
                for i in range(len(payable)):
                    payable = ''.join(payable[i])

                query28 = "SELECT Deduction From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query28, data1)
                ded = cursor.fetchall()
                for i in range(len(ded)):
                    ded = ''.join(ded[i])

                query29 = "SELECT NetPay From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query29, data1)
                net = cursor.fetchall()
                for i in range(len(net)):
                    net = ''.join(net[i])


                query31 = "SELECT CurrentGross From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query31, data1)
                cgross = cursor.fetchall()
                for i in range(len(cgross)):
                    cgross = ''.join(cgross[i])

                query32 = "SELECT PrevGross From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query32, data1)
                pgross = cursor.fetchall()
                for i in range(len(pgross)):
                    pgross = ''.join(pgross[i])

                query33 = "SELECT IET From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query33, data1)
                iet = cursor.fetchall()
                for i in range(len(iet)):
                    iet = ''.join(iet[i])

                query34 = "SELECT NetCh From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query34, data1)
                netch = cursor.fetchall()
                for i in range(len(netch)):
                    netch = ''.join(netch[i])

                query35 = "SELECT CurrentPAYE From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query35, data1)
                cpaye = cursor.fetchall()
                for i in range(len(cpaye)):
                    cpaye = ''.join(cpaye[i])

                query36 = "SELECT PrevPAYE From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query36, data1)
                ppaye = cursor.fetchall()
                for i in range(len(ppaye)):
                    ppaye = ''.join(ppaye[i])

                query37 = "SELECT PAYE From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query37, data1)
                paye = cursor.fetchall()
                for i in range(len(paye)):
                    paye = ''.join(paye[i])

                query38 = "SELECT eCSG From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query38, data1)
                ecsg = cursor.fetchall()
                for i in range(len(ecsg)):
                    ecsg = ''.join(ecsg[i])

                query39 = "SELECT eNSF From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query39, data1)
                ensf = cursor.fetchall()
                for i in range(len(ensf)):
                    ensf = ''.join(ensf[i])

                query40 = "SELECT eLevy From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query40, data1)
                elevy = cursor.fetchall()
                for i in range(len(elevy)):
                    elevy = ''.join(elevy[i])

                query41 = "SELECT Absences From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query41, data1)
                absence = cursor.fetchall()
                for i in range(len(absence)):
                    absence = ''.join(absence[i])

                query42 = "SELECT FirstName From employee WHERE EmployeeID = %s"
                cursor.execute(query42, data2)
                fname = cursor.fetchall()
                for i in range(len(fname)):
                    fname = ''.join(fname[i])

                query43 = "SELECT LastName From employee WHERE EmployeeID = %s"
                cursor.execute(query43, data2)
                lname = cursor.fetchall()
                for i in range(len(lname)):
                    lname = ''.join(lname[i])

                query44 = "SELECT position From employee WHERE EmployeeID = %s"
                cursor.execute(query44, data2)
                pos = cursor.fetchall()
                for i in range(len(pos)):
                    pos = ''.join(pos[i])

                query45 = "SELECT NetPaysheet From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query45, data1)
                pnet = cursor.fetchall()
                for i in range(len(pnet)):
                    pnet = ''.join(pnet[i])            
                
                query46 = "SELECT PrevIET From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query46, data1)
                piet = cursor.fetchall()
                for i in range(len(piet)):
                    piet = ''.join(piet[i])
                
                query47 = "SELECT PrevThreshold From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query47, data1)
                pthes = cursor.fetchall()
                for i in range(len(pthes)):
                    pthes = ''.join(pthes[i])

                query48 = "SELECT Threshold From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query48, data1)
                ths = cursor.fetchall()
                for i in range(len(ths)):
                    ths = ''.join(ths[i])

                query49 = "SELECT PrevSLevy From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query49, data1)
                plevy = cursor.fetchall()
                for i in range(len(plevy)):
                    plevy = ''.join(plevy[i])

                query50 = "SELECT slevyPay From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query50, data1)
                slevypay = cursor.fetchall()
                for i in range(len(slevypay)):
                    slevypay = ''.join(slevypay[i])

                query51 = "SELECT netchar From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query51, data1)
                netchar = cursor.fetchall()
                for i in range(len(netchar)):
                    netchar = ''.join(netchar[i])
                
                query52 = "SELECT PRGF From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query52, data1)
                prgf = cursor.fetchall()
                for i in range(len(prgf)):
                    prgf = ''.join(prgf[i])

                query53 = "SELECT cGrossTax From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query53, data1)
                gtax = cursor.fetchall()
                for i in range(len(gtax)):
                    gtax = ''.join(gtax[i])
                
                print("Before Query Execute")
                query54 = "SELECT Arrears, LocalRef, FixedAllowance, DiscBns, AttBns, Transport, SickRef, SpeBns, OtherAlw, Overseas, OtherDed, Absences, ot1, amt1, ot2, amt2, ot3, amt3, lateness, amt4, TaxDes, tax, NTaxDes, ntax, absenceDays, amt5 FROM ModifyVariables WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query54, data1)
                variable_data = cursor.fetchall()
                length = len(variable_data)

                query55 = "SELECT Workingdays FROM employee WHERE EmployeeID = %s"
                cursor.execute(query55,data2)
                wdays = cursor.fetchall()
                for i in range(len(wdays)):
                    wdays = ''.join(wdays[i])

                query56 = "SELECT paysheet_gross From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query56, data1)
                pay_gross = cursor.fetchall()
                for i in range(len(pay_gross)):
                    pay_gross = ''.join(pay_gross[i])

                return render_template("salary.html", basic=basic, falw=falw, otherded=otherded, ot=ot, disc=disc, nsf=nsf, oalw=oalw, tax=tax, med=med, tran=tran, ntax=ntax, edf=edf, arr=arr, att=att, eoy=eoy, loan=loan, car=car, leave=leave, slevy=slevy, spebns=spebns, late=late, edurel=edurel, speprobns=speprobns, nps=nps, medrel=medrel, payable=payable, ded=ded, net=net, cgross=cgross, pgross=pgross, iet=iet, netch=netch, cpaye=cpaye, ppaye=ppaye, paye=paye, ecsg=ecsg, ensf=ensf, elevy=elevy, absence=absence, eid=eid, fname=fname, lname=lname, pos=pos, month=month, year=year, pnet=pnet, piet=piet, pthes=pthes, ths=ths, plevy=plevy, slevypay = slevypay, netchar=netchar, prgf = prgf, gtax=gtax, vdata = variable_data, length = length, wdays=wdays, paygross = pay_gross)
# ============================================================================================================================================================================================                
            else:
# ============================================================================================================================================================================================                                
                query1 = "SELECT BasicSalary From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query1, data1)
                basic = cursor.fetchall()
                for i in range(len(basic)):
                    basic = ''.join(basic[i])

                query2 = "SELECT Fixedallow From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query2, data1)
                falw = cursor.fetchall()
                for i in range(len(falw)):
                    falw = ''.join(falw[i])

                query3 = "SELECT OtherDeduction From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query3, data1)
                otherded = cursor.fetchall()
                for i in range(len(otherded)):
                    otherded = ''.join(otherded[i])

                query4 = "SELECT Overtime From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query4, data1)
                ot = cursor.fetchall()
                for i in range(len(ot)):
                    ot = ''.join(ot[i])

                query5 = "SELECT DiscBonus From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query5, data1)
                disc = cursor.fetchall()
                for i in range(len(disc)):
                    disc = ''.join(disc[i])

                query6 = "SELECT NSFEmpee From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query6, data1)
                nsf = cursor.fetchall()
                for i in range(len(nsf)):
                    nsf = ''.join(nsf[i])

                query7 = "SELECT OtherAllow From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query7, data1)
                oalw = cursor.fetchall()
                for i in range(len(oalw)):
                    oalw = ''.join(oalw[i])

                query8 = "SELECT TaxableAllow From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query8, data1)
                tax = cursor.fetchall()
                for i in range(len(tax)):
                    tax = ''.join(tax[i])

                query9 = "SELECT Medical From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query9, data1)
                med = cursor.fetchall()
                for i in range(len(med)):
                    med = ''.join(med[i])

                query10 = "SELECT Transport From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query10, data1)
                tran = cursor.fetchall()
                for i in range(len(tran)):
                    tran = ''.join(tran[i])

                query11 = "SELECT NTaxableAllow From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query11, data1)
                ntax = cursor.fetchall()
                for i in range(len(ntax)):
                    ntax = ''.join(ntax[i])

                query12 = "SELECT EDF From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query12, data1)
                edf = cursor.fetchall()
                for i in range(len(edf)):
                    edf = ''.join(edf[i])

                query13 = "SELECT Arrears From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query13, data1)
                arr = cursor.fetchall()
                for i in range(len(arr)):
                    arr = ''.join(arr[i])

                query14 = "SELECT AttendanceBns From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query14, data1)
                att = cursor.fetchall()
                for i in range(len(att)):
                    att = ''.join(att[i])

                # query15 = "SELECT TravelAllow From OriginalData WHERE EmployeeID = %s AND Month = %s"
                # cursor.execute(query15, data1)
                # travel = cursor.fetchall()
                # for i in range(len(travel)):
                #     travel = ''.join(travel[i])

                query16 = "SELECT EOY From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query16, data1)
                eoy = cursor.fetchall()
                for i in range(len(eoy)):
                    eoy = ''.join(eoy[i])

                query17 = "SELECT Loan From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query17, data1)
                loan = cursor.fetchall()
                for i in range(len(loan)):
                    loan = ''.join(loan[i])

                query18 = "SELECT CarBenefit From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query18, data1)
                car = cursor.fetchall()
                for i in range(len(car)):
                    car = ''.join(car[i])

                query19 = "SELECT LeaveRef From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query19, data1)
                leave = cursor.fetchall()
                for i in range(len(leave)):
                    leave = ''.join(leave[i])

                query20 = "SELECT CurrentSLevy From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query20, data1)
                slevy = cursor.fetchall()
                for i in range(len(slevy)):
                    slevy = ''.join(slevy[i])

                query21 = "SELECT SpecialBns From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query21, data1)
                spebns = cursor.fetchall()
                for i in range(len(spebns)):
                    spebns = ''.join(spebns[i])

                query22 = "SELECT Lateness From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query22, data1)
                late = cursor.fetchall()
                for i in range(len(late)):
                    late = ''.join(late[i])

                query23 = "SELECT EducationRel From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query23, data1)
                edurel = cursor.fetchall()
                for i in range(len(edurel)):
                    edurel = ''.join(edurel[i])

                query24 = "SELECT SpeProBns From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query24, data1)
                speprobns = cursor.fetchall()
                for i in range(len(speprobns)):
                    speprobns = ''.join(speprobns[i])

                query25 = "SELECT NPS From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query25, data1)
                nps = cursor.fetchall()
                for i in range(len(nps)):
                    nps = ''.join(nps[i])

                query26 = "SELECT MedicalRel From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query26, data1)
                medrel = cursor.fetchall()
                for i in range(len(medrel)):
                    medrel = ''.join(medrel[i])

                query27 = "SELECT Payable From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query27, data1)
                payable = cursor.fetchall()
                for i in range(len(payable)):
                    payable = ''.join(payable[i])

                query28 = "SELECT Deduction From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query28, data1)
                ded = cursor.fetchall()
                for i in range(len(ded)):
                    ded = ''.join(ded[i])

                query29 = "SELECT NetPay From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query29, data1)
                net = cursor.fetchall()
                for i in range(len(net)):
                    net = ''.join(net[i])


                query31 = "SELECT CurrentGross From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query31, data1)
                cgross = cursor.fetchall()
                for i in range(len(cgross)):
                    cgross = ''.join(cgross[i])

                query32 = "SELECT PrevGross From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query32, data1)
                pgross = cursor.fetchall()
                for i in range(len(pgross)):
                    pgross = ''.join(pgross[i])

                query33 = "SELECT IET From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query33, data1)
                iet = cursor.fetchall()
                for i in range(len(iet)):
                    iet = ''.join(iet[i])

                query34 = "SELECT NetCh From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query34, data1)
                netch = cursor.fetchall()
                for i in range(len(netch)):
                    netch = ''.join(netch[i])

                query35 = "SELECT CurrentPAYE From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query35, data1)
                cpaye = cursor.fetchall()
                for i in range(len(cpaye)):
                    cpaye = ''.join(cpaye[i])

                query36 = "SELECT PrevPAYE From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query36, data1)
                ppaye = cursor.fetchall()
                for i in range(len(ppaye)):
                    ppaye = ''.join(ppaye[i])

                query37 = "SELECT PAYE From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query37, data1)
                paye = cursor.fetchall()
                for i in range(len(paye)):
                    paye = ''.join(paye[i])

                query38 = "SELECT eCSG From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query38, data1)
                ecsg = cursor.fetchall()
                for i in range(len(ecsg)):
                    ecsg = ''.join(ecsg[i])

                query39 = "SELECT eNSF From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query39, data1)
                ensf = cursor.fetchall()
                for i in range(len(ensf)):
                    ensf = ''.join(ensf[i])

                query40 = "SELECT eLevy From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query40, data1)
                elevy = cursor.fetchall()
                for i in range(len(elevy)):
                    elevy = ''.join(elevy[i])

                query41 = "SELECT Absences From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query41, data1)
                absence = cursor.fetchall()
                for i in range(len(absence)):
                    absence = ''.join(absence[i])

                query42 = "SELECT FirstName From employee WHERE EmployeeID = %s"
                cursor.execute(query42, data2)
                fname = cursor.fetchall()
                for i in range(len(fname)):
                    fname = ''.join(fname[i])

                query43 = "SELECT LastName From employee WHERE EmployeeID = %s"
                cursor.execute(query43, data2)
                lname = cursor.fetchall()
                for i in range(len(lname)):
                    lname = ''.join(lname[i])

                query44 = "SELECT position From employee WHERE EmployeeID = %s"
                cursor.execute(query44, data2)
                pos = cursor.fetchall()
                for i in range(len(pos)):
                    pos = ''.join(pos[i])

                query45 = "SELECT NetPaysheet From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query45, data1)
                pnet = cursor.fetchall()
                for i in range(len(pnet)):
                    pnet = ''.join(pnet[i])            
                
                query46 = "SELECT PrevIET From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query46, data1)
                piet = cursor.fetchall()
                for i in range(len(piet)):
                    piet = ''.join(piet[i])
                
                query47 = "SELECT PrevThreshold From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query47, data1)
                pthes = cursor.fetchall()
                for i in range(len(pthes)):
                    pthes = ''.join(pthes[i])

                query48 = "SELECT Threshold From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query48, data1)
                ths = cursor.fetchall()
                for i in range(len(ths)):
                    ths = ''.join(ths[i])

                query49 = "SELECT PrevSLevy From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query49, data1)
                plevy = cursor.fetchall()
                for i in range(len(plevy)):
                    plevy = ''.join(plevy[i])

                query50 = "SELECT slevyPay From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query50, data1)
                slevypay = cursor.fetchall()
                for i in range(len(slevypay)):
                    slevypay = ''.join(slevypay[i])

                query51 = "SELECT netchar From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query51, data1)
                netchar = cursor.fetchall()
                for i in range(len(netchar)):
                    netchar = ''.join(netchar[i])
                
                query52 = "SELECT PRGF From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query52, data1)
                prgf = cursor.fetchall()
                for i in range(len(prgf)):
                    prgf = ''.join(prgf[i])

                query53 = "SELECT cGrossTax From salary WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query53, data1)
                gtax = cursor.fetchall()
                for i in range(len(gtax)):
                    gtax = ''.join(gtax[i])
                
                print("Before Query Execute")
                query54 = "SELECT Arrears, LocalRef, FixedAllowance, DiscBns, AttBns, Transport, SickRef, SpeBns, OtherAlw, Overseas, OtherDed, Absences, ot1, amt1, ot2, amt2, ot3, amt3, lateness, amt4, TaxDes, tax, NTaxDes, ntax FROM ModifyVariables WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query54, data1)
                variable_data = cursor.fetchall()
                length = len(variable_data)

                query55 = "SELECT Workingdays FROM employee WHERE EmployeeID = %s"
                cursor.execute(query55,data2)
                wdays = cursor.fetchall()
                for i in range(len(wdays)):
                    wdays = ''.join(wdays[i])

                query56 = "SELECT paysheet_gross From OriginalData WHERE EmployeeID = %s AND Month = %s"
                cursor.execute(query56, data1)
                pay_gross = cursor.fetchall()
                for i in range(len(pay_gross)):
                    pay_gross = ''.join(pay_gross[i])

                print("Before Salary 2")

                return render_template("salary2.html", basic=basic, falw=falw, otherded=otherded, ot=ot, disc=disc, nsf=nsf, oalw=oalw, tax=tax, med=med, tran=tran, ntax=ntax, edf=edf, arr=arr, att=att, eoy=eoy, loan=loan, car=car, leave=leave, slevy=slevy, spebns=spebns, late=late, edurel=edurel, speprobns=speprobns, nps=nps, medrel=medrel, payable=payable, ded=ded, net=net, cgross=cgross, pgross=pgross, iet=iet, netch=netch, cpaye=cpaye, ppaye=ppaye, paye=paye, ecsg=ecsg, ensf=ensf, elevy=elevy, absence=absence, eid=eid, fname=fname, lname=lname, pos=pos, month=month, year=year, pnet=pnet, piet=piet, pthes=pthes, ths=ths, plevy=plevy, slevypay = slevypay, netchar=netchar, prgf = prgf, gtax=gtax, vdata = variable_data, length = length, wdays=wdays, paygros = pay_gross)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")   
# ===================================================================================================================
    # Save To Database
    elif request.method == "POST" and request.form['action'] == 'save':
        
        print("IN SAVE")

        # Data Of Manually Input Values
        arrears1 = request.form["arr"]
        if arrears1 == "":
            arrears1 = 0
        else:
            arrears1 = arrears1
        
        localRef = request.form["lref"]
        if localRef == "":
            localRef = 0
        else:
            localRef = localRef

        fixedAlw1 = request.form["falw"]
        if fixedAlw1 == "":
            fixedAlw1 = 0
        else:
            fixedAlw1 = fixedAlw1

        discBns1 = request.form["dbns"]
        if discBns1 == "":
            discBns1 = 0
        else:
            discBns1 = discBns1

        attendance1 = request.form["atbns"]
        if attendance1 == "":
            attendance1 = 0
        else:
            attendance1 = attendance1

        transport1 = request.form["tran"]
        if transport1 == "":
            transport1 = 0
        else:
            transport1 = transport1

        sickRef = request.form["sref"]
        if sickRef == "":
            sickRef = 0
        else:
            sickRef = sickRef

        speBns1 = request.form["sbns"]
        if speBns1 == "":
            speBns1 = 0
        else:
            speBns1 = speBns1

        otherAlw1 = request.form["oalw"]
        if otherAlw1 == "":
            otherAlw1 = 0
        else:
            otherAlw1 = otherAlw1

        overseas1 = request.form["oseas"]
        if overseas1 == "":
            overseas1 = 0
        else:
            overseas1 = overseas1

        otherDed1 = request.form["oded"]
        if otherDed1 == "":
            otherDed1 = 0
        else:
            otherDed1 = otherDed1

        absence1 = request.form["abs"]
        if absence1 == "":
            absence1 = 0
        else:
            absence1 = absence1

        ot1 = request.form["hr1"]
        if ot1 == "":
            ot1 = 0
        else:
            ot1 = ot1

        amt1 = request.form["am1"]
        if amt1 == "":
            amt1 = 0
        else:
            amt1 = amt1
        
        ot2 = request.form["hr2"]
        if ot2 == "":
            ot2 = 0
        else:
            ot2 = ot2
        
        amt2 = request.form["am2"]
        if amt2 == "":
            amt2 = 0
        else:
            amt2 = amt2

        ot3 = request.form["hr3"]
        if ot3 == "":
            ot3 = 0
        else:
            ot3 = ot3

        amt3 = request.form["am3"]
        if amt3 == "":
            amt3 = 0
        else:
            amt3 = amt3

        lateness = request.form["hr4"]
        if lateness == "":
            lateness = 0
        else:
            lateness = lateness

        amt4 = request.form["am4"]
        if amt4 == "":
            amt4 = 0
        else:
            amt4 = amt4

        absence_hr = request.form["hr5"]
        if absence_hr == "":
            absence_hr = 0
        else:
            absence_hr = absence_hr

        absence = request.form["abs"]
        if absence == "":
            absence = 0
        else:
            absence = absence

        taxDes = request.form["txdes"]
        if taxDes == "":
            taxDes = " "
        else:
            taxDes = taxDes

        taxamt = request.form["amt1"]
        if taxamt == "":
            taxamt = 0
        else:
            taxamt = taxamt        
        
        ntaxDes = request.form["ntxdes"]
        if ntaxDes == "":
            ntaxDes = " "
        else:
            ntaxDes = ntaxDes
        
        ntaxamt = request.form["amt2"]
        if ntaxamt == "":
            ntaxamt = 0
        else:
            ntaxamt = ntaxamt

# ============================================================================================================================================================

        # basic = request.form["bsal"]
        # if basic == "":
        #     basic = 0

        fixedAlw = request.form["falw2"]
        if fixedAlw == "":
            fixedAlw = 0

        otherDed = request.form["oded2"]
        if otherDed == "":
            otherDed = 0

        overtime = request.form["ot2"]
        if overtime == "":
            overtime = 0

        discBns = request.form["dbns2"]
        if discBns == "":
            discBns = 0

        NSF = request.form["nsf"]
        if NSF == "":
            NSF = 0

        otherAlw = request.form["oalw2"]
        if otherAlw == "":
            otherAlw = 0

        tax = request.form["txdes2"]
        if tax == "":
            tax = 0

        medical = request.form["med2"]
        if medical == "":
            medical = 0

        transport = request.form["tran2"]
        if transport == "":
            transport = 0

        ntax = request.form["ntxdes2"]
        if ntax == "":
            ntax = 0

        edf = request.form["edf"]
        if edf == "":
            edf = 0

        arrears = request.form["arr2"]
        if arrears == "":
            arrears = 0

        attendance = request.form["atbns2"]
        if attendance == "":
            attendance = 0

        eoy = request.form["eoy"]
        if eoy == "":
            eoy = 0

        loan = request.form["lrep"]
        if loan == "":
            loan = 0

        car = request.form["car"]
        if car == "":
            car = 0

        leaveRef = request.form["lref2"]
        if leaveRef == "":
            leaveRef = 0

        paye = request.form["paye3"]
        if paye == "":
            paye = 0

        slevy = request.form["levy"]
        if slevy == "":
            slevy = 0

        speBns = request.form["spbonus2"]
        if speBns == "":
            speBns = 0

        lateness = request.form["late"]
        if lateness == "":
            lateness = 0

        educationRel = request.form["edu"]
        if educationRel == "":
            educationRel = 0

        SpeProBns = request.form["spbonus3"]
        if SpeProBns == "":
            SpeProBns = 0

        NPS = request.form["nps"]
        if NPS == "":
            NPS = 0

        medicalRel = request.form["mrel"]
        if medicalRel == "":
            medicalRel = 0

        Payable = request.form["pay"]
        if Payable == "":
            Payable = 0

        Deduction = request.form["ded"]
        if Deduction == "":
            Deduction = 0

        Net = request.form["npay"]
        if Net == "":
            Net = 0

        cgross = request.form["cgrs2"]
        if cgross == "":
            cgross = 0

        pgross = request.form["pgrs"]
        if pgross == "":
            pgross = 0

        iet = request.form["iet"]
        if iet == "":
            iet = 0

        netch = request.form["netch"]
        if netch == "":
            netch = 0

        cpaye = request.form["paye2"]
        if cpaye == "":
            cpaye = 0

        ppaye = request.form["ppaye"]
        if ppaye == "":
            ppaye = 0

        ecsg = request.form["nps2"]
        if ecsg == "":
            ecsg = 0

        ensf = request.form["nsf2"]
        if ensf == "":
            ensf = 0

        elevy = request.form["ivbt"]
        if elevy == "":
            elevy = 0

        prgf = request.form["prgf"]
        if prgf == "":
            prgf = 0

        pthes = request.form["ths2"]
        if pthes == "":
            pthes = 0

        thes = request.form["ths"]
        if thes == "":
            thes = 0

        netchar = request.form["netchar"]
        if netchar == "":
            netchar = 0

        clevy = request.form["clevy"]
        if clevy == "":
            clevy = 0

        plevy = request.form["plevy"]
        if plevy == "":
            plevy = 0

        slevypay = request.form["levypay"]
        if slevypay == "":
            slevypay = 0

        cgtax = request.form["gtax3"]
        if cgtax == "":
            cgtax = 0

        month = request.form["mon"]

        fname = request.form["fname"]

        eid = request.form["eid"]

        UNQ = month + " " + fname

        paysheet_gross = request.form["cgrs"]
        if paysheet_gross == "":
            paysheet_gross = 0

        NetPaysheet = request.form["pnet"]
        if NetPaysheet == "":
            NetPaysheet = 0

        overseas = request.form["oseas"]
        if overseas == "":
            overseas = 0



        # travel = request.form["tran"]
        otherAlw2 = int(otherAlw) + int(speBns) + int(SpeProBns)

        ded = int(Deduction) + int(slevy)
        netpay = int(Payable) - int(ded)
        bonus = int(otherAlw2) + int(fixedAlw) + int(discBns) + int(attendance) + int(overseas)
        NetPaysheet = netpay
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            print("Before Query Execute")
            month = request.form["mon"]
            fname = request.form["fname"]

            UNQ = month + " " + fname
            data3 = [UNQ]
            
            data1 = [eid]
            query1 = "SELECT salary From employee WHERE EmployeeID = %s"
            cursor.execute(query1, data1)
            basic = cursor.fetchall()
            for i in range(len(basic)):
                basic = ''.join(basic[i])

            print("Basic ", basic)

            query11 = "SELECT LockSal From salary WHERE UNQ = %s"
            cursor.execute(query11,data3)
            lockSal = cursor.fetchall()

            print(lockSal)
            print(len(lockSal))

            if len(lockSal) > 0:
                print("In If")
                for i in range(len(lockSal)):
                    print("In For ")
                    lockSal = ''.join(lockSal[i])
            else:
                print("In Else")
                lockSal = "No"

            if lockSal == "No":
                query1 = """UPDATE salary
                            SET 
                            BasicSalary = %s,
                            FixedAllow = %s,
                            OtherDeduction = %s,
                            Overtime = %s,
                            DiscBonus = %s,
                            NSFEmpee = %s,
                            OtherAllow = %s,
                            TaxableAllow = %s,
                            Medical = %s,
                            Transport = %s,
                            overseas = %s,
                            NTaxableAllow = %s,
                            EDF = %s,
                            Arrears = %s,
                            AttendanceBns = %s,
                            EOY = %s,
                            Loan = %s,
                            CarBenefit = %s,
                            LeaveRef = %s,
                            SLevy = %s,
                            SpecialBns = %s,
                            Lateness = %s,
                            EducationRel = %s,
                            SpeProBns = %s,
                            NPS = %s,
                            MedicalRel = %s,
                            Payable = %s,
                            Deduction = %s,
                            NetPay = %s,
                            NetPaysheet = %s,
                            paysheet_gross = %s,
                            CurrentGross = %s,
                            cGrossTax = %s,
                            PrevGross = %s,
                            IET = %s,
                            NetCh = %s,
                            CurrentPAYE = %s,
                            PrevPAYE = %s,
                            PAYE = %s,
                            eCSG = %s,
                            eNSF = %s,
                            eLevy = %s,
                            PRGF = %s,
                            PrevThreshold = %s,
                            Threshold = %s,
                            netchar = %s,
                            CurrentSLevy = %s,
                            PrevSLevy = %s,
                            slevyPay = %s,
                            Absences = %s
                            WHERE 
                            UNQ = %s;"""
                data1 = [basic ,fixedAlw, otherDed, overtime, discBns, NSF, otherAlw2, tax, medical, transport, overseas, ntax, edf, arrears, attendance, eoy, loan, car, leaveRef, slevy, speBns, lateness, educationRel, SpeProBns, NPS, medicalRel, Payable, Deduction, Net, NetPaysheet, paysheet_gross, cgross, cgtax, pgross, iet, netch, cpaye, ppaye, paye, ecsg, ensf, elevy, prgf, pthes, thes, netchar, clevy , plevy, slevypay, absence, UNQ ]
                cursor.execute(query1, data1)
                print("Database Updated Successfully")

                
                query2 = """ UPDATE payslip
                SET
                TravelAlw = %s,
                Bonus = %s,
                Gross = %s,
                PAYE = %s,
                NPF = %s,
                NSF = %s,
                SLevy = %s,
                Deduction = %s,
                NetPay = %s,
                Payable = %s,
                NetPayAcc = %s,
                eNPF = %s,
                eNSF = %s,
                eLevy = %s,
                ePRGF = %s
                WHERE
                UNQ = %s;"""
                
                data2 = [transport, bonus, Payable, paye, NPS, NSF, slevy, ded, netpay, netpay, netpay, ecsg, ensf, elevy, prgf, UNQ ]
                cursor.execute(query2, data2)
                print("update salary complete")
                
                query3 = """ UPDATE payecsv
                SET
                Emoluments = %s,
                PAYE = %s,
                SLevy = %s,
                EmolumentsNet = %s
                WHERE
                UNQ = %s;
                """
                emoluments = int(basic) + int(arrears) + int(overseas) + int(otherAlw) + int(car) + int(overtime) + int(eoy) + int(leaveRef) + int(fixedAlw) + int(discBns) + int(SpeProBns) + int(speBns) 
                data3 = [emoluments, paye, slevypay, emoluments, UNQ]
                cursor.execute(query3, data3)
                print("UPDATE PAYE Query Successfully")

                query5 = "SELECT EmployeeID FROM ModifyVariables WHERE UNQ = %s "
                data5 = [UNQ]
                cursor.execute(query5,data5)
                emp_id = cursor.fetchall()
                
                query6 = """UPDATE prgfcsv
                SET
                Basic = %s,
                Allowance = %s,
                Commission = %s,
                TotalRem = %s,
                PRGF = %s
                WHERE
                UNQ = %s
                ;"""

                totalRem = int(basic) + int(bonus)
                data6 = [basic, bonus, 0, totalRem, prgf, UNQ]
                cursor.execute(query6, data6)
                query7 = """UPDATE cnpcsv
                SET 
                Basic = %s
                WHERE
                UNQ = %s
                """
                data7 = [basic, UNQ]
                cursor.execute(query7,data7)

                if emp_id == []:
                    insert_query = """INSERT INTO ModifyVariables(
                        EmployeeID,
                        Arrears,
                        LocalRef,
                        FixedAllowance,
                        DiscBns,
                        AttBns,
                        Transport,
                        SickRef,
                        SpeBns,
                        OtherAlw,
                        Overseas,
                        OtherDed,
                        Absences,
                        ot1,
                        amt1,
                        ot2,
                        amt2,
                        ot3,
                        amt3,
                        lateness,
                        amt4,
                        absenceDays,
                        amt5,
                        TaxDes,
                        tax,
                        NTaxDes,
                        ntax,
                        Month,
                        UNQ
                        )
                        VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                        );"""
                    data4 = [eid, arrears1, localRef, fixedAlw1, discBns1, attendance1, transport1, sickRef, speBns1, otherAlw1, overseas1, otherDed1, absence,  ot1, amt1, ot2, amt2, ot3, amt3, lateness, amt4, absence_hr , absence  , taxDes, taxamt, ntaxDes, ntaxamt, month, UNQ]
                    cursor.execute(insert_query, data4)

                    print("Insert Modify Variables")
                else:
                    update_query = """UPDATE ModifyVariables
                    SET
                    Arrears = %s,
                    LocalRef = %s,
                    FixedAllowance = %s,
                    DiscBns = %s,
                    AttBns = %s,
                    Transport = %s,
                    SickRef = %s,
                    SpeBns = %s,
                    OtherAlw = %s,
                    Overseas = %s,
                    OtherDed = %s,
                    Absences = %s,
                    ot1 = %s,
                    amt1 = %s,
                    ot2 = %s,
                    amt2 = %s,
                    ot3 = %s,
                    amt3 = %s,
                    lateness = %s,
                    amt4 = %s,
                    absenceDays = %s,
                    amt5 = %s,
                    TaxDes = %s,
                    tax = %s,
                    NTaxDes = %s,
                    ntax = %s
                    WHERE
                    UNQ = %s
                    ;"""
                    data4 = [arrears1, localRef, fixedAlw1, discBns1, attendance1, transport1, sickRef, speBns1, otherAlw1, overseas1, otherDed1, absence, ot1, amt1, ot2, amt2, ot3, amt3, lateness, amt4, absence_hr, absence, taxDes, taxamt, ntaxDes, ntaxamt, UNQ]
                    cursor.execute(update_query, data4)

                    print("Modify ModifyVariables")

                msg = "Salary Modified Successfully"
            else:
                msg = "Salary Already Locked"

            query15 = "SELECT Basic FROM cnpcsv WHERE month = %s"
            data8 = [month]
            cursor.execute(query15, data8)
            basic_sal = cursor.fetchall()

            temp1 = []
            temp2 = []
            for i in range(len(basic_sal)):
                temp1 = ''.join(basic_sal[i])
                temp2.append(temp1)
            total = 0
            for i in range(len(temp2)):
                total = int(total) + int(temp2[i]) 

            print("Total : ", total)
            cnp = int(total) * 0.015
            update_cnp = """UPDATE cnpcsv
            SET 
            totalRem = %s,
            CNP = %s
            WHERE
            month = %s;"""
            data9 = [total, cnp, month]

            cursor.execute(update_cnp, data9)
            return render_template("salary.html", msg=msg)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("salary.html")

@app.route("/leave", methods=["GET" , "POST", "PUT"])
def leave():
    # global connection
    if request.method == 'POST':
        eid = request.form['eid']
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True) 

            # query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'employee'"
            # cursor.execute(query1)
            # column_name = cursor.fetchall()

            query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'LeaveData' AND ORDINAL_POSITION BETWEEN 3 AND 5;"
            cursor.execute(query1)
            column_name = cursor.fetchall()
            heading_data = []
            data = []
            print(len(column_name))
            for i in range(len(column_name)):
                print("i : " , i)
                # print("j : ", j)
                data = ''.join(column_name[i])
                print("Data :" + data)
                heading_data.append(data)
            
            print(column_name)
            print(heading_data)

            query2 = f"SELECT Date, LeaveType, LeaveDays FROM LeaveData;"
            cursor.execute(query2)
            table_data = cursor.fetchall()

            print(table_data)

            
            print(eid)
            query3 = f"SELECT Localleave, Sickleave FROM employee WHERE EmployeeID = '{eid}'"
            print(query3)
            cursor.execute(query3)
            leaves = cursor.fetchall()
            print(leaves)
            
            # leave_data = []
            # for i in range(len(leaves)):
            #     print("i : " , i)
            #     # print("j : ", j)
            #     data2 = ''.join(leaves[i])
            #     print("Data2 :" + data2)
            #     leave_data.append(data2)
            # print(leave_data[0])
            # print(leaves[0][0])

            query4 = f"SELECT EmployeeID, FirstName, LastName, Position FROM employee WHERE EmployeeID = '{eid}'"
            cursor.execute(query4)
            personal_data = cursor.fetchall()
            print(personal_data)
            print(personal_data[0][0])

            return render_template("leave.html", heading = heading_data, data = table_data, leaves = leaves, eid=eid,personal = personal_data )
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    print("Before")
    return render_template("leave.html")

@app.route("/lock_salary", methods=["GET" , "POST"])
def lock_salary():
    if request.method == "POST":
        mon = request.form["month"]
        year = request.form["year"]
        
        print(mon)
        print(year)
        mon1 = mon.lower()
        print(mon)

        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            
            query = """
            UPDATE salary
            SET
            LockSal = %s
            WHERE
            Month = %s;
            """
            data = ['Yes', mon1]

            cursor.execute(query, data)
            print("Update Query Execute Successfully")
            
            msg = "Locked Salary Of " + mon + " - " + year
            return render_template("lock-salary.html", msg=msg)

        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

        
    return render_template("lock-salary.html")

@app.route("/process_salary", methods=["GET" , "POST"])
def process_salary():
    # global connection
    if request.method == "POST":
        eid = request.form["eid"]
        month = request.form["mon"]
        # print(month)
        year = request.form["year"]
        id = 0
        month = month.lower()
        # print(month)
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            if eid != "ALL":
                print("In If")
                
                id = 0
                month = month.lower()
                data = [eid]
                # print(month)
                if month == "January" or month=="january":
                    print("In Jan")

                    current_date = "2022-"+"01-"+"01"
                    
                    id = 1
                elif month == "February" or month=="february":
                    print("In Feb")
                    
                    current_date = "2022-"+"02-"+"01"
                    id = 2
                elif month == "March" or month=="march":
                    print("In Mar")
                    
                    current_date = "2022-"+"03-"+"01"
                    id = 3
                elif month == "April" or month=="april":
                    print("In Apr")
                    
                    current_date = "2022-"+"04-"+"01"
                    id = 4
                elif month == "May" or month=="may":
                    print("In May")
                    
                    current_date = "2022-"+"05-"+"01"
                    id = 5
                elif month == "June" or month=="june":
                    print("In Jun")
                    
                    current_date = "2022-"+"06-"+"01"
                    id = 6
                elif month == "July" or month=="july":
                    print("In Jul")
                    
                    current_date = "2022-"+"07-"+"01"
                    id = 7
                elif month == "August" or month=="august":
                    print("In Aug")
                    
                    current_date = "2022-"+"08-"+"01"
                    id = 8
                elif month == "September" or month=="september":
                    print("In Sep")
                    
                    current_date = "2022-"+"09-"+"01"
                    id = 9
                elif month == "October" or month=="october":
                    print("In Oct")
                    
                    current_date = "2022-"+"10-"+"01"
                    id = 10
                elif month == "November" or month=="november":
                    print("In Nov")
                    
                    current_date = "2022-"+"11-"+"01"
                    id = 11
                elif month == "December" or month=="december":
                    print("In Dec")
                    
                    current_date = "2022-"+"12-"+"01"
                    id = 12
                else:  
                    print("In Else")
                    msg = "Enter Month Correctly"
                    return render_template("process.html", msg = msg)
                
                mid = id-1
                if mid == 0:
                    mid = 12
                
                # print(calendar.month_name[id])
                month2 = calendar.month_name[mid]
                month2 = month2.lower()

                query = "SELECT Carbenefit, salary, Fixedallow, Travelallow, EDF, Educationrel, Medicalrel, medical, Specialbonus FROM employee WHERE EmployeeID = %s"
                
                cursor.execute(query, data)
                emp_data = cursor.fetchall()

                # print(emp_data)
                # print(emp_data[0][0])
                # print(emp_data[0][1])

                car = int(emp_data[0][0])                
                tbasic = int(emp_data[0][1])
                fixAllow = int(emp_data[0][2])
                trans = int(emp_data[0][3])
                edf = int(emp_data[0][4])
                education = int(emp_data[0][5])
                Medicalrel = int(emp_data[0][6])
                # medical = int(emp_data2[7])
                medical = 0
                SpeProBns = int(emp_data[0][8])

                # lwork = emp_data2[10]
                # print(lwork)

                data2 = [eid,month2]
                # print(month2)

                query_month = "SELECT MONTH(Lastwork) AS Month FROM employee WHERE EmployeeID= %s"
                cursor.execute(query_month, data)
                emp_month = cursor.fetchall()
                
                last_mon = emp_month[0][0]
                

                query_year = "SELECT YEAR(Lastwork) AS Year FROM employee WHERE EmployeeID= %s"
                cursor.execute(query_year, data)
                emp_year = cursor.fetchall()

                last_year = emp_year[0][0]

                # if mon == 0:
                #     mon = id
                # if check_date == "11" or get_date > check_date :
                    # print("In If")

                    # query4 = "SELECT hire, position, NICno FROM employee WHERE EmployeeID = %s"
                    # cursor.execute(query4,data)
                    
                msg = "Employee Not Working"

                query1 = "SELECT FirstName FROM employee WHERE EmployeeID = %s"
                cursor.execute(query1,data)
                fname = cursor.fetchall()
                for i in range(len(fname)):
                    fname = ''.join(fname[i])

                UNQ = month + " " + fname
                data3 = [UNQ]

                hire_date = "SELECT hire FROM employee WHERE EmployeeID= %s"
                cursor.execute(hire_date, data)
                hire_date_emp = cursor.fetchall()
                
                print(hire_date_emp)
                hire_dt = str(hire_date_emp[0][0])

                if (int(last_year) >= int(year) or (last_year == 1 and last_mon == 1)) and (hire_dt < current_date):
                    print("Year Is Correct")
                    if int(last_mon) >= int(id) or (last_year == 1 and last_mon == 1):
                        print("In Start Process")

                        query2 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
                        cursor.execute(query2,data)
                        lname = cursor.fetchall()
                        for i in range(len(lname)):
                            lname = ''.join(lname[i])

                        query3 = "SELECT cGrossTax FROM salary WHERE EmployeeID= %s AND Month = %s"
                        cursor.execute(query3,data2)
                        prevGross = cursor.fetchall()
                        for i in range(len(prevGross)):
                            if prevGross != None:
                                prevGross = ''.join(prevGross[i])
                            else:
                                prevGross = 0
                        if prevGross != 0:
                            prevGross = ''.join(map(str,prevGross))
                            

                        query4 = "SELECT IET FROM salary WHERE EmployeeID= %s AND Month = %s"
                        cursor.execute(query4,data2)
                        piet = cursor.fetchall()
                        for i in range(len(piet)):
                            if piet != None:
                                piet = ''.join(piet[i])
                            else:
                                piet = 0
                        if piet != 0:
                            piet = ''.join(map(str,piet))

                        query5 = "SELECT CurrentPAYE FROM salary WHERE EmployeeID= %s AND Month = %s"
                        cursor.execute(query5,data2)
                        ppaye = cursor.fetchall()
                        # print(ppaye)
                        for i in range(len(ppaye)):
                            if ppaye != None:
                                ppaye = ''.join(ppaye[i])
                                print(ppaye)
                            else:
                                ppaye = 0
                        if ppaye != 0:
                            ppaye = ''.join(map(str,ppaye))

                        query6 = "SELECT Threshold FROM salary WHERE EmployeeID= %s AND Month = %s"
                        cursor.execute(query6,data2)
                        pths = cursor.fetchall()
                        for i in range(len(pths)):
                            if pths != None:
                                pths = ''.join(pths[i])
                            else:
                                pths = 0
                        if pths != 0:
                            pths = ''.join(map(str,pths))

                        query7 = "SELECT CurrentSLevy FROM salary WHERE EmployeeID= %s AND Month = %s"
                        cursor.execute(query7,data2)
                        plevy = cursor.fetchall()
                        print("Before For Loop", plevy)
                        print(len(plevy))

                        if len(plevy) > 0:
                            print("In If")
                            for i in range(len(plevy)):
                                print("In For ")
                                plevy = ''.join(plevy[i])
                        else:
                            print("In Else")
                            plevy = 0    


                        # for i in range(len(plevy)):
                        #     print("In For")
                        #     if plevy != None:
                        #         print("In if1")
                        #         plevy = ''.join(plevy[i])
                        #     else:
                        #         print("In Else")
                        #         plevy = 0
                        
                        # if plevy != 0:
                        #     print("In if2")
                        #     plevy = ''.join(map(str,plevy))
                        
                        print("plevy", plevy)

                        query8 = "SELECT hire FROM employee WHERE EmployeeID = %s"
                        cursor.execute(query8,data)
                        hire = cursor.fetchall()
                        
                        hire = hire[0][0] 
                        hire = str(hire)
                        # print(hire)
                        # print(str(hire))
                        # print(type(str(hire)))
                        # if hire != None:
                        #     for i in range(len(hire)):
                        #         hire = ''.join(hire[i])
                        #     hire = ''.join(map(str,hire))
                        # else:
                        #     hire = 0                    

                        query9 = "SELECT position FROM employee WHERE EmployeeID = %s"
                        cursor.execute(query9,data)
                        pos = cursor.fetchall()
                        for i in range(len(pos)):
                            if pos != None:
                                pos = ''.join(pos[i])
                            else:
                                pos = " "
                        if pos != 0:
                            pos = ''.join(map(str,pos))
                        # print(pos)
                        

                        query10 = "SELECT NICno FROM employee WHERE EmployeeID = %s"
                        cursor.execute(query10,data)
                        nic = cursor.fetchall()
                        # print(nic)
                        for i in range(len(nic)):
                            if nic[0][0] != None:
                                nic = ''.join(nic[i])
                            else:
                                nic = " "
                        if nic != 0:
                            nic = ''.join(map(str,nic))
                        
                        UNQ = month + " " + fname
                        data3 = [UNQ]
                        
                        # query11 = "SELECT LockSal From salary WHERE UNQ = %s"
                        # cursor.execute(query11,data3)
                        # lockSal = cursor.fetchall()

                        # print(lockSal)
                        # print(len(lockSal))

                        # if len(lockSal) > 0:
                        #     print("In If")
                        #     for i in range(len(lockSal)):
                        #         print("In For ")
                        #         lockSal = ''.join(lockSal[i])
                        # else:
                        #     print("In Else")
                        #     lockSal = "No"

                        # query12 = "SELECT working FROM employee WHERE EmployeeID = %s"
                        # cursor.execute(query12, data)
                        # working = cursor.fetchall()

                        # if len(working) > 0:
                        #     print("In If")
                        #     for i in range(len(working)):
                        #         print("In For ")
                        #         working = ''.join(working[i])
                        # else:
                        #     print("In Else")
                        #     working = "Yes"                
                        
                        flname = lname + " " + fname

                        # Values We Don't Get
                        ot = 0
                        otherAllow = 0
                        arrears = 0
                        eoy = 0
                        leave = 0
                        speBns = 0
                        discBns = 0
                        tax = 0
                        ntax = 0
                        attBns = 0
                        overseas = tax + ntax

                        loan = 0
                        lateness = 0
                        otherDed = 0
                        ab = 0

                        # Previous Data
                        # print(type(prevGross))
                        # print(prevGross)
                        if prevGross == "":
                            prevGross = 0
                        else:
                            prevGross = int(prevGross)

                        if piet == "":
                            piet = 0
                        else:
                            piet = int(piet)
                        
                        if ppaye == "":
                            ppaye = 0
                        else:
                            ppaye = int(ppaye)
                        
                        if pths == "":
                            pths = 0
                        else:
                            pths = int(pths)
                        # print(pths)
                        if plevy == "":
                            plevy = 0
                        else:
                            plevy = int(plevy)
                
                        basic = int(tbasic) - int(ab)
                        # Calculations
                        payable = basic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns
                        bonus = speBns + SpeProBns + otherAllow + fixAllow + discBns + attBns

                        pay_gross = tbasic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns

                        # For Overseas Amount
                        if overseas > 0:
                            ntax = round(int(basic) * 0.06)
                            tax = round(int(overseas) - int(ntax))
                        else:
                            ntax = 0
                            tax = 0

                        if trans > 20000:
                            transTax = trans - 20000
                            ntransTax = trans - transTax
                        else:
                            transTax = 0
                            ntransTax = 0

                        # Current Gross
                        cgross = basic + ot + otherAllow + trans + arrears + eoy + leave + discBns + fixAllow + tax + SpeProBns + attBns + car

                        grossTax = basic + ot + transTax +otherAllow + arrears + eoy + leave + discBns + fixAllow  + tax + SpeProBns + attBns + car

                        # print("prev Gross " , prevGross)
                        # print("Curr Gross " , cgross)
                        gross = prevGross + grossTax  # Total Gross
                        # print("gross" , gross)
                        medf = round(int(edf) / 13)
                        ciet = round(( int(edf) + int(Medicalrel) + int(education)) / 13)
                        
                        iet = int(ciet) + int(piet)
                        # print("ciet" , ciet)
                        # print("piet", piet)
                        # print("iet", iet)

                        netch = gross - iet

                        # print("netch" , netch)
                        if netch < 0:
                            netch = 0
                        else:
                            netch = netch

                        if int(basic) > 50000:
                            nps = round(basic * 0.03)
                            # cpaye =  round(netch * 0.15)
                            enps = round(basic * 0.06)
                        else:
                            nps = round(basic * 0.015)
                            # cpaye = round(netch * 0.1)
                            enps = round(basic * 0.03)

                        check = int(basic) + int(otherAllow) - int(medf)
                        if check < 53846:
                            cpaye = round(netch* 0.1)
                        elif check >= 53846 and check < 75000:
                            cpaye = round(netch* 0.125)
                        else:
                            cpaye = round(netch* 0.15)

                        if cpaye < 0:
                            cpaye = 0
                        else:
                            cpaye = int(cpaye)
                        
                        if ppaye < 0:
                            ppaye =0
                        else:
                            ppaye = int(ppaye)

                        # print("cpaye", cpaye)
                        # print("ppaye", ppaye)
                        paye = int(cpaye) - int(ppaye)
                        # print("paye", paye)
                        if paye < 0:
                            paye =0
                        else:
                            paye = int(paye)

                        nsf = int(basic * 0.01)

                        if nsf > 214:
                            nsf = 214
                        else:
                            nsf = int(nsf)

                        temp = int(cgross) * 13
                        slevy = 0
                        tths = round(3000000/13)
                        ths = int(pths) + int(tths)
                        # print(ths)
                        netchar = int(gross) - int(iet) - int(ths)
                        print("gross", gross)
                        print("iet", iet)
                        print("ths", ths)
                        if netchar < 0 :
                            netchar = 0
                        else:
                            netchar = netchar
                        print("netchar", netchar)
                        print("grossTax", grossTax)

                        if int(temp) > 3000000:
                            slevy1 = round(netchar * 0.25)
                            slevy2 = round(gross * 0.1)
                            print("slevy1", slevy1)
                            print("slevy2", slevy2)
                            if slevy1 > slevy2:
                                slevy = int(slevy2)
                            else:
                                slevy = int(slevy1)
                        else:
                            slevy = 0
                        print("slevy", slevy)
                        ensf = round(basic * 0.025)
                        if ensf > 536:
                            ensf = 536
                        else:
                            ensf = round(ensf)
                        levy = round(int(basic) * 0.015)
                        deduction = int(loan) + int(paye) + int(lateness) + int(nps) + int(otherDed) + int(nsf) + int(medical)
                        net = int(payable) - int(deduction)
                        # print(slevy)
                        NetPaysheet = int(net) - int(slevy)
                        slevypay = slevy - plevy
                        print("slevypay", slevypay)
                        otherAllow2 = int(otherAllow) + int(speBns) + int(SpeProBns)
                        
                        tax = int(tax) + int(transTax)
                        ntax = int(ntax) + int(ntransTax)
                        # Payslip Calculation

                        paygross = int(basic) + int(trans) + int(bonus)

                        totalDeduction = int(paye) + int(nps) + int(nsf)

                        netpay = paygross - totalDeduction
                        # eprgf = 0
                        if basic < 200000:
                            eprgf = round((int(basic) + int(bonus)) * 0.035) # + commission
                        else:
                            eprgf = 0

                        get_original  = "SELECT EmployeeID FROM OriginalData WHERE UNQ = %s"
                        cursor.execute(get_original, data3)
                        original_id = cursor.fetchall()

                        if original_id == []:
                            insert_query = """
                                INSERT INTO OriginalData(
                                EmployeeID,
                                EmployeeName,
                                BasicSalary,
                                FixedAllow,
                                OtherDeduction,
                                Overtime,
                                DiscBonus,
                                NSFEmpee,
                                OtherAllow,
                                TaxableAllow,
                                Medical,
                                Transport,
                                overseas,
                                NTaxableAllow,
                                EDF,
                                Arrears,
                                AttendanceBns,
                                EOY,
                                Loan,
                                CarBenefit,
                                LeaveRef,
                                SLevy,
                                SpecialBns,
                                Lateness,
                                EducationRel,                    
                                SpeProBns,
                                NPS,
                                MedicalRel,
                                Payable,
                                Deduction,
                                NetPay,
                                NetPaysheet,
                                paysheet_gross,
                                CurrentGross,
                                cGrossTax,
                                PrevGross,
                                PrevIET,
                                IET,
                                NetCh,
                                CurrentPAYE,
                                PrevPAYE,
                                PAYE,
                                eCSG,
                                eNSF,
                                eLevy,
                                PRGF,
                                PrevThreshold,
                                Threshold,
                                netchar,
                                CurrentSLevy,
                                PrevSLevy,
                                slevyPay,
                                Absences,
                                Month,
                                Year,
                                UNQ,
                                LockSal
                                )
                                VALUES(
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s
                                );
                                """
                            data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, pay_gross, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, month, year, UNQ, 'No']
                            cursor.execute(insert_query, data1)
                            print("Original Data Insert Query Executed")
                        else:
                            update_original = """UPDATE OriginalData
                                            SET
                                            EmployeeID = %s,
                                            EmployeeName = %s,
                                            BasicSalary = %s,
                                            FixedAllow = %s,
                                            OtherDeduction = %s,
                                            Overtime = %s,
                                            DiscBonus = %s,
                                            NSFEmpee = %s,
                                            OtherAllow = %s,
                                            TaxableAllow = %s,
                                            Medical = %s,
                                            Transport = %s,
                                            overseas = %s,
                                            NTaxableAllow = %s,
                                            EDF = %s,
                                            Arrears = %s,
                                            AttendanceBns = %s,
                                            EOY = %s,
                                            Loan = %s,
                                            CarBenefit = %s,
                                            LeaveRef = %s,
                                            SLevy = %s,
                                            SpecialBns = %s,
                                            Lateness = %s,
                                            EducationRel = %s,
                                            SpeProBns = %s,
                                            NPS = %s,
                                            MedicalRel = %s,
                                            Payable = %s,
                                            Deduction = %s,
                                            NetPay = %s,
                                            NetPaysheet = %s,
                                            paysheet_gross = %s,
                                            CurrentGross = %s,
                                            cGrossTax = %s,
                                            PrevGross = %s,
                                            PrevIET = %s,
                                            IET = %s,
                                            NetCh = %s,
                                            CurrentPAYE = %s,
                                            PrevPAYE = %s,
                                            PAYE = %s,
                                            eCSG = %s,
                                            eNSF = %s,
                                            eLevy = %s,
                                            PRGF = %s,
                                            PrevThreshold = %s,
                                            Threshold = %s,
                                            netchar = %s,
                                            CurrentSLevy = %s,
                                            PrevSLevy = %s,
                                            slevyPay = %s,
                                            Absences = %s
                                            WHERE 
                                            UNQ = %s;
                                            """
                            data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, pay_gross, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, UNQ]
                            cursor.execute(update_original, data1)
                            print("Update Original Query Executed")

                        get_salary  = "SELECT EmployeeID FROM salary WHERE UNQ = %s"
                        cursor.execute(get_salary, data3)
                        salary_id = cursor.fetchall()

                        if salary_id == []:
                            insert_query2 = """
                                INSERT INTO salary(
                                EmployeeID,
                                EmployeeName,
                                BasicSalary,
                                FixedAllow,
                                OtherDeduction,
                                Overtime,
                                DiscBonus,
                                NSFEmpee,
                                OtherAllow,
                                TaxableAllow,
                                Medical,
                                Transport,
                                overseas,
                                NTaxableAllow,
                                EDF,
                                Arrears,
                                AttendanceBns,
                                EOY,
                                Loan,
                                CarBenefit,
                                LeaveRef,
                                SLevy,
                                SpecialBns,
                                Lateness,
                                EducationRel,                    
                                SpeProBns,
                                NPS,
                                MedicalRel,
                                Payable,
                                Deduction,
                                NetPay,
                                NetPaysheet,
                                paysheet_gross,
                                CurrentGross,
                                cGrossTax,
                                PrevGross,
                                PrevIET,
                                IET,
                                NetCh,
                                CurrentPAYE,
                                PrevPAYE,
                                PAYE,
                                eCSG,
                                eNSF,
                                eLevy,
                                PRGF,
                                PrevThreshold,
                                Threshold,
                                netchar,
                                CurrentSLevy,
                                PrevSLevy,
                                slevyPay,
                                Absences,
                                Month,
                                Year,
                                UNQ,
                                LockSal,
                                ProcSal
                                )

                                VALUES(
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s
                                );
                                """
                            data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, pay_gross, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, month, year, UNQ, 'No', 'Yes']
                            cursor.execute(insert_query2, data1)
                            print("Salary Insert Query Executed")
                        else:
                            update_salary = """UPDATE salary
                                            SET
                                            EmployeeID = %s,
                                            EmployeeName = %s,
                                            BasicSalary = %s,
                                            FixedAllow = %s,
                                            OtherDeduction = %s,
                                            Overtime = %s,
                                            DiscBonus = %s,
                                            NSFEmpee = %s,
                                            OtherAllow = %s,
                                            TaxableAllow = %s,
                                            Medical = %s,
                                            Transport = %s,
                                            overseas = %s,
                                            NTaxableAllow = %s,
                                            EDF = %s,
                                            Arrears = %s,
                                            AttendanceBns = %s,
                                            EOY = %s,
                                            Loan = %s,
                                            CarBenefit = %s,
                                            LeaveRef = %s,
                                            SLevy = %s,
                                            SpecialBns = %s,
                                            Lateness = %s,
                                            EducationRel = %s,
                                            SpeProBns = %s,
                                            NPS = %s,
                                            MedicalRel = %s,
                                            Payable = %s,
                                            Deduction = %s,
                                            NetPay = %s,
                                            NetPaysheet = %s,
                                            paysheet_gross = %s,
                                            CurrentGross = %s,
                                            cGrossTax = %s,
                                            PrevGross = %s,
                                            PrevIET = %s,
                                            IET = %s,
                                            NetCh = %s,
                                            CurrentPAYE = %s,
                                            PrevPAYE = %s,
                                            PAYE = %s,
                                            eCSG = %s,
                                            eNSF = %s,
                                            eLevy = %s,
                                            PRGF = %s,
                                            PrevThreshold = %s,
                                            Threshold = %s,
                                            netchar = %s,
                                            CurrentSLevy = %s,
                                            PrevSLevy = %s,
                                            slevyPay = %s,
                                            Absences = %s
                                            WHERE
                                            UNQ = %s
                                            """
                            
                            data2 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, pay_gross, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, UNQ]
                            cursor.execute(update_salary, data2)
                            print("Update Salary Query Executed")

                        get_payslip  = "SELECT EmpName FROM payslip WHERE UNQ = %s"
                        cursor.execute(get_payslip, data3)
                        payslip_id = cursor.fetchall()

                        if payslip_id == []:
                            query = """INSERT INTO payslip(
                                        JoinDate,
                                        Company,
                                        EmpName,
                                        Position,
                                        NIC,
                                        BasicSalary,
                                        TravelAlw,
                                        Bonus,
                                        Gross,
                                        PAYE,
                                        NPF,
                                        NSF,
                                        SLevy,
                                        Deduction,
                                        NetPay,
                                        Payable,
                                        NetPayAcc,
                                        eNPF,
                                        eNSF,
                                        eLevy,
                                        ePRGF,
                                        month,
                                        year,
                                        UNQ
                                        )
                                        VALUES(
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s
                                        );
                                        """
                                
                            payslip_data = [hire, "Demo" , flname, pos, nic, basic, trans, bonus, paygross, paye, nps, nsf, slevypay , totalDeduction, netpay,netpay, netpay, enps, ensf, levy, eprgf, month, year, UNQ ]
                            cursor.execute(query, payslip_data)
                            print("Payslip Insert Query Executed")
                        else:
                            update_payslip = """UPDATE payslip
                                    SET
                                    EmpName = %s,
                                    Position = %s,
                                    NIC = %s,
                                    BasicSalary = %s,
                                    TravelAlw = %s,
                                    Bonus = %s,
                                    Gross = %s,
                                    PAYE = %s,
                                    NPF = %s,
                                    NSF = %s,
                                    SLevy = %s,
                                    Deduction = %s,
                                    NetPay = %s,
                                    Payable = %s,
                                    NetPayAcc = %s,
                                    eNPF = %s,
                                    eNSF = %s,
                                    eLevy = %s,
                                    ePRGF = %s,
                                    month = %s
                                    WHERE
                                    UNQ = %s;
                                    """
                            data_payslip = [flname, pos, nic, basic, trans, bonus, paygross, paye, nps, nsf, slevypay, totalDeduction, netpay, netpay, netpay,  enps, ensf, levy, eprgf, month, UNQ]
                            cursor.execute(update_payslip, data_payslip)
                            print("Update Payslip Query Executed")
                        # msg = "Processing Complete"

                        query14 = "SELECT NICno FROM employee WHERE EmployeeID = %s"
                        cursor.execute(query14, data)
                        nic = cursor.fetchall()
                        if nic[0][0] == "":
                            nic = " "
                        else:
                            for i in range(len(nic)):
                                nic = ''.join(nic[i])

                        emolument = int(basic) + int(arrears) + int(overseas) + int(otherAllow) + int(car) + int(ot) + int(eoy) + int(leave) + int(fixAllow) + int(discBns) + int(SpeProBns) + int(speBns) 

                        get_payecsv  = "SELECT EmployeeID FROM payecsv WHERE UNQ = %s"
                        cursor.execute(get_payecsv, data3)
                        payecsv_id = cursor.fetchall()

                        if payecsv_id == []:
                            print("Insert")
                            paye_query = """ INSERT INTO payecsv(
                                            EmployeeID,
                                            LastName,
                                            FirstName,
                                            Emoluments,
                                            PAYE,
                                            working,
                                            SLevy,
                                            EmolumentsNet,
                                            month,
                                            UNQ
                                            )
                                            VALUES(
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s
                                            );"""
                            data4 = [nic, lname, fname, emolument, paye, 'Yes', slevypay, emolument, month, UNQ]

                            cursor.execute(paye_query, data4)
                            print("PAYE Query Executed")
                        else:
                            print("Update")
                            update_payecsv = """UPDATE payecsv
                                            SET
                                            EmployeeID = %s,
                                            LastName = %s,
                                            FirstName = %s,
                                            Emoluments = %s,
                                            PAYE = %s,
                                            SLevy = %s,
                                            EmolumentsNet = %s
                                            WHERE
                                            UNQ = %s;
                                            """

                            data4 = [nic, lname, fname, emolument, paye, slevypay, emolument, UNQ]
                            cursor.execute(update_payecsv, data4)
                            print("Update PAYE CSV Query Executed")

                        query12 = "SELECT NPS FROM employee WHERE EmployeeID = %s"
                        cursor.execute(query12, data)
                        pension = cursor.fetchall()
                        for i in range(len(pension)):
                            pension = ''.join(pension[i])

                        if pension == "Paid":
                            pension = "Yes"
                        else:
                            pension = "No"

                        query13 = "SELECT working FROM employee WHERE EmployeeID = %s"
                        cursor.execute(query13, data)
                        working = cursor.fetchall()
                        for i in range(len(working)):
                            working = ''.join(working[i])
                        
                        print("working ", working)

                        allowance = int(otherAllow) + int(fixAllow) + int(speBns) + int(SpeProBns) + int(discBns) + int(attBns)
                        commission = 0

                        totalRem = int(basic) + int(allowance)

                        get_prgfcsv  = "SELECT EmployeeID FROM prgfcsv WHERE UNQ = %s"
                        cursor.execute(get_prgfcsv, data3)
                        prgfcsv_id = cursor.fetchall()

                        if prgfcsv_id == []:
                            prgf_query = """INSERT INTO prgfcsv(
                                            EmployeeID,
                                            LastName,
                                            FirstName,
                                            Pension,
                                            Working,
                                            Hire,
                                            Basic,
                                            Allowance,
                                            Commission,
                                            TotalRem,
                                            PRGF,
                                            reason,
                                            month,
                                            UNQ
                                            )
                                            VALUES(
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s
                                            );"""
                            if basic < 200000:
                                data5 = [nic, lname, fname, "No", working, hire, basic, allowance, commission, totalRem, eprgf, " " , month, UNQ]
                            else:
                                data5 = [nic, lname, fname, "No", working, hire, basic, 0, 0, 0, 0, " " , month, UNQ]
                            
                            cursor.execute(prgf_query, data5)
                            print("PRGF Insert Query Executed")
                        
                        else:
                            update_prgf = """UPDATE prgfcsv
                                        SET
                                        EmployeeID = %s,
                                        LastName = %s,
                                        FirstName = %s,
                                        Basic = %s,
                                        Allowance = %s,
                                        Commission = %s,
                                        TotalRem = %s,
                                        PRGF = %s
                                        WHERE
                                        UNQ = %s;
                                        """
                            prgf_data = [eid, lname, fname, basic, allowance, commission, totalRem, eprgf, UNQ]

                            cursor.execute(update_prgf, prgf_data)
                            print("Update PRGF Complete")

                        get_cnpcsv  = "SELECT EmployeeID FROM cnpcsv WHERE UNQ = %s"
                        cursor.execute(get_cnpcsv, data3)
                        cnpcsv_id = cursor.fetchall()

                        if cnpcsv_id == []:
                            cnp_query = """INSERT INTO cnpcsv(
                                        EmployeeID,
                                        LastName,
                                        FirstName,
                                        Basic,
                                        Basic2,
                                        Season,
                                        Alphabet,
                                        Number,
                                        Working,
                                        Blank1,
                                        Blank2,
                                        month,
                                        UNQ
                                        )
                                        VALUES(
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s
                                        );"""
                            data6 = [nic, lname, fname, basic, basic, "S2", "M", "1", working, " ", " ", month, UNQ]

                            cursor.execute(cnp_query, data6)
                            print("CNP Insert Query Executed")

                        else:
                            update_cnp = """UPDATE cnpcsv
                                        SET
                                        EmployeeID = %s,
                                        LastName = %s,
                                        FirstName = %s,
                                        Basic = %s,
                                        Basic2 = %s
                                        WHERE
                                        UNQ = %s;
                                        """
                            cnp_data = [eid, lname, fname, basic, basic, UNQ]
                            cursor.execute(update_cnp, cnp_data)

                            print("Update CNP Complete")

                        get_contribution  = "SELECT EmployeeID FROM contribution WHERE UNQ = %s"
                        cursor.execute(get_contribution, data3)
                        contri_id = cursor.fetchall()

                        if contri_id == []:
                            insert_contri = """INSERT INTO contribution(
                                                EmployeeID,
                                                LastName,
                                                FirstName,
                                                IDCard,
                                                Salary,
                                                blank1,
                                                ecsg,
                                                elevy,
                                                ensf,
                                                prgf,
                                                csg,
                                                nsf,
                                                blank2,
                                                slevy,
                                                month,
                                                year,
                                                UNQ
                                                )
                                                VALUES(
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s
                                                );
                                                """
                            contri_data = [eid, lname, fname, nic, basic, " ", enps, levy, ensf, eprgf, nps, nsf, " ", slevypay, month, year, UNQ]
                            cursor.execute(insert_contri, contri_data)
                            print("Contribution Insert Query Executed")

                        else:
                            update_contri = """UPDATE contribution
                                            SET
                                            EmployeeID = %s,
                                            LastName = %s,
                                            FirstName = %s,
                                            Salary = %s,
                                            ecsg = %s,
                                            elevy = %s,
                                            ensf = %s,
                                            prgf = %s,
                                            csg = %s,
                                            nsf = %s,
                                            slevy = %s
                                            WHERE
                                            UNQ = %s;
                                            """
                            contri_data = [eid, lname, fname, basic, enps, levy, ensf, eprgf, nps, nsf, slevypay, UNQ]
                            cursor.execute(update_contri, contri_data)
                            print("Update Contribution Complete")

                        msg = "Re Processing Complete For " + flname + " "
                        print(msg)
                
                if msg == "Employee Not Working":
                    get_empid = "SELECT EmployeeID FROM salary WHERE UNQ = %s"
                    cursor.execute(get_empid, data3)
                    emp_id = cursor.fetchall()
                    msg = "Employee Not Working , Re Processing Complete"

                    if emp_id != []:
                        print("In Delete Employee")
                        delete_original = "DELETE FROM OriginalData WHERE UNQ = %s"
                        cursor.execute(delete_original,data3)
                        print("Delete From Original Data")

                        delete_salary = "DELETE FROM salary WHERE UNQ= %s"
                        cursor.execute(delete_salary,data3)
                        print("Delete From Salary Data")
                        
                        delete_payslip = "DELETE FROM payslip WHERE UNQ = %s"
                        cursor.execute(delete_payslip,data3)
                        print("Delete From Payslip Data")
                        
                        delete_paye = "DELETE FROM payecsv WHERE UNQ = %s"
                        cursor.execute(delete_paye,data3)
                        print("Delete From Payecsv Data")
                        
                        delete_prgf = "DELETE FROM prgfcsv WHERE UNQ = %s "
                        cursor.execute(delete_prgf,data3)
                        print("Delete From PRGF Data")
                        
                        delete_cnp = "DELETE FROM cnpcsv WHERE UNQ = %s"
                        cursor.execute(delete_cnp,data3)
                        print("Delete From CNP Data")
                        
                        delete_contri = "DELETE FROM contribution WHERE UNQ = %s"
                        cursor.execute(delete_contri,data3)
                        print("Delete From Contribution Data")

                        msg = "Employee Not Working , Re Processing Complete"

                query15 = "SELECT Basic FROM cnpcsv WHERE month = %s"
                data7 = [month]
                cursor.execute(query15, data7)
                basic_sal = cursor.fetchall()

                temp1 = []
                temp2 = []
                for i in range(len(basic_sal)):
                    temp1 = ''.join(basic_sal[i])
                    temp2.append(temp1)
                total = 0
                for i in range(len(temp2)):
                    total = int(total) + int(temp2[i]) 

                print("Total : ", total)
                cnp = round(int(total) * 0.015)
                print("CNP : ", cnp)
                
                update_cnp = """UPDATE cnpcsv
                SET 
                totalRem = %s,
                CNP = %s
                WHERE
                month = %s;"""
                data8 = [total, cnp, month]
                cursor.execute(update_cnp, data8)
# =================================================================================================================================

                query16 = "SELECT Salary FROM contribution WHERE month = %s"
                cursor.execute(query16, data7)
                basic_con = cursor.fetchall()

                bas1 = []
                bas2 = []

                for i in range(len(basic_con)):
                    bas1 = ''.join(basic_con[i])
                    bas2.append(bas1)
                bas_total = 0

                for i in range(len(bas2)):
                    bas_total = int(bas_total) + int(bas2[i])

# =================================================================================================================================

                query17 = "SELECT ecsg FROM contribution WHERE month = %s"
                cursor.execute(query17, data7)
                ecsg_con = cursor.fetchall()

                ecsg1 = []
                ecsg2 = []

                for i in range(len(ecsg_con)):
                    ecsg1 = ''.join(ecsg_con[i])
                    ecsg2.append(ecsg1)
                ecsg_total = 0

                for i in range(len(ecsg2)):
                    ecsg_total = int(ecsg_total) + int(ecsg2[i])

# =================================================================================================================================

                query18 = "SELECT elevy FROM contribution WHERE month = %s"
                cursor.execute(query18, data7)
                elevy_con = cursor.fetchall()

                elevy1 = []
                elevy2 = []

                for i in range(len(elevy_con)):
                    elevy1 = ''.join(elevy_con[i])
                    elevy2.append(elevy1)
                elevy_total = 0

                for i in range(len(elevy2)):
                    elevy_total = int(elevy_total) + int(elevy2[i])

# =================================================================================================================================

                query19 = "SELECT ensf FROM contribution WHERE month = %s"
                cursor.execute(query19, data7)
                ensf_con = cursor.fetchall()

                ensf1 = []
                ensf2 = []

                for i in range(len(ensf_con)):
                    ensf1 = ''.join(ensf_con[i])
                    ensf2.append(ensf1)
                ensf_total = 0

                for i in range(len(ensf2)):
                    ensf_total = int(ensf_total) + int(ensf2[i])

# =================================================================================================================================

                query20 = "SELECT csg FROM contribution WHERE month = %s"
                cursor.execute(query20, data7)
                csg_con = cursor.fetchall()

                csg1 = []
                csg2 = []

                for i in range(len(csg_con)):
                    csg1 = ''.join(csg_con[i])
                    csg2.append(csg1)
                csg_total = 0

                for i in range(len(csg2)):
                    csg_total = int(csg_total) + int(csg2[i])

# =================================================================================================================================

                query21 = "SELECT nsf FROM contribution WHERE month = %s"
                cursor.execute(query21, data7)
                nsf_con = cursor.fetchall()

                nsf1 = []
                nsf2 = []

                for i in range(len(nsf_con)):
                    nsf1 = ''.join(nsf_con[i])
                    nsf2.append(nsf1)
                nsf_total = 0

                for i in range(len(nsf2)):
                    nsf_total = int(nsf_total) + int(nsf2[i])

# =================================================================================================================================

                query22 = "SELECT slevy FROM contribution WHERE month = %s"
                cursor.execute(query22, data7)
                slevy_con = cursor.fetchall()

                slevy1 = []
                slevy2 = []

                for i in range(len(slevy_con)):
                    slevy1 = ''.join(slevy_con[i])
                    slevy2.append(slevy1)
                slevy_total = 0

                for i in range(len(slevy2)):
                    slevy_total = int(slevy_total) + int(slevy2[i])

# =================================================================================================================================

                query23 = "SELECT prgf FROM contribution WHERE month = %s"
                cursor.execute(query23, data7)
                prgf_con = cursor.fetchall()

                prgf1 = []
                prgf2 = []

                print(prgf_con)

                for i in range(len(prgf_con)):
                    prgf1 = ''.join(prgf_con[i])
                    prgf2.append(prgf1)
                prgf_total = 0

                for i in range(len(prgf2)):
                    prgf_total = int(prgf_total) + int(prgf2[i])

# =================================================================================================================================

                update_contri = """UPDATE contribution
                SET
                totalRem = %s,
                totalecsg = %s,
                totalelevy = %s,
                totalensf = %s,
                totalprgf = %s,
                totalcsg = %s,
                totalnsf = %s,
                totalslevy = %s
                WHERE 
                month = %s;
                """

                update_contri_data = [bas_total, ecsg_total, elevy_total, ensf_total, prgf_total, csg_total, nsf_total, slevy_total, month]

                cursor.execute(update_contri, update_contri_data)

                print("Contribution Update Complete")


                return render_template("process.html", msg=msg)      

# =================================================================================================================== #

# ========================================== For Employee ID "ALL" ================================================== #

# =================================================================================================================== #

            elif eid == "ALL":                 
                # print(month)
                month = request.form["mon"]
        
                year = request.form["year"]
                id = 0
                month = month.lower()          
                if month == "January" or month=="january":
                    print("In Jan")
                    
                    current_date = "2022-"+"01-"+"01"
                    id = 1
                elif month == "February" or month=="february":
                    print("In Feb")
                    
                    current_date = "2022-"+"02-"+"01"
                    id = 2
                elif month == "March" or month=="march":
                    print("In Mar")
                    
                    current_date = "2022-"+"03-"+"01"
                    id = 3
                elif month == "April" or month=="april":
                    print("In Apr")
                    
                    current_date = "2022-"+"04-"+"01"
                    id = 4
                elif month == "May" or month=="may":
                    print("In May")
                    
                    current_date = "2022-"+"05-"+"01"
                    id = 5
                elif month == "June" or month=="june":
                    print("In Jun")
                    
                    current_date = "2022-"+"06-"+"01"
                    id = 6
                elif month == "July" or month=="july":
                    print("In Jul")
                    
                    current_date = "2022-"+"07-"+"01"
                    id = 7
                elif month == "August" or month=="august":
                    print("In Aug")
                    
                    current_date = "2022-"+"08-"+"01"
                    id = 8
                elif month == "September" or month=="september":
                    print("In Sep")
                    
                    current_date = "2022-"+"09-"+"01"
                    id = 9
                elif month == "October" or month=="october":
                    print("In Oct")
                    
                    current_date = "2022-"+"10-"+"01"
                    id = 10
                elif month == "November" or month=="november":
                    print("In Nov")
                    
                    current_date = "2022-"+"11-"+"01"
                    id = 11
                elif month == "December" or month=="december":
                    print("In Dec")

                    current_date = "2022-"+"12-"+"01"
                    id = 12
                else:  
                    print("In Else")
                    msg = "Enter Month Correctly"
                    return render_template("process.html", msg = msg)
                mid = id-1
                if mid == 0:
                    mid = 12
                
                # print(calendar.month_name[id])
                month2 = calendar.month_name[mid]
                month2 = month2.lower()

                # query3 = "SELECT Carbenefit, salary, Fixedallow, Travelallow, EDF, Educationrel, Medicalrel, medical, Specialbonus FROM employee WHERE EmployeeID = %s "
                # query3 = "SELECT Carbenefit, salary, Fixedallow, Travelallow, EDF, Educationrel, Medicalrel, medical, Specialbonus, EmployeeID FROM employee"
                query = "SELECT Carbenefit, salary, Fixedallow, Travelallow, EDF, Educationrel, Medicalrel, medical, Specialbonus, EmployeeID FROM employee"
                # cursor.execute(query3, data)
                cursor.execute(query)
                emp_data = cursor.fetchall()

                # print(emp_data)

                arrays = {}
                for index,lst in enumerate(emp_data):
                    arrays[str(index+1)] = lst
                # print(arrays)
                
                for i in arrays:
                    # print(i)
                    emp_data2 = list(arrays[i])
                    # emp_data2 = list(emp_data[0])

                    car = int(emp_data2[0])
                    # print(car)
                    # print(type(car))
                    
                    tbasic = int(emp_data2[1])
                    fixAllow = int(emp_data2[2])
                    trans = int(emp_data2[3])
                    edf = int(emp_data2[4])
                    education = int(emp_data2[5])
                    Medicalrel = int(emp_data2[6])
                    # medical = int(emp_data2[7])
                    medical = 0
                    SpeProBns = int(emp_data2[8])
                    eid = emp_data2[9]

                    # lwork = emp_data2[10]
                    # print(lwork)

                    data = [eid]
                    data2 = [eid,month2]
                    # print(month2)

                    query_month = "SELECT MONTH(Lastwork) AS Month FROM employee WHERE EmployeeID= %s"
                    cursor.execute(query_month, data)
                    emp_month = cursor.fetchall()
                    
                    last_mon = emp_month[0][0]

                    query_year = "SELECT YEAR(Lastwork) AS Year FROM employee WHERE EmployeeID= %s"
                    cursor.execute(query_year, data)
                    emp_year = cursor.fetchall()

                    last_year = emp_year[0][0]

                    hire_date = "SELECT hire FROM employee WHERE EmployeeID= %s"
                    cursor.execute(hire_date, data)
                    hire_date_emp = cursor.fetchall()
                    
                    hire_dt = hire_date_emp[0][0]

                    # if mon == 0:
                    #     mon = id    

                    #  last month = employee last month
                    #  last year = employee last year

                    print("last Year ", last_year)
                    print("year ", year)
                    print("last month ", last_mon)
                    print("month ", id)

                    msg = "Processing Complete"

                    hire_date = "SELECT hire FROM employee WHERE EmployeeID = %s"
                    cursor.execute(hire_date, data)
                    hire_date_emp = cursor.fetchall()
                    
                    print(hire_date_emp)
                    hire_dt = str(hire_date_emp[0][0])
                    
                    if (int(last_year) >= int(year) or (last_year == 1 and last_mon == 1)) and (hire_dt < current_date):
                        print("Year Is Correct")
                        if int(last_mon) >= int(id) or (last_year == 1 and last_mon == 1):
                            print("In Start Process")
                            query1 = "SELECT FirstName FROM employee WHERE EmployeeID = %s"
                            cursor.execute(query1,data)
                            fname = cursor.fetchall()
                            for i in range(len(fname)):
                                fname = ''.join(fname[i])

                            query2 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
                            cursor.execute(query2,data)
                            lname = cursor.fetchall()
                            for i in range(len(lname)):
                                lname = ''.join(lname[i])

                            query3 = "SELECT cGrossTax FROM salary WHERE EmployeeID= %s AND Month = %s"
                            cursor.execute(query3,data2)
                            prevGross = cursor.fetchall()
                            for i in range(len(prevGross)):
                                if prevGross != None:
                                    prevGross = ''.join(prevGross[i])
                                else:
                                    prevGross = 0
                            if prevGross != 0:
                                prevGross = ''.join(map(str,prevGross))
                                

                            query4 = "SELECT IET FROM salary WHERE EmployeeID= %s AND Month = %s"
                            cursor.execute(query4,data2)
                            piet = cursor.fetchall()
                            for i in range(len(piet)):
                                if piet != None:
                                    piet = ''.join(piet[i])
                                else:
                                    piet = 0
                            if piet != 0:
                                piet = ''.join(map(str,piet))

                            query5 = "SELECT CurrentPAYE FROM salary WHERE EmployeeID= %s AND Month = %s"
                            cursor.execute(query5,data2)
                            ppaye = cursor.fetchall()
                            # print(ppaye)
                            for i in range(len(ppaye)):
                                if ppaye != None:
                                    ppaye = ''.join(ppaye[i])
                                    print(ppaye)
                                else:
                                    ppaye = 0
                            if ppaye != 0:
                                ppaye = ''.join(map(str,ppaye))

                            query6 = "SELECT Threshold FROM salary WHERE EmployeeID= %s AND Month = %s"
                            cursor.execute(query6,data2)
                            pths = cursor.fetchall()
                            for i in range(len(pths)):
                                if pths != None:
                                    pths = ''.join(pths[i])
                                else:
                                    pths = 0
                            if pths != 0:
                                pths = ''.join(map(str,pths))

                            query7 = "SELECT CurrentSLevy FROM salary WHERE EmployeeID= %s AND Month = %s"
                            cursor.execute(query7,data2)
                            plevy = cursor.fetchall()
                            print("Before For Loop", plevy)
                            print(len(plevy))

                            if len(plevy) > 0:
                                print("In If")
                                for i in range(len(plevy)):
                                    print("In For ")
                                    plevy = ''.join(plevy[i])
                            else:
                                print("In Else")
                                plevy = 0    


                            # for i in range(len(plevy)):
                            #     print("In For")
                            #     if plevy != None:
                            #         print("In if1")
                            #         plevy = ''.join(plevy[i])
                            #     else:
                            #         print("In Else")
                            #         plevy = 0
                            
                            # if plevy != 0:
                            #     print("In if2")
                            #     plevy = ''.join(map(str,plevy))
                            
                            print("plevy", plevy)

                            query8 = "SELECT hire FROM employee WHERE EmployeeID = %s"
                            cursor.execute(query8,data)
                            hire = cursor.fetchall()
                            
                            hire = hire[0][0] 
                            hire = str(hire)
                            # print(hire)
                            # print(str(hire))
                            # print(type(str(hire)))
                            # if hire != None:
                            #     for i in range(len(hire)):
                            #         hire = ''.join(hire[i])
                            #     hire = ''.join(map(str,hire))
                            # else:
                            #     hire = 0                    

                            query9 = "SELECT position FROM employee WHERE EmployeeID = %s"
                            cursor.execute(query9,data)
                            pos = cursor.fetchall()
                            for i in range(len(pos)):
                                if pos != None:
                                    pos = ''.join(pos[i])
                                else:
                                    pos = " "
                            if pos != 0:
                                pos = ''.join(map(str,pos))
                            # print(pos)


                            query10 = "SELECT NICno FROM employee WHERE EmployeeID = %s"
                            cursor.execute(query10,data)
                            nic = cursor.fetchall()
                            # print(nic)
                            for i in range(len(nic)):
                                if nic[0][0] != None:
                                    nic = ''.join(nic[i])
                                else:
                                    nic = " "
                            if nic != 0:
                                nic = ''.join(map(str,nic))
                            
                            UNQ = month + " " + fname
                            data3 = [UNQ]
                            
                            # query11 = "SELECT LockSal From salary WHERE UNQ = %s"
                            # cursor.execute(query11,data3)
                            # lockSal = cursor.fetchall()

                            # print(lockSal)
                            # print(len(lockSal))

                            # if len(lockSal) > 0:
                            #     print("In If")
                            #     for i in range(len(lockSal)):
                            #         print("In For ")
                            #         lockSal = ''.join(lockSal[i])
                            # else:
                            #     print("In Else")
                            #     lockSal = "No"

                            query11 = "SELECT ProcSal From salary WHERE UNQ = %s"
                            cursor.execute(query11,data3)
                            ProcSal = cursor.fetchall()

                            print(ProcSal)
                            print(len(ProcSal))

                            if len(ProcSal) > 0:
                                print("In If")
                                for i in range(len(ProcSal)):
                                    print("In For ")
                                    ProcSal = ''.join(ProcSal[i])
                            else:
                                print("In Else")
                                ProcSal = "No"

                            # query12 = "SELECT working FROM employee WHERE EmployeeID = %s"
                            # cursor.execute(query12, data)
                            # working = cursor.fetchall()

                            # if len(working) > 0:
                            #     print("In If")
                            #     for i in range(len(working)):
                            #         print("In For ")
                            #         working = ''.join(working[i])
                            # else:
                            #     print("In Else")
                            #     working = "Yes"
                            

                            if ProcSal == "No":
                                print("In Process Salary")

                                query = """INSERT INTO payslip(
                                        JoinDate,
                                        Company,
                                        EmpName,
                                        Position,
                                        NIC,
                                        BasicSalary,
                                        TravelAlw,
                                        Bonus,
                                        Gross,
                                        PAYE,
                                        NPF,
                                        NSF,
                                        SLevy,
                                        Deduction,
                                        NetPay,
                                        Payable,
                                        NetPayAcc,
                                        eNPF,
                                        eNSF,
                                        eLevy,
                                        ePRGF,
                                        month,
                                        year,
                                        UNQ
                                        )
                                        VALUES(
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s
                                        );
                                        """
                                
                                
                                flname = lname + " " + fname

                                # Values We Don't Get
                                ot = 0
                                otherAllow = 0
                                arrears = 0
                                eoy = 0
                                leave = 0
                                speBns = 0
                                discBns = 0
                                tax = 0
                                ntax = 0
                                attBns = 0
                                overseas = tax + ntax

                                loan = 0
                                lateness = 0
                                otherDed = 0
                                ab = 0

                                # Previous Data
                                # print(type(prevGross))
                                # print(prevGross)
                                if prevGross == "":
                                    prevGross = 0
                                else:
                                    prevGross = int(prevGross)

                                if piet == "":
                                    piet = 0
                                else:
                                    piet = int(piet)
                                
                                if ppaye == "":
                                    ppaye = 0
                                else:
                                    ppaye = int(ppaye)
                                
                                if pths == "":
                                    pths = 0
                                else:
                                    pths = int(pths)
                                # print(pths)
                                if plevy == "":
                                    plevy = 0
                                else:
                                    plevy = int(plevy)
                        
                                basic = int(tbasic) - int(ab)
                                # Calculations
                                payable = basic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns
                                bonus = speBns + SpeProBns + otherAllow + fixAllow + discBns + attBns

                                pay_gross = tbasic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns
                                
                                # For Overseas Amount
                                if overseas > 0:
                                    ntax = round(int(basic) * 0.06)
                                    tax = round(int(overseas) - int(ntax))
                                else:
                                    ntax = 0
                                    tax = 0

                                if trans > 20000:
                                    transTax = trans - 20000
                                    ntransTax = trans - transTax
                                else:
                                    transTax = 0
                                    ntransTax = 0

                                cgross = basic + ot + otherAllow + trans + arrears + eoy + leave + discBns + fixAllow + tax + SpeProBns + attBns + car

                                grossTax = basic + ot + transTax +otherAllow + arrears + eoy + leave + discBns + fixAllow  + tax + SpeProBns + attBns + car

                                # print("prev Gross " , prevGross)
                                # print("Curr Gross " , cgross)
                                gross = prevGross + grossTax
                                # print("gross" , gross)
                                medf = round(int(edf) / 13)
                                ciet = round(( int(edf) + int(Medicalrel) + int(education)) / 13)
                                
                                iet = int(ciet) + int(piet)
                                # print("ciet" , ciet)
                                # print("piet", piet)
                                # print("iet", iet)

                                netch = gross - iet

                                # print("netch" , netch)
                                if netch < 0:
                                    netch = 0
                                else:
                                    netch = netch

                                if int(basic) > 50000:
                                    nps = round(basic * 0.03)
                                    # cpaye =  round(netch * 0.15)
                                    enps = round(basic * 0.06)
                                else:
                                    nps = round(basic * 0.015)
                                    # cpaye = round(netch * 0.1)
                                    enps = round(basic * 0.03)

                                check = int(basic) + int(otherAllow) - int(medf)
                                if check < 53846:
                                    cpaye = round(netch* 0.1)
                                elif check >= 53846 and check < 75000:
                                    cpaye = round(netch* 0.125)
                                else:
                                    cpaye = round(netch* 0.15)

                                if cpaye < 0:
                                    cpaye = 0
                                else:
                                    cpaye = int(cpaye)
                                
                                if ppaye < 0:
                                    ppaye =0
                                else:
                                    ppaye = int(ppaye)

                                # print("cpaye", cpaye)
                                # print("ppaye", ppaye)
                                paye = int(cpaye) - int(ppaye)
                                # print("paye", paye)
                                if paye < 0:
                                    paye =0
                                else:
                                    paye = int(paye)

                                nsf = int(basic * 0.01)

                                if nsf > 214:
                                    nsf = 214
                                else:
                                    nsf = int(nsf)

                                temp = int(cgross) * 13
                                slevy = 0
                                tths = round(3000000/13)
                                ths = int(pths) + int(tths)
                                # print(ths)
                                netchar = int(gross) - int(iet) - int(ths)
                                print("gross", gross)
                                print("iet", iet)
                                print("ths", ths)
                                if netchar < 0 :
                                    netchar = 0
                                else:
                                    netchar = netchar
                                print("netchar", netchar)
                                print("grossTax", grossTax)

                                if int(temp) > 3000000:
                                    slevy1 = round(netchar * 0.25)
                                    slevy2 = round(gross * 0.1)
                                    print("slevy1", slevy1)
                                    print("slevy2", slevy2)
                                    if slevy1 > slevy2:
                                        slevy = int(slevy2)
                                    else:
                                        slevy = int(slevy1)
                                else:
                                    slevy = 0
                                print("slevy", slevy)
                                ensf = round(basic * 0.025)
                                if ensf > 536:
                                    ensf = 536
                                else:
                                    ensf = round(ensf)
                                levy = round(int(basic) * 0.015)
                                deduction = int(loan) + int(paye) + int(lateness) + int(nps) + int(otherDed) + int(nsf) + int(medical)
                                net = int(payable) - int(deduction)
                                # print(slevy)
                                NetPaysheet = int(net) - int(slevy)
                                slevypay = slevy - plevy
                                print("slevypay", slevypay)
                                otherAllow2 = int(otherAllow) + int(speBns) + int(SpeProBns)
                                
                                tax = int(tax) + int(transTax)
                                ntax = int(ntax) + int(ntransTax)
                                # Payslip Calculation

                                paygross = int(basic) + int(trans) + int(bonus)

                                pay_gross = tbasic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns

                                totalDeduction = int(paye) + int(nps) + int(nsf)

                                netpay = paygross - totalDeduction
                                # eprgf = 0
                                if basic < 200000:
                                    eprgf = round((int(basic) + int(bonus)) * 0.035) # + commission
                                else:
                                    eprgf = 0

                                insert_query = """
                                INSERT INTO OriginalData(
                                EmployeeID,
                                EmployeeName,
                                BasicSalary,
                                FixedAllow,
                                OtherDeduction,
                                Overtime,
                                DiscBonus,
                                NSFEmpee,
                                OtherAllow,
                                TaxableAllow,
                                Medical,
                                Transport,
                                overseas,
                                NTaxableAllow,
                                EDF,
                                Arrears,
                                AttendanceBns,
                                EOY,
                                Loan,
                                CarBenefit,
                                LeaveRef,
                                SLevy,
                                SpecialBns,
                                Lateness,
                                EducationRel,                    
                                SpeProBns,
                                NPS,
                                MedicalRel,
                                Payable,
                                Deduction,
                                NetPay,
                                NetPaysheet,
                                paysheet_gross,
                                CurrentGross,
                                cGrossTax,
                                PrevGross,
                                PrevIET,
                                IET,
                                NetCh,
                                CurrentPAYE,
                                PrevPAYE,
                                PAYE,
                                eCSG,
                                eNSF,
                                eLevy,
                                PRGF,
                                PrevThreshold,
                                Threshold,
                                netchar,
                                CurrentSLevy,
                                PrevSLevy,
                                slevyPay,
                                Absences,
                                Month,
                                Year,
                                UNQ,
                                LockSal
                                )

                                VALUES(
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s
                                );
                                """
                                data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, pay_gross, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, month, year, UNQ, 'No']
                                cursor.execute(insert_query, data1)
                                print("OriginalData Query Executed")

                                insert_query2 = """
                                INSERT INTO salary(
                                EmployeeID,
                                EmployeeName,
                                BasicSalary,
                                FixedAllow,
                                OtherDeduction,
                                Overtime,
                                DiscBonus,
                                NSFEmpee,
                                OtherAllow,
                                TaxableAllow,
                                Medical,
                                Transport,
                                overseas,
                                NTaxableAllow,
                                EDF,
                                Arrears,
                                AttendanceBns,
                                EOY,
                                Loan,
                                CarBenefit,
                                LeaveRef,
                                SLevy,
                                SpecialBns,
                                Lateness,
                                EducationRel,                    
                                SpeProBns,
                                NPS,
                                MedicalRel,
                                Payable,
                                Deduction,
                                NetPay,
                                NetPaysheet,
                                paysheet_gross,
                                CurrentGross,
                                cGrossTax,
                                PrevGross,
                                PrevIET,
                                IET,
                                NetCh,
                                CurrentPAYE,
                                PrevPAYE,
                                PAYE,
                                eCSG,
                                eNSF,
                                eLevy,
                                PRGF,
                                PrevThreshold,
                                Threshold,
                                netchar,
                                CurrentSLevy,
                                PrevSLevy,
                                slevyPay,
                                Absences,
                                Month,
                                Year,
                                UNQ,
                                LockSal,
                                ProcSal
                                )

                                VALUES(
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s
                                );
                                """
                                data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, pay_gross, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, month, year, UNQ, 'No', 'Yes']
                                cursor.execute(insert_query2, data1)
                                print("Salary Query Executed")

                                
                                data3 = [hire, "Demo" , flname, pos, nic, basic, trans, bonus, paygross, paye, nps, nsf, slevypay , totalDeduction, netpay,netpay, netpay, enps, ensf, levy, eprgf, month, year, UNQ ]
                                cursor.execute(query, data3)
                                print("Payslip Query Executed")
                                

                                query14 = "SELECT NICno FROM employee WHERE EmployeeID = %s"
                                cursor.execute(query14, data)
                                nic = cursor.fetchall()
                                if nic[0][0] == "":
                                    nic = " "
                                else:
                                    for i in range(len(nic)):
                                        nic = ''.join(nic[i])
                                
                                    
                                emolument = int(basic) + int(arrears) + int(overseas) + int(otherAllow) + int(car) + int(ot) + int(eoy) + int(leave) + int(fixAllow) + int(discBns) + int(SpeProBns) + int(speBns) 

                                paye_query = """ INSERT INTO payecsv(
                                            EmployeeID,
                                            LastName,
                                            FirstName,
                                            Emoluments,
                                            PAYE,
                                            working,
                                            SLevy,
                                            EmolumentsNet,
                                            month,
                                            UNQ
                                            )
                                            VALUES(
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s
                                            );"""
                                data4 = [nic, lname, fname, emolument, paye, 'Yes', slevypay, emolument, month, UNQ]

                                cursor.execute(paye_query, data4)
                                print("PAYE Query Executed")

                                query12 = "SELECT NPS FROM employee WHERE EmployeeID = %s"
                                cursor.execute(query12, data)
                                pension = cursor.fetchall()
                                for i in range(len(pension)):
                                    pension = ''.join(pension[i])

                                if pension == "Paid":
                                    pension = "Yes"
                                else:
                                    pension = "No"

                                query13 = "SELECT working FROM employee WHERE EmployeeID = %s"
                                cursor.execute(query13, data)
                                working = cursor.fetchall()
                                for i in range(len(working)):
                                    working = ''.join(working[i])
                                
                                query14 = "SELECT NICno FROM employee WHERE EmployeeID = %s"
                                cursor.execute(query14, data)
                                nic = cursor.fetchall()
                                for i in range(len(nic)):
                                    nic = ''.join(nic[i])

                                allowance = int(otherAllow) + int(fixAllow) + int(speBns) + int(SpeProBns) + int(discBns) + int(attBns)
                                commission = 0

                                totalRem = int(basic) + int(allowance)
                                
                                prgf_query = """INSERT INTO prgfcsv(
                                            EmployeeID,
                                            LastName,
                                            FirstName,
                                            Pension,
                                            Working,
                                            Hire,
                                            Basic,
                                            Allowance,
                                            Commission,
                                            TotalRem,
                                            PRGF,
                                            reason,
                                            month,
                                            UNQ
                                            )
                                            VALUES(
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s
                                            );"""
                                if basic < 200000:
                                    data5 = [nic, lname, fname, "No", working, hire, basic, allowance, commission, totalRem, eprgf, " " , month, UNQ]
                                else:
                                    data5 = [nic, lname, fname, "No", working, hire, basic, 0, 0, 0, 0, " " , month, UNQ]
                                
                                cursor.execute(prgf_query, data5)
                                print("PRGF Insert Query Executed")

                                cnp_query = """INSERT INTO cnpcsv(
                                        EmployeeID,
                                        LastName,
                                        FirstName,
                                        Basic,
                                        Basic2,
                                        Season,
                                        Alphabet,
                                        Number,
                                        Working,
                                        Blank1,
                                        Blank2,
                                        month,
                                        UNQ
                                        )
                                        VALUES(
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s
                                        );"""
                                data6 = [nic, lname, fname, basic, basic, "S2", "M", "1", working, " ", " ", month, UNQ]

                                cursor.execute(cnp_query, data6)
                                print("CNP CSV Query Executed")

                                insert_contri = """INSERT INTO contribution(
                                                EmployeeID,
                                                LastName,
                                                FirstName,
                                                IDCard,
                                                Salary,
                                                blank1,
                                                ecsg,
                                                elevy,
                                                ensf,
                                                prgf,
                                                csg,
                                                nsf,
                                                blank2,
                                                slevy,
                                                month,
                                                year,
                                                UNQ
                                                )
                                                VALUES(
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s,
                                                %s
                                                );
                                                """
                                contri_data = [eid, lname, fname, nic, basic, " ", enps, levy, ensf, eprgf, nps, nsf, " ", slevypay, month, year, UNQ]
                                cursor.execute(insert_contri, contri_data)
                                print("Contribution Insert Query Executed")
                                msg = "Processing Complete"
                                # print("Do Something Else")
                        query15 = "SELECT Basic FROM cnpcsv WHERE month = %s"
                        data7 = [month]
                        cursor.execute(query15, data7)
                        basic_sal = cursor.fetchall()

                        temp1 = []
                        temp2 = []
                        for i in range(len(basic_sal)):
                            temp1 = ''.join(basic_sal[i])
                            temp2.append(temp1)
                        total = 0
                        for i in range(len(temp2)):
                            total = int(total) + int(temp2[i]) 

                        print("Total : ", total)
                        cnp = round(int(total) * 0.015)
                        print("CNP : ", cnp)
                        
                        update_cnp = """UPDATE cnpcsv
                        SET 
                        totalRem = %s,
                        CNP = %s
                        WHERE
                        month = %s;"""
                        data8 = [total, cnp, month]
                        cursor.execute(update_cnp, data8)

                        print("CNP Update Query Executed")
        # =================================================================================================================================

                        query16 = "SELECT Salary FROM contribution WHERE month = %s"
                        cursor.execute(query16, data7)
                        basic_con = cursor.fetchall()

                        bas1 = []
                        bas2 = []

                        for i in range(len(basic_con)):
                            bas1 = ''.join(basic_con[i])
                            bas2.append(bas1)
                        bas_total = 0

                        for i in range(len(bas2)):
                            bas_total = int(bas_total) + int(bas2[i])

        # =================================================================================================================================

                        query17 = "SELECT ecsg FROM contribution WHERE month = %s"
                        cursor.execute(query17, data7)
                        ecsg_con = cursor.fetchall()

                        ecsg1 = []
                        ecsg2 = []

                        for i in range(len(ecsg_con)):
                            ecsg1 = ''.join(ecsg_con[i])
                            ecsg2.append(ecsg1)
                        ecsg_total = 0

                        for i in range(len(ecsg2)):
                            ecsg_total = int(ecsg_total) + int(ecsg2[i])

        # =================================================================================================================================

                        query18 = "SELECT elevy FROM contribution WHERE month = %s"
                        cursor.execute(query18, data7)
                        elevy_con = cursor.fetchall()

                        elevy1 = []
                        elevy2 = []

                        for i in range(len(elevy_con)):
                            elevy1 = ''.join(elevy_con[i])
                            elevy2.append(elevy1)
                        elevy_total = 0

                        for i in range(len(elevy2)):
                            elevy_total = int(elevy_total) + int(elevy2[i])

        # =================================================================================================================================

                        query19 = "SELECT ensf FROM contribution WHERE month = %s"
                        cursor.execute(query19, data7)
                        ensf_con = cursor.fetchall()

                        ensf1 = []
                        ensf2 = []

                        for i in range(len(ensf_con)):
                            ensf1 = ''.join(ensf_con[i])
                            ensf2.append(ensf1)
                        ensf_total = 0

                        for i in range(len(ensf2)):
                            ensf_total = int(ensf_total) + int(ensf2[i])

        # =================================================================================================================================

                        query20 = "SELECT csg FROM contribution WHERE month = %s"
                        cursor.execute(query20, data7)
                        csg_con = cursor.fetchall()

                        csg1 = []
                        csg2 = []

                        for i in range(len(csg_con)):
                            csg1 = ''.join(csg_con[i])
                            csg2.append(csg1)
                        csg_total = 0

                        for i in range(len(csg2)):
                            csg_total = int(csg_total) + int(csg2[i])

        # =================================================================================================================================

                        query21 = "SELECT nsf FROM contribution WHERE month = %s"
                        cursor.execute(query21, data7)
                        nsf_con = cursor.fetchall()

                        nsf1 = []
                        nsf2 = []

                        for i in range(len(nsf_con)):
                            nsf1 = ''.join(nsf_con[i])
                            nsf2.append(nsf1)
                        nsf_total = 0

                        for i in range(len(nsf2)):
                            nsf_total = int(nsf_total) + int(nsf2[i])

        # =================================================================================================================================

                        query22 = "SELECT slevy FROM contribution WHERE month = %s"
                        cursor.execute(query22, data7)
                        slevy_con = cursor.fetchall()

                        slevy1 = []
                        slevy2 = []

                        for i in range(len(slevy_con)):
                            slevy1 = ''.join(slevy_con[i])
                            slevy2.append(slevy1)
                        slevy_total = 0

                        for i in range(len(slevy2)):
                            slevy_total = int(slevy_total) + int(slevy2[i])

# =================================================================================================================================

                        query23 = "SELECT prgf FROM contribution WHERE month = %s"
                        cursor.execute(query23, data7)
                        prgf_con = cursor.fetchall()

                        # print(prgf_con[0][0])

                        prgf1 = []
                        prgf2 = []

                        for i in range(len(prgf_con)):
                            prgf1 = ''.join(prgf_con[i])
                            prgf2.append(prgf1)
                        prgf_total = 0

                        for i in range(len(prgf2)):
                            prgf_total = int(prgf_total) + int(prgf2[i])

# =================================================================================================================================

                        update_contri = """UPDATE contribution
                        SET
                        totalRem = %s,
                        totalecsg = %s,
                        totalelevy = %s,
                        totalensf = %s,
                        totalprgf = %s,
                        totalcsg = %s,
                        totalnsf = %s,
                        totalslevy = %s
                        WHERE 
                        month = %s;
                        """

                        update_contri_data = [bas_total, ecsg_total, elevy_total, ensf_total, prgf_total, csg_total, nsf_total, slevy_total, month]

                        cursor.execute(update_contri, update_contri_data)

                        print("Contribution Update Complete")

                return render_template("process.html", msg = msg)                                
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("process.html")

@app.route("/EOY", methods=["GET", "POST"])
def eoy():
    if request.method == "POST" and request.form['action'] == 'process':
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            query1_1 = "SELECT EmployeeID FROM employee WHERE Working = 'Yes'"
            cursor.execute(query1_1)
            emp_id = cursor.fetchall()
            emp_id2 = []
            temp = []
            # print(emp_id)

            for i in range(len(emp_id)):
                temp = ''.join(emp_id[i])
                emp_id2.append(temp)
            
            print(emp_id2)

            query2_1 = "SELECT FirstName FROM employee WHERE Working = 'Yes'"
            cursor.execute(query2_1)
            fname_all = cursor.fetchall()
            fname2 = []
            temp2 = []

            # print(fname)

            for i in range(len(fname_all)):
                temp2 = ''.join(fname_all[i])
                fname2.append(temp2)

            print(fname2)

            query3_1 = "SELECT LastName FROM employee WHERE Working = 'Yes'"
            cursor.execute(query3_1)
            lname_all = cursor.fetchall()
            lname2 = []
            temp3 = []

            # print(lname)

            for i in range(len(lname_all)):
                temp3 = ''.join(lname_all[i])
                lname2.append(temp3)
            print(lname2)

            flname1 = []
            flname_all = []

            for i in range(len(emp_id)):
                flname1 = fname2[i] + " " + lname2[i]
                flname_all.append(flname1)

            print(flname_all)

            length = len(flname_all)

# ===========================================================================================================================================================

            eid = request.form["eid"]
            month = "EOY"
            year = date.today().year
            
            # eoyBns = request.form["eoy"]
            
            data = [eid]
            # print(month)
            
            print(eid)
            # print(eoyBns)

            id = 12
            mid = id-1
            if mid == 0:
                mid = 12
            
            # print(calendar.month_name[id])
            month2 = calendar.month_name[mid]
            month2 = month2.lower()

            # print(emp_data)
            # print(emp_data[0][0])
            # print(emp_data[0][1])

            car = 0
            tbasic = 0
            fixAllow = 0
            trans = 0
            edf = 0
            education = 0
            Medicalrel = 0
            medical = 0
            SpeProBns = 0

            data2 = [eid,month2]
            # print(month2)                    
            print("Before Query1")
            query1 = "SELECT FirstName FROM employee WHERE EmployeeID = %s"
            cursor.execute(query1,data)
            fname = cursor.fetchall()
            for i in range(len(fname)):
                fname = ''.join(fname[i])
            print("After Query1")

            query2 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
            cursor.execute(query2,data)
            lname = cursor.fetchall()
            for i in range(len(lname)):
                lname = ''.join(lname[i])

            UNQ = month + " " + fname
            data3 = [UNQ]

            query3 = "SELECT ProcBns FROM EOY WHERE UNQ = %s"
            cursor.execute(query3,data3)
            proc = cursor.fetchall()
            print(proc)

            if len(proc) > 0:
                print("In If")
                for i in range(len(proc)):
                    print("In For ")
                    proc = ''.join(proc[i])
            else:
                print("In Else")
                proc = "No"    

# ================================================================================================================================================================================            

            query4 = "SELECT BasicSalary From salary WHERE EmployeeID = %s"
            cursor.execute(query4,data)
            basic_all = cursor.fetchall()
            basic1 = []
            basic2 = []

            for i in range(len(basic_all)):
                basic1 = ''.join(basic_all[i])
                basic2.append(basic1)

            basic_total = 0
            for i in range(len(basic2)):
                basic_total = int(basic_total) + int(basic2[i])

# ================================================================================================================================================================================            

            query5 = "SELECT Overtime From salary WHERE EmployeeID = %s"
            cursor.execute(query5,data)
            overtime_all = cursor.fetchall()
            overtime1 = []
            overtime2 = []

            for i in range(len(overtime_all)):
                overtime1 = ''.join(overtime_all[i])
                overtime2.append(overtime1)

            overtime_total = 0
            for i in range(len(overtime2)):
                overtime_total = int(overtime_total) + int(overtime2[i])

# ================================================================================================================================================================================            

            query6 = "SELECT LeaveRef From salary WHERE EmployeeID = %s"
            cursor.execute(query6,data)
            leave_all = cursor.fetchall()
            leave1 = []
            leave2 = []

            for i in range(len(leave_all)):
                leave1 = ''.join(leave_all[i])
                leave2.append(leave1)

            leave_total = 0
            for i in range(len(leave2)):
                leave_total = int(leave_total) + int(leave2[i])

# ================================================================================================================================================================================            

            query7 = "SELECT OtherAllow From salary WHERE EmployeeID = %s"
            cursor.execute(query7,data)
            other_all = cursor.fetchall()
            other1 = []
            other2 = []

            for i in range(len(other_all)):
                other1 = ''.join(other_all[i])
                other2.append(other1)

            other_total = 0
            for i in range(len(other2)):
                other_total = int(other_total) + int(other2[i])

# ================================================================================================================================================================================            

            query13 = "SELECT Absences From salary WHERE EmployeeID = %s"
            cursor.execute(query13,data)
            ab_all = cursor.fetchall()
            ab1 = []
            ab2 = []

            for i in range(len(ab_all)):
                ab1 = ''.join(ab_all[i])
                ab2.append(ab1)

            ab_total = 0
            for i in range(len(ab2)):
                ab_total = int(ab_total) + int(ab2[i])

# ================================================================================================================================================================================            

            # - (Basic + O/TIME + Local Leave Refund + Other Allowance - Absence ) / 12
            eoyBns = round((basic_total + overtime_total + leave_total + other_total - ab_total) / 12)
            print(basic_total)
            print(overtime_total)
            print(leave_total)
            print(other_total)
            print(ab_total)
            print(eoyBns)

# ================================================================================================================================================================================            

            query14 = "SELECT salary From employee WHERE EmployeeID = %s "
            cursor.execute(query14,data)
            basic_nov = cursor.fetchall()
            basic_mon = basic_nov[0][0]

            query_month = "SELECT MONTH(hire) AS Month FROM employee WHERE EmployeeID= %s"
            cursor.execute(query_month, data)
            emp_month = cursor.fetchall()
            
            last_mon = emp_month[0][0]

            total_month = 12 - int(last_mon)
            days = total_month * 26

            eoyBns2 = round((int(basic_mon) /  365) * days)
            
            print("basic_mon ", basic_mon)
            print("days ", days)
            print("eoyBns ", eoyBns2)

# ================================================================================================================================================================================            

            query8 = "SELECT hire FROM employee WHERE EmployeeID = %s"
            cursor.execute(query8,data)
            hire = cursor.fetchall()
            
            hire = hire[0][0] 
            hire = str(hire)
         
            query9 = "SELECT position FROM employee WHERE EmployeeID = %s"
            cursor.execute(query9,data)
            pos = cursor.fetchall()
            for i in range(len(pos)):
                if pos != None:
                    pos = ''.join(pos[i])
                else:
                    pos = " "
            if pos != 0:
                pos = ''.join(map(str,pos))
         
            query10 = "SELECT NICno FROM employee WHERE EmployeeID = %s"
            cursor.execute(query10,data)
            nic = cursor.fetchall()
            # print(nic)
            for i in range(len(nic)):
                if nic[0][0] != None:
                    nic = ''.join(nic[i])
                else:
                    nic = " "
            if nic != 0:
                nic = ''.join(map(str,nic))

            query11 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
            cursor.execute(query11,data)
            ebasic = cursor.fetchall()
            for i in range(len(ebasic)):
                ebasic = ''.join(ebasic[i])

            query12 = "SELECT working FROM employee WHERE EmployeeID = %s"
            cursor.execute(query12,data)
            working = cursor.fetchall()
            for i in range(len(working)):
                working = ''.join(working[i])

# ============================================================================================================================

            query_day = "SELECT DAY(hire) AS Month FROM employee WHERE EmployeeID= %s"
            cursor.execute(query_day, data)
            emp_day = cursor.fetchall()
            
            last_day = emp_day[0][0]

            query_month = "SELECT MONTH(hire) AS Month FROM employee WHERE EmployeeID= %s"
            cursor.execute(query_month, data)
            emp_month = cursor.fetchall()
            
            last_mon = emp_month[0][0]
            
            query_year = "SELECT YEAR(hire) AS Year FROM employee WHERE EmployeeID= %s"
            cursor.execute(query_year, data)
            emp_year = cursor.fetchall()

            last_year = emp_year[0][0]

            current_year = date.today().year
            bonus_year = current_year - 1

            current_month = date.today().month
            bonus_month = current_month + 1

            if proc == "No" and last_year < current_year:
                if last_mon <= current_month:
            
                    prevGross = 0
                    piet = 0
                    ppaye = 0
                    pths = 0
                    plevy = 0
                    
                    flname = lname + " " + fname

                    # Values We Don't Get
                    ot = 0
                    otherAllow = 0
                    arrears = 0
                    eoy = 0
                    leave = 0
                    speBns = 0
                    discBns = 0
                    tax = 0
                    ntax = 0
                    attBns = 0
                    overseas = 0

                    loan = 0
                    lateness = 0
                    otherDed = 0
                    ab = 0

                    # basic = int(tbasic) - int(ab)
                    
                    
                    
                    basic = int(eoyBns)
                    # Calculations
                    payable = basic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns
                    bonus = speBns + SpeProBns + otherAllow + fixAllow + discBns + attBns

                    # For Overseas Amount
                    transTax = 0
                    ntransTax = 0

                    cgross = basic + ot + otherAllow + trans + arrears + eoy + leave + discBns + fixAllow + tax + SpeProBns + attBns + car

                    grossTax = basic + ot + transTax +otherAllow + arrears + eoy + leave + discBns + fixAllow  + tax + SpeProBns + attBns + car

                    # print("prev Gross " , prevGross)
                    # print("Curr Gross " , cgross)
                    gross = prevGross + grossTax
                    # print("gross" , gross)
                    medf = round(int(edf) / 13)
                    ciet = round(( int(edf) + int(Medicalrel) + int(education)) / 13)
                    
                    iet = int(ciet) + int(piet)
                    # print("ciet" , ciet)
                    # print("piet", piet)
                    # print("iet", iet)

                    netch = gross - iet

                    # print("netch" , netch)
                    # netch = 0

                    if int(basic) > 50000:
                        nps = round(basic * 0.03)
                        # cpaye =  round(netch * 0.15)
                        enps = round(basic * 0.06)
                    else:
                        nps = round(basic * 0.015)
                        # cpaye = round(netch * 0.1)
                        enps = round(basic * 0.03)

                    check = int(basic)
                    if check < 53846:
                        print("In check1")
                        cpaye = round(netch* 0.1)
                    elif check >= 53846 and check < 75000:
                        print("In check2")
                        cpaye = round(netch* 0.125)
                    else:
                        print("In check3")
                        cpaye = round(netch* 0.15)

                    print("cpaye " , cpaye)
                    if cpaye < 0:
                        cpaye = 0
                    else:
                        cpaye = int(cpaye)
                    
                    print("ppaye " , ppaye)
                    if ppaye < 0:
                        ppaye = 0
                    else:
                        ppaye = int(ppaye)

                    # print("cpaye", cpaye)
                    # print("ppaye", ppaye)
                    paye = int(cpaye) - int(ppaye)
                    print("paye ", paye)
                    if paye < 0:
                        paye = 0
                    else:
                        paye = int(paye)

                    nsf = int(basic * 0.01)

                    if nsf > 214:
                        nsf = 214
                    else:
                        nsf = int(nsf)

                    slevy = 0
                    netchar = 0
                    
                    tths = round(3000000/13)
                    ths = int(pths) + int(tths)

                    ensf = round(basic * 0.025)
                    if ensf > 536:
                        ensf = 536
                    else:
                        ensf = round(ensf)
                    
                    levy = round(int(basic) * 0.015)
                    
                    deduction = int(loan) + int(paye) + int(lateness) + int(nps) + int(otherDed) + int(nsf) + int(medical)
                    
                    net = int(payable) - int(deduction)
                    
                    # print(slevy)
                    NetPaysheet = int(net) - int(slevy)
                    
                    slevypay = slevy - plevy
                    
                    print("slevypay", slevypay)
                    otherAllow2 = int(otherAllow) + int(speBns) + int(SpeProBns)
                    
                    tax = int(tax) + int(transTax)
                    ntax = int(ntax) + int(ntransTax)
                    # Payslip Calculation

                    paygross = int(basic) + int(trans) + int(bonus)

                    totalDeduction = int(paye) + int(nps) + int(nsf)

                    netpay = paygross - totalDeduction
                    # eprgf = 0
                    if basic < 200000:
                        eprgf = round((int(basic) + int(bonus)) * 0.035) # + commission
                    else:
                        eprgf = 0

                    print("netpay ", netpay)

                    insert_eoy = """INSERT INTO EOY(
                                Employee,
                                BasicSalary,
                                Arrears,
                                Overtime,
                                LeaveRef,
                                EOY,
                                Transport,
                                Overseas,
                                OtherAllow,
                                FixedAllow,
                                Payable,
                                Absences,
                                paye,
                                csg,
                                nsf,
                                Medical,
                                slevy,
                                Lateness,
                                otherDed,
                                Net,
                                month,
                                UNQ,
                                ProcBns,
                                LockBns
                                )
                                VALUES(
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s
                                );
                                """
                    eoy_data = [flname, 0, 0, 0, leave, eoyBns, trans, overseas, otherAllow, 0, payable, 0, paye, nps, nsf, 0, slevypay, 0, otherDed, netpay, "EOY", UNQ, "yes", "no"]
                    cursor.execute(insert_eoy,eoy_data)
                    print("EOY Query Successful")


                    insert_original = """
                            INSERT INTO OriginalData(
                            EmployeeID,
                            EmployeeName,
                            BasicSalary,
                            FixedAllow,
                            OtherDeduction,
                            Overtime,
                            DiscBonus,
                            NSFEmpee,
                            OtherAllow,
                            TaxableAllow,
                            Medical,
                            Transport,
                            overseas,
                            NTaxableAllow,
                            EDF,
                            Arrears,
                            AttendanceBns,
                            EOY,
                            Loan,
                            CarBenefit,
                            LeaveRef,
                            SLevy,
                            SpecialBns,
                            Lateness,
                            EducationRel,                    
                            SpeProBns,
                            NPS,
                            MedicalRel,
                            Payable,
                            Deduction,
                            NetPay,
                            NetPaysheet,
                            CurrentGross,
                            cGrossTax,
                            PrevGross,
                            PrevIET,
                            IET,
                            NetCh,
                            CurrentPAYE,
                            PrevPAYE,
                            PAYE,
                            eCSG,
                            eNSF,
                            eLevy,
                            PRGF,
                            PrevThreshold,
                            Threshold,
                            netchar,
                            CurrentSLevy,
                            PrevSLevy,
                            slevyPay,
                            Absences,
                            Month,
                            Year,
                            UNQ,
                            LockSal
                            )

                            VALUES(
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s
                            );
                            """
                    data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, "December", year, UNQ, 'No']
                    cursor.execute(insert_original, data1)
                    print("Insert Original Query Executed")

                    insert_salary = """
                            INSERT INTO salary(
                            EmployeeID,
                            EmployeeName,
                            BasicSalary,
                            FixedAllow,
                            OtherDeduction,
                            Overtime,
                            DiscBonus,
                            NSFEmpee,
                            OtherAllow,
                            TaxableAllow,
                            Medical,
                            Transport,
                            overseas,
                            NTaxableAllow,
                            EDF,
                            Arrears,
                            AttendanceBns,
                            EOY,
                            Loan,
                            CarBenefit,
                            LeaveRef,
                            SLevy,
                            SpecialBns,
                            Lateness,
                            EducationRel,                    
                            SpeProBns,
                            NPS,
                            MedicalRel,
                            Payable,
                            Deduction,
                            NetPay,
                            NetPaysheet,
                            CurrentGross,
                            cGrossTax,
                            PrevGross,
                            PrevIET,
                            IET,
                            NetCh,
                            CurrentPAYE,
                            PrevPAYE,
                            PAYE,
                            eCSG,
                            eNSF,
                            eLevy,
                            PRGF,
                            PrevThreshold,
                            Threshold,
                            netchar,
                            CurrentSLevy,
                            PrevSLevy,
                            slevyPay,
                            Absences,
                            Month,
                            Year,
                            UNQ,
                            LockSal,
                            ProcSal
                            )

                            VALUES(
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s
                            );
                            """
                    todays_date = date.today()
                    year = todays_date.year
                    data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, "EOY", year, UNQ, 'No', 'Yes']
                    cursor.execute(insert_salary, data1)
                    print("Update Salary Query Executed")

                    insert_payslip = """INSERT INTO payslip(
                                    JoinDate,
                                    Company,
                                    EmpName,
                                    Position,
                                    NIC,
                                    BasicSalary,
                                    TravelAlw,
                                    Bonus,
                                    Gross,
                                    PAYE,
                                    NPF,
                                    NSF,
                                    SLevy,
                                    Deduction,
                                    NetPay,
                                    Payable,
                                    NetPayAcc,
                                    eNPF,
                                    eNSF,
                                    eLevy,
                                    ePRGF,
                                    month,
                                    UNQ
                                    )
                                    VALUES(
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s
                                    );
                                    """
                    data_payslip = [hire, "MAXCITY ASSET MANAGERS LTD RATINGS AFRICA" , flname, pos, nic, basic, trans, bonus, paygross, paye, nps, nsf, slevypay , totalDeduction, netpay,netpay, netpay, enps, ensf, levy, eprgf, "EOY", UNQ ]
                    cursor.execute(insert_payslip, data_payslip)
                    print("Insert Payslip Query Executed")
                    # msg = "Processing Complete"
                    
                    emolument = int(basic) + int(arrears) + int(overseas) + int(otherAllow) + int(car) + int(ot) + int(eoy) + int(leave) + int(fixAllow) + int(discBns) + int(SpeProBns) + int(speBns) 

                    insert_payecsv = """ INSERT INTO payecsv(
                                        EmployeeID,
                                        LastName,
                                        FirstName,
                                        Emoluments,
                                        PAYE,
                                        working,
                                        SLevy,
                                        EmolumentsNet,
                                        month,
                                        UNQ
                                        )
                                        VALUES(
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s,
                                            %s
                                        );"""
                    data4 = [eid, lname, fname, emolument, paye, 'Yes', slevypay, emolument, month, UNQ]
                    cursor.execute(insert_payecsv, data4)
                    print("Insert PAYE CSV Query Executed")

                    msg = "End Of Year Bonus Processing Complete For " + flname + " "
            elif proc == "No" and last_year == current_year:
                prevGross = 0
                piet = 0
                ppaye = 0
                pths = 0
                plevy = 0    

                flname = lname + " " + fname

                # Values We Don't Get
                ot = 0
                otherAllow = 0
                arrears = 0
                eoy = 0
                leave = 0
                speBns = 0
                discBns = 0
                tax = 0
                ntax = 0
                attBns = 0
                overseas = 0

                loan = 0
                lateness = 0
                otherDed = 0
                ab = 0

                # basic = int(tbasic) - int(ab)
                
                
                
                basic = int(eoyBns2)
                # Calculations
                payable = basic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns
                bonus = speBns + SpeProBns + otherAllow + fixAllow + discBns + attBns

                # For Overseas Amount
                transTax = 0
                ntransTax = 0

                cgross = basic + ot + otherAllow + trans + arrears + eoy + leave + discBns + fixAllow + tax + SpeProBns + attBns + car

                grossTax = basic + ot + transTax +otherAllow + arrears + eoy + leave + discBns + fixAllow  + tax + SpeProBns + attBns + car

                # print("prev Gross " , prevGross)
                # print("Curr Gross " , cgross)
                gross = prevGross + grossTax
                # print("gross" , gross)
                medf = round(int(edf) / 13)
                ciet = round(( int(edf) + int(Medicalrel) + int(education)) / 13)
                
                iet = int(ciet) + int(piet)
                # print("ciet" , ciet)
                # print("piet", piet)
                # print("iet", iet)

                netch = gross - iet

                # print("netch" , netch)
                # netch = 0

                if int(basic) > 50000:
                    nps = round(basic * 0.03)
                    # cpaye =  round(netch * 0.15)
                    enps = round(basic * 0.06)
                else:
                    nps = round(basic * 0.015)
                    # cpaye = round(netch * 0.1)
                    enps = round(basic * 0.03)

                check = int(basic)
                if check < 53846:
                    print("In check1")
                    cpaye = round(netch* 0.1)
                elif check >= 53846 and check < 75000:
                    print("In check2")
                    cpaye = round(netch* 0.125)
                else:
                    print("In check3")
                    cpaye = round(netch* 0.15)

                print("cpaye " , cpaye)
                if cpaye < 0:
                    cpaye = 0
                else:
                    cpaye = int(cpaye)
                
                print("ppaye " , ppaye)
                if ppaye < 0:
                    ppaye = 0
                else:
                    ppaye = int(ppaye)

                # print("cpaye", cpaye)
                # print("ppaye", ppaye)
                paye = int(cpaye) - int(ppaye)
                print("paye ", paye)
                if paye < 0:
                    paye = 0
                else:
                    paye = int(paye)

                nsf = int(basic * 0.01)

                if nsf > 214:
                    nsf = 214
                else:
                    nsf = int(nsf)

                slevy = 0
                netchar = 0
                
                tths = round(3000000/13)
                ths = int(pths) + int(tths)

                ensf = round(basic * 0.025)
                if ensf > 536:
                    ensf = 536
                else:
                    ensf = round(ensf)
                
                levy = round(int(basic) * 0.015)
                
                deduction = int(loan) + int(paye) + int(lateness) + int(nps) + int(otherDed) + int(nsf) + int(medical)
                
                net = int(payable) - int(deduction)
                
                # print(slevy)
                NetPaysheet = int(net) - int(slevy)
                
                slevypay = slevy - plevy
                
                print("slevypay", slevypay)
                otherAllow2 = int(otherAllow) + int(speBns) + int(SpeProBns)
                
                tax = int(tax) + int(transTax)
                ntax = int(ntax) + int(ntransTax)
                # Payslip Calculation

                paygross = int(basic) + int(trans) + int(bonus)

                totalDeduction = int(paye) + int(nps) + int(nsf)

                netpay = paygross - totalDeduction
                # eprgf = 0
                if basic < 200000:
                    eprgf = round((int(basic) + int(bonus)) * 0.035) # + commission
                else:
                    eprgf = 0

                print("netpay ", netpay)

                insert_eoy = """INSERT INTO EOY(
                            Employee,
                            BasicSalary,
                            Arrears,
                            Overtime,
                            LeaveRef,
                            EOY,
                            Transport,
                            Overseas,
                            OtherAllow,
                            FixedAllow,
                            Payable,
                            Absences,
                            paye,
                            csg,
                            nsf,
                            Medical,
                            slevy,
                            Lateness,
                            otherDed,
                            Net,
                            month,
                            UNQ,
                            ProcBns,
                            LockBns
                            )
                            VALUES(
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s
                            );
                            """
                eoy_data = [flname, 0, 0, 0, leave, eoyBns2, trans, overseas, otherAllow, 0, payable, 0, paye, nps, nsf, 0, slevypay, 0, otherDed, netpay, "EOY", UNQ, "yes", "no"]
                cursor.execute(insert_eoy,eoy_data)
                print("EOY Query Successful")

                insert_original = """
                        INSERT INTO OriginalData(
                        EmployeeID,
                        EmployeeName,
                        BasicSalary,
                        FixedAllow,
                        OtherDeduction,
                        Overtime,
                        DiscBonus,
                        NSFEmpee,
                        OtherAllow,
                        TaxableAllow,
                        Medical,
                        Transport,
                        overseas,
                        NTaxableAllow,
                        EDF,
                        Arrears,
                        AttendanceBns,
                        EOY,
                        Loan,
                        CarBenefit,
                        LeaveRef,
                        SLevy,
                        SpecialBns,
                        Lateness,
                        EducationRel,                    
                        SpeProBns,
                        NPS,
                        MedicalRel,
                        Payable,
                        Deduction,
                        NetPay,
                        NetPaysheet,
                        CurrentGross,
                        cGrossTax,
                        PrevGross,
                        PrevIET,
                        IET,
                        NetCh,
                        CurrentPAYE,
                        PrevPAYE,
                        PAYE,
                        eCSG,
                        eNSF,
                        eLevy,
                        PRGF,
                        PrevThreshold,
                        Threshold,
                        netchar,
                        CurrentSLevy,
                        PrevSLevy,
                        slevyPay,
                        Absences,
                        Month,
                        Year,
                        UNQ,
                        LockSal
                        )

                        VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                        );
                        """
                data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoy, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, "December", year, UNQ, 'No']
                cursor.execute(insert_original, data1)
                print("Insert Original Query Executed")

                insert_salary = """
                        INSERT INTO salary(
                        EmployeeID,
                        EmployeeName,
                        BasicSalary,
                        FixedAllow,
                        OtherDeduction,
                        Overtime,
                        DiscBonus,
                        NSFEmpee,
                        OtherAllow,
                        TaxableAllow,
                        Medical,
                        Transport,
                        overseas,
                        NTaxableAllow,
                        EDF,
                        Arrears,
                        AttendanceBns,
                        EOY,
                        Loan,
                        CarBenefit,
                        LeaveRef,
                        SLevy,
                        SpecialBns,
                        Lateness,
                        EducationRel,                    
                        SpeProBns,
                        NPS,
                        MedicalRel,
                        Payable,
                        Deduction,
                        NetPay,
                        NetPaysheet,
                        CurrentGross,
                        cGrossTax,
                        PrevGross,
                        PrevIET,
                        IET,
                        NetCh,
                        CurrentPAYE,
                        PrevPAYE,
                        PAYE,
                        eCSG,
                        eNSF,
                        eLevy,
                        PRGF,
                        PrevThreshold,
                        Threshold,
                        netchar,
                        CurrentSLevy,
                        PrevSLevy,
                        slevyPay,
                        Absences,
                        Month,
                        Year,
                        UNQ,
                        LockSal,
                        ProcSal
                        )

                        VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                        );
                        """
                todays_date = date.today()
                year = todays_date.year
                data1 = [eid, flname, basic , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoyBns2, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, "EOY", year, UNQ, 'No', 'Yes']
                cursor.execute(insert_salary, data1)
                print("Update Salary Query Executed")

                insert_payslip = """INSERT INTO payslip(
                                JoinDate,
                                Company,
                                EmpName,
                                Position,
                                NIC,
                                BasicSalary,
                                TravelAlw,
                                Bonus,
                                Gross,
                                PAYE,
                                NPF,
                                NSF,
                                SLevy,
                                Deduction,
                                NetPay,
                                Payable,
                                NetPayAcc,
                                eNPF,
                                eNSF,
                                eLevy,
                                ePRGF,
                                month,
                                UNQ
                                )
                                VALUES(
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s
                                );
                                """
                data_payslip = [hire, "MAXCITY ASSET MANAGERS LTD RATINGS AFRICA" , flname, pos, nic, basic, trans, bonus, paygross, paye, nps, nsf, slevypay , totalDeduction, netpay,netpay, netpay, enps, ensf, levy, eprgf, "EOY", UNQ ]
                cursor.execute(insert_payslip, data_payslip)
                print("Insert Payslip Query Executed")
                # msg = "Processing Complete"
                
                emolument = int(basic) + int(arrears) + int(overseas) + int(otherAllow) + int(car) + int(ot) + int(eoy) + int(leave) + int(fixAllow) + int(discBns) + int(SpeProBns) + int(speBns) 

                insert_payecsv = """ INSERT INTO payecsv(
                                    EmployeeID,
                                    LastName,
                                    FirstName,
                                    Emoluments,
                                    PAYE,
                                    working,
                                    SLevy,
                                    EmolumentsNet,
                                    month,
                                    UNQ
                                    )
                                    VALUES(
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s,
                                        %s
                                    );"""
                data4 = [eid, lname, fname, emolument, paye, 'Yes', slevypay, emolument, month, UNQ]
                cursor.execute(insert_payecsv, data4)
                print("Insert PAYE CSV Query Executed")
                msg = "End Of Year Bonus (Prorata basic) Process Complete For " + flname + " "
            else:
                msg = "Bonus Already Processed."

            print(msg)
            return render_template("eoy.html", msg=msg, eid = emp_id2, name=flname_all, length = length)
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    elif request.method == "POST" and request.form['action'] == 'reprocess':
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            query1_1 = "SELECT EmployeeID FROM employee"
            cursor.execute(query1_1)
            emp_id = cursor.fetchall()
            emp_id2 = []
            temp = []
            # print(emp_id)

            for i in range(len(emp_id)):
                temp = ''.join(emp_id[i])
                emp_id2.append(temp)
            
            # print(emp_id2)

            query2_1 = "SELECT FirstName FROM employee"
            cursor.execute(query2_1)
            fname_all = cursor.fetchall()
            fname2 = []
            temp2 = []

            # print(fname)

            for i in range(len(fname_all)):
                temp2 = ''.join(fname_all[i])
                fname2.append(temp2)

            # print(fname2)

            query3_1 = "SELECT LastName FROM employee"
            cursor.execute(query3_1)
            lname_all = cursor.fetchall()
            lname2 = []
            temp3 = []

            # print(lname)

            for i in range(len(lname_all)):
                temp3 = ''.join(lname_all[i])
                lname2.append(temp3)
            # print(lname2)

            flname1 = []
            flname_all = []

            for i in range(len(emp_id)):
                flname1 = fname2[i] + " " + lname2[i]
                flname_all.append(flname1)

            # print(flname_all)

            length = len(flname_all)
# ===========================================================================================================================================================

            eid = request.form["eid"]
            month = "EOY"
            year = date.today().year
            
            data = [eid]
            # print(month)

            id = 12
            mid = id-1
            if mid == 0:
                mid = 12
            
            # print(calendar.month_name[id])
            month2 = calendar.month_name[mid]
            month2 = month2.lower()

            # print(emp_data)
            # print(emp_data[0][0])
            # print(emp_data[0][1])

            car = 0
            tbasic = 0
            fixAllow = 0
            trans = 0
            edf = 0
            education = 0
            Medicalrel = 0
            medical = 0
            SpeProBns = 0

            data2 = [eid,month2]
            # print(month2)                    

            query1 = "SELECT FirstName FROM employee WHERE EmployeeID = %s"
            cursor.execute(query1,data)
            fname = cursor.fetchall()
            for i in range(len(fname)):
                fname = ''.join(fname[i])

            query2 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
            cursor.execute(query2,data)
            lname = cursor.fetchall()
            for i in range(len(lname)):
                lname = ''.join(lname[i])

            UNQ = month + " " + fname
            data3 = [UNQ]

            print("UNQ ", UNQ)

            query3 = "SELECT ProcBns FROM EOY WHERE UNQ = %s"
            cursor.execute(query3,data3)
            proc = cursor.fetchall()
            print("proc ", proc)

# ================================================================================================================================================================================            

            query4 = "SELECT BasicSalary From salary WHERE EmployeeID = %s"
            cursor.execute(query4,data)
            basic_all = cursor.fetchall()
            basic1 = []
            basic2 = []

            for i in range(len(basic_all)):
                basic1 = ''.join(basic_all[i])
                basic2.append(basic1)

            basic_total = 0
            for i in range(len(basic2)):
                basic_total = int(basic_total) + int(basic2[i])

# ================================================================================================================================================================================            

            query5 = "SELECT Overtime From salary WHERE EmployeeID = %s"
            cursor.execute(query5,data)
            overtime_all = cursor.fetchall()
            overtime1 = []
            overtime2 = []

            for i in range(len(overtime_all)):
                overtime1 = ''.join(overtime_all[i])
                overtime2.append(overtime1)

            overtime_total = 0
            for i in range(len(overtime2)):
                overtime_total = int(overtime_total) + int(overtime2[i])

# ================================================================================================================================================================================            

            query6 = "SELECT LeaveRef From salary WHERE EmployeeID = %s"
            cursor.execute(query6,data)
            leave_all = cursor.fetchall()
            leave1 = []
            leave2 = []

            for i in range(len(leave_all)):
                leave1 = ''.join(leave_all[i])
                leave2.append(leave1)

            leave_total = 0
            for i in range(len(leave2)):
                leave_total = int(leave_total) + int(leave2[i])

# ================================================================================================================================================================================            

            query7 = "SELECT OtherAllow From salary WHERE EmployeeID = %s"
            cursor.execute(query7,data)
            other_all = cursor.fetchall()
            other1 = []
            other2 = []

            for i in range(len(other_all)):
                other1 = ''.join(other_all[i])
                other2.append(other1)

            other_total = 0
            for i in range(len(other2)):
                other_total = int(other_total) + int(other2[i])

# ================================================================================================================================================================================            

            query12 = "SELECT Absences From salary WHERE EmployeeID = %s"
            cursor.execute(query12,data)
            ab_all = cursor.fetchall()
            ab1 = []
            ab2 = []

            for i in range(len(ab_all)):
                ab1 = ''.join(ab_all[i])
                ab2.append(ab1)

            ab_total = 0
            for i in range(len(ab2)):
                ab_total = int(ab_total) + int(ab2[i])

# ================================================================================================================================================================================            

            # - (Basic + O/TIME + Local Leave Refund + Other Allowance - Absence ) / 12
            eoyBns = round((basic_total + overtime_total + leave_total + other_total - ab_total) / 12)
            print(basic_total)
            print(overtime_total)
            print(leave_total)
            print(other_total)
            print(ab_total)
            print(eoyBns)

# ================================================================================================================================================================================            
            
            query14 = "SELECT salary From employee WHERE EmployeeID = %s "
            cursor.execute(query14,data)
            basic_nov = cursor.fetchall()
            basic_mon = basic_nov[0][0]

            query_month = "SELECT MONTH(hire) AS Month FROM employee WHERE EmployeeID= %s"
            cursor.execute(query_month, data)
            emp_month = cursor.fetchall()
            
            last_mon = emp_month[0][0]

            total_month = 12 - int(last_mon)
            days = total_month * 26

            eoyBns2 = round((int(basic_mon) /  365) * days)
            
            print("basic_mon ", basic_mon)
            print("days ", days)
            print("eoyBns ", eoyBns2)

# ================================================================================================================================================================================            
            
            # if len(proc) > 0:
            #     print("In If")
            #     for i in range(len(proc)):
            #         print("In For ")
            #         proc = ''.join(proc[i])
            # else:
            #     print("In Else")
            #     proc = "No"    
            
            query8 = "SELECT hire FROM employee WHERE EmployeeID = %s"
            cursor.execute(query8,data)
            hire = cursor.fetchall()
            
            hire = hire[0][0] 
            hire = str(hire)
         
            query9 = "SELECT position FROM employee WHERE EmployeeID = %s"
            cursor.execute(query9,data)
            pos = cursor.fetchall()
            for i in range(len(pos)):
                if pos != None:
                    pos = ''.join(pos[i])
                else:
                    pos = " "
            if pos != 0:
                pos = ''.join(map(str,pos))

            print("proc ", proc )
         
            query10 = "SELECT NICno FROM employee WHERE EmployeeID = %s"
            cursor.execute(query10,data)
            nic = cursor.fetchall()
            # print(nic)
            for i in range(len(nic)):
                if nic[0][0] != None:
                    nic = ''.join(nic[i])
                else:
                    nic = " "
            if nic != 0:
                nic = ''.join(map(str,nic))

# ============================================================================================================================

            query_day = "SELECT DAY(hire) AS Month FROM employee WHERE EmployeeID= %s"
            cursor.execute(query_day, data)
            emp_day = cursor.fetchall()
            
            last_day = emp_day[0][0]

            query_month = "SELECT MONTH(hire) AS Month FROM employee WHERE EmployeeID= %s"
            cursor.execute(query_month, data)
            emp_month = cursor.fetchall()
            
            last_mon = emp_month[0][0]
            
            query_year = "SELECT YEAR(hire) AS Year FROM employee WHERE EmployeeID= %s"
            cursor.execute(query_year, data)
            emp_year = cursor.fetchall()

            last_year = emp_year[0][0]

            current_year = date.today().year
            bonus_year = current_year - 1

            current_month = date.today().month
            bonus_month = current_month + 1
            
            if proc != [] and last_year < current_year:
                if last_mon <= current_month:
                    print("In If Proc")

                    prevGross = 0
                    piet = 0
                    ppaye = 0
                    pths = 0
                    plevy = 0    
                    
                    flname = lname + " " + fname

                    # Values We Don't Get
                    ot = 0
                    otherAllow = 0
                    arrears = 0
                    eoy = 0
                    leave = 0
                    speBns = 0
                    discBns = 0
                    tax = 0
                    ntax = 0
                    attBns = 0
                    overseas = 0

                    loan = 0
                    lateness = 0
                    otherDed = 0
                    ab = 0

                    # basic = int(tbasic) - int(ab)
                    basic = int(eoyBns)
                    # Calculations
                    payable = basic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns
                    bonus = speBns + SpeProBns + otherAllow + fixAllow + discBns + attBns

                    # For Overseas Amount
                    transTax = 0
                    ntransTax = 0

                    cgross = basic + ot + otherAllow + trans + arrears + eoy + leave + discBns + fixAllow + tax + SpeProBns + attBns + car

                    grossTax = basic + ot + transTax +otherAllow + arrears + eoy + leave + discBns + fixAllow  + tax + SpeProBns + attBns + car

                    # print("prev Gross " , prevGross)
                    # print("Curr Gross " , cgross)
                    gross = prevGross + grossTax
                    # print("gross" , gross)
                    medf = round(int(edf) / 13)
                    ciet = round(( int(edf) + int(Medicalrel) + int(education)) / 13)
                    
                    iet = int(ciet) + int(piet)
                    # print("ciet" , ciet)
                    # print("piet", piet)
                    # print("iet", iet)

                    netch = gross - iet

                    # print("netch" , netch)
                    # netch = 0

                    if int(basic) > 50000:
                        nps = round(basic * 0.03)
                        # cpaye =  round(netch * 0.15)
                        enps = round(basic * 0.06)
                    else:
                        nps = round(basic * 0.015)
                        # cpaye = round(netch * 0.1)
                        enps = round(basic * 0.03)

                    check = int(basic)
                    if check < 53846:
                        print("In check1")
                        cpaye = round(netch* 0.1)
                    elif check >= 53846 and check < 75000:
                        print("In check2")
                        cpaye = round(netch* 0.125)
                    else:
                        print("In check3")
                        cpaye = round(netch* 0.15)

                    print("cpaye " , cpaye)
                    if cpaye < 0:
                        cpaye = 0
                    else:
                        cpaye = int(cpaye)
                    
                    print("ppaye " , ppaye)
                    if ppaye < 0:
                        ppaye = 0
                    else:
                        ppaye = int(ppaye)

                    # print("cpaye", cpaye)
                    # print("ppaye", ppaye)
                    paye = int(cpaye) - int(ppaye)
                    print("paye ", paye)
                    if paye < 0:
                        paye = 0
                    else:
                        paye = int(paye)

                    nsf = int(basic * 0.01)

                    if nsf > 214:
                        nsf = 214
                    else:
                        nsf = int(nsf)

                    slevy = 0
                    netchar = 0
                    
                    tths = round(3000000/13)
                    ths = int(pths) + int(tths)

                    ensf = round(basic * 0.025)
                    if ensf > 536:
                        ensf = 536
                    else:
                        ensf = round(ensf)
                    
                    levy = round(int(basic) * 0.015)
                    
                    deduction = int(loan) + int(paye) + int(lateness) + int(nps) + int(otherDed) + int(nsf) + int(medical)
                    
                    net = int(payable) - int(deduction)
                    
                    # print(slevy)
                    NetPaysheet = int(net) - int(slevy)
                    
                    slevypay = slevy - plevy
                    
                    print("slevypay", slevypay)
                    otherAllow2 = int(otherAllow) + int(speBns) + int(SpeProBns)
                    
                    tax = int(tax) + int(transTax)
                    ntax = int(ntax) + int(ntransTax)
                    # Payslip Calculation

                    paygross = int(basic) + int(trans) + int(bonus)

                    totalDeduction = int(paye) + int(nps) + int(nsf)

                    netpay = paygross - totalDeduction
                    # eprgf = 0
                    if basic < 200000:
                        eprgf = round((int(basic) + int(bonus)) * 0.035) # + commission
                    else:
                        eprgf = 0

                    print("netpay ", netpay)

                    update_eoy = """UPDATE EOY
                                SET
                                Employee = %s,
                                BasicSalary = %s,
                                Arrears = %s,
                                Overtime = %s,
                                LeaveRef = %s,
                                EOY = %s,
                                Transport = %s,
                                Overseas = %s,
                                OtherAllow = %s,
                                FixedAllow = %s,
                                Payable = %s,
                                Absences = %s,
                                paye = %s,
                                csg = %s,
                                nsf = %s,
                                Medical = %s,
                                slevy = %s,
                                Lateness = %s,
                                otherDed = %s,
                                Net = %s,
                                month = %s
                                WHERE
                                UNQ = %s;
                                """

                    print("EOY ", eoyBns2)
                    eoy_data = [flname, 0, 0, 0, leave, eoyBns, trans, overseas, otherAllow, 0, payable, 0, paye, nps, nsf, 0, slevypay, 0, otherDed, netpay, "EOY", UNQ]
                    cursor.execute(update_eoy,eoy_data)
                    print("UPDATE EOY Query Successful")


                    update_original = """UPDATE OriginalData
                                        SET
                                        EmployeeID = %s,
                                        EmployeeName = %s,
                                        BasicSalary = %s,
                                        FixedAllow = %s,
                                        OtherDeduction = %s,
                                        Overtime = %s,
                                        DiscBonus = %s,
                                        NSFEmpee = %s,
                                        OtherAllow = %s,
                                        TaxableAllow = %s,
                                        Medical = %s,
                                        Transport = %s,
                                        overseas = %s,
                                        NTaxableAllow = %s,
                                        EDF = %s,
                                        Arrears = %s,
                                        AttendanceBns = %s,
                                        EOY = %s,
                                        Loan = %s,
                                        CarBenefit = %s,
                                        LeaveRef = %s,
                                        SLevy = %s,
                                        SpecialBns = %s,
                                        Lateness = %s,
                                        EducationRel = %s,
                                        SpeProBns = %s,
                                        NPS = %s,
                                        MedicalRel = %s,
                                        Payable = %s,
                                        Deduction = %s,
                                        NetPay = %s,
                                        NetPaysheet = %s,
                                        CurrentGross = %s,
                                        cGrossTax = %s,
                                        PrevGross = %s,
                                        PrevIET = %s,
                                        IET = %s,
                                        NetCh = %s,
                                        CurrentPAYE = %s,
                                        PrevPAYE = %s,
                                        PAYE = %s,
                                        eCSG = %s,
                                        eNSF = %s,
                                        eLevy = %s,
                                        PRGF = %s,
                                        PrevThreshold = %s,
                                        Threshold = %s,
                                        netchar = %s,
                                        CurrentSLevy = %s,
                                        PrevSLevy = %s,
                                        slevyPay = %s,
                                        Absences = %s
                                        WHERE 
                                        UNQ = %s;
                                        """
                    data1 = [eid, flname, 0 , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoyBns2, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, UNQ]
                    cursor.execute(update_original, data1)
                    print("Update Original Query Executed")

                    update_salary = """UPDATE salary
                                        SET
                                        EmployeeID = %s,
                                        EmployeeName = %s,
                                        BasicSalary = %s,
                                        FixedAllow = %s,
                                        OtherDeduction = %s,
                                        Overtime = %s,
                                        DiscBonus = %s,
                                        NSFEmpee = %s,
                                        OtherAllow = %s,
                                        TaxableAllow = %s,
                                        Medical = %s,
                                        Transport = %s,
                                        overseas = %s,
                                        NTaxableAllow = %s,
                                        EDF = %s,
                                        Arrears = %s,
                                        AttendanceBns = %s,
                                        EOY = %s,
                                        Loan = %s,
                                        CarBenefit = %s,
                                        LeaveRef = %s,
                                        SLevy = %s,
                                        SpecialBns = %s,
                                        Lateness = %s,
                                        EducationRel = %s,
                                        SpeProBns = %s,
                                        NPS = %s,
                                        MedicalRel = %s,
                                        Payable = %s,
                                        Deduction = %s,
                                        NetPay = %s,
                                        NetPaysheet = %s,
                                        CurrentGross = %s,
                                        cGrossTax = %s,
                                        PrevGross = %s,
                                        PrevIET = %s,
                                        IET = %s,
                                        NetCh = %s,
                                        CurrentPAYE = %s,
                                        PrevPAYE = %s,
                                        PAYE = %s,
                                        eCSG = %s,
                                        eNSF = %s,
                                        eLevy = %s,
                                        PRGF = %s,
                                        PrevThreshold = %s,
                                        Threshold = %s,
                                        netchar = %s,
                                        CurrentSLevy = %s,
                                        PrevSLevy = %s,
                                        slevyPay = %s,
                                        Absences = %s
                                        WHERE
                                        UNQ = %s
                                        """
                        
                    data2 = [eid, flname, 0 , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoyBns2, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, UNQ]
                    cursor.execute(update_salary, data2)
                    print("Update Salary Query Executed")

                    update_payslip = """UPDATE payslip
                                SET
                                EmpName = %s,
                                Position = %s,
                                NIC = %s,
                                BasicSalary = %s,
                                TravelAlw = %s,
                                Bonus = %s,
                                Gross = %s,
                                PAYE = %s,
                                NPF = %s,
                                NSF = %s,
                                SLevy = %s,
                                Deduction = %s,
                                NetPay = %s,
                                Payable = %s,
                                NetPayAcc = %s,
                                eNPF = %s,
                                eNSF = %s,
                                eLevy = %s,
                                ePRGF = %s,
                                month = %s
                                WHERE
                                UNQ = %s;
                                """
                    data_payslip = [flname, pos, nic, 0, trans, bonus, paygross, paye, nps, nsf, slevypay, totalDeduction, netpay, netpay, netpay,  enps, ensf, levy, eprgf, "EOY", UNQ]
                    cursor.execute(update_payslip, data_payslip)
                    print("Update Payslip Query Executed")
                    # msg = "Processing Complete"
                    
                    emolument = int(basic) + int(arrears) + int(overseas) + int(otherAllow) + int(car) + int(ot) + int(eoy) + int(leave) + int(fixAllow) + int(discBns) + int(SpeProBns) + int(speBns) 

                    update_payecsv = """UPDATE payecsv
                                        SET
                                        EmployeeID = %s,
                                        LastName = %s,
                                        FirstName = %s,
                                        Emoluments = %s,
                                        PAYE = %s,
                                        SLevy = %s,
                                        EmolumentsNet = %s
                                        WHERE
                                        UNQ = %s;
                                        """

                    data4 = [eid, lname, fname, emolument, paye, slevypay, emolument, UNQ]
                    cursor.execute(update_payecsv, data4)
                    print("Update PAYE CSV Query Executed")

                    msg = "End Of Year Bonus Re-Processing Complete For " + flname + " "
            elif last_year == current_year:
                prevGross = 0
                piet = 0
                ppaye = 0
                pths = 0
                plevy = 0    
                
                flname = lname + " " + fname

                # Values We Don't Get
                ot = 0
                otherAllow = 0
                arrears = 0
                eoy = 0
                leave = 0
                speBns = 0
                discBns = 0
                tax = 0
                ntax = 0
                attBns = 0
                overseas = 0

                loan = 0
                lateness = 0
                otherDed = 0
                ab = 0

                # basic = int(tbasic) - int(ab)
                basic = int(eoyBns2)
                # Calculations
                payable = basic + ot + otherAllow + trans + arrears + eoy + leave + speBns + SpeProBns + fixAllow + discBns + overseas + attBns
                bonus = speBns + SpeProBns + otherAllow + fixAllow + discBns + attBns

                # For Overseas Amount
                transTax = 0
                ntransTax = 0

                cgross = basic + ot + otherAllow + trans + arrears + eoy + leave + discBns + fixAllow + tax + SpeProBns + attBns + car

                grossTax = basic + ot + transTax +otherAllow + arrears + eoy + leave + discBns + fixAllow  + tax + SpeProBns + attBns + car

                # print("prev Gross " , prevGross)
                # print("Curr Gross " , cgross)
                gross = prevGross + grossTax
                # print("gross" , gross)
                medf = round(int(edf) / 13)
                ciet = round(( int(edf) + int(Medicalrel) + int(education)) / 13)
                
                iet = int(ciet) + int(piet)
                # print("ciet" , ciet)
                # print("piet", piet)
                # print("iet", iet)

                netch = gross - iet

                # print("netch" , netch)
                # netch = 0

                if int(basic) > 50000:
                    nps = round(basic * 0.03)
                    # cpaye =  round(netch * 0.15)
                    enps = round(basic * 0.06)
                else:
                    nps = round(basic * 0.015)
                    # cpaye = round(netch * 0.1)
                    enps = round(basic * 0.03)

                check = int(basic)
                if check < 53846:
                    print("In check1")
                    cpaye = round(netch* 0.1)
                elif check >= 53846 and check < 75000:
                    print("In check2")
                    cpaye = round(netch* 0.125)
                else:
                    print("In check3")
                    cpaye = round(netch* 0.15)

                print("cpaye " , cpaye)
                if cpaye < 0:
                    cpaye = 0
                else:
                    cpaye = int(cpaye)
                
                print("ppaye " , ppaye)
                if ppaye < 0:
                    ppaye = 0
                else:
                    ppaye = int(ppaye)

                # print("cpaye", cpaye)
                # print("ppaye", ppaye)
                paye = int(cpaye) - int(ppaye)
                print("paye ", paye)
                if paye < 0:
                    paye = 0
                else:
                    paye = int(paye)

                nsf = int(basic * 0.01)

                if nsf > 214:
                    nsf = 214
                else:
                    nsf = int(nsf)

                slevy = 0
                netchar = 0
                
                tths = round(3000000/13)
                ths = int(pths) + int(tths)

                ensf = round(basic * 0.025)
                if ensf > 536:
                    ensf = 536
                else:
                    ensf = round(ensf)
                
                levy = round(int(basic) * 0.015)
                
                deduction = int(loan) + int(paye) + int(lateness) + int(nps) + int(otherDed) + int(nsf) + int(medical)
                
                net = int(payable) - int(deduction)
                
                # print(slevy)
                NetPaysheet = int(net) - int(slevy)
                
                slevypay = slevy - plevy
                
                print("slevypay", slevypay)
                otherAllow2 = int(otherAllow) + int(speBns) + int(SpeProBns)
                
                tax = int(tax) + int(transTax)
                ntax = int(ntax) + int(ntransTax)
                # Payslip Calculation

                paygross = int(basic) + int(trans) + int(bonus)

                totalDeduction = int(paye) + int(nps) + int(nsf)

                netpay = paygross - totalDeduction
                # eprgf = 0
                if basic < 200000:
                    eprgf = round((int(basic) + int(bonus)) * 0.035) # + commission
                else:
                    eprgf = 0

                print("netpay ", netpay)

                update_eoy = """UPDATE EOY
                            SET
                            Employee = %s,
                            BasicSalary = %s,
                            Arrears = %s,
                            Overtime = %s,
                            LeaveRef = %s,
                            EOY = %s,
                            Transport = %s,
                            Overseas = %s,
                            OtherAllow = %s,
                            FixedAllow = %s,
                            Payable = %s,
                            Absences = %s,
                            paye = %s,
                            csg = %s,
                            nsf = %s,
                            Medical = %s,
                            slevy = %s,
                            Lateness = %s,
                            otherDed = %s,
                            Net = %s,
                            month = %s
                            WHERE
                            UNQ = %s;
                            """

                print("EOY ", eoyBns)
                eoy_data = [flname, 0, 0, 0, leave, eoyBns2, trans, overseas, otherAllow, 0, payable, 0, paye, nps, nsf, 0, slevypay, 0, otherDed, netpay, "EOY", UNQ]
                cursor.execute(update_eoy,eoy_data)
                print("UPDATE EOY Query Successful")

                update_original = """UPDATE OriginalData
                                    SET
                                    EmployeeID = %s,
                                    EmployeeName = %s,
                                    BasicSalary = %s,
                                    FixedAllow = %s,
                                    OtherDeduction = %s,
                                    Overtime = %s,
                                    DiscBonus = %s,
                                    NSFEmpee = %s,
                                    OtherAllow = %s,
                                    TaxableAllow = %s,
                                    Medical = %s,
                                    Transport = %s,
                                    overseas = %s,
                                    NTaxableAllow = %s,
                                    EDF = %s,
                                    Arrears = %s,
                                    AttendanceBns = %s,
                                    EOY = %s,
                                    Loan = %s,
                                    CarBenefit = %s,
                                    LeaveRef = %s,
                                    SLevy = %s,
                                    SpecialBns = %s,
                                    Lateness = %s,
                                    EducationRel = %s,
                                    SpeProBns = %s,
                                    NPS = %s,
                                    MedicalRel = %s,
                                    Payable = %s,
                                    Deduction = %s,
                                    NetPay = %s,
                                    NetPaysheet = %s,
                                    CurrentGross = %s,
                                    cGrossTax = %s,
                                    PrevGross = %s,
                                    PrevIET = %s,
                                    IET = %s,
                                    NetCh = %s,
                                    CurrentPAYE = %s,
                                    PrevPAYE = %s,
                                    PAYE = %s,
                                    eCSG = %s,
                                    eNSF = %s,
                                    eLevy = %s,
                                    PRGF = %s,
                                    PrevThreshold = %s,
                                    Threshold = %s,
                                    netchar = %s,
                                    CurrentSLevy = %s,
                                    PrevSLevy = %s,
                                    slevyPay = %s,
                                    Absences = %s
                                    WHERE 
                                    UNQ = %s;
                                    """
                data1 = [eid, flname, 0 , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoyBns2, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, UNQ]
                cursor.execute(update_original, data1)
                print("Update Original Query Executed")

                update_salary = """UPDATE salary
                                    SET
                                    EmployeeID = %s,
                                    EmployeeName = %s,
                                    BasicSalary = %s,
                                    FixedAllow = %s,
                                    OtherDeduction = %s,
                                    Overtime = %s,
                                    DiscBonus = %s,
                                    NSFEmpee = %s,
                                    OtherAllow = %s,
                                    TaxableAllow = %s,
                                    Medical = %s,
                                    Transport = %s,
                                    overseas = %s,
                                    NTaxableAllow = %s,
                                    EDF = %s,
                                    Arrears = %s,
                                    AttendanceBns = %s,
                                    EOY = %s,
                                    Loan = %s,
                                    CarBenefit = %s,
                                    LeaveRef = %s,
                                    SLevy = %s,
                                    SpecialBns = %s,
                                    Lateness = %s,
                                    EducationRel = %s,
                                    SpeProBns = %s,
                                    NPS = %s,
                                    MedicalRel = %s,
                                    Payable = %s,
                                    Deduction = %s,
                                    NetPay = %s,
                                    NetPaysheet = %s,
                                    CurrentGross = %s,
                                    cGrossTax = %s,
                                    PrevGross = %s,
                                    PrevIET = %s,
                                    IET = %s,
                                    NetCh = %s,
                                    CurrentPAYE = %s,
                                    PrevPAYE = %s,
                                    PAYE = %s,
                                    eCSG = %s,
                                    eNSF = %s,
                                    eLevy = %s,
                                    PRGF = %s,
                                    PrevThreshold = %s,
                                    Threshold = %s,
                                    netchar = %s,
                                    CurrentSLevy = %s,
                                    PrevSLevy = %s,
                                    slevyPay = %s,
                                    Absences = %s
                                    WHERE
                                    UNQ = %s
                                    """
                    
                data2 = [eid, flname, 0 , fixAllow, otherDed, ot, discBns, nsf, otherAllow2, tax, medical, trans, overseas, ntax, edf, arrears, attBns, eoyBns2, loan, car, leave, slevypay, speBns, lateness, education, SpeProBns, nps, Medicalrel, payable, deduction, net, NetPaysheet, cgross, gross,  prevGross, piet, iet, netch, cpaye, ppaye, paye, enps ,ensf, levy, eprgf, pths, ths, netchar, slevy ,plevy, slevypay, ab, UNQ]
                cursor.execute(update_salary, data2)
                print("Update Salary Query Executed")

                update_payslip = """UPDATE payslip
                            SET
                            EmpName = %s,
                            Position = %s,
                            NIC = %s,
                            BasicSalary = %s,
                            TravelAlw = %s,
                            Bonus = %s,
                            Gross = %s,
                            PAYE = %s,
                            NPF = %s,
                            NSF = %s,
                            SLevy = %s,
                            Deduction = %s,
                            NetPay = %s,
                            Payable = %s,
                            NetPayAcc = %s,
                            eNPF = %s,
                            eNSF = %s,
                            eLevy = %s,
                            ePRGF = %s,
                            month = %s
                            WHERE
                            UNQ = %s;
                            """
                data_payslip = [flname, pos, nic, 0, trans, bonus, paygross, paye, nps, nsf, slevypay, totalDeduction, netpay, netpay, netpay,  enps, ensf, levy, eprgf, "EOY", UNQ]
                cursor.execute(update_payslip, data_payslip)
                print("Update Payslip Query Executed")
                # msg = "Processing Complete"
                
                emolument = int(basic) + int(arrears) + int(overseas) + int(otherAllow) + int(car) + int(ot) + int(eoy) + int(leave) + int(fixAllow) + int(discBns) + int(SpeProBns) + int(speBns) 

                update_payecsv = """UPDATE payecsv
                                    SET
                                    EmployeeID = %s,
                                    LastName = %s,
                                    FirstName = %s,
                                    Emoluments = %s,
                                    PAYE = %s,
                                    SLevy = %s,
                                    EmolumentsNet = %s
                                    WHERE
                                    UNQ = %s;
                                    """

                data4 = [eid, lname, fname, emolument, paye, slevypay, emolument, UNQ]
                cursor.execute(update_payecsv, data4)
                print("Update PAYE CSV Query Executed")

                msg = "End Of Year Bonus Re-Processing Complete For " + flname + " "
                
            else:
                msg = "No Data Available (Process Bonus First)"

            return render_template("eoy.html",msg=msg, eid = emp_id2, name=flname_all, length = length)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    else:
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            query1 = "SELECT EmployeeID FROM employee WHERE Working = 'Yes'"
            cursor.execute(query1)
            emp_id = cursor.fetchall()
            emp_id2 = []
            temp = []
            # print(emp_id)

            for i in range(len(emp_id)):
                temp = ''.join(emp_id[i])
                emp_id2.append(temp)
            
            print(emp_id2)


            query2 = "SELECT FirstName FROM employee WHERE Working = 'Yes'"
            cursor.execute(query2)
            fname = cursor.fetchall()
            fname2 = []
            temp2 = []

            # print(fname)

            for i in range(len(fname)):
                temp2 = ''.join(fname[i])
                fname2.append(temp2)

            print(fname2)

            query3 = "SELECT LastName FROM employee WHERE Working = 'Yes'"
            cursor.execute(query3)
            lname = cursor.fetchall()
            lname2 = []
            temp3 = []

            # print(lname)

            for i in range(len(lname)):
                temp3 = ''.join(lname[i])
                lname2.append(temp3)
            print(lname2)

            flname1 = []
            flname = []

            for i in range(len(emp_id)):
                flname1 = fname2[i] + " " + lname2[i]
                flname.append(flname1)

            print(flname)

            length = len(flname)

            
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        return render_template("eoy.html", eid = emp_id2, name = flname, length = length)

@app.route("/summary", methods = ["POST" , "GET"])
def summary():
    if request.method == "POST" and request.form["action"] == "summary":

        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            get_emp = "SELECT DISTINCT EmployeeID, EmployeeName FROM OriginalData"
            cursor.execute(get_emp)
            emp_data = cursor.fetchall()

            emp1 = []
            emp2 = []

            for i in range(len(emp_data)):
                # emp1 = ','.join(emp_data[i])
                emp2.append(emp_data[i])

            # print(emp2)
            # print(emp2)

            all_data = []
            data2 = []

            basic_total = []
            arrears_total = []
            overtime_total = []
            leave_total = []
            eoy_total = []
            trans_total = []
            overseas_total = []
            oalw_total = []
            falw_total = []
            pay_total = []
            ab_total = []
            paye_total = []
            csg_total = []
            nsf_total = []
            medical_total = []
            slevy_total = []
            late_total = []
            oded_total = []
            net_total = []
            
            # print(len(emp2))
            for i in range(len(emp2)):
                query = "SELECT Month, Year, BasicSalary, Arrears, Overtime, LeaveRef, EOY, Transport, Overseas, OtherAllow, FixedAllow, Payable, Absences, PAYE, NPS, NSFEmpee, Medical, SLevy, Lateness, OtherDeduction, NetPaysheet FROM salary WHERE EmployeeID = %s "
                data = [emp2[i][0]]
                
                cursor.execute(query,data)
                pay_data = cursor.fetchall()
                # print(len(pay_data))

# ==========================================================================================================================================================================

                get_basic = "SELECT BasicSalary FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_basic,data)
                basic_all = cursor.fetchall()

                basic_all2 = []
                for i in range(len(basic_all)):
                    basic_all2.append(basic_all[i][0])

                basic_sum = 0
                for i in range(len(basic_all2)):
                    basic_sum = basic_sum + int(basic_all2[i])

                # basic_tsum = [basic_sum]                
                basic_total.append(basic_sum)
                
# ==========================================================================================================================================================================

                get_arr = "SELECT Arrears FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_arr,data)
                arr_all = cursor.fetchall()

                arr_all2 = []
                for i in range(len(arr_all)):
                    arr_all2.append(arr_all[i][0])

                arr_sum = 0
                for i in range(len(arr_all2)):
                    arr_sum = arr_sum + int(arr_all2[i])

                # arr_tsum = [arr_sum]
                arrears_total.append(arr_sum)

# ==========================================================================================================================================================================

                get_ot = "SELECT Overtime FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_ot,data)
                ot_all = cursor.fetchall()

                ot_all2 = []
                for i in range(len(ot_all)):
                    ot_all2.append(ot_all[i][0])

                ot_sum = 0
                for i in range(len(ot_all2)):
                    ot_sum = ot_sum + int(ot_all2[i])

                # ot_tsum = [ot_sum]
                overtime_total.append(ot_sum)

# ==========================================================================================================================================================================

                get_leave = "SELECT LeaveRef FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_leave,data)
                leave_all = cursor.fetchall()

                leave_all2 = []
                for i in range(len(leave_all)):
                    leave_all2.append(leave_all[i][0])

                leave_sum = 0
                for i in range(len(leave_all2)):
                    leave_sum = leave_sum + int(leave_all2[i])

                # leave_tsum = [leave_sum]
                leave_total.append(leave_sum)

# ==========================================================================================================================================================================

                get_eoy = "SELECT EOY FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_eoy,data)
                eoy_all = cursor.fetchall()

                eoy_all2 = []
                for i in range(len(eoy_all)):
                    eoy_all2.append(eoy_all[i][0])

                eoy_sum = 0
                for i in range(len(eoy_all2)):
                    eoy_sum = eoy_sum + int(eoy_all2[i])

                # eoy_tsum = [eoy_sum]
                eoy_total.append(eoy_sum)

# ==========================================================================================================================================================================

                get_trans = "SELECT Transport FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_trans,data)
                trans_all = cursor.fetchall()

                trans_all2 = []
                for i in range(len(trans_all)):
                    trans_all2.append(trans_all[i][0])

                trans_sum = 0
                for i in range(len(trans_all2)):
                    trans_sum = trans_sum + int(trans_all2[i])

                # trans_tsum = [trans_sum]
                trans_total.append(trans_sum)

# ==========================================================================================================================================================================

                get_overseas = "SELECT Overseas FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_overseas,data)
                overseas_all = cursor.fetchall()

                overseas_all2 = []
                for i in range(len(overseas_all)):
                    overseas_all2.append(overseas_all[i][0])

                overseas_sum = 0
                for i in range(len(overseas_all2)):
                    overseas_sum = overseas_sum + int(overseas_all2[i])

                # overseas_tsum = [overseas_sum]
                overseas_total.append(overseas_sum)

# ==========================================================================================================================================================================

                get_oalw = "SELECT OtherAllow FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_oalw,data)
                oalw_all = cursor.fetchall()

                oalw_all2 = []
                for i in range(len(oalw_all)):
                    oalw_all2.append(oalw_all[i][0])

                oalw_sum = 0
                for i in range(len(oalw_all2)):
                    oalw_sum = oalw_sum + int(oalw_all2[i])

                # oalw_tsum = [oalw_sum]
                oalw_total.append(oalw_sum)

# ==========================================================================================================================================================================

                get_falw = "SELECT FixedAllow FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_falw,data)
                falw_all = cursor.fetchall()

                falw_all2 = []
                for i in range(len(falw_all)):
                    falw_all2.append(falw_all[i][0])

                falw_sum = 0
                for i in range(len(falw_all2)):
                    falw_sum = falw_sum + int(falw_all2[i])

                # falw_tsum = [falw_sum]
                falw_total.append(falw_sum)

# ==========================================================================================================================================================================

                get_pay = "SELECT Payable FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_pay,data)
                pay_all = cursor.fetchall()

                pay_all2 = []
                for i in range(len(pay_all)):
                    pay_all2.append(pay_all[i][0])

                pay_sum = 0
                for i in range(len(pay_all2)):
                    pay_sum = pay_sum + int(pay_all2[i])

                # pay_tsum = [pay_sum]
                pay_total.append(pay_sum)

# ==========================================================================================================================================================================

                get_ab = "SELECT Absences FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_ab,data)
                ab_all = cursor.fetchall()

                ab_all2 = []
                for i in range(len(ab_all)):
                    ab_all2.append(ab_all[i][0])

                ab_sum = 0
                for i in range(len(ab_all2)):
                    ab_sum = ab_sum + int(ab_all2[i])

                # ab_tsum = [ab_sum]
                ab_total.append(ab_sum)

# ==========================================================================================================================================================================

                get_paye = "SELECT PAYE FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_paye,data)
                paye_all = cursor.fetchall()

                paye_all2 = []
                for i in range(len(paye_all)):
                    paye_all2.append(paye_all[i][0])

                paye_sum = 0
                for i in range(len(paye_all2)):
                    paye_sum = paye_sum + int(paye_all2[i])

                # paye_tsum = [paye_sum]
                paye_total.append(paye_sum)

# ==========================================================================================================================================================================

                get_csg = "SELECT NPS FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_csg,data)
                csg_all = cursor.fetchall()

                csg_all2 = []
                for i in range(len(csg_all)):
                    csg_all2.append(csg_all[i][0])

                csg_sum = 0
                for i in range(len(csg_all2)):
                    csg_sum = csg_sum + int(csg_all2[i])

                # csg_tsum = [csg_sum]
                csg_total.append(csg_sum)

# ==========================================================================================================================================================================

                get_nsf = "SELECT NSFEmpee FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_nsf,data)
                nsf_all = cursor.fetchall()

                nsf_all2 = []
                for i in range(len(nsf_all)):
                    nsf_all2.append(nsf_all[i][0])

                nsf_sum = 0
                for i in range(len(nsf_all2)):
                    nsf_sum = nsf_sum + int(nsf_all2[i])

                # nsf_tsum = [nsf_sum]
                nsf_total.append(nsf_sum)                                                                                                                

# ==========================================================================================================================================================================

                get_medical = "SELECT Medical FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_medical,data)
                medical_all = cursor.fetchall()

                medical_all2 = []
                for i in range(len(medical_all)):
                    medical_all2.append(medical_all[i][0])

                medical_sum = 0
                for i in range(len(medical_all2)):
                    medical_sum = medical_sum + int(medical_all2[i])

                # medical_tsum = [medical_sum]
                medical_total.append(medical_sum)                

# ==========================================================================================================================================================================

                get_slevy = "SELECT SLevy FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_slevy,data)
                slevy_all = cursor.fetchall()

                slevy_all2 = []
                for i in range(len(slevy_all)):
                    slevy_all2.append(slevy_all[i][0])

                slevy_sum = 0
                for i in range(len(slevy_all2)):
                    slevy_sum = slevy_sum + int(slevy_all2[i])

                # slevy_tsum = [slevy_sum]
                slevy_total.append(slevy_sum)

# ==========================================================================================================================================================================

                get_late = "SELECT Lateness FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_late,data)
                late_all = cursor.fetchall()

                late_all2 = []
                for i in range(len(late_all)):
                    late_all2.append(late_all[i][0])

                late_sum = 0
                for i in range(len(late_all2)):
                    late_sum = late_sum + int(late_all2[i])

                # late_tsum = [late_sum]
                late_total.append(late_sum)

# ==========================================================================================================================================================================

                get_oded = "SELECT OtherDeduction FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_oded,data)
                oded_all = cursor.fetchall()

                oded_all2 = []
                for i in range(len(oded_all)):
                    oded_all2.append(oded_all[i][0])

                oded_sum = 0
                for i in range(len(oded_all2)):
                    oded_sum = oded_sum + int(oded_all2[i])

                # oded_tsum = [oded_sum]
                oded_total.append(oded_sum)

# ==========================================================================================================================================================================

                get_net = "SELECT NetPaysheet FROM salary WHERE EmployeeID = %s "
                cursor.execute(get_net,data)
                net_all = cursor.fetchall()

                net_all2 = []
                for i in range(len(net_all)):
                    net_all2.append(net_all[i][0])

                net_sum = 0
                for i in range(len(net_all2)):
                    net_sum = net_sum + int(net_all2[i])

                # net_tsum = [net_sum]
                net_total.append(net_sum)                                                                

# ==========================================================================================================================================================================

                data2.append(pay_data)

            # print(basic_total)
            # print(arrears_total)
            # print(overtime_total)
            # print(leave_total)
            # print(eoy_total)
            # print(trans_total)
            # print(overseas_total)
            # print(oalw_total)
            # print(falw_total)
            # print(pay_total)
            # print(ab_total)
            # print(paye_total)
            # print(csg_total)
            # print(nsf_total)
            # print(medical_total)
            # print(slevy_total)
            # print(late_total)
            # print(oded_total)
            # print(net_total)

            length2 = len(emp2)
            # print(length2)
            length = len(pay_data)
            # print(length)

            length3 = len(all_data)

            # print("ALL Data ", all_data)
            # print(data2)
            # return "success"
            return render_template("summary2.html", length = length, data = emp2, data2 = data2, length2 = length2 ,basic = basic_total, arr = arrears_total, ot = overtime_total, leave = leave_total, eoy = eoy_total, trans = trans_total, overseas = overseas_total, oalw = oalw_total, falw = falw_total, pay = pay_total, ab = ab_total, paye = paye_total, csg = csg_total, nsf = nsf_total, medical = medical_total, slevy = slevy_total, late = late_total, oded = oded_total, net = net_total )
        except Error as e:
            print("Error While connecting to MySQL : ", e )
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    elif request.method == "POST" and request.form["action"] == "back":
        return render_template("summary.html")
    return render_template("summary.html")

@app.route("/payslip", methods = ["GET", "POST"])            
def payslip():
    # global connection
    if request.method == "POST" and request.form['action'] == 'word':
        month = request.form["mon"]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            query = "SELECT JoinDate, Company, EmpName, Position, NIC, BasicSalary, TravelAlw, Bonus, Gross, PAYE, NPF, NSF, SLevy , Deduction, NetPay, Payable, NetPayAcc, eNPF, eNSF, eLevy, ePRGF, year FROM payslip WHERE month = %s "
            data1 =[month]
            cursor.execute(query,data1)
            data = cursor.fetchall()
            length = len(data)
            print(data)
            print(length)

            query2 = "SELECT EOY FROM EOY WHERE month = %s"
            cursor.execute(query2, data1)
            EOY = cursor.fetchall()

            if month == "EOY":
                print("In If")
                return render_template("payslipeoy.html", data=data, length=length, month = month, EOY=EOY)    
            else:
                return render_template("payslip2.html", data=data, length=length, month = month, EOY=EOY)

            # return render_template("payslip2.html")
        except Error as e:
            print("Error While connecting to MySQL : ", e )
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("payslip.html")

@app.route("/paysheet", methods=["GET" , "POST"])
def paysheet():
    
    # For Pdf Generate
    if request.method == "POST" and request.form['action'] == 'pdf':
        month = request.form["mon"]
        year = request.form["year"]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            data1 = [month]
            data2 = [year]
            # query1 = "SELECT * FROM paysheet"
            # query1 = "SELECT EmployeeName, BasicSalary, Arrears, Overseas, TravelAllow, OtherAllow, Gross, PAYE, CSG, NSF, Medical, SLevy, Net FROM paysheet"
            if month == "EOY":
                query1 = "SELECT Employee, BasicSalary, Arrears, Overtime, LeaveRef, EOY, Transport, Overseas, OtherAllow, FixedAllow, Payable, Absences, paye, csg, nsf, Medical, slevy, Lateness, otherDed, Net FROM EOY WHERE month = %s"  
            else:  
                query1 = "SELECT EmployeeName, BasicSalary, Arrears, Overtime, LeaveRef, EOY, Transport, Overseas, OtherAllow, FixedAllow, paysheet_gross, Absences, PAYE, NPS, NSFEmpee, Medical, SLevy, Lateness, OtherDeduction, NetPaysheet FROM salary WHERE Month = %s "
            cursor.execute(query1,data1)
            data = cursor.fetchall()
            
            session["data"] = data
            length = len(data)
            
            for i in range(len(data1)):
                month = ' '.join(data1[i])

            for i in range(len(data2)):
                year = ' '.join(data2[i])
            
            # return month
            return render_template("paysheet2.html", data=data, length=length, month = month, year = year)
            # return redirect(url_for('download', data = data))
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        
    # For Excel Generate

    if request.method == "POST" and request.form['action'] == 'excel':
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            # query1 = "SELECT * FROM paysheet"
            query1 = "SELECT EmployeeName, BasicSalary, Arrears, Overseas, TravelAllow, OtherAllow, FixedAllow, Gross, PAYE, CSG, NSF, Medical, SLevy, Net FROM paysheet"
            cursor.execute(query1)
            data = cursor.fetchall()
            print(data)
            session["data"] = data
            return render_template("paysheet2.html", data=data,month = month)
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    if request.method == "POST" and request.form['action'] == 'back':
        return render_template("paysheet.html")

    return render_template("paysheet.html") 

@app.route('/payecsv', methods=["GET", "POST"])
def payecsv():
    if request.method == "POST" and request.form['action'] == 'paye':
        mon = request.form["mon"]
        year = request.form["year"]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            data1 = [mon]
            data2 = [year]


            for i in range(len(data1)):
                month = ' '.join(data1[i])

            for i in range(len(data2)):
                year = ' '.join(data2[i])


            # query1 = "SELECT * FROM paysheet"
            # query1 = "SELECT EmployeeName, BasicSalary, Arrears, Overseas, TravelAllow, OtherAllow, Gross, PAYE, CSG, NSF, Medical, SLevy, Net FROM paysheet"
            query1 = "SELECT EmployeeID, LastName, FirstName, Emoluments, PAYE, working, SLevy, EmolumentsNet FROM payecsv WHERE Month = %s "
            cursor.execute(query1,data1)
            data = cursor.fetchall()
            print(data)
            session["data"] = data
            length = len(data)
            print(length)
            return render_template("payecsv2.html", data=data, length=length, month = month, year= year)
            # return redirect(url_for('download', data = data))
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    
    return render_template("payecsv.html")

@app.route("/prgfcsv", methods=["GET", "POST"])
def prgfcsv():
    if request.method == "POST" and request.form['action'] == 'prgf':
        mon = request.form["mon"]
        year = request.form["year"]
        data = [mon]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            data2 = [year]
            for i in range(len(data)):
                month = ' '.join(data[i])

            for i in range(len(data2)):
                year = ' '.join(data2[i])

            query = "SELECT EmployeeID, LastName, FirstName, Pension, Working, Hire, Basic, Allowance, Commission, TotalRem, PRGF, reason FROM prgfcsv WHERE month = %s"
            cursor.execute(query,data)
            prgf = cursor.fetchall()

            length = len(prgf)

            return render_template("prgfcsv2.html", length = length, data= prgf, month = month, year = year)        

            
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("prgfcsv.html")


@app.route("/cnpcsv", methods=["GET", "POST"])
def cnpcsv():
    if request.method == "POST" and request.form['action'] == 'cnp':
        mon = request.form["mon"]
        year = request.form["year"]
        data = [mon]
        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            data2 = [year]
            for i in range(len(data)):
                month = ' '.join(data[i])

            for i in range(len(data2)):
                year = ' '.join(data2[i])

            query = "SELECT EmployeeID, LastName, FirstName, Basic, Basic2, Season, Alphabet, Number, Working, Blank1, Blank2 FROM cnpcsv WHERE month = %s"

            cursor.execute(query,data)
            cnp_data = cursor.fetchall()

            length = len(cnp_data)

            query2 = "SELECT totalRem FROM cnpcsv WHERE month = %s"
            cursor.execute(query2, data)
            total = cursor.fetchall()

            total = total[0][0]

            query3 = "SELECT CNP FROM cnpcsv WHERE month = %s"
            cursor.execute(query3, data)
            cnp = cursor.fetchall()

            cnp = cnp[0][0]

            return render_template("cnpcsv2.html", length = length, data= cnp_data, month = month, year = year, total=total, cnp=cnp)        
            
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("cnpcsv.html")


@app.route('/contribution', methods=["POST", "GET"])
def contribution():
    if request.method == "POST" and request.form['action'] == 'contri':
        mon = request.form["mon"]
        year = request.form["year"]
        data = [mon]

        try:
            connection = mysql.connector.connect(host='demo-do-user-12574852-0.b.db.ondigitalocean.com',
                                                    database='defaultdb',
                                                    user='doadmin',
                                                    port='25060',
                                                    password='AVNS_PcXvrtUuNMOXoepk9DT') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            data2 = [year]
            for i in range(len(data)):
                month = ' '.join(data[i])

            for i in range(len(data2)):
                year = ' '.join(data2[i])

            query = "SELECT EmployeeID, LastName, FirstName, IDCard, Salary, blank1, ecsg, elevy, ensf, prgf, csg, nsf FROM contribution WHERE month = %s"

            cursor.execute(query,data)
            contri_data = cursor.fetchall()

            length = len(contri_data)

            query2 = "SELECT totalRem FROM contribution WHERE month = %s"
            cursor.execute(query2, data)
            totalRem = cursor.fetchall()

            totalRem = totalRem[0][0]

            query3 = "SELECT totalecsg FROM contribution WHERE month = %s"
            cursor.execute(query3, data)
            totalecsg = cursor.fetchall()

            totalecsg = totalecsg[0][0]

            query4 = "SELECT totalelevy FROM contribution WHERE month = %s"
            cursor.execute(query4, data)
            totalelevy = cursor.fetchall()

            totalelevy = totalelevy[0][0]

            query5 = "SELECT totalensf FROM contribution WHERE month = %s"
            cursor.execute(query5, data)
            totalensf = cursor.fetchall()

            totalensf = totalensf[0][0]

            query6 = "SELECT totalcsg FROM contribution WHERE month = %s"
            cursor.execute(query6, data)
            totalcsg = cursor.fetchall()

            totalcsg = totalcsg[0][0]

            query7 = "SELECT totalnsf FROM contribution WHERE month = %s"
            cursor.execute(query7, data)
            totalnsf = cursor.fetchall()

            totalnsf = totalnsf[0][0]

            query8 = "SELECT totalslevy FROM contribution WHERE month = %s"
            cursor.execute(query8, data)
            totalslevy = cursor.fetchall()

            totalslevy = totalslevy[0][0]

            query9 = "SELECT totalprgf FROM contribution WHERE month = %s"
            cursor.execute(query9, data)
            totalprgf = cursor.fetchall()

            totalprgf = totalprgf[0][0]

            return render_template("contribution2.html", length = length, data= contri_data, month = month, year = year, totalRem = totalRem, totalecsg = totalecsg, totalelevy = totalelevy, totalensf = totalensf, totalcsg = totalcsg,totalnsf = totalnsf, totalslevy = totalslevy, totalprgf = totalprgf )

        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")        

    return render_template("contribution.html")

@app.route('/download')
def download():
    
    if "data" in session:
        print("In IF")
        data = session["data"]
    rendered = render_template('demo.html')
    options = {
        'page-size': 'A3',
        'margin-top': '0.75in',
        'margin-right': '0.5in',
        'margin-bottom': '0.75in',
        'margin-left': '0.1in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'no-outline': None
    }
    config = pdfkit.configuration(wkhtmltopdf='/home/apps/dir/usr/local/bin/wkhtmltopdf')
    pdfkit.from_url('https://www.youtube.com/', 'out-test1.pdf', configuration=config)
    # config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

    # pdf = pdfkit.from_string(rendered,'paysheet.pdf' , False, configuration=config)
    # response = make_response(pdf)
    # response.headers["Content-Type"] = "application/pdf"
    # response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    
    # return render_template('paysheet2.html',filename='css/style.css', data=data)
    # p = "./paysheet.pdf"
    return "Ready"


# @app.route("/download")
# def download():
#     pdfkit.from_url('http://micropyramid.com', 'micro.pdf')
    # return "Done"
    
if __name__ == "__main__":
    app.run(debug=True)