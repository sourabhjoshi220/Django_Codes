from django import template
register=template.Library()

def truncate3(value):
    #Custom Filter
    result=value[0:3]
    return result
register.filter('truncate3',truncate3)