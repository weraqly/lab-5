from dataclasses import dataclass
from enum import Enum
'''class Enum enables create lists with constants'''
class Type(Enum):
    '''Enumeration of clothing types''' 
    SHIRT = 1
    JEANS = 2
    JACKET = 3

@dataclass
class Clothing:
    name: str
    description: str
    location: str
    colour: str
    size: str
    element: Type
    def __str__(self):  
            return f"Clothing(\'{self.name}\',\
            \'{self.description}\',\
            \'{self.location}\',\
            \'{self.colour}\',\
            \'{self.size}\',\
            {self.element.name})"
    
    def __repr__(self):
        return f"Clothing(\'{self.name}\',\
        \'{self.description}\',\
        \'{self.location}\',\
        \'{self.colour}\',\
        \'{self.size}\',\
        {self.element.name})"

    def get_size(self):
        return self.size
    '''Returns attribute size value'''

    def get_name(self):
        return self.name
        '''
        Returns attribute name value
        '''

    def get_type(self):
        return self.element
        '''
        Returns attribute element value 
        '''

class Wardrobe:
    def __init__(self):
        self.__clothing = []

    def add_clothing(self, wardrobe_item):
        self.__clothing.append(wardrobe_item)

    def remove_clothing(self, wardrobe_item_name):
        for index, wardrobe_item in enumerate(self.__clothing):
            '''
                this cycle 'for' checks every element in the wardrobe
            '''
            if wardrobe_item.get_name() == wardrobe_item_name:
                ''' 
                Method get_name() checks that the name of
                the clothing responds to passed item_name 
                '''
                self.__clothing.pop(index)
                '''
                if name matches, the method pop(index), that 
                removes elements from list be index, are called
                '''

    def get_clothing(self):
        return self.__clothing

    def sort_clothing_by_size(self):
        sorted_clothes = sorted(self.__clothing, key=lambda x: x.get_size())
        return sorted_clothes

    def are_go_out(self):
        types = set()
        for item in self.get_clothing():
            types.add(item.get_type())
        if len(types) > 3:
            return "Yes, you can go out."

if __name__ == "__main__":
    clothing1 = Clothing("T-shirt", "Casual shirt", "Wardrobe", "Blue", "M", Type.SHIRT)
    clothing2 = Clothing("Jeans", "Classic jeans", "Wardrobe", "Blue", "32", Type.JEANS)
    clothing3 = Clothing("Jacket", "Winter jacket", "Wardrobe", "Black", "M", Type.JACKET)

    wardrobe = Wardrobe()

    wardrobe.add_clothing(clothing1)
    wardrobe.add_clothing(clothing2)
    wardrobe.add_clothing(clothing3)

    print('Original Wardrobe: ' + ', '.join([wardrobe_item.get_name() for wardrobe_item in wardrobe.get_clothing()]))

    wardrobe.sort_clothing_by_size()
    print("Wardrobe after sorting by size: " + ', '.join([wardrobe_item.get_name() for wardrobe_item in wardrobe.get_clothing()]))

    print("\nCan you go out?")
    print(wardrobe.are_go_out())

    wardrobe.remove_clothing("Jeans")
    print("\nWardrobe after removing Jeans:")
    for wardrobe_item in wardrobe.get_clothing():
        print(wardrobe_item)
