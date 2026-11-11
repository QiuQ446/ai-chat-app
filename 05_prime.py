def main():
    
    number = 0
    for i in range(2,101):
        is_prime = True
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i,end=" ")
            number += 1
            
            if number % 10 == 0:
                print()

if __name__ == "__main__":
    main()

         