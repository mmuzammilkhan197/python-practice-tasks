name = input("Enter customer name: ")
units = int(input("Enter electricity units: "))

if units <= 0:
    print("Invalid Units")

else:
    if units <= 100:
        rate = 10
    elif units <= 200:
        rate = 15
    elif units <= 300:
        rate = 20
    else:
        rate = 25

    basic_bill = units * rate
    tax = basic_bill * 5 / 100
    final_bill = basic_bill + tax

    print("\n" + "=" * 35)
    print("       ELECTRICITY BILL")
    print("=" * 35)

    print(f"Customer Name : {name}")
    print(f"Units Consumed: {units}")
    print(f"Rate Per Unit : Rs. {rate}")
    print(f"Basic Bill    : Rs. {basic_bill:.2f}")
    print(f"Tax (5%)      : Rs. {tax:.2f}")
    print(f"Final Bill    : Rs. {final_bill:.2f}")

    print("=" * 35)
