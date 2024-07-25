def encryptRailFence(plain_text, depth):
    
    # creates a matrix with char \n in it
    rail = [['\n' for i in range(len(plain_text))]
                for j in range(depth)]

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
    return("" . join(result))

print(encryptRailFence('hello', 3))
