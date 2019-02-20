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

class ptc_rx:
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

    def rx_init(self, phy, channel, duration=5):
        print "Configure transmitter"
        res = self.ex.Execute("R")
        for m in res.Messages: print m
        res = self.ex.Execute("AN 0")
        for m in res.Messages: print m
        res = self.ex.Execute("PHY"+ phy) 
        for m in res.Messages: print m
        res = self.ex.Execute("CH "+str(channel))
        for m in res.Messages: print m
        res = self.ex.Execute("RX ON")
        for m in res.Messages: print m
        print "******************************Receiver configuration*************************************************"
        #res = self.ex.Execute("I")
        #for m in res.Messages: print m
        print "Done"

    def rx_packet_received(self):
		print "Received packet count"
		res = self.ex.Execute("P")
		for m in res.Messages: print m
		time.sleep(2)
		
    def rx_packet_count_reset(self):
		print "Received packet count"
		res = self.ex.Execute("R")
		for m in res.Messages: print m
		#res = self.ex.Execute("P") 
		#for m in res.Messages: print m

#if __name__ == "__main__":
#	interface = "serial"
#	arg1 = "COM15"
#	arg2 = "57600"
#	ptc = ptc(interface, arg1, arg2)
#	ch=13
    # transmit RF4CE packets with random payload
#	ptc.rx_init(phy='RF4CE', channel=ch, duration=5)
    # send out a carrier wave
#	ch=12
#	ptc.rx_channel(channel=ch,duration=2)
    # receive packets
#	ptc.rx_packet_received()
	#packet count reset
#	ptc.rx_packet_count_reset()
