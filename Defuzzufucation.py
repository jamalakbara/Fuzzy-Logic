class Defuzzification:
    __blt = []
    __zStar = 0
    def __init__(self,aTidak, aCons, aYa, index, data):
        self.__aTidak = aTidak
        self.__aCons = aCons
        self.__aYa = aYa
        self.__index = index
        self.__data = data
    # enddef
    def sugeno(self):
        self.__zStar = float(((self.__aTidak * 50) + (self.__aCons * 70) + (self.__aYa * 100)) / (self.__aTidak + self.__aCons + self.__aYa))
        if self.__zStar >= 70 and self.__zStar < 100:
            self.__blt.append([self.__data[self.__index][0], self.__zStar])
        elif self.__zStar == 100:
            self.__blt.append([self.__data[self.__index][0], self.__zStar])
        # endif
    # enddef
    def getBlt(self):
        return self.__blt
    # endif