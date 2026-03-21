import time as tm


a = tm.time()
while tm.time() - a<=0.2:
    print("time",tm.time()-a)