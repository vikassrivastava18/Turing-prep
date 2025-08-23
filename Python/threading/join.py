import threading
import time

def func(name):
    print(f'Hello: {name}')
    time.sleep(5)
    print("func call completed.")


if __name__ == '__main__':
    print("In the main thread")
    t = threading.Thread(target=func, args=['vikas'])
    t.start()
    t.join()
    print("Main thread ends!.")
