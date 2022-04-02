from django import template

register = template.Library()


@register.filter()
def addclass(value, class_name):
    print("ff", value.label)
    return value.as_widget(attrs={'class': class_name})


@register.filter()
def addclassplaceholder(value, class_name):
    return value.as_widget(attrs={'class': class_name, 'placeholder': value.label})


@register.filter
def model_type(value):
    return type(value).__name__


@register.filter()
def star(value):
    return value * u"\u2605"


@register.simple_tag(takes_context=True)
def page_name(context, user, has_review):
    if context['user'] == user:
        if has_review:
            return "Ticket - Vous"
        return "Vous avez publié un ticket"

