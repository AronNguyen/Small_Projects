import random

class Coin:

    def _init_(self):
        self.sideup = "Heads"

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()

    print("This side is up", my_coin._init_())
    print("I am tossing the coin ...", my_coin.toss())
    print("It landed on ", my_coin.get_sideup())
print(main())
