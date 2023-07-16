#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="", size=0):
        self.brand =brand
        self._size = size
        self.condition = "New"
    
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")
            
    size = property(get_size, set_size)

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = "New"
        
    def cobble(self):
        print("Your shoe is as good as new!")

           