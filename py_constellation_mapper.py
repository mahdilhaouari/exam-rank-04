def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    result = [['.'] * dim for _ in range(dim)]
    for constellation in stars:
        row, colom = constellation
        if 0 <= colom < dim and 0 <= row < dim:
            result[row][colom] = '*'
    return(["".join(rows) for rows in result])
    
constellation_mapper([(0,0),(2,2)], 3)
