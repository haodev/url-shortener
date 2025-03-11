import random
import string
from ..models import ShortUrl

def generate_short_url():
    """Generate a random 6-char string for the short URL"""
    available_chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(available_chars) for _ in range(6))
    return short_url

def get_or_create_short_url(original_url):
    """Get existing short URL or create a new one"""
    # Try to get existing URL
    url_obj = ShortUrl.objects.filter(original_url=original_url).first()
    if url_obj:
        return url_obj.short_url
    
    # Create new short URL
    short_url = generate_short_url()
    url_obj = ShortUrl.objects.create(
        original_url=original_url,
        short_url=short_url
    )
    return short_url