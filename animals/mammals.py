class Mammals:
    def __init__(self):
        ''' Constructor foor this class. '''
        # Create soome member animals
        self.members = ['Sloth', 'Hedgehog', 'Tiger']
        
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)