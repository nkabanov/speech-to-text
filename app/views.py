from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def main(request):
    return render(request, 'index.html')

@csrf_exempt
def process_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '')
        return JsonResponse({'response': f'Ты сказал: {text}'})
