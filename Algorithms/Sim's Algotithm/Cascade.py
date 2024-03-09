from Location import Location
from Table import Table


def cascade(table: Table, cascades_to_do: list, index: int):
    location = cascades_to_do[index]
    for i in range(1, len(location) + 1):
        if location.loc[i] != i:
            if table.table[i - 1][location.loc[i] - 1] is None:
                table.table[i - 1][location.loc[i] - 1] = location
                cascades_to_do.append(location * location)
                for loc in cascades_to_do[:]:
                    cascades_to_do.append(loc * location)
                    cascades_to_do.append(location * loc)
                return table
            else:
                location = location * Location(table.table[i - 1][location.loc[i] - 1].reverse())
    return table


