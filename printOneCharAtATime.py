import time, sys

def printThenWait(line):
  for char in line:
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.1)
  time.sleep(0.5)
  print()

printThenWait("this is line 1")
printThenWait("this is line 2")
