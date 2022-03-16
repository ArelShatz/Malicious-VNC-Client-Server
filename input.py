import sys
import time

sys.path.append(sys.path[0] + "\\externals")    #add the externals folder to the path in order to import external dependencies
from pynput import keyboard, mouse


"""def on_click(x, y, button, pressed):
        help(button)

listener = mouse.Listener(
        on_click=on_click,
        suppress=False)

listener.start()
listener.join()"""

def keyPressed(key):
        if key == keyboard.Key.esc:
                return False
        
def keyReleased(key):
	pass

def win32_block(msg, data):
        if data.vkCode != 0x1B:
                listener._suppress = True

        else:
                listener._suppress = False

        return True


if __name__ == "__main__":
	listener = keyboard.Listener(
		on_press=keyPressed,
		on_release=keyReleased,
		win32_event_filter=win32_block)

	listener.start()
	listener.join()
	#while True: time.sleep(0.01)



"""import asyncio

async def keyboardEvents():
	with keyboard.Events() as events:
		event = await events.get()
		if event is not None:
			print(event)


async def main():
	i = 0
	task = asyncio.create_task(keyboardEvents())

	while True:
		await asyncio.sleep(0.5)
		print(i)
		i += 1


if __name__ == "__main__":
	asyncio.run(main())



async def asyncInput():
        a = input()
        print("input was" + str(a))


async def main():
        i = 0
        while True:
                await asyncInput()
                print(i)
                i += 1


if __name__ == "__main__":
	asyncio.run(main())"""

