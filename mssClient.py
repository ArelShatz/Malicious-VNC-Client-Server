from vidgear.gears import ScreenGear
from vidgear.gears import NetGear
import cv2
import time


client = NetGear(receive_mode=True)

while True:

    frame = client.recv()
    cv2.imshow("Output Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
client.close()
