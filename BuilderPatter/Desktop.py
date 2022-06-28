import abc


class Desktop(object):
    def __init__(self):
        self.keyboard = None
        self.processor = None
        self.ram = None
        self.monitor = None

    def setRam(self, ram):
        self.ram = ram

    def setMonitor(self, monitor):
        self.monitor = monitor

    def setProcessor(self, processor):
        self.processor = processor

    def setKeyboard(self, keyboard):
        self.keyboard = keyboard

    def printSpecs(self):
        return {
            "name": self.ram,
            "monitor": self.monitor,
            "processor": self.processor,
            "keyboard":self.keyboard
        }


class DesktopImplementor(metaclass=abc.ABCMeta):
    def __init__(self):
        self.desktop = Desktop()

    @abc.abstractmethod
    def buildRam(self):
        pass

    @abc.abstractmethod
    def buildMonitor(self):
        pass

    @abc.abstractmethod
    def buildProcessor(self):
        pass

    @abc.abstractmethod
    def buildKeyboard(self):
        pass

    def getDesktop(self):
        return self.desktop


class HPDesktopImplementor(DesktopImplementor):

    def buildRam(self):
        self.desktop.setRam("HP ramp")

    def buildMonitor(self):
        self.desktop.setMonitor("HP Monitor")

    def buildProcessor(self):
        self.desktop.setProcessor("HP processor")

    def buildKeyboard(self):
        self.desktop.setKeyboard("HP keyboard")


class DellDesktopImplementor(DesktopImplementor):

    def buildRam(self):
        self.desktop.setRam("Dell ramp")

    def buildMonitor(self):
        self.desktop.setMonitor("Dell Monitor")

    def buildProcessor(self):
        self.desktop.setProcessor("Dell processor")

    def buildKeyboard(self):
        self.desktop.setKeyboard("Dell keyboard")


class Director(object):

    def __init__(self, desktopImplementor):
        self.desktopImplementor = desktopImplementor

    def createDesktop(self):
        self.desktopImplementor.buildRam()
        self.desktopImplementor.buildKeyboard()
        self.desktopImplementor.buildMonitor()
        self.desktopImplementor.buildProcessor()

    def getDesktop(self):
        return self.desktopImplementor.getDesktop()


if __name__ == "__main__":
    hpDirector = Director(HPDesktopImplementor())
    dellDirector = Director(DellDesktopImplementor())
    hpDirector.createDesktop()
    dellDirector.createDesktop()
    specs = hpDirector.getDesktop().printSpecs()
    print(specs)
    specs = dellDirector.getDesktop().printSpecs()
    print(specs)
