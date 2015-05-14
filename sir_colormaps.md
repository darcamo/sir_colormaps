---
title: SIR Colormaps
author: Darlan Cavalcante Moreira
date: May 10, 2014
---


# Descrição do Cenário #

O cenário é composto de um andar de uma construção contendo 144 salas
quadradas com 10 m de lado. A densidade de AN será variada de 1 AN em cada
sala até 1 AN a cada 9 salas, como mostrado nas 4 figuras abaixo.


![1 AP in each room](./figs/scenario_1_ap_1_room.{{imageExt}})

![1 AP every 2 rooms](./figs/scenario_1_ap_2_rooms.{{imageExt}})

![1 AP every 4 rooms](./figs/scenario_1_ap_4_rooms.{{imageExt}})

![1 AP every 9 rooms](./figs/scenario_1_ap_9_rooms.{{imageExt}})



# Cálculo Analítico da SIR #

Calcular a SIR analiticamente, pelo menos nas bordas.


O modelo de path loss utilizado foi

$$PL = A \cdot \log_{10}(d) + B + C \cdot \log_{10}(f_c/5) + X,$$

onde $f_c$ é dado em GHz e $d$ em metros. O valor de $X$ é dado por
$5 (n_w - 1)$, onde $n_w$ corresponde ao número de paredes que o sinal
atravessa.

Os valores de $A$, $B$ e $C$ são diferentes para o caso com linha divisada
(LOS) e sem linha divisada (NLOS), como mostrado na tabela abaixo.

 Cenário       A        B       C
----------  -------  -------  ------
   LOS        18.7     46.8     20 
   NLOS       36.8     43.8     20

Table: Parâmetros de Path Loss


Considere agora a figura abaixo mostrando uma região do cenário com
densidade de 1 AN a cada duas salas.

![1 AP every 2 rooms](./figs/scenario_1_ap_2_rooms_sub.{{imageExt}})

Ambos os usuários **A** e **B** estão mais próximos do ponto de acesso 3 e
se conectam com ele, onde o usuário **A** está na mesma sala (LOS) e o
usuário **B** está em uma sala diferente do ponto de acesso.

A distâncias entre usuários **A** e **B** e cada pondo de acesso mostrado
são indicadas na tabela abaixo, assim como o número de paredes que o sinal
precisa atravessar para chegar no usuário.

Usuário          AN1    AN2      AN3    AN4      AN5    AN6
--------        -----  ------  ------  ------  ------  ------
   A            21.21  15.81    7.07   15.81    7.07   15.81
   B            22.36  22.36    10.0   10.0     10.0    10.0
   A (paredes)   2       2       0       2        2      2
   B (paredes)   3       3       1       1        1      1
   
Table: Distâncias e número de paredes para cada ponto de acesso


<!-- ANs = np.array([-.5 + 1j * 1.5, 1.5 + 1j * 1.5, 0.5 + 1j * 0.5, -.5 + 1j * -0.5, 1.5 + 1j * -0.5, 0.5 + 1j * -1.5]) -->


Considerando uma portadora com 900 MHz, a perda de percurso do sinal
desejado para o usuário **A** é dada por

$$PL_A[3] = 18.7 \cdot \log_{10}(7.07) + 46.8 + 20 \cdot \log_{10}(0.9/5) = 47.79\text{dB}$$

e do sinal desejado para o usuário **B** é dada por

$$PL_B[3] = 36.8 \cdot \log_{10}(10) + 43.8 + 20 \cdot \log_{10}(0.9/5) + 5(1-1) + 1*5= 70.71 \text{dB}.$$

Note que além da perda por cada parede contabilizada em $X$ também foi
incluída uma perda extra de 5dB por parede como descrito no cenário. Com
isso, os valores totais de perda de **A** e **B** para cada ponto de acesso
são então mostrados (em dB) na tabela abaixo.

Usuário          AN1    AN2      AN3    AN4      AN5    AN6
--------        -----  ------  ------  ------  ------  ------
   A            87.72   83.03   47.79   83.03   70.17   83.03
   B            93.57   93.57   70.71   70.71   70.71   70.71

Table: Valores de perda de percurso em dB


Para calcular os valores de SIR, basta convertermos os valores da tabela
acima para escala linear (lembrando de usar o negativo dos valores visto
tratar-se de uma perda), o que resulta na tabela abaixo.

