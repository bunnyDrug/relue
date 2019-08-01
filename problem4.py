#A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

#iterative approach 

first_number = 91
second_number = 99



for i in range(999, 100, -1):
    for x in range(999,100,-1):
        product = i * x
        product_rev = str(product)[::-1]
        
        if product_rev == str(product):
            print("found a pally")
            print(f"{product}={x}*{i}")
            exit(0)
        else:
            print(f"{x}{i}")
        
        
