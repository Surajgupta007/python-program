nterms = int(input("How many terms?"))
n1=0
n2=1
count=0
#check if the number of the term is valid
if nterms<=0:
    print("plz enter a positive integer")

#if there is only one term, return n1
elif nterms ==1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count<nterms:
        print(n1)
        nth = n1 + n2
        #updating values
        n1=n2
        n2=nth
        count += 1
