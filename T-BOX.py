import os
import threading
#==================================banner==========================================
print('                                                     ')
print('################################################################')
print('                                                     ')
print('mmmmmmm           ===  mmmm')
print('   #   mmm   mmm---H---#   #  mmm   m   m   {0.1#dev}')
print("   #  #' '# #' '# [)]  #mmm' #' '#   #m#")
print('   #  #   # #   # [I]  #   # #   #   m#m')
print('   #  "#m#" "#m#" [I]  #mmm" "#m#"  m" "m')
print(" 		  [I]...")
print('                   V')
print('#################################################################')
print('------------------------------[9 exploit]')
print('------------------------------[8 auxiliary]')
print('------------------------------[6 钓鱼模板]')
print('                                                     ')
print('                                                     ')
#===============================phishing=================================================

def start_facebook():
    print('ohishing working on 127.0.0.1/facebook')
    os.system('cd auxiliary/phishing && python phishing-facebook.py')

def start_IP():
    print('ohishing working on 127.0.0.1/hello')
    os.system('cd auxiliary/phishing && python phishing-IP.py')

def start_QQ():
    print('ohishing working on 127.0.0.1/QQlogin')
    os.system('cd auxiliary/phishing && python phishing-QQ.py')

def start_QQmali():
    print('ohishing working on 127.0.0.1/QQmalilogin')
    os.system('cd auxiliary/phishing && python phishing-QQmali.py')

def start_twitter():
    print('ohishing working on 127.0.0.1/Twitterlogin')
    os.system('cd auxiliary/phishing && python phishing-Twitter.py')

def start_sqlmap_GUI():
    print('ohishing working on 127.0.0.1/sqlmapGUI')
    os.system('cd auxiliary/phishing && python sqlmap-GUI.py')

while True:
    #============================================================================
    cmd = input('T-BOX >')
    #=================================auxiliary===========================================
    if cmd == 'use auxiliary/Directory collection':
        os.system('cd auxiliary && python Directory_collection.py')

    elif cmd == 'use auxiliary/dos':
        os.system('cd auxiliary && python dos.py')

    elif cmd == 'use auxiliary/synflood':
        os.system('cd auxiliary && python synflood.py')

    elif cmd == 'use auxiliary/password/ssh':
        os.system('cd auxiliary/password && python ssh.py')

    elif cmd == 'use auxiliary/password/windows':
        os.system('cd auxiliary/password && python windows.py')

    elif cmd == 'use auxiliary/summon/php':
        os.system('cd auxiliary/summon && python php-web.py')

    elif cmd == 'use auxiliary/summon/python':
        os.system('cd auxiliary/summon && python python-shell.py')
    
    elif cmd == 'use auxiliary/summon/windows':
        os.system('cd auxiliary/summon && python windwos.py')

    elif cmd == 'use auxiliary/phishing/facebook':
        t1 = threading.Thread(target=start_facebook)
        t1.start()

    elif cmd == 'use auxiliary/phishing/IP':
        t2 = threading.Thread(target=start_IP)
        t2.start()

    elif cmd == 'use auxiliary/phishing/QQ':
        t3 = threading.Thread(target=start_QQ)
        t3.start()

    elif cmd == 'use auxiliary/phishing/QQmali':
        t4 = threading.Thread(target=start_QQmali)
        t4.start()

    elif cmd == 'use auxiliary/phishing/twitter':
        t5 = threading.Thread(target=start_twitter)
        t5.start()

    elif cmd == 'use auxiliary/phishing/sqlmap-gui':
        t6 = threading.Thread(target=start_sqlmap_GUI)
        t6.start()

    #==============================exploit================================

    elif cmd == 'use exploit/arp':
        os.system('cd exploit && python arp.py')

    elif cmd == 'use exploit/arpspoof':
        os.system('cd exploit && python arpspoof.py')

    elif cmd == 'use exploit/wifi/deauth':
        os.system('cd exploit/wifi && python deauth.py')

    elif cmd == 'use exploit/wifi/find-wifi':
        os.system('cd exploit/wifi && python find-wifi.py')

    elif cmd == 'use exploit/wifi/password-wifi':
        os.system('cd exploit/wifi && python password-wifi.py')

    elif cmd == 'use exploit/listen/python':
        os.system('cd exploit/listen && python python.py')

    elif cmd == 'use exploit/listen/php':
        os.system('cd exploit/listen && python php.py')
    
    elif cmd == 'use exploit/listen/windows':
        os.system('cd exploit/listen && python windows.py')
    #==============================other======================================


    elif cmd == '?' or cmd == 'help':
        print('[+]和msf用法一样')
        print('------命令----------------用法--------------------功能---------------------例子-------')
        print('      use              use + 路径             启动一个模块            use exploit/listen/php')
        print('      exit                                       退出')
        print('     search            searc + 模块名         搜索模块路径            search php')
        print('  show options                         展示需要填写的选项(已经启用模块)')
        print('  show exploit                               展示所有攻击模块')
        print(' show auxiliary                              展示所有辅助模块')
        print('     run                              开始攻击(已经启动模块并填写好信息)')
        print('     set            set + 选项 + 参数      填写信息(已经启用模块)       set rhost 192.168.0.3') 
        print('    back                                       退出模块')

    elif cmd == 'show auxiliary':
        print('--------------------路径------------------------------作用-------')
        print(' auxiliary/Directory collection                  检索响应中的网址')
        print(' auxiliary/dos                                     dos流量攻击')
        print(' auxiliary/synflood                                syn流量攻击')
        print(' auxiliary/password/ssh                              爆破ssh密码')
        print(' auxiliary/password/windows                        爆破windows密码')
        print(' auxiliary/summon/php                             生成php一句话木马')
        print(' auxiliary/summon/python                         生成后门python文件')
        print(' auxiliary/summon/windows                         生成后门exe执行文件')
        print(' auxiliary/phishing/facebook                     搭建facebook钓鱼网站')
        print(' auxiliary/phishing/IP                            搭建IP获取钓鱼网站')
        print(' auxiliary/phishing/QQmali                       搭建QQ邮箱钓鱼网站')
        print(' auxiliary/phishing/QQ                           搭建QQ登入钓鱼网站')
        print(' auxiliary/phishing/twitter                    搭建twitter登入钓鱼网站')
        print(' auxiliary/phishing/sqlmap-gui                   搭建sqlmap GUIweb界面')
    elif cmd == 'show exploit':
        print('--------------------路径------------------------------作用-------')
        print(' exploit/arp                                     arp欺骗断网攻击(单人)')
        print(' exploit/arpspoof                                arp欺骗断网攻击(整个网段)')
        print(' exploit/wifi/deauth                             wifi deauth攻击(不需要连接网络)')
        print(' exploit/wifi/find-wifi                          寻找周围wifi的MAC')
        print(' exploit/wifi/password-wifi                      爆破wifi密码')
        print(' exploit/listen/python                           python后门监听')
        print(' exploit/listen/php                              连接后门php')
        print(' exploit/listen/windows                           windows后门监听')
    elif cmd[:6] == 'search':
        print('[-]search 命令还没有做好qwq')

    elif cmd == '':
        pass

    elif cmd == 'exit':
        print('[*]goodbye')
        break
    else:
        print("[-]can't find command: " + cmd)
    
