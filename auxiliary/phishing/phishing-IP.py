from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/hello')
def index():
    print('[*]',request.remote_addr,'访问了这个界面')
    return render_template('phishing-IP.html')

@app.route('/IP',methods=['POST'])
def getIP():
    return "404 Not Found"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8080)