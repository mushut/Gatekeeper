import data_packet
import paho.mqtt.client as mqttClient
import time
import json
import gps_data


def main():
    print("Gatekeeper for Fleet Application")
    gps_receiver = gps_data.gps_data()
    index = 0

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            global Connected
            Connected = True
        else:
            print("Connection failed")

    Connected = False

    broker_address = "m21.cloudmqtt.com"
    port = 14655
    user = "lvwvnzhs"
    password = "nqpqsMe0M0Q2"
    client = mqttClient.Client("GPSBroker")
    client.username_pw_set(user, password=password)
    client.on_connect = on_connect
    client.connect(broker_address, port=port)
    client.loop_start()

    #client.publish("GPS/coordinates", payload=json.dumps(data.return_json()), qos=2, retain=False)

    log = open("/home/fleetmaster/Gatekeeper/driving_log.txt", "a")
    log.write("NEW LOG\n")


    while True:
        if index < 60:
            coord_data = gps_receiver.read_gprmc()
            #coord_data = [0.0, 0.0]
            data = data_packet.data_packet(coord_data, index)
            log.write(data.return_log_data())
            #print(data.return_log_data(), end='')
            #mqtt_sender.send_data(data.return_json())
            client.publish("GPS/coordinates", payload=data.return_json(), qos=2, retain=False)

            index += 1
        else:
            index = 0
        
        time.sleep(1)


main()
