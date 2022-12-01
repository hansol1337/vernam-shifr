import time
import random
import itertools


def wordGenerator(len):
    iterable = ''.join(chr(x) for x in range(256)).encode('utf-16', 'surrogatepass').decode('utf-16', 'ignore')
    yield from map(''.join, itertools.product(iterable, repeat=len))


def key_generator(len):
    random.seed(time.time())
    key = ''
    for i in range(len):
        key += chr(random.randint(0, 0x10ffff))

    return key


def vernam(text, key, mode):
    if mode == 'en':
        text = str(text)
        text = text.replace(' ', '')
        ciphertext = ''
        for x in range(len(text)):
            simb = ord(text[x])
            keysimb = ord(key[x])
            simb = (simb + keysimb)
            ciphertext += chr(simb)

        return ciphertext
    if mode == 'de':
        text = str(text)
        text = text.replace(' ', '')
        ciphertext = ''
        for x in range(len(text)):
            simb = ord(text[x])
            keysimb = -1 * ord(key[x])
            simb = (simb + keysimb)
            ciphertext += chr(simb)

        return ciphertext


if __name__ == '__main__':
    mode = input('(en)crypt or (de)crypt or crypto analysis(ca)? ')

    if str.lower(mode) == 'en' or str.lower(mode) == 'encrypt':

        plaintext = input('text: ')
        in_key = input('key, same length as text (random if not filled): ')
        if not in_key:
            in_key = key_generator(len(plaintext))
            print('key is %s' % in_key)
        if not plaintext:
            print('error, no data!')
        else:
            print(vernam(plaintext, in_key, 'en'))

    elif str.lower(mode) == 'de' or str.lower(mode) == 'decrypt':

        ciphertext = input('ciphertext: ')
        in_key = input('key: ')
        if not (ciphertext or in_key):
            print('error, no data!')
        else:
            print(vernam(ciphertext, in_key, 'de'))

    elif str.lower(mode) == 'ca' or str.lower(mode) == 'crypto analysis':
        ciphertext = input('ciphertext: ')
        key = input('key: ')
        awaitedtext = vernam(ciphertext, key, 'de')

        for i in wordGenerator(len(ciphertext)):
            print(i)
            if i == awaitedtext:
                print('Text found!')
                break

    else:
        print('wrong cmd')
