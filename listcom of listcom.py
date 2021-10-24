list=[90,76,45,33,23,12,6,5]

even_list = [num for num in list if num%2 == 0 ]
odd_list = [num for num in list if num not in even_list]
print(even_list)
print(odd_list)

# implementing list comprehension in another list comprehension
odd_one = [num for num in list if num not in (num for num in list if num%2 == 0)]
print(odd_one)
