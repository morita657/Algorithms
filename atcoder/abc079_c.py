L = list('9999999999')
L = list(raw_input())
total = 0
for bit in range(2**(len(L) - 1)):
    P = [""] * (len(L))
    for k in range(len(L) - 1):
        if bit & (1 << k):
            P[k] = ""
        else:
            P[k] = "+"
    calc = ""
    for i in range(len(L)):
        calc += L[i] + P[i]
    calc = eval(calc)
    total += calc
print(total)
