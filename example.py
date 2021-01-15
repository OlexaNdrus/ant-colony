import numpy as np
import xlrd

from ant_colony import AntColony

workbook = xlrd.open_workbook('Дані.xlsx')
ws = workbook.sheet_by_index(0)
cost_mat=[]
for col in range(2, ws.ncols):
    cost_mat.append([])
    for row in range(1, ws.nrows):
        if ws.cell_value(row, col)==0:
            cost_mat[col - 2].append(np.inf)
        else:
            cost_mat[col-2].append(int(ws.cell_value(row, col)))

distances = np.array([[np.inf, 2, 2, 5, 7],
                      [2, np.inf, 4, 8, 2],
                      [2, 4, np.inf, 1, 3],
                      [5, 8, 1, np.inf, 2],
                      [7, 2, 3, 2, np.inf]])

distances = np.array(cost_mat)

ant_colony = AntColony(distances, 50, 50, 100, 0.2, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("shorted_path: {}".format(shortest_path))

