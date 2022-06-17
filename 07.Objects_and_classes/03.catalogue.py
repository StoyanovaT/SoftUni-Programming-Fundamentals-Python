class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []
        self.by_letters = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        by_letters = [x for x in self.products if first_letter == x[0]]
        return by_letters

    def __repr__(self):
        self.products.sort()
        print_first_line = f"Items in the {self.name} catalogue:\n"
        return print_first_line + ("\n".join(map(str, self.products)))


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
