#Escreva uma função chamada most_frequent que receba uma string e exiba as letras em ordem decrescente de frequência.


def most_frequent(text):

  
  count = {}
  for letter in text:
    if letter in count:
      count[letter] += 1
    else:
      count[letter] = 1

  return [(letter, count[letter]) for letter in sorted(count, key=count.get, reverse=True)]


