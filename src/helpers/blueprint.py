from abc import ABC, abstractmethod

class ModelBlueprint(ABC):
    @property
    @abstractmethod
    def model(self):
        pass
    
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def run(self):
        pass
