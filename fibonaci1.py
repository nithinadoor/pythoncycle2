nterms=int(input("enter  how many terms"))
count=0
n1=0
n2=1
if(nterms<0):
    print("enter  positive number")
elif(nterms==1):
    print("fibonacci series upto",nterms,"is")
    print(n1)
else:
    while(count<nterms):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1



