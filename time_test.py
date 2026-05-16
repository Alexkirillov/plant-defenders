import time


time2 = time.time()
while True:
    if time.time() - time2 >= 1:
        print(round(time.time() - time2))