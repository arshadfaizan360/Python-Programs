def sum_num(n):
    if n == 1:
        ans = 1
    else:
        ans = n + sum_num(n-1)
    return ans

def pyramid_sum(n):
    if n == 1:
        ans = 1
    else:
        ans = sum_num(n) + pyramid_sum(n-1)
    return ans 

print(pyramid_sum(int(input('Enter a number to find the sum of all of the numbers up to and including it: '))))

