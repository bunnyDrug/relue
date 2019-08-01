#A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

#iterative approach 

first_number = 91
second_number = 99

pallys = []


for i in range(999, 99, -1):
    for x in range(999,99,-1):
        product = i * x
        product_rev = str(product)[::-1]
        
        if product_rev == str(product):
            pallys.append(product)
            
pallys.sort()
print(pallys.pop())

