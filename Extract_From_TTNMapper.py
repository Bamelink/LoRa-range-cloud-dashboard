from datetime import date
from time import sleep
import pandas as pd # pip install pandas
import pygeohash as pgh # pip install pygeohash
import paho.mqtt.client as paho # pip install paho-mqtt

flag_connected = 0

def on_connect(client, userdata, flags, rc):
   global flag_connected
   flag_connected = 1

def on_disconnect(client, userdata, rc):
   global flag_connected
   flag_connected = 0
   
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

today = date.today()

startdate = input("Enter startdate int format yyyy-mm-dd (default today, type 'all' to get all data): ")
if startdate.lower() == "all":
    startdate = ""
elif not startdate:
    startdate = today.strftime("%Y-%m-%d")

link = f"https://ttnmapper.org/gateways/csv-pg.php?gateway=haemi-gate&startdate={startdate}&enddate=&gateways=on&lines=on&points=on"

data = pd.read_csv(link)

values = []
for i in range(data.shape[0] - 1):
    values.append({
        "spreading factor": data["spreading factor"][i],
        "geohash": pgh.encode(data["latitude"][i], data["longitude"][i], precision=9),
        "rssi": data["rssi"][i]
    })
    
for value in values:
    text = "{geohash}, {rssi}".format(geohash = value["geohash"], rssi = value["rssi"])
    mqttTopic_with_SF = f'{mqttTopic}_SF{int(value["spreading factor"])}'
    print(mqttTopic_with_SF)
    if flag_connected == 1:
        client.publish(mqttTopic_with_SF, text,0)
    else:
        print("Disconnected, trying to reconnect")
        sleep(2)