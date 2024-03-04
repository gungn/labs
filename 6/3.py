def find_delit(num):
    delit = []
    for i in range(2, int(num*0.5)):
        if num % i == 0:
            delit.append((i, num//i))
    return delit


for num in range(174457, 174506):
    delit = find_delit(num)
    if len(delit) == 2:
        delit1, delit2 = delit[0]
        print(delit1, delit2)
