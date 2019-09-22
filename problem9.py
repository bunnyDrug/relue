# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


from sympy import prime


def make_a(n, m):
    return (n ** 2) - (m ** 2)


def make_b(n, m):
    return 2 * (m * n)


def make_c(n, m):
    return (n ** 2) + (m ** 2)


def rules(x):
    return [
            make_a(x[0], x[1]),
            make_b(x[0], x[1]),
            make_c(x[0], x[1])
            ]

def product(number):
    return reduce((lambda x, y: x * y), number)

n_and_m = ([2,1],[3,2],[6,3],[9,6],[6,1],[7,1],[8,1],[9,1])

somelist = []
for i in range (0, 100):
    for x in range(0,100):
        somelist.append([i,x])

# print(somelist)
filteredlist = [(n,m) for n, m in somelist if n > m]

triples = map(rules, filteredlist)

sum_to_1000 = filter(lambda x: sum(x) == 1000, triples)

print(sum_to_1000) # [[375, 200, 425]] == 31,875,000
