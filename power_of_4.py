def power_of_4(a: int) -> None:
    
    if a and (a & a - 1) == 0 and a % 3 == 1:
        print("It's a power of 4")
    else: 
        print("It's not a power of 4")       
    
def main():
    
    a = input("Enter a number to check for poweer of 4: ")
    a = int(a)
    power_of_4(a)


if __name__ == "__main__":
    main()
