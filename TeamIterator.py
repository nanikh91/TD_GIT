class TeamIterator:
    def __init__(self, team):
        self.__team = team
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__team):
            result = self.__team[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration