import py_gnmicli
import json
import constants
import os
import time

TARGET = constants.target
PORT = constants.port
USER = constants.user
PASSWORD = constants.password
AP_NAME = constants.ap_name
SSID = constants.ssid

def get_aprssi(client_mac):
  """Get the APs POV for clients RSSI.

  Args:
    client_mac: (str) Local macbooks MAC address.
  Returns:
    integer of your clients RSSI to the AP.
  """
  xpath = ('/access-points/access-point[hostname=%s]/ssids/ssid[name=%s]/clients/'
          'client[mac=%s]/client-rf/state/rssi' % (AP_NAME, SSID, client_mac))
  paths = py_gnmicli._parse_path(py_gnmicli._path_names(xpath))
  certs = {'root_cert': None, 'private_key': None, 'cert_chain': None}
  if 'mist.com' in constants.target:
    creds = py_gnmicli._build_creds(TARGET, PORT, False, certs, False)
    stub = py_gnmicli._create_stub(creds, TARGET, PORT, None)
  else:
    creds = py_gnmicli._build_creds(TARGET, PORT, True, certs, False)
    stub = py_gnmicli._create_stub(
      creds, TARGET, PORT,'openconfig.mojonetworks.com')
  response = py_gnmicli._get(stub, paths, USER, PASSWORD)
  return response.notification[0].update[0].val.int_val


def get_clientrssi():
  """Get the Clients POV for RSSI.

  Returns:
    integer of your clients RSSI from the AP.
  """
  input = os.popen('/usr/local/sbin/airport -I')
  return int(''.join([x.split()[1] for x in input if 'agrCtlRSSI' in x]))


def get_macbookmac():
  """Get local macbooks en0 MAC address."""
  input = os.popen('ifconfig en0')
  if 'mist.com' in constants.target:
    return ''.join([x.split()[1] for x in input if 'ether' in x])
  return ''.join([x.split()[1] for x in input if 'ether' in x]).upper()


def main():
  client_mac = get_macbookmac()
  while True:
    ap_rssi = get_aprssi(client_mac)
    client_rssi = get_clientrssi()
    print(time.asctime())
    print('RSSI from AP POV is: %i' % ap_rssi)
    print('RSSI from Client POV is: %i\n' % client_rssi)
    time.sleep(3)

if __name__ == '__main__':
  main()
