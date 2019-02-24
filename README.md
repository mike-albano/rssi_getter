# RSSI Getter

A simple Python script that prints your clients RSSI and APs POV of your clients RSSI.

## Dependencies

This uses the OSS py_gnmicli client at:
[gNXI Repo](https://github.com/google/gnxi/tree/master/gnmi_cli_py)

The dependencies can be installed to either (1) your host's python environment or (2) within a python virtual environment.

System Python Installation
```
pip install -r requirements.txt
```
You may also need to pip install setuptools.

Virtualenv Installation
```
# install virtualenv
pip install virtualenv

# create a virtual environment
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage Examples
Change the info in constants.py to suit your needs.

Usage example, and output:
```
mbp$python rssi_getter.py
Sun Feb 24 14:01:42 2019
RSSI from AP POV is: -50
RSSI from Client POV is: -54

Sun Feb 24 14:01:46 2019
RSSI from AP POV is: -50
RSSI from Client POV is: -54
...
```
