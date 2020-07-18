from flask import Flask, render_template,request
import os
import re
import threading   

app = Flask(__name__)

@app.route('/sqlmapGUI')
def sqlmapGUI():
    return render_template('sqlmap-GUI.html')

def send_cmd(new_cmd,number):
    os.system(new_cmd)


@app.route('/wait',methods=['GET'])
def wait():
    print(request.url)
    url = request.args.get('url')
    thread = request.args.get('thread')
    data = request.args.get('data')
    user_agent = request.args.get('user-agent')
    cookie = request.args.get('cookie')
    tamper = request.args.get('tamper')
    tampers = request.args.get('tampers')
    level = request.args.get('level')
    win = tampers = request.args.get('win')
    
    cmd = []

    
    new_url = '-u' + '"' + url + '?id=1' +'"' + " "
    cmd.append(new_url)
    if thread == "":
        pass
    else:
        new_thread = '--' + 'thread' + ' ' + thread + " "
        cmd.append(new_thread)
    
    if data == '默认':
        pass
    else:
        new_data = '--dbms' + ' ' + '"' + data + '"' + " "
        cmd.append(new_data)
    
    if user_agent == "":
        pass
    else:
        new_user_agent = '--user-agent' + ' ' + '"' + user_agent + '"' + ' '
        cmd.append(new_user_agent)
    
    if cookie == "":
        pass
    else:
        new_cookie = '--cookie' + ' '+ '"' + cookie + '"' + " "
        cmd.append(new_cookie)
    
    if tamper == '':
        if tampers == '':
            pass
        else:
            new_tampers = '--tamper=' + ' ' + '"' + tampers + '.py' + '"' + ' '
            cmd.append(new_tampers)
    else:
        new_tamper = '--tamper' + ' ' + '"' + tamper + '.py' + '"' + " "
        cmd.append(new_tamper)
    
    if level == "":
        pass
    else:
        new_level = '--level' + ' '+ level + " "
    
    win_url = url + '&'
    
    if win == "":
        pass
    else:
        p1 = re.compile(r'&win=(.*?)&', re.S)
        res = re.findall(p1, url)
        for i in res:
            r1 = '--' + i
            cmd.append(i)

    print(cmd)
    b = ''
    for i in cmd:
        b = b + i
    
    c = b + '--batch' 
    new_cmd = 'python' + ' ' + 'sqlmap/sqlmap.py' + ' ' + c
    number = 1
    t = threading.Thread(target=send_cmd, args=(new_cmd,number))
    t.start()
    #t.join()
    return '完成, 详情请见命令行'


def main():
    print('hello')
    app.run(host="0.0.0.0",debug=True,port=8080)


main()