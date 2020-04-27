import blinkt
import os
import re
import subprocess
import time



if __name__ == "__main__":
  response = subprocess.Popen('speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()
  blinkt.set_pixel(0, 255, 255, 255)
  blinkt.show()
  blinkt.set_pixel(0, 255, 255, 255)
  blinkt.show()
  ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
  download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
  upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

  ping[0] = ping[0].replace(',', '.')
  download[0] = download[0].replace(',', '.')
  upload[0] = upload[0].replace(',', '.')
