class grandma_shopping:
    def __init__(self):
        self.products = {}

    def add_products(self):
        count = int(input("How many products you want to enter? "))
        for _ in range(count):
            while True:
                name = input("Enter product name: ")
                if is_valid_name(name):
                    break
                else:
                    print("Product name should be letters only.")

            while True:
                price_input = input(f"Enter product {name} price: ")
                if is_valid_price(price_input):
                    price = float(price_input)
                    break
                else:
                    print("The price should be a number.")

            self.products[name] = price

    def get_most_expensive(self):
        prices = list(self.products.values())
        prices.sort()
        max_price = prices[-1]
        result = []
        for name, price in self.products.items():
            if price == max_price:
                result.append(name)
        return result

    def get_cheapest(self):
        prices = list(self.products.values())
        prices.sort()
        min_price = prices[0]
        result = []
        for name, price in self.products.items():
            if price == min_price:
                result.append(name)
        return result

    def get_average_price(self):
        total = 0
        for price in self.products.values():
            total += price
        average = total / len(self.products)
        return average

    def show_results(self):
        expensive = self.get_most_expensive()
        cheap = self.get_cheapest()
        average = self.get_average_price()

        if len(expensive) == 1:
            print(f"The most expensive product is {expensive[0]}")
        else:
            print("The most expensive products: ", ", ".join(expensive))

        if len(cheap) == 1:
            print(f"The most cheap product is {cheap[0]}")
        else:
            print(f"The most cheap products are: ", ", ".join(cheap))

        print(f"Average price of products are: {round(average)}")

def is_valid_name(name):
    return name.isalpha()

def is_valid_price(price_input):
    try:
        float(price_input)
        return True
    except ValueError:
        return False


#RUN
print("Grandma is entering the products!")
grandma = grandma_shopping()
grandma.add_products()
grandma.show_results()
