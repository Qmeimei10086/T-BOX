# T-BOX
我的QQ号:2991859305  
bilbil账号(有发布视频):离ん殇  
T-BOX是一个小巧可爱的脚本,集成了多个稳定的脚本,于大名鼎鼎的msf操作方式几乎相同  
由python3编写  
适合于 windows / linux  
  
# 需要安装的库:  
scapy  
requests  
flask  
paramiko  
fs.smbfs  
pywifi  
pyinstaller  
  
但是你不一定要全部安装!你可以安装想用的功能,模块简单易读,分为 exploit和auxiliary  
或者cd setup    
python(python3) setup.py来自动安装  
  
# 启动:python(python3) T-BOX.py  
你可以用'?' 或者'help'命令查看帮助  
  
# 亮点:  
exploit/listen/windows模块生成的winodws exe后门免杀效果出奇的好,可以绕过火绒!  
于别的后门不同,它是向我们搭建的网站提供命令执行结果,轻松绕过火绒和防火墙!  

# 注意:后门要配合监听使用,先启动监听在启动生成的后门  
例如:先开启exploit/listen/windows 的监听再开启auxiliary/summon/windows生成的后门  
  
     
感谢你的观看:)  
 
  



















