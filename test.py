import os
dirname = os.path.dirname('/far/boo/fam.txt')
print(dirname)


class animal():
    def __init__(self):
        pass

    def animal_type(self, type):
        print('Animal type: %s' %type)


a = animal()
a.animal_type(type='tiger')
