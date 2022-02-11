"""
Calculo de sequencia de numeros fibonnaci
"""
#Usando lista:

def fib_list(max):
    nums = []
    a, b = 0,1
    while len(nums)<max:
        nums.append(b)
        a, b = b, a + b
    return nums

for n in fib_list(10):
    print(f"\033[1;36mlista -> {n}\033[0m")


############    ###########     #############   ########
#Usando gerador:

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador<max:
        a, b = b, a + b
        yield a
        contador = contador + 1

for m in fib_gen(10):
    print(f"\033[1;31mgerador->{m}\033[0m")
