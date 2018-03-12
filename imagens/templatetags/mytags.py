from django import template

register = template.Library()


@register.assignment_tag
def define(val=None):
    return val

@register.simple_tag(takes_context=True)
def set_global_context(context, key, value):
    """
    Sets a value to the global template context, so it can
    be accessible across blocks.

    Note that the block where the global context variable is set must appear
    before the other blocks using the variable IN THE BASE TEMPLATE.  The order
    of the blocks in the extending template is not important. 

    Usage::
        {% extends 'base.html' %}

        {% block first %}
            {% set_global_context 'foo' 'bar' %}
        {% endblock %}

        {% block second %}
            {{ foo }}
        {% endblock %}
    """
    context.dicts[0][key] = value
    return ''

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter(name='placeholder')
def placeholder(field, css, place):
   return field.as_widget(attrs={"class":css, "placeholder":place})