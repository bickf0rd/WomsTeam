from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageDimensions(object):
    """
        Проверка изображения по высоте и ширине
    """

    def __init__(self, width, height):
        self.width, self.height = width, height

    def __call__(self, value):
        width, height = get_image_dimensions(value)
        if width > self.width or height > self.height:
            raise ValidationError('Картинка превышает размеры {}x{}'.format(self.width, self.height))

    def __eq__(self, other):
        return other.width == self.width and other.height == self.height
