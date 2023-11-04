# [Capitulo 1](https://linktr.ee/enthonyaraujo)
## Motivação

Este livro foi escrito com o iniciante em programação em mente. Embora a
linguagem Python seja muito poderosa e rica em recursos modernos de programação,
este livro não pretende ensinar apenas a linguagem em si, mas ensinar a
programar em qualquer linguagem. Alguns recursos da linguagem Python não
foram utilizados. O objetivo foi privilegiar os exercícios de lógica de programação
e melhor preparar o leitor para outras linguagens. Essa escolha não impediu que
recursos poderosos da linguagem fossem apresentados, mas este livro não é uma
referência da linguagem Python.

O capitulo 1 visa a apresentar o desafio de aprender e estimular o estudo da
programação de computadores, apresentando problemas e aplicações do dia a dia.

Vejamos um pequeno programa escrito em Python na listagem 1.1.
- Programa Olá Mundo
```py
print("Olá Mundo")
```

A palavra **print** é uma função utilizada para enviar dados a tela do computador.
Observe que as aspas (") não aparecem na tela. Esse é um dos detalhes da programação:
precisamos marcar ou limitar o início e o fim de nossas mensagens com um símbolo, 
nesse caso, aspas.

# [Capitulo 2](https://linktr.ee/enthonyaraujo)
## Preparando o ambiente

Você pode baixar python em https://www.python.org/downloads/ .E escolher seu sistema, seja ele Windows, Linux ou MacOS.

##  Usando o interpretador
Com o Python instalado, vamos começar a trabalhar.
O IDLE é uma interface gráfica para o interpretador Python, permitindo também
a edição e execução de nossos programas. No Windows Vista e no Windows 7,
você deve ter uma pasta no menu Iniciar > Programas > Python 3.4. Escolha IDLE. No
Windows 8 e 8.1, procure por Python 3.12 na lista de aplicativos e, então, por IDLE
(Python GUI).

No Linux, abra o terminal e digite:
```
idle-python3.12 &
```

No Mac OS X, abra o terminal e digite:
```
IDLE3.12 &
```

- Usando o interpretador como calculadora.
```
*>>>* 2 + 3

5
```
- Subtração
```  
*>>>* 5-3

2
```
- Adição e subtração
```  
>>> 10-4+2

8
```
- Multiplicação e divisão
```
>>> 2*10

20
```
```
>>> 20/4

5.0
```
- Exponenciação
``` 
>>> 2**3
 
8
```
Os parênteses são utilizados em Python da mesma forma que em expressões
matemáticas, ou seja, para alterar a ordem de execução de uma operação. Para
relembrar a ordem de precedência das operações, temos as seguintes prioridades:

| Tipo | Forma | 
| :--------- | :------: | 
| Potenciação |(**) | 
| Multiplicação | (*) |
| Divisão | (/ e %) |
| Adição | (+) |
| Subtração | (-) |

## Conceitos de variáveis e atribuição

Para armazenar algo nesses compartimentos, usaremos o símbolo de igualdade (=) 
entre o nome do compartimento e o valorque queremos armazenar. Chamaremos essa 
operação de atribuição, onde umvalor é atribuído a uma variável. Quando lermos 
nosso programa, as operaçõesde atribuição serão chamadas de “recebe”, ou seja, 
uma variável recebe um valor.

- O primeiro programa com variáveis
```py
a = 2 (1)
b = 3 (2)
print (a + b) (3)
```
Vemos que cada linha significa uma coisa. Nas linhas 1 e 2, **a recebe 2** e **b recebe 3**, que após isso  a função **print** realiza a impressão, mas, antes, o resultado de **a + b** é calculado.

- Exemplo mostrado no interpretador
```
>>> a = 2                                              
>>> b = 3                                                                    
>>> print ( a + b )                                                            
5
```
As duas primeiras linhas não enviam nada para a tela; por isso, apenas o resultado
da terceira linha é mostrado.

Outra maneira de resolver o problema seria: 
- Outra forma de resolver o problema
```
print (2 + 3)
```
Dessa forma o resultado seria o mesmo:

- Outra forma de resolver o problema
```
print (5)
```
Então, por que escolhemos resolver o problema usando variáveis? Primeiramente,
para podermos falar de variáveis, mas também para exemplificar uma grande
diferença entre resolver um problema no papel e por meio de um computador.
Quando estamos resolvendo um problema de matemática no papel, como somar
dois números, realizamos diversos cálculos mentalmente e escrevemos parte desse
processo no papel, quando necessário. Depois de escrito no papel, mudar os valores
não é tão simples. Ao programarmos um computador, estamos transferindo
esse cálculo para o computador. Como programar é descrever os passos para a
solução do problema, é aconselhável escrevermos programas o mais claramente
possível, de forma que possamos alterá-los caso precisemos e, mais importante,
que possamos entendê-los mais tarde.

- Cálculo de aumento de salário
```
salário = 1500 ❶
aumento = 5 ❷
print (salário + (salário * aumento / 100)) ❸
```
Em ❶ temos uma variável que é chamada salário, recebendo o valor 1500. Em ❷,
outra variável, aumento, recebe o valor 5. Finalmente, em ❸ descrevemos a fórmula
que calculará o valor do novo salário depois de receber um aumento. Teríamos,
então, o resultado de **1575**.

# [Capitulo 3](https://linktr.ee/enthonyaraujo)
## Variáveis e entrada de dados

Nomes de variaveis devem inciar com letra, mas podem ter números e o simbolo de underline(_)

Exemplos: 
| Nome | Válido | Comentários |
| :--------- | :------: | :------: |
| a1 | Sim | Embora contenha um número, o nome a1 inicia com letra. | 
| velocidade | Sim | Nome formado por letras. |
| velocidade90 | Sim Nome formado por letras e números, mas iniciado por letra. |
| salário_médio | Sim | O símbolo sublinha (_) é permitido e facilita a leitura de nomes grandes. |
| salário médio | Não | Nomes de variáveis não podem conter espaços em branco. |
| _b | Sim | O sublinha (_) é aceito em nomes de variáveis, mesmo no início. |
| 1a | Não | Nomes de variáveis não podem começar com números. |
                                       
Python tem vários tipos de dados, mas os mais comuns são números inteiros, números de
ponto flutuante e strings. Além de poder armazenar números e letras, as variáveis
em Python também armazenam valores como verdadeiro ou falso.

## Variáveis numéricas 
Dizemos que uma variável é numérica quando armazena números inteiros ou
de ponto flutuante.
- Os números inteiros são aqueles sem parte decimal.
- Números de ponto flutuante ou decimais são aqueles com parte decimal                                         
Em Python, e na maioria das linguagens de programação, utilizamos o ponto, e
não a vírgula.


