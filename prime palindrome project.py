i=0
while True:
    i+=1
    def palindrome_prime(x):
        n, c = 1, 0
        while (c < x):
            n += 1
            for i in range(2, n + 1):
                if (n % i == 0):
                    break
            if (i == n):
                s = str(n)
                if (s == s[::-1]):  # checking reverse of number is same or not
                    c = c + 1
        print(str(x)+"th","palindrome prime no.=", n)



    x = int(input("Enter the no. to find nth palindrome prime no.: "))
    palindrome_prime(x)
    print("press 1:Run Again ","press 2 : Not Run again ",sep="\n")
    y=int(input("press 1 for run again :",))
    if y==1:
        continue
    else:
        print("program is ended")
        break




