from time import perf_counter, sleep


minFrameDelta = 0.03333
estimate = 0.01

def SpinLock(seconds):
    end = 0
    start = perf_counter()
    while end - start < seconds:
        end = perf_counter()
        
    return

    #print("fps: " + str(round(1/(end - start))))


def halt(seconds):
    while seconds > estimate:
        start = perf_counter()
        sleep(0.001)
        end = perf_counter()
        seconds -= (end - start)

    SpinLock(seconds)
