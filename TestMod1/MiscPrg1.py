# import speedtest

# speedTest = speedtest.Speedtest()
# print(speedTest.get_best_server())

# #Check download speed
# print(speedTest.download())

# #Check upload speed
# print(speedTest.upload())


# import pyspeedtest
# st = pyspeedtest.SpeedTest()
# st.ping()
# st.download()
# st.upload()

import wmi
data = wmi.WMI()
for os_name in data.Win32_OperatingSystem():
  print(os_name.Caption) # Microsoft Windows 11 Home