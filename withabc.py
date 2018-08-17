import abc
import logging

class Event:

    def __init__(self):
        self.observers = []
        self.subject_state = None

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except:
            raise ValueError("Handler is not handling this event, so cannot unhandle it.")
        return self

    def fire(self, *args, **kargs):
        for event in self.observers:
            event(*args, **kargs)

    @property
    def subject_state(self):
        return self.subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self.subject_state = arg
        self.fire()


class Observer(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def newmessage(self, arg):
        pass


class CreatingEvent(Observer):

    def newmessage(self, arg):
        self._observer_state = arg
        return self._observer_state



if __name__ == "__main__":
    main()
