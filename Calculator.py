import math

def getReal(string):
    if((len(string)==1 or len(string)==2) and 'i' in string):
        real = 0
    elif('i' not in string):
        if(string[0]=='-'):
            real = int(string[1:])*-1
        else:
            real = int(string)
    else:
        if('+' in string):
            real = int(string[:string.index("+")])
        if('+' not in string):
            if(string[0]=='-'):
                string = string[1:]
                real = int(string[:string.index("-")])*-1
            else:
                real = int(string[:string.index("-")])
    return real


def getImag(string):
    if(len(string)==1 and 'i' in string):
        imag = 1
    elif(len(string)==2 and 'i' in string):
        imag = -1
    elif('i' not in string):
        imag = 0
    else:
        if('+' in string):
            imag = int(string[string.index("+")+1:string.index("i")])
        if('+' not in string):
            if(string[0]=='-'):
                string = string[1:]
                imag = int(string[string.index("-") + 1:string.index("i")])*-1
            else:
                imag = int(string[string.index("-") + 1:string.index("i")]) * -1
    return imag



class Triangle(object):
    def __init__(self,r,t):
        self.r = r
        self.t = t

    def print(self):
        print("%3.1f(Cos(%d)+iSin(%d))"%(self.r,self.t,self.t))

    def __mul__(self, other):
        print('**********\n Product\n**********')
        return Triangle((self.r * other.r),(self.t + other.t))

    def __truediv__(self, other):
        print('**********\n Division\n**********')
        return Triangle((self.r / other.r),(self.t - other.t))



def nroot(r, n):
    for i in range(1, n):
        r = math.sqrt(r)
    return r



class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def print(self):
        print('(', self.real, ')', '+', '(', self.imag, ')', 'i', sep='')

    def __add__(self, other):
        print('**********\n   Sum\n**********')
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        print('**********\nDifference\n**********')
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        print('**********\n Product\n**********')
        return Complex((self.real * other.real) - (self.imag * other.imag),
                       (self.imag * other.real) + (self.real * other.imag))

    def __truediv__(self, other):
        print('**********\n Division\n**********')
        r = (other.real**2 + other.imag**2)
        return Complex((self.real*other.real + self.imag*other.imag)/r,
                       (self.imag*other.real - self.real*other.imag)/r)

    def conjugate(self):
        print('**********\n Conjugate \n**********')
        return Complex(self.real,(self.imag)*(-1))

    def triangle(self):
        print('**********\nTriangle Form\n**********')
        r = math.sqrt((self.real*self.real)+(self.imag*self.imag))
        teta = math.atan(self.imag/self.real)
        if(self.real<0 and self.imag>0):
            deg =(teta * 180) / math.pi
            deg += 180
        elif(self.real<0 and self.imag<0):
            deg = (teta * 180)/math.pi
            deg += 180
        else:
            deg = (teta * 180) / math.pi
        print("Z = %3.1f(Cos(%3.1f) + i Sin(%3.1f))"%(r,deg,deg))

    def power(self,p):
        print('**********\n  Power\n**********')
        flag = 1
        if(p<0):
            p *= -1
            flag = -1
        r = math.sqrt((self.real * self.real) + (self.imag * self.imag))
        rr = math.pow(r,p)
        if(flag==-1 and p%2!=0):
            rr *= -1
        if(flag==-1):
            rr = 1 / rr
        if(self.real==0):
            teta = 90
            if(self.imag<0):
                deg = 270
        else:
            teta = math.atan(self.imag / self.real)
            if (self.real < 0 and self.imag > 0):
                deg = (teta * 180) / math.pi
                deg += 180
            elif (self.real < 0 and self.imag < 0):
                deg = (teta * 180) / math.pi
                deg += 180
            else:
                deg = (teta * 180) / math.pi
        if(flag==1):
            print("Z^(%d) = r^(%d)(Cos(%d\u03B8) + i Sin(%d\u03B8)) = %.4f(Cos(%d*%.1f) + i Sin(%d*%.1f))"%(p,p,p,p,rr,p,deg,p,deg))
        elif(flag==-1):
            print("Z^(-%d) = r^(-%d)(Cos(-%d\u03B8) + i Sin(-%d\u03B8)) = %f(Cos(%d*%.1f) - i Sin(%d*%.1f))"%(p,p,p,p,rr,p,deg,p,deg))
            print("Z^(-%d) = r^(-%d)(Cos(%d\u03B8) - i Sin(%d\u03B8)) = %f(Cos(%d*%.1f) + i Sin(%d*%.1f))"%(p,p,p,p,rr,p*-1,deg,p*-1,deg))

    def absolute(self):
        print('**********\n Absolute\n**********')
        r = math.sqrt((self.real * self.real) + (self.imag * self.imag))
        print(r)

    def root(self,n):
        r = math.sqrt((self.real * self.real) + (self.imag * self.imag))
        r = nroot(r,n)
        if (self.real == 0):
            teta = 90
            if (self.imag < 0):
                deg = 270
        else:
            teta = math.atan(self.imag / self.real)
            if (self.real < 0 and self.imag > 0):
                deg = (teta * 180) / math.pi
                deg += 180
            elif (self.real < 0 and self.imag < 0):
                deg = (teta * 180) / math.pi
                deg += 180
            else:
                deg = (teta * 180) / math.pi
        print("It has %d roots." % (n))
        for i in range (0,n):
            fi = (deg+(2*i*3))/n
            print("%dth root = sqrt(r){%d}(Cos((\u03B8+2*%d*\u03C0)/%d)+iSin((\u03B8+2*%d*\u03C0)/%d) = %f(Cos(%.3f)+iSin(%.3f))"%(i+1,n,i,n,i,n,r,fi,fi))


    def euler(self):
        print('**********\n  Euler\n**********')
        r = math.sqrt((self.real * self.real) + (self.imag * self.imag))
        if (self.real == 0):
            teta = 90
            if (self.imag < 0):
                deg = 270
        else:
            teta = math.atan(self.imag / self.real)
            if (self.real < 0 and self.imag > 0):
                deg = (teta * 180) / math.pi
                deg += 180
            elif (self.real < 0 and self.imag < 0):
                deg = (teta * 180) / math.pi
                deg += 180
            else:
                deg = (teta * 180) / math.pi
        print("Z = re^i(\u03F4) = %.3fe^i(%.3f)"%(r,deg))




