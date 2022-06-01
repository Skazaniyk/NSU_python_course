PRICE_USD = 100


class Money:
    @property
    def rubles(self):
        return self.value

    @rubles.setter
    def rubles(self, value):
        self.value = value

    @property
    def dollar(self):
        return self.value

    @dollar.setter
    def dollar(self, value):
        self.value = value

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.rubles == other.rubles

    def __ne__(self, other):
        return self.rubles != other.rubles

    def __lt__(self, other):
        return self.rubles < other.rubles

    def __gt__(self, other):
        return self.rubles > other.rubles

    def __le__(self, other):
        return self.rubles <= other.rubles

    def __ge__(self, other):
        return self.rubles >= other.rubles


class Dollar(Money):
    @property
    def rubles(self):
        return self.value * PRICE_USD

    @rubles.setter
    def rubles(self, value):
        self.value += value / PRICE_USD

    def __add__(self, other):
        return Dollar(self.value + other.dollar)


class Ruble(Money):
    @property
    def dollar(self):
        return self.value / PRICE_USD

    @dollar.setter
    def dollar(self, value):
        self.value += value * PRICE_USD

    def __add__(self, other):
        return Ruble(self.value + other.rubles)


wallet_1 = Ruble(0)
wallet_2 = Dollar(0)
wallet_1 += Ruble(100)
wallet_1 += Dollar(-2)
wallet_1 += Ruble(20)
wallet_2 += Dollar(100)
wallet_2 += Ruble(-1000)

print(wallet_1.rubles)
print(wallet_1.dollar)
print(wallet_2.rubles)
print(wallet_2.dollar)

print(wallet_1 == wallet_2)
print(wallet_1 != wallet_2)
print(wallet_1 < wallet_2)
print(wallet_1 <= wallet_2)
print(wallet_1 > wallet_2)
print(wallet_1 >= wallet_2)
