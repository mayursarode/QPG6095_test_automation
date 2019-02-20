import os, sys, inspect, time

# import Python for .NET
import clr

# add the location of the PTCDriver.dll and TestCompsInterfaceContract.dll to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"dependencies")))

# import PTCDriver DLL
clr.AddReference("PTCDriver")
from Qorvo.Drivers.PTC import *

# define the location of the PTC dll extension files 
# for this example, they are located in the subfolder "extensions"
extensions_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"extensions"))

class ptc_tx:
    # this example uses an ethernet connection. USB and serial are also possible
    def __init__(self, interface, arg1 , arg2):
        self.ex = Executor(extensions_path)
        if interface == 'serial':
            res = self.ex.InitSerial(arg1, int(arg2))
        else: # ethernet
            res = self.ex.InitEthernet(arg1, arg2)

        for m in res.Messages: print m
        if not res.Success:
            for m in res.ErrorMessages: print m
            raise Exception("Unable to connect to PTC")

    def tx_init(self, phy, channel, power, length,count,interval, duration):
        print "Configure transmitter"
        res = self.ex.Execute("R")
        for m in res.Messages: print m
        res = self.ex.Execute("PHY"+ phy) 
        for m in res.Messages: print m
        res = self.ex.Execute("MR 0")  		
        for m in res.Messages: print m
        res = self.ex.Execute("AN 0")  		
        for m in res.Messages: print m
        res = self.ex.Execute("PACKETLENGTH " + str(length))      
        for m in res.Messages: print m
        res = self.ex.Execute("CH" + str(channel))                
        for m in res.Messages: print m
        res = self.ex.Execute("W " + str(power))                  
        for m in res.Messages: print m
        res = self.ex.Execute("PACKETCOUNT " + str(count))
        for m in res.Messages: print m
        res = self.ex.Execute("SETTXDATA aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        for m in res.Messages: print m
        res = self.ex.Execute("PACKETINTERVAL "+ str(interval))
        for m in res.Messages: print m
        print "**********************Transmitter configuration***********************************************"
        #res = self.ex.Execute("I")
        #for m in res.Messages: print m
        print "Done"

    def tx_packet_send(self, duration):
		print "Start packet transmission"
		res = self.ex.Execute("TX ON")
		time.sleep(duration)
		print("DONE")
		print "*******Total number of packets received*******"
		#res = self.ex.Execute("P") 
		#for m in res.Messages: print m
		#print "Done" 

    def tx_packet_reset(self,duration):
		print "Reset packet count"
		res = self.ex.Execute("R")
		for m in res.Messages: print m
		#res = self.ex.Execute("P") 
		#for m in res.Messages: print m

#if __name__ == "__main__":
    #interface = "serial"
    #arg1 = "COM17"
    #arg2 = "57600"
    #ptc_tx = ptc_tx(interface, arg1, arg2)
    # transmit RF4CE packets with random payload
    #ptc.tx_init(phy='RF4CE', channel=11, power=0, length=20, count=1000, interval =10, duration=5)
    # send out a carrier wave
    #ptc.tx_packet_send(duration=15)
    # receive packets
    #ptc.tx_packet_reset(duration=2)
