#import random

# Lista de vogais e consoantes
#vowels = 'aeiou'
#consonants = 'bcdfghjklmnpqrstvwxyz'

#def generate_random_word(length=5):
    #"""
    #Gera uma palavra aleatória com a combinação de vogais e consoantes.
    #"""
    #word = ''
    #for _ in range(length):
        #if random.choice([True, False]):
           # word += random.choice(vowels)
       # else:
           # word += random.choice(consonants)
   # return word

# Exemplo de uso
#random_word = generate_random_word()
#print(f"Palavra aleatória: {random_word}")
print(f"{5 * '='} My guessing game! {5 * '='}")
print('See the list of words below:')
print(55 * '-')
print('''apple, banana, cat, dog, elephant, flower, grape, house,
island, jungle, kite, lemon, mountain, nest, ocean, piano,
queen, rainbow, sun, tree, umbrella, violet, watermelon,
xylophone, yellow, zebra.''')
print(55 * '-')
import random
v = 5
#while True:
english_words = [
        "apple", "banana", "cat", "dog", "elephant", "flower", "grape", "house",
        "island", "jungle", "kite", "lemon", "mountain", "nest", "ocean", "piano",
        "queen", "rainbow", "sun", "tree", "umbrella", "violet", "watermelon",
        "xylophone", "yellow", "zebra"
    ]
    #def generate_meaningful_word():
        #"""
        #Gera uma palavra aleatória com significado a partir do dicionário.
        #"""
        #return random.choice(english_words)
s = random.choice(english_words)
while True:
    n = input(str('Try to guess the word!: '))
    #s = generate_meaningful_word()
    if n == s:
        print(f'Great, you guessed the word {s}')
        j = input('Do you want to continue? yes or no: ').lower()
        if j == 'yes':
            ''
            s = random.choice(english_words)
            if v == 5:
                ''
            elif v == 4:
                v += 2
            elif v == 3:
                v += 3
            elif v == 2:
                v += 4
            elif v == 1:
                v += 5
        else:
            break
    if n != s:
        v -= 1
        print(f'Try again, now you have your chance {v} !')
        if n > s:
            print('Dica: Tá na esquerda!')
        else:
            print('Dica: Tá na direita!')
    if v == 0:
        j = input(f' The wold was {s}! Do you want to continue? yes or no: ').lower()
        if j == 'yes':
            ''
        else:
            break
print('Thanks for playing!')






