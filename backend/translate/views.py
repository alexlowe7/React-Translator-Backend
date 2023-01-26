from django.shortcuts import render
import json
from django.http import JsonResponse
import deepl
from django.views.decorators.csrf import csrf_exempt

auth_key = "3d120b62-3760-cc5e-9df6-95b82f6f86f3:fx"
translator = deepl.Translator(auth_key)

@csrf_exempt
def translate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get("text")
        source = data.get("source")
        target = data.get("target")
        result = translator.translate_text(text, target_lang=target, source_lang=source)
        return JsonResponse({"translated_text": result.text, "source_lang": result.detected_source_lang}, status=201)