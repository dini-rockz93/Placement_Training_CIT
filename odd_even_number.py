def odd_even(a: int) -> None:
    
    if a & 1:
        print("It's a odd number")
    else: 
        print("It's a even number")       
    
def main():
    
    a = input("Enter a number to check for odd/even: ")
    a = int(a)
    odd_even(a)


if __name__ == "__main__":
    main()
