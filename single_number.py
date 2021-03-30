"""
    
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    
"""

def singleNumber(nums):
      
        a = 0
        for i in nums:
            a ^= i
        return a


def main():
    
    arr = [2,2,1]
    print(singleNumber(arr))


if __name__ == "__main__":
    main()