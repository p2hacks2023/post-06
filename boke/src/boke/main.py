import os
import glob
import time
import random

def main():
  paths = glob.glob("data/speech/[!_]*.mp3")

  random.shuffle(paths)

  for path in paths:
    file = path.split("/")[-1]
    print(file)

    os.system("afplay " + path)

    time.sleep(30)


if __name__ == "__main__":
  main()