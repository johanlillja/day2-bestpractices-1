class Fish:
    def __init__(self):
        ''' Constructor foor this class. '''
        # Create soome member animals
        self.members = ['Cod', 'Herring', 'Tuna']
        
    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)