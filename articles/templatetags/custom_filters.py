from django import template

register = template.Library()

@register.filter(name='count_occurrences')
def count_occurrences(text, substring):
    return text.count(substring)