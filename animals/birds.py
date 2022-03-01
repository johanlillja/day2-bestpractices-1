class Birds:
    def __init__(self):
        ''' Constructor foor this class. '''
        # Create soome member animals
        self.members = ['Seagull', 'Eagle', 'Albatross']
        
    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)