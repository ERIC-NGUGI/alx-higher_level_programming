#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    a = 10
    b = 5
    """addition"""
    print("{} + {} = {}".format(a, b, calculator.add(a, b)))
    """subtraction"""
    print("{} - {} = {}".format(a, b, calculator.sub(a, b)))
    """multiplication"""
    print("{} * {} = {}".format(a, b, calculator.mul(a, b)))
    """division"""
    print("{} / {} = {}".format(a, b, calculator.div(a, b)))
