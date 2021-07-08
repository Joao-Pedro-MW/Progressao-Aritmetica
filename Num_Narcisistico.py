

def narcissistic(value):
    valor,str_v = 0, str(value)
    expoente = len(str_v)
    for i in str_v:
        valor += (int(i))**expoente
    valor = int(valor)
    print(valor)
    if valor == value: return True
    else: return False   

print(narcissistic(153))
