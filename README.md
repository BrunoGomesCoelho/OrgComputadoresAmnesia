# OrgComputadoresAmnesia
Trabalho para a matéria organização e arquitetura de computadores usando o software Amnésia


PDF no Overleaf: https://www.overleaf.com/9992982kywmzhcdxqwv


## Estrutura da arquitetura base:

1. Tamanho da memória principal: 2048 palavras = 2048 * 4 bytes = 8192 bytes

2. Tamanho da palavra: 4 bytes

3. Tamanho da cache: 256 palavras

4. Tamanho do bloco: 16 palavras

5. Função de mapeamento: Associativo por conjunto

6. Número de blocos por conjunto: 4 blocos (k = 4)
    - Número de conjuntos: 4 conjuntos

7. Algoritmo de substituição: FIFO

8. Poltica de Escrita: Write Through

9. Número de caches: 1 cache

10. Tipo da(s) cache(s): Unificada
