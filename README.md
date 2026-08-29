# Polygon Explode - QGIS

Plugin de Processing para QGIS que transforma partes de uma geometria poligonal em feicoes separadas.

A operacao principal e equivalente, para cada feicao, a:

ST_Dump(ST_Polygonize(ST_Boundary(geom)))

O plugin:
- recebe uma camada poligonal;
- polygoniza a fronteira de cada feicao;
- cria uma feicao para cada poligono resultante;
- copia todos os atributos da feicao original;
- opcionalmente renumera o campo `gid` de forma sequencial;
- funciona como algoritmo da Caixa de Ferramentas de Processamento.

Testado como estrutura para QGIS 3.44+.
