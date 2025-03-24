import random
# import string
import hashlib
import base62
from ..models import ShortUrl

# Deprecated
# def generate_short_url():
#     """Generate a random 6-char string for the short URL"""
#     available_chars = string.ascii_letters + string.digits
#     short_url = ''.join(random.choice(available_chars) for _ in range(6))
#     return short_url

def genenerate_short_code(original_url):
    """use md5 and pybase62 to generate unique url-safe 6-digit code"""
    while True:
        md5_hash = hashlib.md5(original_url.encode()).digest()
        base62_encoded = base62.encodebytes(md5_hash)
        short_code = base62_encoded[:6]

        if not ShortUrl.objects.filter(short_url=short_code).exists():
            return short_code
        
        # if short code is already in use, append a random string to original url and re-hash
        original_url += str(random.randint(1, 1000))
         

def create_short_url(original_url):
    """Get existing short URL or create a new one"""
    url_obj = ShortUrl.objects.filter(original_url=original_url).first()
    if url_obj:
        return url_obj.short_url

    short_code = genenerate_short_code(original_url)

    ShortUrl.objects.create(
        original_url=original_url,
        short_url=short_code
    )
    return short_code