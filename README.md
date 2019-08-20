## Unit Testing Assignment

by Chananchida Fuachai.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Empty list             |  Empty list         |
| One item               |  List with 1 item   |
| One item many times    |  List with 1 item   |
| 2 items, many times, many orders | 2 items list, items in same order  |
| Many items, many times, many orders | List of one duplicate of each items |
| Very large list of items | List of one duplicate of each items |
| non-list               |  TypeError          |


## Test Cases for Fraction

**Initialize (`__init__`)**

| Test case              |  Expected Result    |
|------------------------|---------------------|
| non-zero demominator and numerator | Represent in numerator/Demominator |
| non-int or non-float | TypeError |
| Demominator and numerator = 0 |  ValueError   |

**String representation (`__str__`)**

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Demominator is not 1 or 0 | Represent in numerator/Demominator |
| Only numerator |  Whole number of the numerator and provide default denominator = 1   |
| Demominator = 0, numerator > 0 | Represent in 1/0 |
| Demominator = 0, numerator < 0 | Represent in -1/0 |
| Denominator is negative and numerator is positive | The numerator is negative, the denominator is positive|
| Denominator and numerator are both zero |  ValueError   |
| non-int or non-float | TypeError |

**Addition Operator (`__add__`)**

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Positive fractions add together | Positive fraction |
| Negative fractions add together | Negative fraction |
| Fraction add zero | The same fraction |

**Subtraction Operator (`__sub__`)**

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Positive fractions subtract together | Positive fraction |
| Negative fractions subtract together | Negative/positive fraction |
| Fraction subtract zero | The same fraction |

**Multiple Operator (`__mul__`)**

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Positive fractions multiple together | Positive fraction |
| Negative fractions multiple together | Positive fraction |
| Negative and positive fraction multiple together | Negative fraction |
| Fraction subtract zero | Zero |

**Equal Operator (`__eq__`)**

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Proper form and internal representation | Equal |
| Proper form and other fraction | Not equal |

**Greater than (`__gt__`)**

| Test case              |  Expected Result    |
|------------------------|---------------------|
| One fraction greater than other fraction | True |
| One fraction less than other fraction | False |
| Two fractions are equal | False |

**Negative (`__neg__`)**

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Positive fraction | Negative fraction |
| Negative fraction | Positive fraction |
| Zero | Zero |
