from flask import Flask,render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("form.html")
@app.route('/submit',methods=['POST'])
def submit():
    name=request.form.get('name')
    password=request.form.get('password')
    email=request.form.get('email')
    return render_template('result.html',name=name,email=email,password=password)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port="5000",debug=True)
