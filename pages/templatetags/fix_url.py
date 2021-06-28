from django import template

from pprint import pprint

register = template.Library()

@register.simple_tag(takes_context=True)
def screen_it(context):
    print(context['request'])
    return "Worked"

@register.filter
def print_url(value):
    print(pprint(vars(value)))
    return value

@register.filter
def print_again(value):
    print(value)
    return value

@register.simple_tag(takes_context=True)
def fix(context, pa):
    try:
        print("HELLO" + pa)
        return True
    except Exception:
        return False
