class Harmless:
    def __init__(self):
        class Birds:
            def __init__(self):
                ''' Constructor foor this class. '''
                # Create soome member animals
                self.members = ['Seagull', 'Albatross']
                
            def printMembers(self):
                print('Printing members of the harmless bird class')
                for member in self.members:
                    print('\t%s ' % member)
        class Fish:
            def __init__(self):
                ''' Constructor foor this class. '''
                # Create soome member animals
                self.members = ['Cod', 'Herring', 'Tuna']
                
            def printMembers(self):
                print('Printing members of the harmless fish class')
                for member in self.members:
                    print('\t%s ' % member)
        class Mammal:
            def __init__(self):
                ''' Constructor foor this class. '''
                # Create soome member animals
                self.members = ['Sloth', 'Hedgehog']
                
            def printMembers(self):
                print('Printing members of the harmless mammal class')
                for member in self.members:
                    print('\t%s ' % member)                