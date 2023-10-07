# The main function I use for testing.


# def cuboid_volume(l):
#     return l * l * l


# test_input_value told me, that def cuboid_volume doesn't take care on input being passed to it properly. So I have to change the main function:


class Cuboid:
    def __init__(self, l):
        self.l = l

    def cuboid_volume(self):
        if not isinstance(self.l, (int, float)):
            raise TypeError("Argument must be an int or float")
        return self.l * self.l * self.l
