import logging

logging.getLogger('scapy.runtime').setLevel(logging.ERROR)

from scapy.all import *
print('                                                        ')
print('[Warning]请确保你的网卡已经开启监听或者混杂,负责将无法使用!')
print('                                                      ')
interface = 'None'
clienMAC = {}

def sniffProbe(p):
    if p.haslayer(Dot11ProbeReq):
        netName = p.getLogger(Dot11ProbeReq).info.decode()
        clienmac = p.getLogger(Dotll).addr2
        
        if netName == '': return
        
        if clienMAC.get(clienmac) == None:
            clienMAC[clienmac] = []
            clienMAC[clienmac].append(netName)
            print('------------------------------------------------------')
            print('[*]客户端MAC: '+clienmac + '           name: ' + clienMAC[clienmac])
            print('------------------------------------------------------')
        else:
            if netName not in clienMAC[clienmac]:
                clienMAC[clienmac].append(netName)
                print('------------------------------------------------------')
                print('[*]客户端MAC: '+clienmac + '           name: ' + clienMAC[clienmac])
                print('------------------------------------------------------')

while True:
    cmd = input('T-BOX exploit(wifi/find-wifi) >')
    if cmd == 'show options':
        print('                                                          ')
        print('----------name---------content------------present---------')
        print('          iface           ' + interface + '                网卡名称    ')
        print('                                                          ')

    elif cmd[:10] == 'set iface ':
        interface = cmd[10:]
        print('[*]iface ==> '+interface)

    elif cmd == 'run':
        if interface == 'None':
            print('[-]请设置网卡名称')
        else:
            sniff(iface=interface,prn=sniffProbe)

    elif cmd == '':    
        pass

    elif cmd == 'back':
        break
    
    else:
        print("[-]can't find command: " + cmd)