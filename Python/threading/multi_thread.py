import threading
import time


def func1(name):
    print(f'Hello: {name}')
    time.sleep(5)
    print("func1 call completed.")


def func2(name):
    print(f'Hello: {name}')
    time.sleep(5)
    print("func2 call completed.")


def func3(name):
    print(f'Hello: {name}')
    time.sleep(5)
    print("func3 call completed.")

if __name__ == '__main__':
    print("Starting the main thread execution.")
    t1 = threading.Thread(target=func1, args=['foo'])
    t1.start()

    t2 = threading.Thread(target=func2, args=['foo foo'])
    t2.start()
    
    t3 = threading.Thread(target=func3, args=['foo foo foo'])
    t3.start()
    
    print("Main thread executed")

