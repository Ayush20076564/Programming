a=3
b=5
limit=1000
def sum_multiples(limit):
    total = 0
    for number in range(limit):
        if number % a == 0 or number % b == 0:
            total += number
    print (total)

sum_multiples(limit)