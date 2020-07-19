import socket
from concurrent.futures import ThreadPoolExecutor
import threading

#header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
realm_name = 'None'
def summon(url):
    #url_list = []
    subdomain = []
    new_zym_list = []
    zym_list = open('zym.txt').read().splitlines()
    for i in zym_list:
        #new_zym = 'https://'+i + '.'+url + '/'
        zym = i + '.'+url
        #url_list.append(new_zym)
        subdomain.append(zym)
    return subdomain
    


def scan(ym):
    try:
        tgt = socket.gethostbyname(ym)
        print('[*] ' + ym + ' ==> '+tgt)
    except:
        pass

while True:
    cmd = input('T-BOX auxiliary(subdomain) >')
    if cmd == 'show options':
        print('                                                          ')
        print('----------name---------content------------present---------')
        print('       realm_name    '+realm_name+'            头域名例如:baidu.com   ')
        print('                                                          ')

    elif cmd[:14] == 'set realm_name':
        realm_name = cmd[15:]
        print('[*]realm_name ==> '+realm_name)


    elif cmd == '':
        pass

    elif cmd == 'run':
        if realm_name == 'None':
            print('[*]请设置头域名')
        else:
            poor = ThreadPoolExecutor(100)
            a = summon(realm_name)
            for ym in a:
                poor.submit(scan,ym)
            poor.shutdown(wait=True)

    elif cmd == 'back':
        break

    else:
        print("[-]can't find command: " + cmd)
