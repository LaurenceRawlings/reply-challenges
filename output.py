class Output:

    def __init__(self, path):
        self.path = path
    
    def __call__(self, libraries):
        with open(self.path, 'w') as file:
            outputText = ''

            file.write(outputText)