# ---- using lambdas ----
multiples_of_three_and_five = filter(lambda i: i % 3 == 0 or i % 5 == 0, range(1000))
print(sum(multiples_of_three_and_five))

# ---- list comprehension ----
multiples_of_three_and_five = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
print(sum(multiples_of_three_and_five))


# ---- reusable function ----
def multiples_upto(max_int):
    return lambda x: filter(lambda num: num % x == 0, range(max_int))


from itertools import chain

multiple_factory = multiples_upto(1000)
multiples_of_three = multiple_factory(3)
multiple_of_five = multiple_factory(5)
multiples_of_three_and_five = set(chain(multiples_of_three, multiple_of_five))
print(sum(multiples_of_three_and_five))
