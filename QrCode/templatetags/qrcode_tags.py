from django import template
from django.urls import reverse
import urllib.parse

register = template.Library()

@register.simple_tag
def qrcode_url(data):
    """
    Returns the URL to generate a QR code image for the given data.
    Usage in a Django template:
    
      <img src="{% qrcode_url 'Some text to encode' %}" alt="QR Code">
    """
    base_url = reverse("qrcode:generate")
    query_string = urllib.parse.urlencode({"data": data})
    return f"{base_url}?{query_string}"
