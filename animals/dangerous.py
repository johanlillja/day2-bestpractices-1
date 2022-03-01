class Dangerous:
    class Bird:
        def __init__(self):
            ''' Constructor foor this class. '''
            # Create soome member animals
            self.members = ['Eagle']
            
        def printMembers(self):
            print('Printing members of the dangerous bird class')
            for member in self.members:
                print('\t%s ' % member)
    class Fish:
        def __init__(self):
            ''' Constructor foor this class. '''
            # Create soome member animals
            self.members = []
            
        def printMembers(self):
            print('Printing members of the dangerous fish class')
            for member in self.members:
                print('\t%s ' % member)
    class Mammal:
        def __init__(self):
            ''' Constructor foor this class. '''
            # Create soome member animals
            self.members = ['Tiger']
            
        def printMembers(self):
            print('Printing members of the dangerous mammal class')
            for member in self.members:
                print('\t%s ' % member)                