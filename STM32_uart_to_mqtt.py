import serial.tools.list_ports
import paho.mqtt.client as paho
import sys
from time import sleep

flag_connected = 0

def on_connect(client, userdata, flags, rc):
   global flag_connected
   flag_connected = 1

def on_disconnect(client, userdata, rc):
   global flag_connected
   flag_connected = 0


#Configure Serial Communication
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")
for x in range(0,len(portList)):
    if portList[x].startswith("COM"+str(val)):
        portVar = "COM" + str(val)
        print(portList[x])
        
br = 115200
try:
    serialInst.baudrate = int(br)
    serialInst.port = portVar
    serialInst.open()
except serial.serialutil.SerialException:
    print("Error: Port not found")
    print("Did you plug in the device and select the correct port?")
    print("Exiting...")
    exit(-1)

ip = "192.168.178.114"
mqttPort = 1883
mqttTopic = input("Set MQTT Topic to publish data on: ")
if not mqttTopic:
    print("ERROR: No MQTT Topic Set")
    print("Exiting...")  
    exit(-1)

#Configure MQTT
client = paho.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect(ip, int(mqttPort))
client.loop_start()

adcVal = 0
while(1):
    if serialInst.in_waiting:
        try:
            packet = serialInst.readline()
            packet = packet.decode('utf')
            geohash = packet[packet.find("data:")+6 : packet.find("(RSSI:")-1] # Geohash in Nodered doesnt support full 12 presicion unfortunately
            rssi = int(packet[packet.find("RSSI:")+5 : packet.find("SNR:")-5])
            print(f"Received geohash: {geohash} with a single strength of {rssi}")
            if flag_connected == 1:
                client.publish(mqttTopic, f"{geohash}, {rssi}",0) # (mqttTopic, "u1r09m2vy, -60", 0)
            else:
                print("Disconnected, trying to reconnect")
                sleep(2)
        except:
            pass