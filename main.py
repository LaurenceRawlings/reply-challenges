import reader as r
import output as o
import math

## Algorithm ##
def calculate(dict):
    width = dict.get('width')
    height = dict.get('height')
    office = dict.get('office')
    devs = dict.get('devs')
    pms = dict.get('pms')
    


    devs_return = sorted(devs, key=lambda i:i['id'], reverse=False)
    pms_return = sorted(pms, key=lambda i:i['id'], reverse=False)

    return devs_return + pms_return

## Helpers ##
def seat(x, y):
    return str(x) + " " + str(y)

## Run ##
print('Start')
read = r.Reader('input/a_solar.txt')
out = o.Output('output/a_solar_out.txt')
out(calculate(read()))
print('Finished A')

"""
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
"""