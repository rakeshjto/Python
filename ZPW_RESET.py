import pyautogui,time,subprocess
subprocess.Popen(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")
pyautogui.PAUSE = 4
pyautogui.moveTo(100, 100)
pyautogui.click()
pyautogui.typewrite('00700143', interval=0)
pyautogui.PAUSE = 1
pyautogui.press(['tab']) 
password= 'bsnl@222'
pyautogui.typewrite(password, interval=0)
pyautogui.press(['enter'])
#pyautogui.PAUSE = 5
pyautogui.typewrite('ZPW_RESET', interval=0)
pyautogui.press(['enter'])
userid= pyautogui.prompt(text='', title='Enter SAP GUI ID' , default='')
pyautogui.typewrite(userid, interval=0)
option1= pyautogui.confirm(text='Do You want to reset Password Only', title='', buttons=['OK', 'Cancel'])
if option1== 'OK': #Password Reset Only
	pyautogui.press(['tab']) 
	pyautogui.press('down')
	pyautogui.press('down')
	pyautogui.press('f8')
	pyautogui.typewrite('bsnlelr@123', interval=0)	
	pyautogui.press(['tab']) 
	pyautogui.typewrite('bsnlelr@123', interval=0)	
	pyautogui.press(['enter'])
if option1== 'Cancel': 
	option2= pyautogui.confirm(text='Do You want to Unlock Only', title='', buttons=['OK', 'Cancel'])
	if option2== 'OK': ##Unlock Only 
		pyautogui.press(['tab']) 
		pyautogui.press('down')
		pyautogui.press('f8')
		pyautogui.press(['enter'])
	if option2== 'Cancel': #Both Unlock & Password Reset 
		pyautogui.press(['tab']) 
		pyautogui.press('down')
		pyautogui.press('f8')
		pyautogui.press(['enter'])
		pyautogui.press(['tab']) 
		pyautogui.press('down')
		pyautogui.press('f8')
		pyautogui.typewrite('bsnlelr@123', interval=0)	
		pyautogui.press(['tab']) 
		pyautogui.typewrite('bsnlelr@123', interval=0)	
		pyautogui.press(['enter'])
pyautogui.hotkey('alt', 'y')
pyautogui.press('up')
pyautogui.press(['enter'])
pyautogui.press(['tab']) 
pyautogui.press(['enter'])

