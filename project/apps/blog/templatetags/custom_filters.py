from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="calificacion_estrellas")
def calificacion_estrellas(calificacion):
       stars = '⭐' * calificacion
       return mark_safe(stars)