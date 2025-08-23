import threading
import concurrent.futures
import time

def func(name):
    print(f'Hello: {name}')
    time.sleep(5)
    print(f'func with {name} call completed.')


if __name__ == '__main__':
    print("Testing threading")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as t:
        t.map(func, ['foo1', 'foo2', 'foo3'])
    print("The end!.")
