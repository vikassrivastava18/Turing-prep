import random
from concurrent.futures import ThreadPoolExecutor
import threading

producers = []
consumers = []

class Pipeline:
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
        self.prod_lock = threading.Lock()
        self.cons_lock = threading.Lock()
        # Consumer must wait initially
        self.cons_lock.acquire()

    def set_message(self, message):
        self.prod_lock.acquire()
        print(f'Producing message: {message}')
        producers.append(message)
        self.message = message
        self.cons_lock.release()

    def get_message(self):
        self.cons_lock.acquire()
        print(f'Consuming message: {self.message}')
        message = self.message
        consumers.append(message)
        self.prod_lock.release()
        return message

def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1, 100)
        pipeline.set_message(message)

    pipeline.set_message('The End.')

def consumer(pipeline):
    import time
    message = None
    while message != 'The End.':
        message = pipeline.get_message()
        time.sleep(random.random())

if __name__ == '__main__':
    pipeline = Pipeline(5)
    with ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline)
        ex.submit(consumer, pipeline)

    print("Produced:", producers)
    print("Consumed:", consumers)

