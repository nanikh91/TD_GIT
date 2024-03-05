from abc import ABC, abstractmethod

class Team(ABC):
    def __init__(self, members):
        self._members = members

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]

    @abstractmethod
    def __iter__(self):
        pass