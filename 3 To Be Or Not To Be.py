"""
Write a function expect that helps developers test their code. It should take in any value val and return an object with the following two functions.

toBe(val) accepts another value and returns true if the two values === each other. If they are not equal, it should throw an error "Not Equal".
notToBe(val) accepts another value and returns true if the two values !== each other. If they are equal, it should throw an error "Equal".
 

Example 1:

Input: func = () => expect(5).toBe(5)
Output: {"value": true}
Explanation: 5 === 5 so this expression returns true.
Example 2:

Input: func = () => expect(5).toBe(null)
Output: {"error": "Not Equal"}
Explanation: 5 !== null so this expression throw the error "Not Equal".
Example 3:

Input: func = () => expect(5).notToBe(null)
Output: {"value": true}
Explanation: 5 !== null so this expression returns true.
"""
class Expect:
    def __init__(self, data):
        self.value = data
      
    def toBe(self, expected):
        if self.value != expected:
            raise ValueError("Not Equal")
        return {"value": True}

    def notToBe(self, expected):
        if self.value == expected:
            raise ValueError("Equal")
        return {"Value": True}

try:
    result1 = Expect(5).toBe(5)
    print(result1)  
except ValueError as error:
    #handle error
    print({"error": str(error)})  

try:
    result2 = Expect(5).toBe(None)
    #this won't be reached due to the error
    print(result2)  
except ValueError as error:
    print({"error": str(error)}) 

try:
    result3 = Expect(5).notToBe(None)
    print(result3)  
except ValueError as error:
    #this won't be reached due to the successful check
    print({"error": str(error)})  


