import os
frequency = '10'
realm_name = 'None'

while True:
    cmd = input('T-BOX auxiliary(dos) >')
    if cmd == 'show options':
        print('                                                          ')
        print('----------name---------content------------present---------')
        print('       realm_name    '+realm_name+'        域名           ')
        print('                                                          ')
    elif cmd[:14] == 'set realm_name':
        realm_name = cmd[15:]
        print('[*]realm_name ==> '+realm_name)

    elif cmd[:13] == 'set frequency':
        frequency = cmd[14:]

    elif cmd == '':
        pass
    elif cmd == 'run':
        if realm_name == 'None':
            print('[*]请设置域名')
        
        else:
            new_cmd = 'python syn-termux.py' + ' ' + realm_name 
            os.system(new_cmd)

    elif cmd == 'back':
        break
        
    else:
        print("[-]can't find command: " + cmd)



 
