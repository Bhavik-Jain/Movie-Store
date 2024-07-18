from django.http import JsonResponse

def success_response(message, status, data=None):
    response = {
        "status": status,
        "message": message,
        "data": data
    }
    return JsonResponse(response, status=status)

def error_response(message, status):
    response = {
        "status": status,
        "message": message
    }
    return JsonResponse(response, status=status)
