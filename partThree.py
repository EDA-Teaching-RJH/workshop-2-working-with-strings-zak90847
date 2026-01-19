def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
   d_without_currency = d.replace("£" , "")
   return float(d_without_currency)


def percent_to_float(p):
    p_without_percentage = p.replace("%", "")
    return float(p_without_percentage)/100

main()
