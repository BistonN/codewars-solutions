# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python
def sudoku(puzzle):
    while constain_zeros(puzzle):
        row, col = get_better_position_by_mean()
        print("Better position", row, col)
        a = get_nulls(row, col)
        print("Value", a)
        puzzle[row][col] = a
        for i in puzzle:
            print(i)
        print()
    return puzzle

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
    
# def get_better_list():
#     better_list = []
#     for i in range(9):
#         current_better = max([
#             list(filter(lambda x: x != 0, get_row(i))),
#             list(filter(lambda x: x != 0, get_col(i))),
#             list(filter(lambda x: x != 0, get_area(i)))
#         ], key=len)
#         better_list = current_better if len(current_better) > len(better_list) else better_list
#         print(better_list)
#     print('\n\n', better_list)

def get_better_position_by_mean():
    mean_puzzle = []
    better_mean = 0
    better_position = []
    for row in range(9):
        mean_row = []
        for col in range(9):
            if puzzle[row][col] == 0:
                mean = 27 - (
                    get_area(set_id_area(row, col)).count(0) + 
                    get_row(row).count(0) + 
                    get_col(col).count(0)
                )
                mean_row.append(mean)
                if mean > better_mean:
                    better_mean = mean
                    better_position = [row, col]
            else:
                mean_row.append(0)
        mean_puzzle.append(mean_row) # talvez posso tirar o processamento do append
    return better_position
            
def set_id_area(i_row, i_col):
    for key in areas:
        start = range(int(areas[key][0]), int(areas[key][1]))
        end = range(int(areas[key][2]), int(areas[key][3]))
        if i_row in start and i_col in end:
            return key

def get_nulls(row, col):
    completed = list(range(10)) 
    a = list(set(get_row(row) + get_col(col) + get_area(set_id_area(row, col))))
    result = [item for item in completed if item not in a]
    result = result[0] if len(result) == 1 else result
    return result

def constain_zeros(matrix):
    for y in matrix:
        for x in y:
            if x == 0:
                return True
    return False 


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

sudoku(puzzle)