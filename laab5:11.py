from enum import Enum

class Type(Enum): 
    SHIRT = 1
    JEANS = 2
    JACKET = 3 

class Clothing:
    def __init__(self, name, description, location, colour, size, type):
        self.__name = name 
        self.__description = description
        self.__location = location
        self.__colour = colour 
        self.__size = size
        self.__type = type

    def __str__(self):
        return f"Clothing: {self.__name}, description: {self.__description}, location: {self.__location}, colour: {self.__colour}, size: {self.__size}, type: {self.__type.name}" 

    def __repr__(self):
        return f"Clothing: ({self.__name}, {self.__description}, {self.__location}, {self.__colour}, {self.__size}, {self.__type.name})"


    def get_size(self):
        return self.__size
    
    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

class Wardrobe:
    def __init__(self):
        self.__clothing = [] 

    def add_clothing(self, item): 
        self.__clothing.append(item)

    def remove_clothing(self, item_name):
        for index, item in enumerate(self.__clothing):  # Цикл for перебирає всі елементи списку в гардеробі
            if item.get_name() == item_name: 
                '''
                Перевіряє, чи ім'я поточного предмету одягу (отриманого за
             допомогою методу get_name()) відповідає переданому item_name, яке слід видалити.
             '''
                self.__clothing.pop(index) 
                '''Якщо ім'я збігається, то викликається метод pop(index), який видаляє
                   елемент зі списку за вказаним індексом index'''
    
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
        else:
            return "No, you can't go out."
    
if __name__ == "__main__":
    clothing1 = Clothing("T-shirt", "Casual shirt", "Wardrobe", "Blue", "M", Type.SHIRT)
    clothing2 = Clothing("Jeans", "Classic jeans", "Wardrobe", "Blue", "32", Type.JEANS)
    clothing3 = Clothing("Jacket", "Winter jacket", "Wardrobe", "Black", "M", Type.JACKET)

    wardrobe = Wardrobe() 

    wardrobe.add_clothing(clothing1) 
    wardrobe.add_clothing(clothing2)
    wardrobe.add_clothing(clothing3)

    print('Original Wardrobe: ' + ', '.join([item.get_name() for item in wardrobe.get_clothing()]))

    wardrobe.sort_clothing_by_size()
    print("Wardrobe after sorting by size: " + ', '.join([item.get_name() for item in wardrobe.get_clothing()]))

    '''
    [item.get_name() for item in wardrobe.get_clothing()] - витягує імена предметів одягу з гардеробу для отримання імені кожного предмета.
    ', '.join(...): Використовує функцію join для об'єднання всіх імен предметів у єдиний рядок, розділений комою та пробілом.
    Цей вираз формує рядок, який містить імена всіх предметів одягу у гардеробі, розділені комою та пробілом
    '''

    print("\nCan you go out?") 
    print(wardrobe.are_go_out())

    wardrobe.remove_clothing("Jeans")
    print("\nWardrobe after removing Jeans:")
    for item in wardrobe.get_clothing():'''Цикл for перебирає всі елементи списку предметів одягу у гардеробі'''
        print(item)