while 1:
    print("**************\n  Calculator\n**************")
    print("1. Simple calculations(+,-,/,*)\n2. Conjugate\n3. Triangle form\n4. Power\n5. Absolute value\n6. Root\n7. Euler form\n8. Exit")
    selected_item = int(input("Please enter the option you want to choose :"))
    if(selected_item==1):
        print("You choosed first option.")
        c = Complex(0,0)
        c = Triangle(0,0)
        operators = ['+','-','*','/']
        print("Which form ? (Rectangle(R) or Triangle(T))")
        form = input()
        if(form=='T' or form=='t'):
            print("Enter a complex number in Triangle form (r(Cos(teta)+iSin(teta)): ")
            r1 = int(input("r = "))
            t1 = int(input("teta = "))
            c1 = Triangle(r1,t1)
            c1.print()

            while 1:
                print("Enter an operator : ")
                op = input()
                if (op == '+' or op == '-'):
                    print("Sum and Sub are not allowed here.Please try Mul or Div!")
                    continue
                elif (op in operators):
                    break
                else:
                    print("Invalid operator! Try again ")
                    continue

            print("Enter a complex number in Triangle form (r(Cos(teta)+iSin(teta)): ")
            r2 = int(input("r = "))
            t2 = int(input("teta = "))
            c2 = Triangle(r2, t2)
            c2.print()

            if (op == '*'):
                c = c1 * c2
                c.print()
            else:
                while 1:
                    if (c2.r == 0 and c2.t == 0):
                        print("Division by zero!Please enter a non zero complex number :")
                        r2 = int(input("r = "))
                        t2 = int(input("teta = "))
                        c2 = Triangle(r2, t2)
                        c2.print()
                    else:
                        break
                c = c1 / c2
                c.print()

            while 1:
                while 1:
                    print("Enter an operator (or 'end' to finish calculating): ")
                    op = input()
                    if (op == '+' or op == '-'):
                        print("Sum and Sub are not allowed here.Please try Mul or Div!")
                        continue
                    elif (op in operators):
                        break
                    elif(op=='end'):
                        break
                    else:
                        print("Invalid operator! Try again ")
                        continue

                if (op == 'end'):
                    print("Calculation finished !")
                    break

                print("Enter a complex number in Triangle form (r(Cos(teta)+iSin(teta)): ")
                r3 = int(input("r = "))
                t3 = int(input("teta = "))
                c3 = Triangle(r3, t3)
                c3.print()

                if (op == '*'):
                    c = c * c3
                    c.print()
                else:
                    while 1:
                        if (c2.r == 0 and c2.t == 0):
                            print("Division by zero!Please enter a non zero complex number :")
                            r2 = int(input("r = "))
                            t2 = int(input("teta = "))
                            c2 = Triangle(r2, t2)
                            c2.print()
                        else:
                            break
                    c = c1 / c2
                    c.print()
        elif(form=="R" or form=='r'):
            print("Enter a complex number in Rectangle form (x+iy) : ")
            num1 = input()
            real1 = getReal(num1)
            imag1 = getImag(num1)
            c1 = Complex(real1,imag1)
            c1.print()

            while 1:
                print("Enter an operator : ")
                op = input()
                if (op in operators):
                    break
                else:
                    print("Invalid operator! Try again ")
                    continue

            print("Enter a complex number in Rectangle form (x+iy): ")
            num2 = input()
            real2 = getReal(num2)
            imag2 = getImag(num2)
            c2 = Complex(real2,imag2)
            c2.print()

            if(op=='+'):
                c = c1 + c2
                c.print()
            elif(op=='-'):
                c = c1 - c2
                c.print()
            elif(op=='*'):
                c = c1 * c2
                c.print()
            else:
                while 1:
                    if(c2.real==0 and c2.imag==0):
                        print("Division by zero!Please enter a non zero complex number :")
                        num2 = input()
                        real2 = getReal(num2)
                        imag2 = getImag(num2)
                        c2 = Complex(real2,imag2)
                        c2.print()
                    else:
                        break
                c = c1 / c2
                c.print()

            while 1:
                while 1:
                    print("Enter an operator (or 'end' to finish calculating): ")
                    op = input()
                    if (op in operators):
                        break
                    elif(op=='end'):
                        break
                    else:
                        print("Invalid operator! Try again ")
                        continue

                if(op=='end'):
                    print("Calculation finished !")
                    break

                print("Enter a complex number in Rectangle form (x+iy):: ")
                num3 = input()
                real3 = getReal(num3)
                imag3 = getImag(num3)
                c3 = Complex(real3, imag3)
                c3.print()

                if (op == '+'):
                    c = c + c3
                    c.print()
                elif (op == '-'):
                    c = c - c3
                    c.print()
                elif (op == '*'):
                    c = c * c3
                    c.print()
                else:
                    while 1:
                        if (c3.real == 0 and c3.imag == 0):
                            print("Division by zero!Please enter a non zero complex number :")
                            num3 = input()
                            real3 = getReal(num3)
                            imag3 = getImag(num3)
                            c3 = Complex(real3, imag3)
                            c3.print()
                        else:
                            break
                    c = c / c3
                    c.print()
    if (selected_item == 2):
        print("You choosed second option.")
        while 1:
            print("Enter a complex number (or 'end' to back to menu) :")
            num = input()
            if(num=='end'):
                break
            else:
                real = getReal(num)
                imag = getImag(num)
                c = Complex(real,imag)
                c = c.conjugate()
                c.print()
    if (selected_item == 3):
        print("You choosed third option.")
        while 1:
            print("Enter a complex number (or 'end' to back to menu) :")
            num = input()
            if(num=='end'):
                break
            else:
                real = getReal(num)
                imag = getImag(num)
                c = Complex(real,imag)
                c.triangle()
                c.print()

    if (selected_item == 4):
        print("You choosed fourth option.")
        while 1:
            print("Enter a complex number (or 'end' to back to menu) :")
            num = input()
            if(num=='end'):
                break
            else:
                real = getReal(num)
                imag = getImag(num)
                c = Complex(real,imag)
            print("Enter the power :(posetive or negetive)")
            p = int(input())
            c.power(p)

    if (selected_item == 5):
        print("You choosed fifth option.")
        while 1:
            print("Enter a complex number (or 'end' to back to menu) :")
            num = input()
            if (num == 'end'):
                break
            else:
                real = getReal(num)
                imag = getImag(num)
                c = Complex(real, imag)
            c.absolute()

    if (selected_item == 6):
        print("You choosed sixth option.")
        while 1:
            print("Enter a complex number (or 'end' to back to menu) :")
            num = input()
            if (num == 'end'):
                break
            else:
                real = getReal(num)
                imag = getImag(num)
                c = Complex(real, imag)
            print("Enter the root :")
            n = int(input())
            c.root(n)

    if (selected_item == 7):
        print("You choosed seventh option.")
        while 1:
            print("Enter a complex number (or 'end' to back to menu) :")
            num = input()
            if (num == 'end'):
                break
            else:
                real = getReal(num)
                imag = getImag(num)
                c = Complex(real, imag)
            c.euler()

    if (selected_item == 8):
        exit()