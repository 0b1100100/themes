from django import template

register = template.Library()


@register.filter(name='replacer')
def replacer(value):
    if value.split('.')[-1] in ['jpeg', 'jpg', 'png', 'gif', 'bmp']:
        print(value.split('.')[-1])
        return True
    else:
        return False


@register.filter(name='get_name')
def get_name(value):
    return value.split('/')[-1]
