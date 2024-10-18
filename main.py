from ESPythoNOW import *
import os
import time

_interface = str(os.getenv("INTERFACE", "wlxc01c3038d5a8"))

def callback(from_mac, to_mac, msg):
  print("ESP-NOW message from %s to %s: %s" % (from_mac, to_mac, msg))

espnow = ESPythoNow(interface=_interface, accept_all=True, callback=callback)
espnow.start()
print("sniffing packets")

while True:
    print("send packet")
    espnow.send("FF:FF:FF:FF:FF:FF", "hello from docker")
    time.sleep(3)