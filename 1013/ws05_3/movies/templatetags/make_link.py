from django import template
import re


register = template.Library()

@register.filter
def add_link (value):
    content = value.content
    tags = value.hashtags.all()

    for tag in tags:
        content = re.sub(r'\#'+tag.content+r'\b', '<a href="movies/'+'tag.pk'+'/hashtag/">'+tag.content+'</a>', content)

    return content