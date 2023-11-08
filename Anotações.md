# [Capitulo 1](https://linktr.ee/enthonyaraujo)
# Motivação

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
# Preparando o ambiente

Você pode baixar python em https://www.python.org/downloads/ .E escolher seu sistema, seja ele Windows, Linux ou MacOS.

##  Usando o interpretador
Com o Python instalado, vamos começar a trabalhar.
O IDLE é uma interface gráfica para o interpretador Python, permitindo também
a edição e execução de nossos programas. No Windows Vista e no Windows 7,
você deve ter uma pasta no menu Iniciar > Programas > Python3. Escolha IDLE. No
Windows 8 e 8.1, procure por Python 3 na lista de aplicativos e, então, por IDLE
(Python GUI).

No Linux, abra o terminal e digite:
```
python3
```

No Mac OS X, abra o terminal e digite:
```
python3
```

- Usando o interpretador como calculadora.
Podemos fazer contas matematicas no interpretador.
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
# Variáveis e entrada de dados

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
- Os **números inteiros** são aqueles sem parte decimal.
- **Números de ponto flutuante** ou decimais são aqueles com parte decimal                                         
Em Python, e na maioria das linguagens de programação, utilizamos o ponto, e
não a vírgula.

## Variáveis do tipo Lógico
Muitas vezes, queremos armazenar um conteúdo simples: verdadeiro ou falso em
uma variável. Nesse caso, utilizaremos um tipo de variável chamado **tipo lógico
ou booleano**. Em Python, escreveremos **True** para verdadeiro e **False** para falso.

```
verdadeiro = True
Falso = False
```

## Operadores relacionais

Operador | Operação | Símbolo matemático |
| :--------- | :------: | :------: |
| == | igualdade | = |
| > | maior que | > |
| < | menor que | < | 
| != | diferente | ≠ |
| >= | maior ou igual | ≥ |
| <= | menor ou igual | ≤ |

Exemplo: 
```
>>> a=1
>>> b=5
>>> c=2
>>> d=1
>>> b==a
False
>>> b>a
True
>>> a<b
True
```

## Comentarios
Em Python é usado # para escrever comentarios.

## Operadores lógicos
| Operador Python | Operação |
| :------: | :------: | 
| not | não |
| and | e |
| or | ou |

- O operador **not*8 (não) é o mais simples, pois precisa apenas de um operador.

```
>>> not True
False
>>> not False
True
```

- O operador **and** (e) resulta verdadeiro apenas quando seus dois operadores forem verdadeiros.
```
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
```

- O operador **or** (ou) resulta em false apenas se seus dois operadores também forem falsos. Se apenas um de seus operadores for verdadeiro, ou se os dois forem, o resultado da operação é verdadeiro.
```
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
```

## Expressões lógicas

Os operadores lógicos podem ser combinados em expressões lógicas mais complexas. Quando uma expressão tiver todos os operadores lógicos eles são executas com uma ordém.

Operador **not** primeiramente, seguido do operador **and** e por fim o operador **or**. Vejamos o exemplo:
```
True or False and not True
True or False and False
True or False
True
```

## Variaveis Strings
Variaveis do Tipo Strings armazenam nomes e textos em geral. São do tipo caractere.
Para escrever em strings é utilizado aspas simples ('') ou aspas duplas ("").

#### Função len()

A função len() determina o tamanho de uma string.
```
>>> print(len("Ola a todos"))
11
```

Uma característica de strings é poder acessar seu conteúdo caractere a caractere. Esses números são chamados de indice, e começamos a contar do zero.
| 0 | 1 | 2 | 3 | 4 | 5 |
| :------: | :------: | :------: | :------: |  :------: | :------: |
| A | B | C | D | E | F | 

Para acessar os indices em qualquer string é utilizado colchetes **[]**, e dentro do colchetes o indice que você quer escolher.
```
>>> letras = "ABCDEF"
>>> print(letras[0])
A
````

## Concatenação
Para juntar (concatear) duas ou mais strings utilizamos o simbolo de **(+)**.
```
>>> j = "ABC"
>>> s = "DEF"
>>> print(j+s)
ABCDEF
```

## Composição
Marcadores de posição.
| Marcador | Tipo |
| :------: | :------: | 
| %d | Números inteiros |
| %s | Strings |
| %f |Números decimais |

Exemplo de uma composição **inteiro**
```
>>> idade = 20
>>> print("%d" % idade)
20
```
Exemplo de uma composição **float**
```
>>> peso = 58.60
>>> print("%.2f" %peso)
58.60
```
Exemplo de uma composição **string**
```
>>> nome = "Enthony"
>>> idade = 20
>>> peso = 58.60
>>> print("%s tem %d anos e pesa %.2f kilos" % (nome, idade, peso))
Enthony tem 20 anos e pesa 58.60 kilos
```

## Fatiamento 
Podemos fatiar uma string, por exemplo se temos a string ABBCDEF, utilizando os indices [0:2], podemos fatiar para que apareça apenas o AB, isso explica que o número da direita diz a posição inicial, e o do outro lado a posição final. Nesse caso o C não está incluso, por que é até onde o fatiamento vai.

```
>>> s = "ABCDEF"
>>> print(s[0:2])
AB
```
Se quisermos o CD:
```
>>> s = "ABCDEF"
>>> print(s[2:4])
CD
````
E assim sucessivamente.                                                            
Podemos também utilizar valores negativos, como **-1**, nesse caso ele mostra o ultimo valor.

## Sequências e tempo
Um programa é executado linha por linha assim se você declara uma variavel, iniciamente ela pode ter um valor e depois ter outro, ou seja, ela pode mudar com o tempo.
```
>>> divida = 0 #inicialmente começa com 0
>>> compra = 100
>>> divida = divida + compra #apos aumenta mais 100
>>> compra = 200
>>> divida = divida + compra #soma 100 com 200
>>> print(divida) #divida = 300
300
```

## Entrada de dados
Para melhorar os programas é não trabalhar com valores conhecidos, e sim com valores que o usuario quiser colocar, pra o programa ficar mais intuitivo. Chamamos de entrada de dados (como o teclado do computador). A função **input** é utilizada para solicitar esses dados do usuario.
```
>>> x = input("Digite seu numero: ")
Digite seu numero: 8
>>> print(x)
8
```

```
Exemplo de entrada de dados com **String**
nome = input("Digite seu nome: ")
print("Voce digitou %s" % nome  )
```

## Conversão de entradas de dados
A função **input** sempre retorna valores em string, mesmo se for números. Para resolver esse problema utilizando a função **int** ou **float**.

```
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
print("Você tem: %d Anos e pesa %f" % (idade,peso))
```

# [Capitulo 4 ](https://linktr.ee/enthonyaraujo)
# Condições                                                                          
Nem sempre todas as linhas dos programas serão executadas. Muitas vezes é mias interessante decidir que partes do programa devem ser executadas com base em uma condição.

## if                                                                                                        
O **if** nada mais é que o nosso “se”. Poderemos então entendê-lo em português da
seguinte forma: se a condição for verdadeira, faça alguma coisa.

```
if <condição>
  bloco verdadeiro
```
Exemplo de condição: 

```
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

if a > b:
    print("%d maior que %d" %(a,b))
if b > a:
    print("%d maior que %d"%(b,a))
```


