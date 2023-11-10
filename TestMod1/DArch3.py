# Loose coupling between Python classes will look like :
class Person:
    def __init__(self, goods, money=0):
        """
        :param goods: list
        :param money: int
        """
        self.money = money
        self.goods = goods


class Buyer(Person):
    def buy(self, product_name, price):
        """
        :param product_name: str
        :param price: int
        :return: None
        """
        self.goods.append(product_name)
        self.money -= price


class Seller(Person):
    def sell(self, product_name, price):
        """
        :param product_name: str
        :param price: int
        :return: None
        """
        product_position = self.goods.index(product_name)
        del self.goods[product_position]
        self.money += price


class DealsManager:
    def __init__(self):
        self._prices = {"apples": 10, "bread": 5}

    def sell_a_product(self, product_name, buyer, seller):
        """
        :param product_name: str
        :param buyer: Buyer class instance
        :param seller: Seller class instance
        :return: buyer instance, seller instance, str(response)
        """
        if product_name not in seller.goods:
            return buyer, seller, "Seller has no such product named {}".format(product_name)
        product_price = self._prices.get(product_name)
        if product_price is None:
            return buyer, seller, "Product {} is not managed by the DealsManager, sorry".\
                format(product_name)
        if product_price > buyer.money:
            return buyer, seller, "Buyer has not enough money"
        self._perform_a_deal(buyer, product_name, product_price, seller)
        return buyer, seller, "Success"

    @staticmethod
    def _perform_a_deal(buyer, product_name, product_price, seller):
        buyer.buy(product_name, product_price)
        seller.sell(product_name, product_price)


deals_manager = DealsManager()
buyer_john = Buyer(goods=[], money=100)
seller_mike = Seller(goods=["apples", "bread"], money=100)

buyer_john, seller_mike, response = deals_manager.sell_a_product(
    "apples", buyer_john, seller_mike
)
print("Deal status is {}".format(response))
print("Seller has {} dollars and {} in goods".format(seller_mike.money, seller_mike.goods))
print("Buyer has {} dollars and {} in goods".format(buyer_john.money, buyer_john.goods))
