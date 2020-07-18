import requests
import re

url = 'None'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}


def findurl(url,header):
    number = 1
    print('[*]正在发送请求')
    res = requests.get(url,headers=header).text
    print('[*]成功接收响应')
    urls=re.findall(r'<a href="([a-zA-z]+://[^\s]*)"',res)
    for i in urls:
        print('[*]',number,': ',i)
        number = number + 1
    return True
    
while True:
    cmd = input('T-BOX auxiliary(Directory collection) >')
    if cmd == 'show options':
        print('                                                          ')
        print('----------name---------content------------present---------')
        print('          URL           ' + url + '                网址    ')
        print('                                                          ')
    elif cmd == '':    
        pass
    elif cmd[:7] == 'set url' or cmd[:7] == 'set URL':
        url = cmd[8:]
        print('[*]url ==> ' + url)

    elif cmd == 'run':
        if url == 'None':
            print('[-]请设置url')
        else:
            findurl(url=url,header=header)
    elif cmd == 'back':
        break
    else:
        print("[-]can't find command: " + cmd)
        
    

    
