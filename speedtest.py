import speedtest
import pandas as pd

NUM_TESTS = 2
TEST_NAME = "test 1"

def dl_speed(speedtest):
  return speedtest.download()

def ul_speed(speedtest):
  return speedtest.upload()

if __name__ == "__main__":
  s = speedtest.Speedtest()
  s.get_best_server()
  download = []
  upload = []
  for test in range(0, NUM_TESTS):
    download.append(s.download())
    upload.append(s.upload())


  d = pd.DataFrame(data = [download,upload], columns = ["download","upload"])
  d.to_csv(TEST_NAME + ".csv")
