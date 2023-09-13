from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def sales_invoice(request):
    print(type(request.body))
    body = request.body
    print("body", body.decode("utf-8"))
    print("type of body", type(body))
    items = json.loads(body.decode())
    print("items", items)
    print("type of items", type(items))
    for item in items:
        print(item)
    return JsonResponse({"status": "ok"})
