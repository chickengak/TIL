def solution(sizes):
    width = 0
    height = 0
    for w, h in sizes:
        if w > h:
            if w > width:
                width = w
            if h > height:
                height = h
        else:
            if h > width:
                width = h
            if w > height:
                height = w
    return width*height
