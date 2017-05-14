from django import template
import classifieds.settings as settings

register = template.Library()

@register.simple_tag
def image_path():
    return settings.STATIC_IMAGE_PATH