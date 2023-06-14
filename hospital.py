
from flask import render_template,url_for
from flask import redirect
from flask import request
from flask import Flask
from flask import flash
import mysql.connector as mq


# db = DB_management()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        doctors = request.form['doctors']
        department = request.form['department']
        times = request.form['time']
        sex = request.form['sex']
        dates = request.form['date']
        val = [fullname, phone, doctors,
               times, sex, department, dates]
        print(val)
        query = '''insert into appointment(Fullname,phone,doctors,times,sex,department,dateandtime)values(%s,%s,%s,%s,%s,%s,%s)'''
        try:
            conn = mq.connect(host='localhost', user='root', password='')
            mqcursor = conn.cursor()
            if conn.is_connected():
                mqcursor.execute('use hospital')
                mqcursor.execute(query, val)
                conn.commit()
                mqcursor.close()
                conn.close()
                print('successfully')
                flash('You have successfully make a appointment !','success')
                return redirect('/')
            else:
                print('Unsuccessfully')
                flash('Sorry try again make a appointment !','danger')
                return redirect('/')
        except:
            pass
    
    return render_template('hospital.html')



@app.route('/singup', methods=['POST', 'GET'])

def singup():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dob =request.form['dob']
        email = request.form['emailid']
        sex = request.form['sex']
        specialist = request.form['department']
        phototgraphy = request.form['photo']
        phone = request.form['phone']
        workExp = request.form['workExp']
        qualification = request.form['quali']
        permanentAdd = request.form['addper']
        temporaryAdd = request.form['addtemp']
        fathername = request.form['fathername']
        mothername = request.form['mothername']
        parentNumber = request.form['pphone']
        parentEmail = request.form['pemailid']
        vals = [firstname, lastname, dob, email, sex, specialist, phototgraphy,
                phone, workExp, qualification, permanentAdd, temporaryAdd, fathername, mothername, parentNumber, parentEmail]
        print(vals)
        print(type(dob))
        return redirect(url_for('index'))

@app.route('/hospital')
def hospital(self):
    # us.appointment()
    return render_template('hospital.html')


if __name__ == "__main__":

    app.run(debug=True)


# #Try and try and try and never cry
# from life import try_somthing, enjoy, cry

# while True:
#     if try_somthing(is_new=True)=='succeeded':
#         enjoy()
#     else:
#         continue
#         cry()
