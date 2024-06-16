# Made by ElectroMuffin (posted on GitHub)

def tetrate(num, tet_by):
    if tet_by == 1:
        return num
    else:
        return num ** tetrate(num, tet_by - 1)

def tetrate_iteration(num, tet_by):
    while tet_by > 0:
        num = num ** num
        tet_by = tet_by - 1
    return num