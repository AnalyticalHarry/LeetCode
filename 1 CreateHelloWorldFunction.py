"""
Write a function createHelloWorld. It should return a new function that always returns "Hello World".

Example 1:

Input: args = []
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".

Example 2:

Input: args = [{},null,42]
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".

Constraints:

0 <= args.length <= 10
"""
#creating a function createHelloWorld
def createHelloWorld():
  #creating print function
    def function():
      #return print "Hello World"
        return "Hello World"
    #returning function
    return function()
#cretae varaible which store function
f = createHelloWorld()
#printing on screen
print(f)

#Hemant Thapa
#Date: 20.01.2024
