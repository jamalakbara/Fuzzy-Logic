class Fuzzification:
    __myuKecil = 0
    __myuBiasa = 0
    __myuGede = 0
    __mKecil = 0
    __mBiasa = 0
    __mGede = 0
    def __init__(self, penghasilan, hutang):
        self.__penghasilan = penghasilan
        self.__hutang = hutang
    # enddef
    def triangularPenghasilan(self):
        if self.__penghasilan >= 0 and self.__penghasilan <= 2:
            if self.__penghasilan == 0:
                self.__mKecil = 1
                self.__mBiasa = 0
                self.__mGede = 0
            elif self.__penghasilan == 1:
                self.__mKecil = 0
                self.__mBiasa = 1
                self.__mGede = 0
            elif self.__penghasilan == 2:
                self.__mKecil = 0
                self.__mBiasa = 0
                self.__mGede = 1
            elif self.__penghasilan > 0 and self.__penghasilan<= 0.25:
                b = float(0)
                c = float(0.5)
                self.__mKecil = (c - self.__penghasilan) / (c - b)
                self.__mBiasa = 0
                self.__mGede = 0
            elif self.__penghasilan >= 0.5 and self.__penghasilan < 1:
                a = float(0.25)
                b = float(1)
                self.__mKecil = 0
                self.__mBiasa = (self.__penghasilan - a) / (b - a)
                self.__mGede = 0
            elif self.__penghasilan > 1 and self.__penghasilan<= 1.25:
                b = float(1)
                c = float(1.5)
                self.__mKecil = 0
                self.__mBiasa = (c - self.__penghasilan) / (c - b)
                self.__mGede = 0
            elif self.__penghasilan >= 1.5 and self.__penghasilan < 2:
                a = float(1.25)
                b = float(2)
                self.__mKecil = 0
                self.__mBiasa = 0
                self.__mGede = (self.__penghasilan - a) / (b - a)
            elif self.__penghasilan > 0.25 and self.__penghasilan < 0.5:
                b1 = float(0)
                c1 = float(0.5)
                a2 = float(0.25)
                b2 = float(2)
                self.__mKecil = (c1 - self.__penghasilan) / (c1 - b1)
                self.__mBiasa = (self.__penghasilan - a2) / (b2 - a2)
                self.__mGede = 0
            elif self.__penghasilan > 1.25 and self.__penghasilan < 1.5:
                b1 = float(1)
                c1 = float(1.5)
                a2 = float(1.25)
                b2 = float(2)
                self.__mKecil = 0
                self.__mBiasa = (c1 - self.__penghasilan) / (c1 - b1)
                self.__mGede = (self.__penghasilan - a2) / (b2 - a2)
            else:
                print('ccd')
            # endif
        # endif
    # enddef
    def trapezoidalHutang(self):
        if self.__hutang >= 0 and self.__hutang <= 100:
            if self.__hutang >= 0 and self.__hutang <= 20:
                self.__myuKecil = 1
                self.__myuBiasa = 0
                self.__myuGede = 0
            elif self.__hutang >= 35 and self.__hutang <= 60:
                self.__myuKecil = 0
                self.__myuBiasa = 1
                self.__myuGede = 0
            elif self.__hutang >= 85:
                self.__myuKecil = 0
                self.__myuBiasa = 0
                self.__myuGede = 1
            elif self.__hutang > 20 and self.__hutang < 35:
                c1 = 20
                d1 = 35
                a2 = 20
                b2 = 35
                self.__myuKecil = (d1 - self.__hutang) / (d1 - c1)
                self.__myuBiasa = (self.__hutang - a2) / (b2 - a2)
                self.__myuGede = 0
            elif self.__hutang > 60 and self.__hutang < 85:
                a1 = 60
                b1 = 85
                c2 = 60
                d2 = 85
                self.__myuKecil = 0
                self.__myuBiasa = (d2 - self.__hutang) / (d2 - c2)
                self.__myuGede = (self.__hutang - a1) / (b1 - a1)
            else:
                print('ccd')
            # endif
        # endif
    # enddef
    def getMKecil(self):
        return self.__mKecil
    # enddef
    def getMBiasa(self):
        return self.__mBiasa
    # enddef
    def getMGede(self):
        return self.__mGede
    # enddef
    def getMyuKecil(self):
        return self.__myuKecil
    # enddef
    def getMyuBiasa(self):
        return self.__myuBiasa
    # enddef
    def getMyuGede(self):
        return self.__myuGede
    # enddef