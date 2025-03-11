from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import ShortUrl
from .utils.short_url_generator import get_or_create_short_url
from .utils.url_helper import extract_short_code
import json

def home(request):
    """Render the home page"""
    return render(request, 'url_shortener_app/home.html')

@require_http_methods(["POST"])
@csrf_exempt
def shorten_url(request):
    """Given a long URL, return a short URL"""

    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
            original_url = data.get('url')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        original_url = request.POST.get("url")

    if not original_url:
        return JsonResponse({"error": "URL is required"}, status=400)
    
    short_url = get_or_create_short_url(original_url)

    return JsonResponse({"short_url": short_url})

@require_http_methods(["GET"])
def get_original_url(request):
    """Get the original URL from a short URL"""
    short_url = request.GET.get('short-url')
    if not short_url:
        return JsonResponse({'error': 'short-url is required'}, status=400)

    short_code = extract_short_code(short_url)
    url_obj = ShortUrl.objects.filter(short_url=short_code).first()

    if not url_obj:
        return JsonResponse({'error': 'No long url associated with this short url'}, status=404)
    
    return JsonResponse({'original_url': url_obj.original_url})

def redirect_to_original(request):
    """Redirect to the original URL and increment click_count"""
    short_url = request.GET.get('short-url')
    if not short_url:
        return JsonResponse({'error': 'short-url is required'}, status=400)
    
    short_code = extract_short_code(short_url)
    url_obj = ShortUrl.objects.filter(short_url=short_code).first()

    if not url_obj:
        return JsonResponse({'error': 'No long url associated with this short url'}, status=404)
    
    url_obj.click_count += 1
    url_obj.save()
    
    return redirect(url_obj.original_url)

