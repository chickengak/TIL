def calc_time(start, end):
    # if end == '00:00':
    #     end = '24:00'
    return (int(end[:2])*60 + int(end[3:])) - (int(start[:2])*60 + int(start[3:]))

def remove_sharp(string):
    return string.replace('C#', 'Z').replace('D#', 'Y').replace('F#', 'X').replace('G#', 'W').replace('A#', 'Q')

def solution(m, musicinfos):
    answers = []
    m = remove_sharp(m)
    for idx, val in enumerate(musicinfos):
        start, end, title, info = val.split(',')
        music_time = calc_time(start, end)
        info = remove_sharp(info)
        infos = (info * (music_time//len(info) + 1))[:music_time]
        if m in infos:
            answers.append((music_time, idx, title))

    return sorted(answers, key=lambda x: (-x[0], x[1]))[0][2] if answers else "(None)"