from Group import Group
from Table import Table
from Location import Location
from Cascade import cascade

def sims_algorithm(group : Group, table: Table):
    cascades_to_do = group.group[:]
    k = 0
    while k < len(cascades_to_do):
        table = cascade(table, cascades_to_do, k)
        k += 1
    for i in range(len(table.table)):
        for q in range(len(table.table)):
            if table.table[i][q] is not None:
                print('[1, 2, 3, 4]\t', end='')
            else:
                print('\t\t\t', end='\t')
        print()
        for j in range(len(table.table[0])):
            if table.table[i][j] is not None:
                print(table.table[i][j], end='\t')
            else:
                print('\t\t\t', end='\t')
        print('\n')


lc1 = Location({1: 2, 2: 1, 3: 3, 4: 4})
lc2 = Location({1: 2, 2: 3, 3: 4, 4: 1})

group = Group(lc1, lc2)
table = Table(len(lc1))

sims_algorithm(group, table)
print()

lc1 = Location({1: 3, 2: 4, 3: 1, 4: 2})
lc2 = Location({1: 2, 2: 4, 3: 3, 4: 1})

group = Group(lc1, lc2)
table = Table(len(lc1))

sims_algorithm(group, table)
