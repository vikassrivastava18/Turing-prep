import time

def func(name):
    print(f'Hello: {name}')
    time.sleep(5)
    print("func call completed.")


if __name__ == '__main__':
    print("Testing threading")
    func("vikas")
    print("The end!.")
