class Inference:
    __aTidak = 0
    __aCons = 0
    __aYa = 0
    def __init__(self, myuKecil, myuBiasa, myuGede, mKecil, mBiasa, mGede):
        self.__myuKecil = myuKecil
        self.__myuBiasa = myuBiasa
        self.__myuGede = myuGede
        self.__mKecil = mKecil
        self.__mBiasa = mBiasa
        self.__mGede = mGede
    # enddef
    def fuzRules(self):
        if self.__myuKecil > 0 and self.__mKecil > 0:
            self.__aTidak = min(self.__myuKecil, self.__mKecil)

        if self.__myuKecil > 0 and self.__mBiasa > 0:
            self.__aTidak = min(self.__myuKecil, self.__mBiasa)

        if self.__myuKecil > 0 and self.__mGede > 0:
            self.__aTidak = min(self.__myuKecil, self.__mGede)

        if self.__myuBiasa > 0 and self.__mKecil > 0:
            self.__aCons = min(self.__myuBiasa, self.__mKecil)

        if self.__myuBiasa > 0 and self.__mBiasa > 0:
            self.__aCons = min(self.__myuBiasa, self.__mBiasa)

        if self.__myuBiasa > 0 and self.__mGede > 0:
            self.__aTidak = min(self.__myuBiasa, self.__mGede)

        if self.__myuGede > 0 and self.__mKecil > 0:
            self.__aYa = min(self.__myuGede, self.__mKecil)

        if self.__myuGede > 0 and self.__mBiasa > 0:
            self.__aYa = min(self.__myuGede, self.__mBiasa)

        if self.__myuGede > 0 and self.__mGede > 0:
            self.__aTidak = min(self.__myuGede, self.__mGede)

    # enddef
    def getATidak(self):
        return self.__aTidak
    # enddef
    def getACons(self):
        return self.__aCons
    # enddef
    def getAYa(self):
        return self.__aYa
    # enddef