class Calculadora:

    def calcular(self, op, n1, n2):
        if op == '+':
            return self.__add(n1, n2)
        elif op == '-':
            return self.__sub(n1, n2)
        else:
            return 'Invalid op'
    
    def __add(self, n1, n2):
        return n1 + n2
    
    def __sub(self, n1, n2):
        return n1 - n2
    

calc = Calculadora()
result_sum = calc.calcular(op='+', n1=1, n2=2)
result_sub = calc.calcular(op='-', n1=2, n2=2)

print(result_sum)
print(result_sub)
