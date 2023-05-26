import re

def automato(entrada):
    estados = [
        {
            'X': 1,
            '[^ab]': 33,
            '[ab]': 0
        },
        {
            '[^ab]': 33,
            '[ab]': 1
        }
    ]
    estado_atual = 0
    cadeia_atual = ''
    for i in range(len(entrada)):
        char = entrada[i]
        #verifica se a cadeia é impar
        if len(entrada)%2==0:
            return f"{entrada} Cadeia não reconhecida"
        #verifica se o estado atual é aceito
        if estado_atual >= len(estados):
            return f'{entrada} Cadeia não reconhecida'
        #percorre a lista de estados e ve se existe algum compativel
        for regex, prox in estados[estado_atual].items():
            if estado_atual!=1 and char!='X':
                if re.match(f'^{regex}$', char):
                    estado_atual = prox
                    cadeia_atual = char + cadeia_atual
                    break
            else:
                #percebe o meio da palavra 'X' e muda o estado
                if char=='X':
                    estado_atual = prox
                    break
                else:
                    #percorre a cadeia_atual
                    if len(entrada[i+1:])!=len(cadeia_atual):
                        for x in cadeia_atual:
                            if x!=entrada[i]:
                                return f'{entrada} Cadeia nao reconhecida'
                            else:
                                #remove um caracter da lista
                                cadeia_atual=cadeia_atual[1:]
                            break
                        break
                    else:
                        return f'{entrada} Cadeia nao reconhecida'
    finais = {
        1: 'palavra com wXwr'
    }
    if estado_atual in finais:
        return f'{entrada} - Cadeia aceita como:  [{finais[estado_atual]}]'
    else:
        return f'{entrada} - Cadeia não reconhecida'

print(automato('X'))
print(automato('baXab'))
print(automato('abaXaa'))
print(automato('abaaaaaXaba'))
print(automato('aaXaa'))
print(automato('abaXba'))
print(automato('aXaba'))