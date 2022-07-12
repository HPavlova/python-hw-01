# Напишите класс метакласс Meta, который всем классам, для кого он будет метаклассом, устанавливает порядковый номер

# classes=[]

class Meta(type):
    def __new__(cls, name, bases, attrs):
        # classes.append({'cls': cls, 'name': name, 'number': len(classes)})
        attrs['class_number'] = Meta.children_number
        Meta.children_number +=1
        return type.__new__(cls, name, bases, attrs)


Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)

if __name__=='__main__':
    print(a.class_number, b.class_number)
    # print(classes)
