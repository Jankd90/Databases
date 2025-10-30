import network, time
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("VRV95171A66FE", "47miVdnLcFCY")
while not wlan.isconnected():
    time.sleep(1)
print(wlan.ifconfig())   # shows ESP32 IP
