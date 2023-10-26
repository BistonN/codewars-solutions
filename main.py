# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python
# https://www.youtube.com/watch?v=1i3kVj0aB5U
def test_branch(puzzle, contador = 0, trys = 1):
    contador += 1
    print('Contador: ',contador)
    if not constain_zeros(puzzle):
        return puzzle
    row, col = get_better_position_by_mean(trys)
    print("Better position", row, col)
    values = get_better_values(row, col)
    if len(values) == 0:
        return puzzle
    for value in values:
        print("Value:", value, values)
        puzzle[row][col] = value
        for i in puzzle:
            print(i)
        print()
        if not constain_zeros(puzzle):
            return puzzle
        puzzle = test_branch(puzzle, contador)
        
    if constain_zeros(puzzle):
        test_branch(puzzle, contador, trys=trys+1)

def get_row(row):
    return puzzle[row]

def get_col(col):
    a = list(map(lambda x: x[col], puzzle))
    return a

def get_area(id):
    id = str(id)
    b = []
    a = map(lambda x: x[int(areas[id][2]) : int(areas[id][3])], puzzle[int(areas[id][0]) : int(areas[id][1])])
    for i in a:
        b += i
    return b

def get_better_position_by_mean(trys = 1):
    mean_puzzle = []
    better_mean = [0]
    better_position = []
    for row in range(9):
        mean_row = [0]
        for col in range(9):
            if puzzle[row][col] == 0:
                mean = 27 - (
                    get_area(set_id_area(row, col)).count(0) + 
                    get_row(row).count(0) + 
                    get_col(col).count(0)
                )
                mean_row.append(mean)
                if mean > better_mean[-1]:
                    better_mean.append(mean)
                    better_position.append([row, col])
            else:
                mean_row.append(0)
        mean_puzzle.append(mean_row) # talvez posso tirar o processamento do append
    return better_position[-trys]
            
def set_id_area(i_row, i_col):
    for key in areas:
        start = range(int(areas[key][0]), int(areas[key][1]))
        end = range(int(areas[key][2]), int(areas[key][3]))
        if i_row in start and i_col in end:
            return key

def get_better_values(row, col):
    completed = list(range(10)) 
    a = list(set(get_row(row) + get_col(col) + get_area(set_id_area(row, col))))
    result = [item for item in completed if item not in a]
    return result

def constain_zeros(matrix):
    try:
        for y in matrix:
            for x in y:
                if x == 0:
                    return True
        return False
    except:
        return True

def count_voids(matrix):
    return sum(elemento == 0 for linha in matrix for elemento in linha)


areas = {
    '0': '0303',
    '1': '0336',
    '2': '0369',
    '3': '3603',
    '4': '3636',
    '5': '3669',
    '6': '6903',
    '7': '6936',
    '8': '6969'
}

puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

resolved = test_branch(puzzle)
for i in resolved:
    print(i)