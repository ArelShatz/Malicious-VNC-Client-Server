from os import system, path
from sys import path as sys_path

pip_safe_path = path.dirname(sys_path[1]) + "\Scripts\pip.exe"
commands = [f'{pip_safe_path} install ', f'pip install ']

packages = ["pyscreenshot", "mss", "opencv-python", "colorlog", "PyQt5", "simplejpeg", "zmq", "pynput", "numpy", "tqdm", "requests", "Pillow", "win32gui"]

for cmd in commands:
    for pkg in packages:
        print(f'Installing {pkg}...')
        output = system(cmd + pkg)
        if output == 0:
            print("successfuly installed\n")

        elif output == 1:
            print("pip doesn't exist on this system\n")
            break
