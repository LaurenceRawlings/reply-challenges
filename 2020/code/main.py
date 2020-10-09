import reader as r
import output as o
import math
from random import randint

## Variables ##
width = 0
height = 0
office = [[]]
devs = []
pms = []
unseated_devs = []

## Algorithm ##
def calculate(dict):
    global width
    global height
    global office
    global devs
    global pms
    global unseated_devs
    global unseated_pms

    width = dict.get('width')
    height = dict.get('height')
    office = dict.get('office')
    devs = dict.get('devs')
    pms = dict.get('pms')

    unseated_devs = []
    for dev in devs:
        unseated_devs.append(dev)

    unseated_pms = []
    for pm in pms:
        unseated_pms.append(pm)    
    
    for row in range(0, height):
        for seat in range(0, width):
            symbol = office[row][seat]
            
            if symbol == '_':
                r_int = randint(0, len(unseated_devs)-1)
                office[row][seat] = 'D' + str(unseated_devs[r_int]['id'])
                seat_dev(seat, row, unseated_devs[r_int])

            elif symbol == 'M':
                if not(len(unseated_pms) == 0):
                    r_int = randint(0, len(unseated_pms)-1)
                    office[row][seat] = 'M' + str(unseated_pms[r_int]['id'])
                    seat_pm(seat, row, unseated_pms[r_int])      

    devs_return = sorted(devs, key=lambda i:i['id'], reverse=False)
    pms_return = sorted(pms, key=lambda i:i['id'], reverse=False)

    return devs_return + pms_return

## Helpers ##
def seat_dev(x, y, dev):
    global width
    global height
    global office
    global devs
    global pms
    global unseated_devs
    devs.remove(dev)
    dev.update( { 'seat': str(x) + " " + str(y) } )
    unseated_devs.remove(dev)
    devs.append(dev)

def seat_pm(x, y, pm):
    global width
    global height
    global office
    global devs
    global pms
    global unseated_devs
    global unseated_pms
    pms.remove(pm)
    pm.update( { 'seat': str(x) + " " + str(y) } )
    unseated_pms.remove(pm)
    pms.append(pm)



def get_dev(id):
    global width
    global height
    global office
    global devs
    global pms
    global unseated_devs
    return next(dev for dev in devs if dev['id'] == id)

def get_pm(id):
    global width
    global height
    global office
    global devs
    global pms
    global unseated_devs
    return next(pm for pm in pms if pm['id'] == id)

def neighbour_score(neighbour):
    global width
    global height
    global office
    global devs
    global pms
    global unseated_devs
    scores = []
    n_skills = neighbour.get('skills')
    for unseated_dev in unseated_devs:
        score = 0
        skills = unseated_dev['skills']
        for n_skill in n_skills:
            for skill in skills:
                if n_skill == skill:
                    score += 1
                else:
                    score -= 1
        scores.append(abs(score))

    return unseated_devs[scores.index(min(scores))]

def neighbours_score(neighbour_left, neighbour_above):
    global width
    global height
    global office
    global devs
    global pms
    global unseated_devs

    neighbour = neighbour_above
    scores_above = []
    n_skills = neighbour.get('skills')
    for unseated_dev in unseated_devs:
        score = 0
        skills = unseated_dev['skills']
        for n_skill in n_skills:
            for skill in skills:
                if n_skill == skill:
                    score += 1
                else:
                    score -= 1
        scores_above.append(abs(score))
    score1 = min(scores_above)
    dev1 = unseated_devs[scores_above.index(score1)]

    neighbour = neighbour_left
    scores_left = []
    n_skills = neighbour.get('skills')
    for unseated_dev in unseated_devs:
        score = 0
        skills = unseated_dev['skills']
        for n_skill in n_skills:
            for skill in skills:
                if n_skill == skill:
                    score += 1
                else:
                    score -= 1
        scores_left.append(abs(score))
    score2 = min(scores_left)
    dev2 = unseated_devs[scores_left.index(score2)]

    if score1 < score2:
        return dev1
    else:
        return dev2
    

## Run ##
print('Start')
read = r.Reader('input/a_solar.txt')
out = o.Output('output/a_solar_out.txt')
out(calculate(read()))
print('Finished A')

read = r.Reader('input/b_dream.txt')
out = o.Output('output/b_dream_out.txt')
out(calculate(read()))
print('Finished B')

read = r.Reader('input/c_soup.txt')
out = o.Output('output/c_soup_out.txt')
out(calculate(read()))
print('Finished C')

read = r.Reader('input/d_maelstrom.txt')
out = o.Output('output/d_maelstrom_out.txt')
out(calculate(read()))
print('Finished D')

read = r.Reader('input/e_igloos.txt')
out = o.Output('output/e_igloos_out.txt')
out(calculate(read()))
print('Finished E')

read = r.Reader('input/f_glitch.txt')
out = o.Output('output/f_glitch_out.txt')
out(calculate(read()))
print('Finished F')