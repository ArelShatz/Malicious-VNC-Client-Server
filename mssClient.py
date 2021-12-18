from vidgear.gears import ScreenGear
from vidgear.gears import NetGear
import cv2
import time
import zlib


def SpinLock(seconds):
    end = 0
    start = time.perf_counter()
    while end - start < seconds:
        end = time.perf_counter()
        
    return

    #print("fps: " + str(round(1/(end - start))))


def halt(seconds):
    while seconds > estimate:
        start = time.perf_counter()
        time.sleep(0.001)
        end = time.perf_counter()
        seconds -= (end - start)

    SpinLock(seconds)


minFrameDelta = 0.016666
estimate = 0.01


client = NetGear(
    receive_mode=True,
    address="192.168.1.132",
    port="5900",
    protocol="tcp",
    pattern=1,
    logging=False
)

while True:

    #frameStart = time.perf_counter()
    
    frame = client.recv()
    #frame = zlib.decompress(frame)
    cv2.imshow("Output Frame", frame)
    
    #frameEnd = time.perf_counter()
    #frameTimeElapsed = frameStart - frameEnd
    #halt(minFrameDelta - frameTimeElapsed)
    #frameWaitPeriodEnd = time.perf_counter()
    #print(1/ (frameWaitPeriodEnd - frameStart))
    

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
client.close()
