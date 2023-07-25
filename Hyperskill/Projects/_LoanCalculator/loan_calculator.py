import math
import argparse

parser = argparse.ArgumentParser(description="Description")
parser.add_argument("--type", type=str, default="", help="Either diff or annuity")  # Type
parser.add_argument("--payment", type=int, default=0, help="Integer of monthly payment")  # A
parser.add_argument("--principal", type=int, default=0, help="Integer of principal payment")  # P
parser.add_argument("--periods", type=int, default=0, help="Integer of periods")  # n
parser.add_argument("--interest", type=float, default=0, help="Float of interest")  # Ai

args = parser.parse_args()


def main():

    if args.type == "diff":
        if args.principal >= 1 and args.periods >= 1 and args.interest >= 1:
            overpayment = 0
            for m in range(1, args.periods + 1):
                result = fnc_differentiate_payment(args.principal, args.periods, args.interest, m)
                print(f"Month {m}: payment is {result}")
                overpayment = overpayment + result
            print(f"Overpayment = {overpayment - args.principal}")
        else:
            fnc_error_msg()

    elif args.type == "annuity":
        if args.payment >= 1 and args.periods >= 1 and args.interest >= 1:
            result = fnc_loan_principal(args.payment, args.periods, args.interest)
            overpayment = (args.periods * args.payment) - result
            print(f"Your loan principal = {result}!")
            print(f"Overpayment = {overpayment}")
        elif args.principal >= 1 and args.periods >= 1 and args.interest >= 1:
            result = fnc_ordinary_annuity(args.principal, args.periods, args.interest)
            overpayment = (args.periods * result) - args.principal
            print(f"Your annuity payment = {result}!")
            print(f"Overpayment = {overpayment}")
        elif args.principal >= 1 and args.payment >= 1 and args.interest >= 1:
            result = fnc_number_of_months(args.principal, args.payment, args.interest)
            overpayment = (result * args.payment) - args.principal
            if result == 1:  # 1 month
                print(f"it will take {result} month to repay this loan!")
            elif result < 12:  # 2 - 11 months
                print(f"it will take {result} months to repay this loan!")
            elif result == 12:  # 12 months
                print(f"it will take {result / 12} year to repay this loan!")
            else:  # 13 months and more
                print(f"it will take {result // 12} years and {result % 12} months to repay this loan!")
            print(f"Overpayment = {overpayment}")
        else:
            fnc_error_msg()


def fnc_error_msg():
    print("Incorrect parameters")
    exit()


def fnc_number_of_months(P, A, Ai):
    i = float(Ai / (12 * 100))
    return math.ceil(math.log((A / (A - i * P)), (1 + i)))


def fnc_loan_principal(A, n, Ai):
    i = float(Ai / (12 * 100))
    x = pow((1 + i), n)
    return round(A / ((i * x) / (x - 1)))


def fnc_ordinary_annuity(P, n, Ai):
    i = float(Ai / (12 * 100))
    x = pow((1 + i), n)
    return math.ceil(P * ((i * x) / (x - 1)))


def fnc_differentiate_payment(P, n, Ai, m):
    i = float(Ai / (12 * 100))
    return math.ceil((P / n) + (i * (P - (P * (m - 1)) / n)))


if __name__ == "__main__":
    main()
