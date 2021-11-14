from django.template.defaultfilters import register

@register.filter
def keyvalue(dict, key):    
    try:
        return dict[key]
    except KeyError:
        return 
