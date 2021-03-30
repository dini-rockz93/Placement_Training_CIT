def gcd(a: int, b: int) -> None:
    
    if (a == 0): 
        return b 
    if (b == 0): 
        return a 
  
    if (a == b): 
        return a 
  
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a) 

def main():
    
    a,b = input("Enter two numbers to find GCF: ").split()
    a = int(a)
    b = int(b)
    
    print("GCD of two numbers is ",gcd(a,b))


if __name__ == "__main__":
    main()
