# [Capítulo 1](https://linktr.ee/enthonyaraujo)
# Motivação

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

# [Capítulo 2](https://linktr.ee/enthonyaraujo)
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

# [Capítulo 3](https://linktr.ee/enthonyaraujo)
# Variáveis e entrada de dados

Nomes de variaveis devem inciar com letra, mas podem ter números e o simbolo de underline(_)

Exemplos: 
| Nome | Válido | Comentários |
| :--------- | :------: | :------: |
| a1 | Sim | Embora contenha um número, o nome a1 inicia com letra. | 
| velocidade | Sim | Nome formado por letras. |
| velocidade90 | Sim | Nome formado por letras e números, mas iniciado por letra. |
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
- Os `números inteiros` são aqueles sem parte decimal.
- `Números de ponto flutuante` ou decimais são aqueles com parte decimal                                         
Em Python, e na maioria das linguagens de programação, utilizamos o ponto, e
não a vírgula.

## Variáveis do tipo Lógico
Muitas vezes, queremos armazenar um conteúdo simples: verdadeiro ou falso em
uma variável. Nesse caso, utilizaremos um tipo de variável chamado `tipo lógico
ou booleano`. Em Python, escreveremos `True` para verdadeiro e `False` para falso.

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
Em Python é usado `#` para escrever comentarios.

## Operadores lógicos
| Operador Python | Operação |
| :------: | :------: | 
| not | não |
| and | e |
| or | ou |

- O operador `not` (não) é o mais simples, pois precisa apenas de um operador.

```
>>> not True
False
>>> not False
True
```

- O operador `and` (e) resulta verdadeiro apenas quando seus dois operadores forem verdadeiros.
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

- O operador `or` (ou) resulta em false apenas se seus dois operadores também forem falsos. Se apenas um de seus operadores for verdadeiro, ou se os dois forem, o resultado da operação é verdadeiro.
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

Operador `not` primeiramente, seguido do operador `and` e por fim o operador `or`. Vejamos o exemplo:
```
True or False and not True
True or False and False
True or False
True
```

## Variaveis Strings
Variaveis do Tipo Strings armazenam nomes e textos em geral. São do tipo caractere.
Para escrever em strings é utilizado aspas simples ('') ou aspas duplas ("").

`Função len()`

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
Para juntar (concatear) duas ou mais strings utilizamos o simbolo de `(+)`.
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

Exemplo de uma composição `inteiro`
```
>>> idade = 20
>>> print("%d" % idade)
20
```
Exemplo de uma composição `float`
```
>>> peso = 58.60
>>> print("%.2f" %peso)
58.60
```
Exemplo de uma composição `string`
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
Para melhorar os programas é não trabalhar com valores conhecidos, e sim com valores que o usuario quiser colocar, pra o programa ficar mais intuitivo. Chamamos de entrada de dados (como o teclado do computador). A função `input` é utilizada para solicitar esses dados do usuario.
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
A função `input` sempre retorna valores em string, mesmo se for números. Para resolver esse problema podemos utilizar a função `int` ou `float`.

```
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
print("Você tem: %d Anos e pesa %f" % (idade,peso))
```

# [Capítulo 4 ](https://linktr.ee/enthonyaraujo)
# Condições                                                                          
Nem sempre todas as linhas dos programas serão executadas. Muitas vezes é mias interessante decidir que partes do programa devem ser executadas com base em uma condição.

## if                                                                                                        
O `if` nada mais é que o nosso “se”. Poderemos então entendê-lo em português da
seguinte forma: se a condição for verdadeira, faça alguma coisa.

```
if <condição>: 
  bloco verdadeiro
```
Exemplo de condição: 

```py
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
  print("Seu carro é novo") 
if idade > 3:
  print("Seu carro é velho") 
```

## else

Usamos `else` para especificar o que fazer caso o resultado da avaliação da condição seja falso, o else seria o **se não**.

Exemplo de condição else: 

```py
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
  print("Seu carro é novo")
else:
  print("Seu carro é velho")
```

## Estruturas aninhadas

Nem sempre os programas serão tão simples e muitas vezes é preciso aninhar varios **if** no codigo. Aninhar signifca utilizar um **if** dentro do outro.

Exemplo dessa condição: 

```py
categoria = int(input("Digite a caterogia do produto: "))

if categoria == 1:
    preço = 10
else: 
    if categoria == 2:
        preço = 18 
    else:
        if categoria == 3:
            preço = 23 
        else:
            if categoria == 4:
                preço = 26 
            else:
                if categoria == 5:
                    preço = 31
                else:
                    print("Categoria Invalida digite um valor entre 1 e 5")
                    preço = 0
print("O preço do produto é: %6.2f" %preço)
```

## elif

Uma solução para um problema com varios **if**s é a cláusula **elif**. Com ele você não precisará ficar colocando **if** e **else** simultaneamente.

