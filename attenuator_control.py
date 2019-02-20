#code to set and reset attenuator
import serial

#def set_attenuator():

class att:
	def __init__(self, interface, arg1 , arg2):
		s_att=serial.Serial(port='COM30', bauddrate=9600, bytesize=8, parity='N', stopbits=1,timeout=1)

	def init_attenuator():
		s_w1 = 'sa1 '+ str(0)+'\r'
		s_att.write(s_w1)
		s_att.write("\n")
		s_read = s_att.readline()
		print(s_read)
		s_att.close()

	def set_attenuator(att):
		s_w1= 'sa1 '+ str(att)+'\r'
		s_att.write(s_w1)
		s_att.write("\n")
		s_read=s_att.readline()
		print(s_read) 
		s_att.close()




