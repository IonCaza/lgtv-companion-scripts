import usb.core

def list_connected_devices():
    devices = usb.core.find(find_all=True)

    for device in devices:
        print(f"Device: {device.product} (Vendor ID: {device.idVendor}, Product ID: {device.idProduct})")

while 1:
    list_connected_devices()