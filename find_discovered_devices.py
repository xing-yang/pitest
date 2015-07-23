#!/usr/bin/env python

# Use python bluetooth bindings
import bluetooth
import cPickle as pickle

pkl_file = open('bluetooth_devices.pkl', 'rb')
mydicts = pickle.load(pkl_file)
pkl_file.close()
print mydicts

# List the currently seen devices
devices = bluetooth.discover_devices(flush_cache=True, lookup_names=True)

found_dev = None
for device_address, name in devices:
   for mydev in mydicts:
       if mydev['address'] == device_address:
           print "Found Device: %s -> %s" % (device_address, name)
           found_dev = mydev
           break
