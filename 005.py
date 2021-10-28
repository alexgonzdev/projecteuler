def compute(whole: int):
    divisible = True
    for i in range(1,21):
        if whole % i == 0:
            continue
    
        else:
            return False
            break
    return True


def iterate():
    
    numberFound = False
    i = 20
    

    while compute(i) == False:
        i += 20
    print(i)
        
    return i








if __name__ == "__main__":
    iterate()

