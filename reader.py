class Reader:

    def __init__(self, path):
        self.path = path
    
    def __call__(self):
        with open(self.path, 'r') as file:
            lines = file.read().split('\n')
            dict = {
                'width': 0,
                'height': 0,
                'office': [[]],
                'devs': [],
                'pms': []
            }

            dimensions = lines[0].split(' ')
            dict.update( { 'width':  int(dimensions[0]) } )
            dict.update( { 'height': int(dimensions[1]) } )
            
            line = 1
            office = []
            for i in range(0, int(dimensions[1])):
                map.append(list(lines[line]))
                line += 1

            dict.update( { 'office': office } )

            devs = []
            for i in range(0, int(lines[line])):
                line += 1
                dev = lines[line].split(' ')

                skills = []
                for j in range(0, int(dev[2])):
                    skills.append(dev[3+j])

                devs.append({
                    'id': i,
                    'company': dev[0],
                    'bonus': int(dev[1]),
                    'skills': skills,
                    'seat': 'X'
                })

            dict.update( { 'devs': devs } )

            line += 1
            pms = []
            for i in range(0, int(lines[line])):
                line += 1
                pm = lines[line].split(' ')

                pms.append({
                    'id': i,
                    'company': pm[0],
                    'bonus': int(pm[1]),
                    'seat': 'X'
                })

            dict.update( { 'pms': pms } )

            return dict