import re

from django import template

from pages.models import Page


register = template.Library()


class PagesForSectionNode(template.Node):
    def __init__(self, section, var_name):
        self.section = template.Variable(section)
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = Page.objects.filter(
            section=self.section.resolve(context), 
            landing=False,
        )

        return ""


@register.tag
def pages_for_section(parser, token):
    """
    Gets pages for the given section slug
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]

    m = re.search(r'(.*?) as (\w+)', arg)

    if not m:
        raise template.TemplateSyntaxError, "%r had invalid arguments" % tag_name

    section, var_name = m.groups()

    return PagesForSectionNode(section, var_name)
