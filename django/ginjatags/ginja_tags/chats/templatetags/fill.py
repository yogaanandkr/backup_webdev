from django import template
register=template.Library()


@register.filter('mailname')
def mailname(val):
    out = ''
    for i in val:
        if i != '@':
            out += i 
        else:
            return out.title()
        

@register.filter('palindrome')
def palindrome(val):
    if val == val[::-1]:
        return 'palindrome'
    return 'not palindrome'

@register.filter('license')
def license(age):
      # Convert age to an integer
    if int(age) >= 18:
        return "Eligible for License"
    else:
        return "Not Eligible for License"
