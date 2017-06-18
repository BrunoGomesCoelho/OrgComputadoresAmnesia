from random import randint, random 
import operator
# randint: retorna um número inteiro aleatorio (a, b) tq a <= N <= b
# random: numero aleatorio entre 0 e 1

# Variaveis da memoria
tamBloco = 16 # palavras
qtdBlocos = 128 # blocos na mem principal

tamMemoria = tamBloco * qtdBlocos

qtdTraces = 10000

#Variaveis do algoritmo em geral
freqLeitura = 0.68
freqEscrita = 1 - freqLeitura
threshold = 2

# Variaveis pro principioTemporal
freqTemporal = 0.6
time =  20
tamVetor = time*5
freqChoosenVector = 0.1#1 - (1-freqTemporal) ** (1.0 / tamVetor)
vetorAux = []

# Variaveis para impressão
rotLeitura = 2
rotEscrita = 1


# Funções auxiliares

def addVector(newPos):
    # adiciona um elemento no vetor (se não tiver espaço, removendo o último)
    if (len(vetorAux) == tamVetor): 
        vetorAux[len(vetorAux)-1] = [newPos, time]
    else:
        vetorAux.append([newPos, time])
    

    
def updateVector(newPos):
    # atualiza o tempo de um vetor
    for k in range(len(vetorAux)):
        if vetorAux[k][0] == newPos:
            vetorAux[k][1] = time
            
    
# Decrementa todas as posições do vetor, como se o tempo estivesse rodando.
def decrementVector():
    for l in range(len(vetorAux)):
        vetorAux[l][1] -= 1
            
            

def principioTemporal():
    global vetorAux
    global hit
    '''
    Isso escolhe o quanto agrupado os dados serão agrupados.
    
    Se usarmos o vetor ordenado por tempo (vetorAux.sort(key=operator.itemgetter(1))), então
        os dados serão razuavelmente agrupados.
    
    Se usarmos random.shuffle(vetorAux), temos uma randomização das posições do array e temos um agrupamento médio
    
    Se invertemos o array ordenado, temos muito pouco agrupamento.
        vetorAux.sort(key=operator.itemgetter(1))
        vetorAux = vetorAux[::-1]
    '''
    vetorAux.sort(key=operator.itemgetter(1))
    vetorAux = vetorAux[::-1]
    
    for element in vetorAux:
        if element[1] > 0:
            randy = random()
            # Decidimos aleatoriamente se aquele elemento do vetor será o selecionado
            if (randy <= freqChoosenVector):
                updateVector(element[0])
                hit += 1
                return element[0]
                
    newPos = randint(0, tamMemoria-1)
    addVector(newPos)
    return newPos
    

# Principio Espacial
def principioEspacial(oldPos):
    newPos = oldPos + randint(-threshold*tamBloco, threshold*tamBloco)
    
    if (newPos < 0 or newPos > tamMemoria-1):
        newPos = randint(0, tamMemoria-1)
    
    return newPos
    
    

# inicializando Variaveis necessárias
hit = 0
pos = randint(0, tamMemoria-1)


for i in range(qtdTraces):
    
    rand = random();
    if (rand <= freqLeitura):
        print(rotLeitura, end = " ")
    else:
        print(rotEscrita, end = " ")
    
    decrementVector();    
    randPrinciple = random()
    
    if (randPrinciple <= 0.2): # 20% aleatorio
        pos = randint(0, tamMemoria-1)
    elif (randPrinciple <= 0.6):    # 40% espacial
        pos = principioEspacial(pos)
    else:
        pos = principioTemporal() # 40% temporal

    print(pos)

    
# OBS: hit temporal guarda a frequencia apenas temporal
