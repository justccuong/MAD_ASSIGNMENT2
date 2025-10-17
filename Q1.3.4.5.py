import math
def modulo(a, n, d): # -> m congruent with a^n mod d
    power_of_2 = [int(math.log2(n))]
    n_dup = n - 2 ** power_of_2[-1]
    while n_dup > 0:
        power_of_2.append(int(math.log2(n_dup)))
        n_dup -= 2 ** power_of_2[-1]
        
    mod = [a % d]
    i = 2
    while i <= 2 ** power_of_2[0]:
        mod.append((mod[-1] ** 2) % d)
        i *= 2
    
    total_r = 1
    for n in power_of_2:
       total_r *= mod[n]
       
    print(total_r % d)
    return total_r % d

def q13(i, j, k):
    # c = (i + j + k)! / (i! * j! * k!) mod 9999
    c = 1
    n = 1
    MAX = max(i, j, k)
    MIN = min(i, j, k)
    MID = i + j + k - MAX - MIN
    SUM = i + j + k
    for i in range(MID + 1, SUM + 1):
        c *= i
    for i in range(1, MIN + 1):
        n *= i ** 2
    for i in range(MIN + 1, MID + 1):
        n *= i
    c = int(c / n)
    print(f"Q1.3. ", end = "")
    return modulo(c, 1, 9999)
q13(100, 90, 80)

def q14(n):
    dn = 3 ** n + 1
    for i in range(1, n):
        dn -= n - i
    print(f"Q1.4. ", end = "")
    return modulo(dn, 1, 9999)
q14(1000)

def q15(n):
    if n == 1:
        print(3)
        return
    f = [0] * (n - 1)
    e = [0] * n
    f[0] = 2
    e[0] = 3
    for i in range(1, n - 1):
        f[i] = f[i - 1] + 1
    for i in range(1, n):
        e[i] = e[i - 1] + f[i - 1] + 1
    #print(f)
    #print(e)
    #print(e[n - 1])
    print(f"Q1.5. ", end = "")    
    return modulo(e[n - 1], 1, 999)
q15(1000)


