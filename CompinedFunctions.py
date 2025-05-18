class Multifunctions:
    #Print
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    #OddEven
    def OddEven():
            num=int(input("Enter a number:"));
            if num%2==0:
                print(num,"is Even number")
            else:
                 print(num,"is Odd number")
    #Elg for Mrg
    def Elegible():
            gender = input("Your Gender: ")
            age = int(input("Your age: "))
            if gender=="male" and age >=21:
                print("Eligible");
            elif gender=="female" and age >=18:
                print("Eligible");
            else:
                print("Not Eligible");
            
    #Triange area,perimeter
    def triangle():
            h=float(input("Height:"))
            b=float(input("Breadth:"))
            print("Area formula: (Height*Breadth)/2") 
            area=(h*b)/2
            print("Area of Triangle:",area) 
            h1=float(input("Height1:"))
            h2=float(input("Height2:"))
            b=float(input("Breadth:"))
            print("Perimeter formula: Height1+Height2+Breadth") 
            perimeter=h1+h2+b
            print("Perimeter of Triangle:",perimeter)
    #Percent
    def percentage():
                sub1=int(input("Subject1="))
                sub2=int(input("Subject2="))
                sub3=int(input("Subject3="))
                sub4=int(input("Subject4="))
                sub5=int(input("Subject5="))
                total=sub1+sub2+sub3+sub4+sub5
                percent=total/5
                print("Total:",total)
                print("Percentage:",percent)     