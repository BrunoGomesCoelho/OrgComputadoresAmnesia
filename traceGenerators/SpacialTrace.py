from random import randint, random 
# randint: retorna um número inteiro aleatorio (a, b) tq a <= N <= b
# random: numero aleatorio entre 0 e 1

tamBloco = 16 # palavras
qtdBlocos = 128 # blocos na mem principal

tamMemoria = tamBloco * qtdBlocos

qtdTraces = 1000

freqLeitura = 0.68
freqEscrita = 1 - freqLeitura
threshold = 2

rotLeitura = 2
rotEscrita = 1

pos = randint(0, tamMemoria-1)


for i in range(qtdTraces):
    rand = random();
    if (rand <= freqLeitura):
        print(rotLeitura, end = " ")
    else:
        print(rotEscrita, end = " ")
    
    pos += randint(-threshold*tamBloco, threshold*tamBloco)
    
    if (pos < 0 or pos > tamMemoria-1):
        pos = randint(0, tamMemoria-1)
    print(pos)
