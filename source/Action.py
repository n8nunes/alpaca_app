from abc import ABC, abstractmethod

class Action(ABC):
    @abstractmethod
    def execute (self) -> str:
        pass

    @abstractmethod
    def menudescription (self) -> str:
        pass
