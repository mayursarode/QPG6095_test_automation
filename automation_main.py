# main program for QPG6095 automation
from ptc_example_rx import *
from ptc_example_tx import *
from attenuator_control import *
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



if __name__ == "__main__":
	#Open PTC control for transmitter change COM Port
	interface = "serial"
	arg1 = "COM17"
	arg2 = "57600"
	ptc_tx = ptc_tx(interface, arg1, arg2)
	
	interface_rx = "serial"
	#Open PTC control for receiver change COM Port
	arg1_rx = "COM15"
	arg2_rx = "57600"
	ptc_rx = ptc_rx(interface_rx, arg1_rx, arg2_rx)
	
	#att.init_attenuator()
	tx_p=1000 # Packet count
	int=10 # packet interval
	txp=0 # transmit power 
	start_ch=11 # Intial Zigbee channel
	stop_ch=13   # Final Zigbee channel
	ch_step=1 # Channel step
	i=0
	j=0
	att_start=0 #Start attenuator
	att_step=3 # Attenuation step, change according to interval you need.
	att_stop=3 #Stop attenuator
	for i in range(start_ch,stop_ch+1):
		for j in range (att_start,att_stop+1):
			#Change attenuator
			att.set_attenuator(j)
			# function to initialize Transmitter
			ptc_tx.tx_init(phy='RF4CE', channel=start_ch, power=txp, length=20, count=tx_p, interval =int, duration=5)
			# function to initialize recevier
			ptc_rx.rx_init(phy='RF4CE', channel=start_ch, duration=5)
			# function to start packet transmission
			ptc_tx.tx_packet_send(duration=20)
			# function to see number of packets recevied.
			print("Zigbee Channel number: % d" % i)
			print("Attenuator value:%d" % j)
			ptc_rx.rx_packet_received()
			# function to reset packet count
			ptc_rx.rx_packet_count_reset()