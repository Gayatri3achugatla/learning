# program to get even and odd numbers using list comprehension

list1 = [1,34,33,77,98,76,23,21,65,79]
even_odd = ['even' if num%2 ==0 else 'odd' for num in list1]
print(even_odd)
