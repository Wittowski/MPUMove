from autopy import *
import serial
import sys
import glob
import math

# Global Variable
ScreenX, ScreenY = screen.get_size()
result = []
data = []
print '\n'
print '===================================================================='
print '|| MM    MM PPPPPP  U    U    MM    MM OOOOOO U    U SSSSS EEEEEE ||'
print '|| MMM  MMM P    PP U    U    MMM  MMM O    O U    U SS    E      ||'
print '|| MM MM MM PPPPPP  U    U    MM MM MM O    O U    U SSSSS EEEEEE ||'
print '|| MM    MM P       U    U    MM    MM O    O U    U    SS E      ||'
print '|| MM    MM P       UUUUUU    MM    MM OOOOOO UUUUUU SSSSS EEEEEE ||'
print '===================================================================='
print '\nMPU Mouse is program to move mouse cursor with Arduino MPU detector'

#ListPorts function
def ListPorts():
	i = 0
	ports = ['COM%s' % (i + 1) for i in range(256)]
	for port in ports:
	    try:
	        s = serial.Serial(port)
	        s.close()
	        result.append(port)
	    except (OSError, serial.SerialException):
	        pass
	print '\n\n\nAvailable Port\n'
	arrlen = len(result)        
	for i in range(0,arrlen) :
		print str(i)+'.'+result[i]
#End ListPorts function

#SelectPort function
def SelectPort():
	ListPorts()
	#input selected num
	SelectedNum = raw_input("\nSelect Port : ")
	if SelectedNum != '' :
		try :
			DefX = ScreenX / 2
			DefY = ScreenY / 2 
			mouse.move(DefX,DefY) #Move cursor to center of screen
	   		val = int(SelectedNum)
	   		ser = serial.Serial(result[val], 115200)  # open serial port
			print(ser.name)         # check which port was really used
			for n in range(0,3) :
				print ser.readline()
			ser.write('a')

			while True :				
				strData = ser.readline()
				data = strData.split('/')
				DataX = (float(data[0]) / 100) * ScreenX
				DataY = (float(data[2]) / 100) * ScreenY
				mouse.move(int(DataX),int(DataY))
				# print data[0],data[1],data[2]
				# MoveCursor(int(DataX),int(DataY))
				# print int(MoveX),'X',int(MoveY)

	   	#except if val not int type
		except ValueError :
	   		print("! Number only")
	   		ListPorts()
	#except if val = ''
	else :
		print('! Empty input')
		ListPorts()
#End SelectPort function

#MoveCursor function
# def MoveCursor(MoveX,MoveY):
# 	mouse.move(MoveX, MoveY)
#End MoveCursor function

if __name__ == '__main__':
	SelectPort()


	
