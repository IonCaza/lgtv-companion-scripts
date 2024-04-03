# Scripts to help in a KVM scenario
Switching between multiple computers isn't natively supported by LGTV Companion. My use case is to switch between Mac and Windows using a KVM. I want to capture USB connection events on both platforms and then automatically turn on the monitors and disable LGTV's auto management mechanism on the disconnected device.

## Mac

### Requirements
`brew install libusb`