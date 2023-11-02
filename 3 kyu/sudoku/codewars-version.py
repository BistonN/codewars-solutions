def sudoku(main_puzzle):
    import copy

    def deep_search(grafo):
        while len(grafo) > 0:
            puzzle =  copy.deepcopy(grafo[-1])

            if not constain_zeros(puzzle):
                return puzzle

            row, col = get_better_position_by_mean(puzzle)
            values = get_better_values(row, col, puzzle)

            if len(values) == 0:
                grafo.pop()
                continue

            grafo.pop()
            for value in values:
                puzzle[row][col] = value
                grafo.append(copy.deepcopy(puzzle))

    def get_row(row, puzzle):
        return puzzle[row]

    def get_col(col, puzzle):
        a = list(map(lambda x: x[col], puzzle))
        return a

    def get_area(id, puzzle):
        id = str(id)
        b = []
        a = map(lambda x: x[int(areas[id][2]) : int(areas[id][3])], puzzle[int(areas[id][0]) : int(areas[id][1])])
        for i in a:
            b += i
        return b

    def get_better_position_by_mean(puzzle):
        mean_puzzle = []
        better_mean = [0]
        better_position = []
        for row in range(9):
            mean_row = [0]
            for col in range(9):
                if puzzle[row][col] == 0:
                    mean = 27 - (
                        get_area(set_id_area(row, col), puzzle).count(0) + 
                        get_row(row, puzzle).count(0) + 
                        get_col(col, puzzle).count(0)
                    )
                    mean_row.append(mean)
                    if mean > better_mean[-1]:
                        better_mean.append(mean)
                        better_position = [row, col]
                else:
                    mean_row.append(0)
            mean_puzzle.append(mean_row)
        return better_position

    def set_id_area(i_row, i_col):
        for key in areas:
            start = range(int(areas[key][0]), int(areas[key][1]))
            end = range(int(areas[key][2]), int(areas[key][3]))
            if i_row in start and i_col in end:
                return key

    def get_better_values(row, col, puzzle):
        completed = list(range(10)) 
        a = list(set(get_row(row, puzzle) + get_col(col, puzzle) + get_area(set_id_area(row, col), puzzle)))
        result = [item for item in completed if item not in a]
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

    return deep_search([main_puzzle])