def booleanTrueReturn(*args, **kwargs):
    return True

def booleanFalseReturn(*args, **kwargs):
    return False

def noneNoneReturn():
    return None, None

def noneReturn():
    return None

def lengthAndPathReturn(current, start, came_from):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return len(path) - 1, path

def pathReturn(current, start, came_from):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path