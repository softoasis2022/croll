from pywinauto import findwindows
from pywinauto import application

app = application.Application(backend='uia') 

# 프로세스의 경로를 넣어 실행해준다.
app.start("C:\Program Files (x86)\Melon Player\Melon Player.exe")
#멜론 C:\Program Files (x86)\Melon Player\Melon Player.exe