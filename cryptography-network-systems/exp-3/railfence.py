def encryptRailFence(plain_text, depth):
    
    # creates a matrix with default char \n in it
    rail = [['\n' for i in range(len(plain_text))] for j in range(depth)]

    # initially it goes upward
    dir_down = False

    # keeps the track of current mat loc
    row, col = 0, 0
    
    for i in range(len(plain_text)):
        
        # change the dir if at top or bottom
        if (row == 0) or (row == depth - 1):
            dir_down = not dir_down
        
        # inserts plain_text letter at the specific loc
        rail[row][col] = plain_text[i]
        col += 1

        # navigates through matrix (up or down)
        if dir_down:
            row += 1
        else:
            row -= 1
    
    # empty cipher matrix
    result = []
    for i in range(depth):
        for j in range(len(plain_text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "" . join(result)


def decryptRailFence(cipher_text, depth):
    rail = [['\n' for i in range(len(cipher_text))] for j in range(depth)]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == depth - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(depth):
        for j in range(len(cipher_text)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher_text))):
                rail[i][j] = cipher_text[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher_text)):

        if row == 0:
            dir_down = True
        if row == depth - 1:
            dir_down = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


print(f'Aditya Kirti after encryption with depth = 3 --> {encryptRailFence('Aditya Kirti', 3)}')
print(f'AyidtaKrii t after decryption with depth = 3 --> {decryptRailFence('AyidtaKrii t', 3)}')
