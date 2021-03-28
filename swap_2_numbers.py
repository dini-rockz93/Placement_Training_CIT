def swap(a: int, b: int) -> None:
       
    print("Before swapping ", a, b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping ", a, b)
    

def main():
    
    a,b = input("Enter two numbers to swap: ").split()
    a = int(a)
    b = int(b)
    
    swap(a,b)


if __name__ == "__main__":
    main()
