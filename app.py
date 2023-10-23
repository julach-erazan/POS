from flask import Flask,render_template,request, url_for, redirect
#from flask import flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pos_sys_db'

mysql = MySQL(app)

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        username = request.form['username']
        shopName = request.form['shopName']
        shopAddress = request.form['shopAddress']
        shopRegNo = request.form['shopRegNo']
        phoneNo = request.form['phoneNo']
        email = request.form['email']
        password = request.form['password']

        #try:
            # Creating a connection cursor
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO user (username, shopName, shopAddress, shopRegNo, phoneNo, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (username, shopName, shopAddress, shopRegNo, phoneNo, email, password))

            # Saving the actions performed on the DB
        #mysql.connection.commit()

            # Closing the cursor
        #cur.close()
        # except Exception as e:
        #     # Handle the database error here, e.g., log the error or return an error response to the user
        #     print("Database error:", str(e))
        #     return "An error occurred while processing your request."

        cur.execute("SELECT * FROM user")
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', data=data)
        #return "Data inserted successfully."

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/cashier')
def cashier():
    return render_template('cashier.html')

if __name__ == '__main__':
    app.run(debug=True)