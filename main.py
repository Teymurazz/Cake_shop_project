class Cake:
    def __init__(self, 
            name: str, 
            weight: float, 
            ingredients: list, 
            price: float, 
            in_stock: float
            ) -> None:
        self.name = name
        self.weight = weight
        self.ingredients = ingredients
        self.price = price
        self.in_stock = in_stock

    def __str__(self) -> str:
        return f"{self.name} ({self.price}$)"

    def __repr__(self) -> str:
        return self.__str__()


class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cashbox = 0
        self.case = [ ]

    def __str__(self) -> str:
        return f"{self.name} {self.case}"

    def show_cakes(self):
        for num, cake in enumerate(self.case, start=1):
            print(f"{num}. {cake.name} - {cake.price}$ ({cake.in_stock} in stock)")

    def add_cake(self, cake: Cake) -> None:
        self.case.append(cake)

    def sell_cake(self, cake_index, count) -> None:
        in_stock = self.case[cake_index].in_stock
        price = self.case[cake_index].price

        if in_stock >= count:
            self.case[cake_index].in_stock -= count
            total = price * count
            self.cashbox += total

        if self.case[cake_index].in_stock == 0:
            print("men burdayam")
            self.case.pop(cake_index)
        

napoleon = Cake(
    name="Napoleon",
    weight=0.8,
    ingredients=["Vanilla", "Butter"],
    price=12,
    in_stock=2
)
my_shop = Shop(name="SweetDreams")
my_shop.add_cake(napoleon)

while True:
    print("Choose cake to buy:")
    my_shop.show_cakes()
    answer = int(input(">> ").strip().lower())
    cake_idx = answer - 1
    print("How many ???")
    amount = int(input(">> "))
    my_shop.sell_cake(cake_idx, amount)