from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr_name):
    """
    Dynamically retrieves an attribute from an object.
    Usage: {{ object|get_attr:attribute_name_variable }}
    """
    return getattr(obj, attr_name, "") # returns an empty string if not found


@register.filter
def nav_filter(request, group_name):
    """
    Dynamically retrieves an attribute from an object.
    Usage: {{ object|get_attr:attribute_name_variable }}
    """

    available_groups = {
        "home":[
                'admin-banner-page',
                'admin-testimonials-page',
                'admin-partners-page',
        ],
        "services":[
            'admin-services-page'
        ],
        "departments":[
            'admin-departments-page',
            'admin-doctors-page',
            'admin-appointments-page',
        ],
        "blogs": [
            'admin-blog-cat-page',
            'admin-blog-tag-page',
            'admin-blog-page',
        ]
    }
    cond = request.resolver_match.url_name in available_groups.get(group_name) 
    

    return  'open' if cond else ''


