def solution(wallpaper):
    left = 50
    right = 0
    up = 50
    down = 0
    for y, row in enumerate(wallpaper):
        for x, val in enumerate(row):
            if val == '#':
                if x > right:
                    right = x
                if x < left:
                    left = x
                if y > down:
                    down = y
                if y < up:
                    up = y
    return [up, left, down+1, right+1]