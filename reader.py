class Reader:

    def __init__(self, path):
        self.path = path
    
    def __call__(self):
        with open(self.path, 'r') as file:
            lines = file.read().split('\n')
            dict = {
                '': [],
                '': [],
                '': 0
            }

        return dict