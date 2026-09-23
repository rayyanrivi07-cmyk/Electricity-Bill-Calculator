print("Electricity Bill Calculator")

units = int(input("Enter the number of units consumed: "))

if units < 0:
    print("Invalid input. Units cannot be negative.")

else:
    if units <= 100:
        energy_charge = units * 5

    elif units <= 200:
        energy_charge = (100 * 5) + ((units - 100) * 7)

    elif units <= 300:
        energy_charge = (100 * 5) + (100 * 7) + ((units - 200) * 9)

    elif units <= 500:
        energy_charge = (100 * 5) + (100 * 7) + (100 * 9) + ((units - 300) * 12)

    else:
        energy_charge = (100 * 5) + (100 * 7) + (100 * 9) + (200 * 12) + ((units - 500) * 15)

    fixed_charge = 100

    total_bill = energy_charge + fixed_charge

    print("Units consumed:", units)
    print("Energy charge: ₹", energy_charge)
    print("Fixed charge: ₹", fixed_charge)
    print("Total electricity bill: ₹", total_bill)