low=int(input("enter first : "))
hih=int(input("enter last : "))
for num in range(low,hih+1):
    if num>1 :
        for i in range(2,num):
            if(num%i)==0 :
                
                break
            else:
                print(num)
                break
