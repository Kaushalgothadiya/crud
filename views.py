from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import YourModel

@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        item = YourModel.objects.create(data=data)
        return JsonResponse({'id': item.id, 'data': item.data})

@csrf_exempt
def read_item(request, item_id):
    if request.method == 'GET':
        try:
            item = YourModel.objects.get(id=item_id)
            return JsonResponse({'id': item.id, 'data': item.data})
        except YourModel.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)

@csrf_exempt
def update_item(request, item_id):
    if request.method == 'PUT':
        try:
            item = YourModel.objects.get(id=item_id)
            item.data = request.PUT.get('data')
            item.save()
            return JsonResponse({'id': item.id, 'data': item.data})
        except YourModel.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)

@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'DELETE':
        try:
            item = YourModel.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully'})
        except YourModel.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)
