class BasicCalculation:

    def sum_two_number(self, x,y):
        '''
        here we are  adding two numbers
        '''
        return x +y
    
    def mul_two_numbers(self, x,y):
        '''
        here we find product of two number
        '''
        return x*y

num_calc = BasicCalculation()
sum = num_calc.sum_two_number(3,4)
print(f"the sum of two number is: {sum}")
mul = num_calc.mul_two_numbers(3,4)
print(f"the mul of two number is: {mul}")

###
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y