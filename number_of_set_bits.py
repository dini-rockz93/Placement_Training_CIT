def set_bits(a: int) -> None:
    
    count = 0
    while a:
        
        a &= a - 1
        count += 1
    
    print("number of set bits ", count)

def main():
    
    a = input("Enter a number to count number of set bits ")
    a = int(a)
    set_bits(a)


if __name__ == "__main__":
    main()
