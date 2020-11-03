# This is a collection of functions that may be helpful to
# business users. 
import math

def breakeven(fixed, variable, sell):
    ''' Calculates the breakeven point in units.
    '''
    # calculate the breakeven point
    units = math.ceil(fixed/(sell-variable))  #breakeven formula
    return units

def markdown(price, percent):
    # use the original price and markdown percent passed to the function
    # to calculate the new price.
    discount_price = price * percent
    return discount_price

def sales_tax(subtotal):
    # use the pretax subtotal to calculated tax due in Conway, AR
    # Conway's tax rate = 8.75%
    SALES_TAX_RATE = 0.0875
    return subtotal * SALES_TAX_RATE

def grade_lookup(id_num):
    # use the id number to return data about the student
    if id_num == 1:
        name = 'Arthur'
        grade = 'A'
        avg = 89.6
    elif id_num == 2:
        name = 'Galahad'
        grade = 'A'
        avg = 92.3
    elif id_num == 3:
        name = 'Gawain'
        grade = 'D'
        avg = 61.8
    elif id_num == 4:
        name = 'Lancelot'
        grade = 'C'
        avg = 78.1
    else:
        name = 'None'
        grade = 'Z'
        avg = 0.0

    return name, grade, avg
