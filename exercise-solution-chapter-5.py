products = ["manzana", "pan", "leche"]
prices = [1.5, 2.0, 3.2]
product_prices_dict = {product: price for product, price in zip(products, prices) if price > 1.8}
print(product_prices_dict) # {'pan': 2.0, 'leche': 3.2}
