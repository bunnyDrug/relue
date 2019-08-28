# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


from sympy import prime


def make_a(n, m):
    return m ** 2 - n ** 2


def make_b(n, m):
    return 2 * m * n


def make_c(n, m):
    return m ** 2 + n ** 2


# rules:
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# where m > n and both numbers are prime


# limit = 50  # not sure how far to go, lets try this for now.
only_prime_numbers = list(range(1, 100))

n_and_m = map(
    lambda counter: list(only_prime_numbers)[counter : counter + 2],
    range(0, len(only_prime_numbers) - 1),
)


triples = map(
    lambda x: [make_a(x[0], x[1]), make_b(x[0], x[1]), make_c(x[0], x[1])],
    n_and_m,
)



sum_to_100 = map(lambda x: sum(x), triples)

# print(list(triples))
print(list(sum_to_100))
