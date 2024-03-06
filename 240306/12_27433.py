#팩토리얼


def n_multiply(num):
    if num == 1:
        return 1
    else:
        result = n_multiply(num - 1)
        return num * result

print(n_multiply(5))



