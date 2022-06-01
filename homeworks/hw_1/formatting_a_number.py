def format_number(n):
    print(f'{n:*^30,.3f}'.replace(',', ' ').replace('.', ' .'))

n = float(input())
format_number(float(input()))
