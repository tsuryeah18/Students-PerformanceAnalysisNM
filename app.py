from flask import Flask, render_template


app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def  home():
    render_template('index.html')

@app.route('/dashboard',methods = ["GET","POST"])
def  dashboard():
    render_template('dashboard.html')

@app.route('/report',methods = ["GET","POST"])
def  report():
    render_template('report.html')

@app.route('/story',methods = ["GET","POST"])
def  story():
    render_template('story.html')


if __name__ == "__main__":
    app.run(debug=True)