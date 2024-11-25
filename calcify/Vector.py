import math


class Vector:
    def __init__(self, x, y, z=None, w=None):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def v_add(self, other):
        result = self.__class__(self.x + other.x, self.y + other.y)

        if self.z != None and other.z != None:
            result.z = self.z + other.z

        if self.w != None and other.w != None:
            result.w = self.w + other.w

        return result

    def v_subtract(self, other):
        result = self.__class__(self.x - other.x, self.y - other.y)

        if self.z != None and other.z != None:
            result.z = self.z - other.z

        if self.w != None and other.w != None:
            result.w = self.w - other.w

        return result

    def dot_product(self, other):
        sum = self.x * other.x + self.y * other.y

        if self.z != None:
            if other.z != None:
                sum += self.z * other.z
            else:
                raise TypeError(
                    "When taking the 'dot_product' of two vectors, both vectors should have the same number of dimensions.")

        if self.w != None:
            if other.w != None:
                sum += self.w * other.w
            else:
                raise TypeError("When taking the 'dot_product' of two vectors, both vectors should have the same number of dimensions.")

        return sum

    def cross_product(self, other):
        if (self.z != None and other.z != None) and (self.w == None and other.w == None):
            return self.__class__(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
        else:
            raise TypeError("When taking the 'cross_product' of two vectors, both vectors should have 3 dimensions and no 4th dimension or 'w'-component.")

    def magnitude(self):
        sum = (self.x) ** 2 + (self.y) ** 2

        if self.z != None:
            sum += (self.z) ** 2

        if self.w != None:
            sum += (self.w) ** 2

        return pow(sum, 0.5)

    def angle2D(self):
        if self.z == None and self.w == None:
            if self.x > 0 and self.y > 0:
                return math.atan(self.y / self.x)
            elif self.x < 0 and self.y < 0:
                return 2 * math.pi + math.atan(self.y / self.x)
            elif self.x == 0 and self.y > 0:
                return math.pi / 2
            elif self.x == 0 and self.y < 0:
                return 3 * math.pi / 2
            elif self.x > 0 and self.y == 0:
                return 0
            elif self.x < 0 and self.y == 0:
                return math.pi
            else:
                return math.pi + math.atan(self.y / self.x)
        else:
            raise TypeError("When taking the 'angle2D' function of a vector, the vector should have 2 dimensions and no 3rd dimension or 'z'-component nor any 4th dimension or 'w'-component.")