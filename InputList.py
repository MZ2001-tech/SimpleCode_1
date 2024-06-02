
def main():
    name = input("Enter Your Name: ")
    salary = float(input("enter your Salary per hour: "))
    hours = float(input("Enter the number of hours you worked: "))

    Gross_pay = Calculate(salary, hours)
    print(f"Your Name is {name}, and your grosspay is {Gross_pay}")


def Calculate(salary, hours):
    Gross_pay = salary * hours
    return Gross_pay


if __name__ == "__main__":
    main()




