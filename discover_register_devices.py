#!/usr/bin/env python

# Use python bluetooth bindings
import bluetooth
import cPickle as pickle

# List the currently seen devices
devices = bluetooth.discover_devices(flush_cache=True, lookup_names=True)

bt_dicts = []
for device_address, name in devices:
   print "Device: %s -> %s" % (device_address, name)
   bt_dicts.append({'address': device_address, 'name': name})
output = open('bluetooth_devices.pkl', 'wb')
pickle.dump(bt_dicts, output)
output.close()

pkl_file = open('bluetooth_devices.pkl', 'rb')
mydicts = pickle.load(pkl_file)
pkl_file.close()
print mydicts
