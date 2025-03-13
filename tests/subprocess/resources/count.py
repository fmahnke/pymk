import sys
import time

stop = 5
sleep_time = 1.0

for index, arg in enumerate(sys.argv[1:]):
    if index == 0:
        stop = int(arg)
    elif index == 1:
        sleep_time = float(arg)

for it in range(stop):
    print(f'{it}')

    time.sleep(sleep_time)

if stop == 0:
    sys.exit(1)
