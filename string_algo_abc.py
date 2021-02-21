from abc import ABC, abstractmethod, abstractproperty


class string_algorithm_abc(ABC):


    @abstractmethod
    def process() -> str:
        pass
