#created by- vishal jain
#date-08/01/2019
#interpreter-IDLE python 3.7
#program name- ATM
#condition- minimum one note of hundred rupees should be come out



a=int(input("enter the amount(amount should be divisible by 50)"))
if(a%50==0):
        b=a-100
        c=b//2000
        d=b%2000
        e=d//500
        f=d%500
        g=f//200
        h=f%200
        i=h//100
        j=h%100
        k=j//50
        l=i+1
        print("number of two thousand rupees note=",c)
        print("number of five hundred rupees note=",e)
        print("number of two hundred rupees note=",g)
        print("number of one hundred rupees note=",l)
        print("number of fifty rupees note=",k)
else:
        print("THIS AMOUNT IS NOT DIVISIBLE BY 50")
        print("THANK YOU!")
