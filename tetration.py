# Made by ElectroMuffin (posted on GitHub)

def tetrate(num, tet_by):
    if tet_by == 1:
        return num
    else:
        return num ** tetrate(num, tet_by - 1)

def tetrate_iteration(num, tet_by):
    result = num
    while tet_by > 1:
        result = result ** num
        tet_by -= 1
    return result
