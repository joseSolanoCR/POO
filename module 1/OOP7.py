class Calc:
    # atributos y variables de clase

    # constructor / inicializador de clase
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def total(self):
        return self.num1 + self.num2

    def diff(self):
        return self.num1 - self.num2


        # atributos y variables de objeto
        # metodos

def main():
    print("hola desde main()")
    calc1 = Calc(10,20)
    total1 = calc1.total()
    diff1 = calc1.diff()
    print("total : ", total1)
    print("diff : ", diff1)

    print("-----------")
    calc2 = Calc(5, 25)
    total2 = calc2.total()
    diff2 = calc2.diff()
    print("total 2: ", total2)
    print("diff 2: ", diff2)


    #Values

if __name__ == '__main__':
    main()
