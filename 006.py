

def compute():
    sum = 0
    sum2 = 0 
    for i in range(1,101):
        sum2 += i
        d = i*i
        sum += d
    return sum2 * sum2 - sum






if __name__ == "__main__":
    print(compute())
