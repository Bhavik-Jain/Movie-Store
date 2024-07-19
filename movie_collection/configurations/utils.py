from django.http import JsonResponse
import requests
from requests.auth import HTTPBasicAuth
from rest_framework import status
from django.conf import settings

def success_response(message, status, data=None):
    response = {
        "status": status,
        "message": message,
        "data": data
    }
    return JsonResponse(response, status=status)

def error_response(message, status, api):
    response = {
        "status": status,
        "message": message
    }
    print('api', api)
    return JsonResponse(response, status=status)


def fetch_movies_with_retries(url, retries=10):
    username = 'iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0'
    password = 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'
    attempt = 0
    success = False
    while attempt < retries and not success:
        try:
            auth = HTTPBasicAuth(username, password)
            response = requests.get(url, auth=auth, timeout=10, verify=False)
            if response.status_code == status.HTTP_200_OK:
                success = True
                return response.json()
            else:
                print(f"Attempt {attempt + 1} failed with status code: {response.status_code}")
                attempt += 1
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1

    return None
