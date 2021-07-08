def find_missing(sequence):
    values = []
    for i in range(len(sequence)):
        v = i+1
        #lidando com erro IndexError
        if v == len(sequence): break
        else:  
            i = sequence[i] 
            v = sequence[v] 
            values.append(v-i) 
#a falha e descoberta ao saber que existe um 
#número diferente dos demais na lista
    if values[0] > 0:
        maximo = max(values)
    #index_do_erro: localiza o maior valor (erro) na lista
        index_do_erro = min(values.index(maximo))
    #e o valor da progressao aritmetica 
        valor_soma = min(values) 
    #soma o valor antes do erro mais o valor da progressao aritmetica
        valor_falta = sequence[index_do_erro] + valor_soma
        return valor_falta
    else:
        maximo = min(values)
    #index_do_erro: localiza o maior valor (erro) na lista
        index_do_erro = values.index(maximo)
    #e o valor da progressao aritmetica 
        valor_soma = max(values) 
    #soma o valor antes do erro mais o valor da progressao aritmetica
        valor_falta = sequence[index_do_erro] + valor_soma
        return valor_falta

   