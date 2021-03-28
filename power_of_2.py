def power_of_2(a: int) -> None:
    
    if a and (a & a - 1):
        print("It's not a power of 2")
    else: 
        print("It's a power of 2")       
    
def main():
    
    a = input("Enter a number to check for poweer of 2: ")
    a = int(a)
    power_of_2(a)


if __name__ == "__main__":
    main()
