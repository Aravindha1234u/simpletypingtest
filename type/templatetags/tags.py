from django import template
register = template.Library()

@register.filter(name="flag")
def flag(value):
  return "SKCETCTF{B0ts_4r3_n0t_fUtuR3}"