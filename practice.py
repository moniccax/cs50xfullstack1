spam = ['apples', 'bananas', 'tofu', 'cats']

frase = spam[1] + spam[2]
print(frase)


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


rows = len(grid) # Number of elements in the list
cols = len(grid[0]) # Number of elements in every single element in the list

for j in range(cols):
    for i in range(rows):
        print(grid[i][j], end='')
    print()
