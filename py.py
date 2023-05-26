def automato(string):
    pilha=[]
    i=0  

    while i <len(string) and string[i] in ("a","b"):
        pilha.append(string[i])
        i+=1

    if string[i]=='X':
        i+=1
    else:
        return "Cadeia nao reconhecida"
    
    while i < len(string) and pilha:
        if string[i]==pilha[-1]:
            pilha.pop()
            i+=1
        else:
            return "Cadeia nao reconhecida"
    
    return 'cadeia reconhecida'

print(automato('abbbaXabbba'))
