import threading
from threading import Lock
from threading import Thread


class Singleton(object):
    cnt = 0
    __singleton = None

    @classmethod
    def createSingleton(cls):
        if cls.__singleton:
            return cls.__singleton

        with Lock():
            cls.__singleton = Singleton()
            cls.cnt += 1


def createSingletons():
    Singleton().createSingleton()
    print(f"total objects created {Singleton.cnt} thread name is {threading.currentThread().getName()}")


if __name__ == "__main__":
    t1 = Thread(target=createSingletons(), args=())
    t2 = Thread(target=createSingletons(), args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# private static object instance rakhna hota h

