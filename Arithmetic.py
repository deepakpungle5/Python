"""create a module name as arithmetic which contains 4 functions as Add() for addition sub() sub() for substraction 
mul() for multiplication and div() for division. all functions accepts two parameter as number and perform the operation.
write a python perform which call  all the function   and arithmetic from arithmetic module by accepting the parameter from user. """

def Add(no1,no2):
    return no1 + no2

def Sub(no1,no2):
    return no1 - no2

def Mul(no1,no2):
    return no1 * no2

def Div(no1,no2):
    if no2 == 0:
        return "Divisible by Zero Error "
    
    return no1 / no2