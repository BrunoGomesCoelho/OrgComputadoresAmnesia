from random import randint, random, shuffle
import operator
# randint: retorna um número inteiro aleatorio (a, b) tq a <= N <= b
# random: numero aleatorio entre 0 e 1

# Variaveis da memoria
tamMemoria = 10000
tamBloco = 4

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

pos = randint(0, tamMemoria-1)
vetorAux.append([pos, time])

hit = 0

def addVector(newPos):
    for j in range(len(vetorAux)):
        vetorAux[j][1] -= 1
    if (len(vetorAux) == tamVetor): 
        vetorAux[len(vetorAux)-1] = [newPos, time]
    else:
        vetorAux.append([newPos, time])
    
    
    
def updateVector(newPos):
    for k in range(len(vetorAux)):
        if vetorAux[k][0] == newPos:
            vetorAux[k][1] = time
        else:
            vetorAux[k][1] -= 1
            
            

def principioTemporal():
    global vetorAux
    '''
    Em ordem decrescente de tempo
    vetorAux.sort(key=operator.itemgetter(1))

    Em ordem crescente de tempo
    vetorAux.sort(key=operator.itemgetter(1))
    vetorAux = vetorAux[::-1]
    '''
    
    # Embaralhando o vetor
    shuffle(vetorAux)
    global hit
    
    for element in vetorAux:
        if element[1] > 0:
            randy = random()
            # hard coded
            if (randy <= freqChoosenVector):
                updateVector(element[0])
                hit += 1
                return element[0]
                
    newPos = randint(0, tamMemoria-1)
    addVector(newPos)
    return newPos

aux = 0


for i in range(qtdTraces):
    
    if (i == qtdTraces/2):
        aux = hit   
    
    rand = random();
    if (rand <= freqLeitura):
        print(rotLeitura, end = " ")
    else:
        print(rotEscrita, end = " ")
    
    pos = principioTemporal()
    print(pos)
    # print(vetorAux)
    
    
print("hit / total %f" % ((hit * 1.0) / qtdTraces))    
