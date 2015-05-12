---
title: SIR Colormaps
author: Darlan Cavalcante Moreira
date: May 10, 2014
---


Fiquei interessado nos teus resultados para incluir nas aulas dos cursos de
comunicações moveis, aquela analise de SIR do grid de cômodos quadrados.



# Descrição do Cenário #

O cenário é composto de um andar de uma construção contendo 144 salas
quadradas com 10 m de lado. A densidade de AN será variada de 1 AN em cada
sala até 1 AN a cada 9 salas, como mostrado nas 4 figuras abaixo.


![1 AP in each room](./figs/scenario_1_ap_1_room.{{imageExt}})

![1 AP every 2 rooms](./figs/scenario_1_ap_2_rooms.{{imageExt}})

![1 AP every 4 rooms](./figs/scenario_1_ap_4_rooms.{{imageExt}})

![1 AP every 9 rooms](./figs/scenario_1_ap_9_rooms.{{imageExt}})



# Análise teórica simples #

Calcular a SIR analiticamente, pelo menos nas bordas.


# Medir a SIR em pontos específicos #

Para visualizar como a SIR varia foi feita uma discretização de cada sala,
resultando em 225 pontos uniformemente distribuídos. A figura abaixo mostra
os pontos discretos para uma única sala, com o access node (caso exista
nessa sala) indicado nom centro.

![Discrete points](./figs/discretized_room.{{imageExt}})

Note que a distância entre a borda da sala e o ponto mais próximo é
exatamente igual a metade da distância entre dois pontos, de forma que a
distância entre dois os pontos mais próximo de duas salas vizinhas seja a
mesma distância entre dois pontos mais próximos na mesma sala.


**TODO**: Agora vamos medir a SIR em alguns pontos específicos: 

- Medir a SIR em pontos específicos que caracterizariam certos cenários
    - os 4 cantos na borda e depois você constrói quadrados virtuais de
      raio menor, dentro do comodo
    - por exemplo a 50% do raio e a 10% do raio
    - e calcula a SIR nos 4 cantos desses quadrados virtuais,
      caracterizando situações de borda, meio de célula e próximo do AP
    - Ai você calcula a media e os percentis 10%, 50% e 90%. 


# Reduzir efeitos de borda #

A fim de reduzir os efeitos de borda nas estatísticas de SIR, vamos agora
considerar apenas as **6x6** salas mais internas nos cálculos de SIR mínima
e média, mas ainda incluindo a interferência causada pelas salas mais
externas.

**TODO**: Implement


- Acho que vale a pena também reduzir os efeitos de borda
    - incluir os cômodos de borda apenas na geração de interferência nos
      demais cômodos internos, mas excluir a SIR dos cômodos de borda nas
      estatísticas globais (podem enviesar os resultados)


# Variação com diferentes layouts de disposição dos APs #

- Outra variação que pode ser verificada eh se cabem diferentes layouts de
  disposição dos APs no grid e como isso influencia os resultados.
