import speedtest
import pandas as pd
import time
import blinkt

NUM_TESTS = 2
TEST_NAME = "test 1"

def set_green():
  blinkt.clear()
  blinkt.set_brightness(.1)
  blinkt.set_pixel(0, 0, 255, 0)
  time.sleep(1)
  blinkt.show()
  blinkt.set_pixel(1, 0, 255, 0)
  time.sleep(1)
  blinkt.show()
  blinkt.set_pixel(2, 0, 255, 0)
  time.sleep(1)
  blinkt.show()
  blinkt.set_pixel(3, 0, 255, 0)
  time.sleep(1)
  blinkt.show()
  blinkt.set_pixel(4, 0, 255, 0)
  time.sleep(1)
  blinkt.show()
  blinkt.set_pixel(5, 0, 255, 0)
  time.sleep(1)
  blinkt.show()
  blinkt.set_pixel(6, 0, 255, 0)
  time.sleep(1)
  blinkt.show()
  blinkt.set_pixel(7, 0, 255, 0)
  time.sleep(1)
  blinkt.show()

def set_blue():
  blinkt.clear()
  blinkt.set_brightness(.1)
  blinkt.set_pixel(0, 0, 0, 255)
  blinkt.set_pixel(1, 0, 0, 255)
  blinkt.set_pixel(2, 0, 0, 255)
  blinkt.set_pixel(3, 0, 0, 255)
  blinkt.set_pixel(4, 0, 0, 255)
  blinkt.set_pixel(5, 0, 0, 255)
  blinkt.set_pixel(6, 0, 0, 255)
  blinkt.set_pixel(7, 0, 0, 255)
  blinkt.show()

def set_red():
  blinkt.clear()
  blinkt.set_brightness(.1)
  blinkt.set_pixel(0, 255, 0, 0)
  blinkt.set_pixel(1, 255, 0, 0)
  blinkt.set_pixel(2, 255, 0, 0)
  blinkt.set_pixel(3, 255, 0, 0)
  blinkt.set_pixel(4, 255, 0, 0)
  blinkt.set_pixel(5, 255, 0, 0)
  blinkt.set_pixel(6, 255, 0, 0)
  blinkt.set_pixel(7, 255, 0, 0)
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
