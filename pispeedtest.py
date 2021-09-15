import speedtest
import pandas as pd
import time
import blinkt

NUM_TESTS = 5
TEST_NAME = "1ft"

#set the light blue for a download speed test
def set_blue():
  blinkt.clear()
  blinkt.set_brightness(.1)
  for i in range(7):
    blinkt.set_pixel(i, 0, 0, 255)
  blinkt.show()

#set the light red to indicate an upload speed test
def set_red():
  blinkt.clear()
  blinkt.set_brightness(.1)
  for i in range(7):
    blinkt.set_pixel(0, 255, 0, 0)
  blinkt.show()
  
#green is used as a timer, so lights should update individually, therefore show is contained in the loop
def set_green():
  blinkt.clear()
  blinkt.set_brightness(.1)
  for i in range(7):
    blinkt.set_pixel(i, 0, 255, 0)
    time.sleep(1)
    blinkt.show()


  

def dl_speed(speedtest):
  set_blue()
  s = speedtest.download()
  print(s)
  return s

def ul_speed(speedtest):
  set_red()
  s = speedtest.upload()
  print(s)
  return s

if __name__ == "__main__":
  s = speedtest.Speedtest()
  s.get_best_server()

  d = pd.DataFrame(columns = ["download","upload"])

  for test in range(0, NUM_TESTS):
    download = []

    set_green()
    download.append(dl_speed(s))
    download.append(ul_speed(s))
    print(download)
    a = pd.Series(download, index = d.columns)
    d = d.append(a, ignore_index=True)
    print(d)

  print(d)
  d.to_csv(TEST_NAME + ".csv")
