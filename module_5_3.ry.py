class House:
        def __init__(self, House):
            self.House = House

        def __eq__(self, other):
            return self.House == other.House

        def __lt__(self, other):
            return self.House < other.House

        def __le__(self, other):
            return self.House <= other.House

        def __gt__(self, other):
            return self.House > other.House

        def __ge__(self, other):
            return self.House >= other.House

        def __ne__(self, other):
            return self.House != other.House

        def __add__(self, value):
            self.House += value
            return self


        def __radd__(self, value):
            return self.__add__(value)

        def __iadd__(self, value):
            return self.__add__(value)

H1 = House(10)
H2 = House(20)
print(H1 == H2)
print(H1 < H2)
print(H1 <= H2)
print(H1 > H2)
print(H1 >= H2)
print(H1 != H2)
H1=H1+10
print(H1==H2)
