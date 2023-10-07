from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/cashier')
def cashier():
    return render_template('cashier.html')

if __name__ == '__main__':
    app.run(debug=True)