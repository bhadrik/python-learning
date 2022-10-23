import sys
from xmlrpc.client import MAXINT

#USE HASH SET 
def containsDuplicate(nums: list[int]):
    data = set()
    for i in nums:
        if i in data:
            print("True")
            return
        data.add(i)
    print("False")
    return

if __name__ == "__main__":
    # a = [188,265,3547,6764,56458,9787,24,7,8,7976,553,7,8,8]
    a = [1,2,3,4,5,6,7,8,9,0,0]
    containsDuplicate(a)