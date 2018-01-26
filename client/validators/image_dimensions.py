from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError


class ImageDimensions:
    """ Проверка изображения по высоте и ширине
    """
    def __init__(self, width, height):
        self.__width, self.__height = width, height

    def __call__(self, value):
        width, height = get_image_dimensions(value)
        if width > self.__width or height > self.__height:
            raise ValidationError('Картинка превышает размеры {}x{}'.format(self.__width,self.__height))
