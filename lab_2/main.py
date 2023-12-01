class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        result_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def subtract(self, other):
        result_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def multiply(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other):
        try:
            result_numerator = self.numerator * other.denominator
            result_denominator = self.denominator * other.numerator
            return Fraction(result_numerator, result_denominator)
        except:
            ZeroDivisionError
            return None

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

sum_result = fraction1.add(fraction2)
print(f"Addition: {fraction1} + {fraction2} = {sum_result}")

difference_result = fraction1.subtract(fraction2)
print(f"Subtraction: {fraction1} - {fraction2} = {difference_result}")

product_result = fraction1.multiply(fraction2)
print(f"Multiplication: {fraction1} * {fraction2} = {product_result}")

quotient_result = fraction1.divide(fraction2)
print(f"Division: {fraction1} / {fraction2} = {quotient_result}")