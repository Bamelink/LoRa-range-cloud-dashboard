import numpy as np
from math import sqrt
import paho.mqtt.client as paho
import sys
from time import sleep


flag_connected = 0 #global variable


# ------------------------------------------------------------- GPS DATA ----------------------------------------------------------------------------------
def degreesToRadians(degrees):
    return degrees * np.pi / 180


def distanceInKmBetweenEarthCoordinates(lat1, lon1, lat2, lon2):
  earthRadiusKm = 6372.795477598

  dLat = degreesToRadians(lat2-lat1)
  dLon = degreesToRadians(lon2-lon1)
  
  lon1 = degreesToRadians(lon1)
  lon2 = degreesToRadians(lon2)
  lat1 = degreesToRadians(lat1)
  lat2 = degreesToRadians(lat2)

  a = np.sin(dLat/2) * np.sin(dLat/2) + np.sin(dLon/2) * np.sin(dLon/2) * np.cos(lat1) * np.cos(lat2)
  c = 2 * np.arctan2(sqrt(a), sqrt(1-a))
  return earthRadiusKm * c


def map(x):
    in_min = 0.0
    in_max = 4.0
    out_min = -80.0
    out_max = -160.0
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# ------------------------------------------------------------- MQTT ----------------------------------------------------------------------------------
def on_connect(client, userdata, flags, rc):
   global flag_connected
   flag_connected = 1

def on_disconnect(client, userdata, rc):
   global flag_connected
   flag_connected = 0


def main():
    upper_lat = 52.172188
    lower_lat = 52.135150
    left_long = 9.903338
    right_long = 10.000875

    home = [52.150010, 9.953342]

    data_samples = 100

    #random latitude and longitude values
    latitudes = np.random.uniform(lower_lat, upper_lat, data_samples) #y Werte
    longitudes = np.random.uniform(left_long, right_long, data_samples) #x Werte

    #generate rssi values (the more distance, the lower rssi gets)
    rssi = []
    for i in range(data_samples):
        distance = distanceInKmBetweenEarthCoordinates(latitudes[i],longitudes[i],home[0],home[1])
        rssi.append(int(map(distance)))
    
    #Configure MQTT
    client = paho.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect("192.168.178.63", 1883) #configure ip address and port
    client.loop_start()
    
    for i in range(data_samples):
        msg = f"'{latitudes[i]}', '{longitudes[i]}', {rssi[i]}"
        if flag_connected == 1:
            client.publish("GPS/Testdata", msg, 0)
            sleep(0.1)
            print(i)
        else:
            print("Disconnected, trying to reconnect")
            sleep(2)


if __name__ == "__main__":
    main()