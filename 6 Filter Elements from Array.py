"""
Given an integer array arr and a filtering function fn, return a filtered array filteredArr.

The fn function takes one or two arguments:

arr[i] - number from the arr
i - index of arr[i]
filteredArr should only contain the elements from the arr for which the expression fn(arr[i], i) evaluates to a truthy value. A truthy value is a value where Boolean(value) returns true.

Please solve it without the built-in Array.filter method.

Example 1:

Input: arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }
Output: [20,30]
Explanation:
const newArray = filter(arr, fn); // [20, 30]
The function filters out values that are not greater than 10
Example 2:

Input: arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; }
Output: [1]
Explanation:
fn can also accept the index of each element
In this case, the function removes elements not at index 0
Example 3:

Input: arr = [-2,-1,0,1,2], fn = function plusOne(n) { return n + 1 }
Output: [-2,0,1,2]
Explanation:
Falsey values such as 0 should be filtered out
 
Constraints:

0 <= arr.length <= 1000
-109 <= arr[i] <= 109

"""
def filter(arr, fn):
    result = []
    for i, value in enumerate(arr):
        if fn(value, i):
            result.append(value)
    return result

#filter values greater than 10
arr1 = [0, 10, 20, 30]
greater_than_10 = lambda n, i: n > 10
print(filter(arr1, greater_than_10))  

#keep only the first element
arr2 = [1, 2, 3]
first_index = lambda n, i: i == 0
print(filter(arr2, first_index)) 

#filter where the number plus one is truthy
arr3 = [-2, -1, 0, 1, 2]
plus_one = lambda n, i: n + 1
print(filter(arr3, plus_one)) 