Exemplo anterior usando o **elif**

```py
categoria = int(input("Digite a caterogia do produto: "))

if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18 
elif categoria == 3:
    preço = 23 
elif categoria == 4:
    preço = 26 
elif categoria == 5:
    preço = 31
else:
    print("Categoria Invalida digite um valor entre 1 e 5")
    preço = 0
print("O preço do produto é: %6.2f" %preço)
```

# [Capítulo 5](https://linktr.ee/enthonyaraujo)
# Repetições

As estruturas de repetições é um recurso muito importante nas linguagem de programação. Permite executar a mesma parte do programa varias vezes.

Podemos imaginar um programa que imprima os números de 1 a 100, seria muito trabalhoso ficar digitando:
```py
print(1)
print(2)
print(3)
...
...
...
```
Outra forma de escrever:
```py
x=1
print(x)
x=2
print(x)
x=3
print(x)
...
...
...
```
Outra maneira de escrever incremetando:
```py
x=1
print(x)
x=x+1
print(x)
x=x+1
print(x)
...
...
...
```
Seria melhor declarar uma varialvel **x** onde x pode variar de 1 a 100 (1<x<100). Por isso usaremos os laços de repetições para facilitar a escrita do programa, as estruturas usadas são `while`, `do-while` e `for` .

## while

Formato da estrutura de repetição com **while**:
```
while <condição>:
  bloco
```

Para resolvermos o problema anterior de imprimir o números de 1 a 100 usando o **while** fica bem simples:

```py
x = 1 
while x<=100:
    print(x)
    x = x+1
```

A execução desse programa seria um pouco diferente do que vimos até agora.
Primeiramente, seria executada inicializando a variável x com o valor 1. A linha
2 seria uma combinação de estrutura condicional com estrutura de repetição.
Podemos entender a condição do while da mesma forma que a condição de if. A
diferença é que, se a condição for verdadeira, repetiremos as linhas 3 e 4 (bloco)
enquanto a avaliação da condição for verdadeira.

## Contadores

O poder das estruturas de repetições é muito interessante, principalmente quandoutilizamos condições com mais de uma variável. Imagine um problema onde deveríamos imprimir os números inteiros entre 1 e um valor digitado pelo usuário.

```py
final = int(input("Digite o ultimo número para imprimir: "))
x = 1
while x <= final:
    print(x)
    x = x + 1
```
Logo diremos que x é um contador. Um contador é uma variável utilizada para contar o número de ocorrências de um determinado evento; nesse caso, o número de repetições do while, que satisfaz às necessidades de nosso problema.

O programa a seguir vai imprimir números pares onde o final é definido pelo o usuário:
```py
final = int(input("Digite o ultimo número para imprimir: "))
x = 0
while x <= final:
    if x % 2 == 0:
        print(x)
    x = x + 1
```

O operador `%` em Python é lido como "por cento" ou "módulo", dependendo do contexto em que está sendo usado.

Se x(numero) % == 0 **ele é par**

Se x(numero) % == 1 **ele é impar**

Outro exemplo, imprimir a tabuada de adição de 1 a 10 de um número digitado pelo usuário.

```py
n = int(input("Digite o ultimo número para imprimir: "))
x = 1 
while x <= 10:
    print(n+x)
    x=x+1
```

## Acumuladores

Nem só de contadores precisamos. Em programas para calcular o total de uma soma, por exemplo, precisaremos de acumuladores. A diferença entre um contador e um acumulador é que nos contadores o valor adicionado é constante e, nos acumuladores, variável.
```py
n = 1
soma = 0

while n<=10:
    x = int(input('Digite o %d numero:' %n))
    soma = soma + x #ACUMULADOR
    n += 1 #CONTADOR
    
print('Soma: %d' %soma)
```

## Interrompendo a repetição

O comando `break` é utilizado para interromper a execução do `while` independente do valor atual de sua condição.
```py
s = 0

while True:
    v = int(input('Digite um número a somar ou 0 para sair: '))
    if v == 0:
        break
    s = s+v
print(s)
```
Nesse exemplo, substituímos a condição do while por True em . Dessa forma, o while executará para sempre, pois o valor de sua condição de parada (True) é constante. Temos a instrução break sendo ativada dentro de um if, especificamente quando v é zero. Porém, enquanto v for diferente de zero, a repetição continuará a somar v a s.

## Repetições aninhadas

Podemos combinar vários `while` de forma a obter resultados mais interessantes, como a repetição com incremento de duas variáveis.

Exemplo com uma tabuada:
```py
tabuada = 1

while tabuada <=10:
    numero = 1
    print('Tabuada de %d' %tabuada)
    while numero <=10:
        print('%d x %d = %d' %(tabuada,numero,numero*tabuada    ))
        numero +=1
    tabuada +=1
```



