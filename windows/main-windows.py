import wmi

raw_wql1 = "SELECT * FROM __InstanceCreationEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
c = wmi.WMI ()
watcher1 = c.watch_for(raw_wql=raw_wql1)

raw_wql2 = "SELECT * FROM __InstanceDeletionEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
watcher2 = c.watch_for(raw_wql=raw_wql2)

while 1:
  usb1 = watcher1 ()
  usb2 = watcher2 ()
  print('usb1 ' + usb1)
  print('usb2 ' + usb2)
  # "USB\\VID_0781&PID_5567\\03001211011823044706": #Sandisk usb
  # "USB\\VID_1341&PID_0001\\8&7D461FC&0&4": #lavry
  if usb1.DeviceID == "USB\\VID_0781&PID_5567\\03001211011823044706": #Sandisk usb
    print("pluggedin")
  if usb2.DeviceID == "USB\\VID_0781&PID_5567\\03001211011823044706": #Sandisk usb
    print("unplugged")