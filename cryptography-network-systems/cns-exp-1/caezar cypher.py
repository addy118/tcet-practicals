plain_text = input('Enter the plain text: ')
cypher_text = input('Enter the cypher text: ')
key = int(input('Enter the additive depth: '))

def encrypt(plain, key):
    cypher_text = ''
    for ch in plain:
        alpha_code = ((ord(ch) + key - 65) % 26 + 65)
        encrypted_alpha = chr(alpha_code)
        cypher_text += encrypted_alpha
    print('Cypher text of {} is {}'.format(plain, cypher_text))


def decrypt(cypher, key):
    plain_text = ''
    for ch in cypher:
        alpha_code = ((ord(ch) - key - 65) % 26 + 65)
        decrypted_alpha = chr(alpha_code)
        plain_text += decrypted_alpha
    print('Plain text of {} is {}'.format(cypher, plain_text))

encrypt(plain_text, key)
decrypt(cypher_text, key)