Usuário          AN1         AN2       AN3       AN4       AN5      AN6
--------        --------  --------  --------  --------  --------  --------
   A            1.69E-09  4.98E-09  1.66E-05  4.98E-09  9.62E-08  4.98E-09
   B            4.40E-10  4.40E-10  8.50E-08  8.50E-08  8.50E-08  8.50E-08

Table: Valores de perda de percurso em escala linear


Depois disso basta dividir o valor referente ao ponto de acesso 3
(desejado) pela soma dos valores dos demais pontos de acesso
(interferences), o que resulta nos valores de SIR mostrados abaixo

Usuário    SIR
--------  ----- 
   A      21.68
   B      -4.79

Table: SIR (em dB)




# Medir a SIR em pontos específicos #

Para visualizar como a SIR varia foi feita uma discretização de cada sala,
resultando em 225 pontos uniformemente distribuídos. A figura abaixo mostra
os pontos discretos para uma única sala, com o access node (caso exista
nessa sala) indicado nom centro.

![Discrete points](./figs/discretized_room.{{imageExt}})

Note que a distância entre a borda da sala e o ponto mais próximo é
exatamente igual a metade da distância entre dois pontos, de forma que a
distância entre os dois pontos mais próximo de duas salas vizinhas seja a
mesma distância entre dois pontos mais próximos na mesma sala.


As figuras abaixo mostram a SIR para cada densidade de ANs.

![1 AP in each room](./figs/sinr_1_ap_1_room.{{imageExt}})

![1 AP every 2 rooms](./figs/sinr_1_ap_2_rooms.{{imageExt}})

![1 AP every 4 rooms](./figs/sinr_1_ap_4_rooms.{{imageExt}})

![1 AP every 9 rooms](./figs/sinr_1_ap_9_rooms.{{imageExt}})

Para cada densidade podemos computar a SIR mínima e média em todos os 225
pontos de cada sala, resultando na tabela abaixo.

  Density    Minimum SIR    Mean SIR     Maximum SIR
----------  -------------  -----------  -------------
   1/1          14.505         21.050       67.599
   1/2          -4.778         19.852       84.310
   1/4          -4.777         17.314       88.763
   1/9           7.146         26.268       105.222

Table: Valores de SIR em todas as salas


Vale lembrar que apenas a perdade percurso com a distância, além das perdas
por cada parede foram contabilidadas.


A fim de reduzir os efeitos de borda nas estatísticas de SIR, vamos agora
considerar apenas as **6x6** salas mais internas nos cálculos de SIR
mínima, média e máxima, mas ainda incluindo a interferência causada pelas
salas mais externas. Os novos valores de SIR são mostrados na tabela
abaixo.


  Density    Minimum SIR    Mean SIR     Maximum SIR
----------  -------------  -----------  -------------
   1/1         14.505        20.479         64.527
   1/2         -4.778        19.008         79.147
   1/4         -4.777        14.812         85.749
   1/9          7.146        22.143        102.227

Como podemos ver, os valores de SIR mínima para cada densidade de ANs
permaneceram inalterados, já que esses valores ocorrem na(s) sala(s) mais
centrais do grid. Já os valores de SIR máximos sofreram uma redução, visto
que ocorrem em salas mais próximas da borda do grid. 


## Regiões Interessantes  ##

Frequentemente estamos interessados nos valores de SIR em alguns pontos
chaves que caracterizam cenários como *borda da célula*, *meio de célula* e
*próximo a base.*

**TODO**: A sequir mostramos a SIR para essas diferentes regiões.

- Medir a SIR em pontos específicos que caracterizariam certos cenários
    - os 4 cantos na borda e depois você constrói quadrados virtuais de
      raio menor, dentro do comodo
    - por exemplo a 50% do raio e a 10% do raio
    - e calcula a SIR nos 4 cantos desses quadrados virtuais,
      caracterizando situações de borda, meio de célula e próximo do AP
    - Ai você calcula a media e os percentis 10%, 50% e 90%. 



# Variação com diferentes layouts de disposição dos APs #

**TODO**

- Outra variação que pode ser verificada eh se cabem diferentes layouts de
  disposição dos APs no grid e como isso influencia os resultados.
