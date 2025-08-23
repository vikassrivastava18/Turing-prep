import threading
import time

def func(name):
    print("Execiting sleep next")
    time.sleep(5)
    print("Sleep call ended")


if __name__ == '__main__':
    t = threading.Thread(target=func, args=['vikas'])
    t.start()
    print("Program ends.")

