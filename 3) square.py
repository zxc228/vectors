import numpy as np
vecs = [[6.44, 5.05],
        [3.59, 7.71],
        [8.81, 2.02],
        [8.71, 7.8 ],
        [5.51, 2.53],
        [6.35, 4.89],
        [7.88, 3.52],
        [4.89, 5.83],
        [1.66, 5.24],
        [3.1 , 8.91],
        [5.11, 8.22],
        [7.06, 7.15],
        [2.15, 2.78],
        [7.25, 8.94],
        [1.62, 4.97],
        [8.86, 4.11],
        [8.59, 8.38],
        [2.18, 7.01],
        [8.24, 8.57],
        [9.97, 1.82]]
def square_by_matrix(x):
    index = np.where(vecs == x)[0][0]
    if(index != len(vecs)-1 and index != len(vecs)-2):
        matrix=[[vecs[index][0]-vecs[index+2][0],vecs[index][1]-vecs[index+2][1]],
                [vecs[index+1][0]-vecs[index+2][0],vecs[index+1][1]-vecs[index+2][1]]]
        return abs(np.linalg.det(matrix))/2
res = np.apply_along_axis(square_by_matrix, axis=1, arr=vecs)
print(res[:-2:])