class Output:

    def __init__(self, path):
        self.path = path
    
    def __call__(self, replyers):
        with open(self.path, 'w') as file:
            outputText = ''

            for replyer in replyers:
                outputText += replyer.get('seat') + '\n'

            file.write(outputText)