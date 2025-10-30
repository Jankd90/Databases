#data communication & data processing
#databases
#Peter Kamphuis (kapj) Jos Bos (bosj)
#date: 17 january 2024


import network

# Function to read SSID and pasword from secure.txt
def read_credentials():
    with open('secure.txt', 'r') as file:
        lines = file.readlines()
        ssid = lines[0].strip()
        password = lines[1].strip()
        return ssid, password

# Setup connection  with WiFi-network
def connect_to_wifi():
    ssid, password = read_credentials()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connect to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connect to WiFi:', wlan.ifconfig())

# Create connection to WiFi-network
connect_to_wifi()
