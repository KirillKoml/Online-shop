from django import template

register = template.Library()


@register.filter()
def media_filter(pach):
    if pach:
        return f"/media/{pach}"
    return "#"