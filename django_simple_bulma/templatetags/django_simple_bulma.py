"""
Template tags loaded in by the Django
templating engine when {% load django_simple_bulma %}
is called.
"""

from pathlib import Path

from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.safestring import mark_safe


# If BULMA_SETTINGS has not been declared if no extensions
# have been defined, default to all extensions.
if hasattr(settings, "BULMA_SETTINGS"):
    extensions = settings.BULMA_SETTINGS.get("extensions", "_all")
else:
    extensions = "_all"

register = template.Library()
simple_bulma_path = Path(__file__).resolve().parent.parent
js_folder = simple_bulma_path / "js"


@register.simple_tag
def bulma():
    """
    Build and return all the HTML required to
    import bulma and the javascript for all
    active extensions.
    """
    # Build the html to include the stylesheet
    css = static("css/bulma.css")
    html = [f'<link rel="stylesheet" href="{css}">']

    # Build html to include all the js files required.
    for filename in js_folder.iterdir():
        js_file = static(f"js/{filename.name}")
        extension_name = filename.stem

        if extension_name in extensions or extensions == "_all":
            html.append(f'{" " * 8}<script type="text/javascript" src="{js_file}"></script>')

    return mark_safe("\n".join(html))  # noqa
