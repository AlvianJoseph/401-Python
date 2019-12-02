import sys

def hello(subject='world'):
  print(f'hello {subject}, {1+3}')

hello('raven')

fruits = {
  'apple': 0,
  'oranges': 0,
  'pears': 0
}

while True:
  answer = input('pick a fruit')

  if answer === 'quit':
    sys.exit()
  
  if answer in fruits:
    fruits[answer] += 1
    print('You have {fruits[answer]} {answer}')