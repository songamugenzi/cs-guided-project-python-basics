"""
Challenge #4:
​
Create a function that takes length and width and finds the perimeter of a
rectangle.
​
to get the perimeter of a renctangle we could use either (l * 2 + w * 2) or (l + w) * 2
​
Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
# def find_perimeter(length, width):
#     # Your code here
#     # set a perimeter to the value of the expression (length + width) * 2
#     perimeter = (length + width) * 2
​
#     # return the perimeter to the caller
#     return perimeter
​
def find_perimeter(length, width):
    """
    a function that takes length and width and finds the perimeter of a
rectangle.
    """
    # return the value of the expression (length + width) * 2 to the caller
    return (length + width) * 2
​
print(find_perimeter(6, 7)) # ➞ 26
print(find_perimeter(20, 10)) # ➞ 60
print(find_perimeter(2, 9)) # ➞ 22
