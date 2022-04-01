from django import template

register = template.Library()


@register.filter()
def addclass(value, class_name):
    print("ff", value.label)
    return value.as_widget(attrs={'class': class_name})


@register.filter()
def addclassplaceholder(value, class_name):
    return value.as_widget(attrs={'class': class_name, 'placeholder': value.label})
