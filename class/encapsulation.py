class Wallet:
    # def __init__(self, money):
    #     self.__money = money    

    def show_money(self, money):
        print(f"Money in wallet is {money}")

wallet = Wallet()
wallet.show_money(1000)
# wallet.__money = 5000
# print(wallet.__money)
# # wallet.show_money()