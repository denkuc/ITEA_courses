from threading import Thread
import random
import time


# def random_generator(num, thread_name):
#     for i in range(num):
#         time.sleep(random.randint(0, 5))
#         print(f"I'm executing from {thread_name}")
#     print(f"The end of {thread_name}")
#
#
# thread1 = Thread(target=random_generator, args=(5, "thread1"))
# thread2 = Thread(target=random_generator, args=(5, "thread2"))
#
# thread1.start()
# thread2.start()
#
# random_generator(5, "main_thread")

#
# def file_writer(filename, num_of_lines):
#
#     with open(filename, "w") as f:
#         for l in range(num_of_lines):
#             f.write(str(random.randint(0, 5000)))
#
#
# list_of_threads = []
#
# for i in range(10):
#     t = Thread(target=file_writer, args=(str(random.randint(0, 5000))+".txt",
#                                          random.randint(0, 100)))
#     list_of_threads.append(t)
#     t.start()
#
# print(list_of_threads)


class RandomGeneratorThread(Thread):
    def __init__(self, num, name):
        Thread.__init__(self, name=name)
        self._num = num
        self._name = name

    def run(self):
        for i in range(self._num):
            time.sleep(random.randint(0, 5))
            print(f"I'm executing from {self._name}")
        print(f"The end of {self._name}")


a = RandomGeneratorThread(10, "Thread a")
b = RandomGeneratorThread(10, "Thread b")
a.daemon = True
b.daemon = True
a.start()
b.start()
