from threading import Thread
import requests as r


def thread_decorator(thread_name, is_daemon):
    def inner_decorator(func):
        def wrapper(link_string):
            print(f"{thread_name} is started")
            print(f"{link_string} is downloading now")
            thread = Thread(target=func, args=thread_name, daemon=is_daemon)
            thread.start()
        return wrapper
    return inner_decorator


@thread_decorator("Thread", False)
def download_file(link_string):
    r.get(link_string)


links_list = [
    'https://www.wikipedia.org/',
    'https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)',
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://en.wikipedia.org/wiki/Decorator_pattern',
    'https://en.wikipedia.org/wiki/Singleton_pattern',
    'https://en.wikipedia.org/wiki/Software_design_pattern',
    'https://en.wikipedia.org/wiki/Stack_(abstract_data_type)',
    'https://en.wikipedia.org/wiki/Queue_(abstract_data_type)',
    'https://en.wikipedia.org/wiki/Thread_(computing)',
    'https://en.wikipedia.org/wiki/Process_(computing)',
]

for link in links_list:
    download_file(link)
