def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    price = float(input("100 "))
    discount_percent = float(input("20%: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price == 100:
        print(f"No discount applied. The final price is {100:.2f}.")
    else:
        print(f"A discount of {discount_percent}% has been applied. The final price is ${final_price:.2f}.")

if __name__ == "__main__":
    main()