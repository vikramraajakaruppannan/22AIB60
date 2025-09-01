import requests
from django.utils.deprecation import MiddlewareMixin

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJ2aWtyYW1yYWFqYV8yMmFpYjYwQGtna2l0ZS5hYy5pbiIsImV4cCI6MTc1NjcwNDgwMSwiaWF0IjoxNzU2NzAzOTAxLCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiZDZmZDk1MGYtZWZjZi00N2Y0LWI5OWEtNjRjMGZiZGY0ZDgxIiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoidmlrcmFtIHJhYWphIGsiLCJzdWIiOiIxMmNkZTU3MC1kMTFjLTRiMmUtOGNkMC04NTE0Mjc4ZDc2YTYifSwiZW1haWwiOiJ2aWtyYW1yYWFqYV8yMmFpYjYwQGtna2l0ZS5hYy5pbiIsIm5hbWUiOiJ2aWtyYW0gcmFhamEgayIsInJvbGxObyI6IjIyYWliNjAiLCJhY2Nlc3NDb2RlIjoiZHFYdXdaIiwiY2xpZW50SUQiOiIxMmNkZTU3MC1kMTFjLTRiMmUtOGNkMC04NTE0Mjc4ZDc2YTYiLCJjbGllbnRTZWNyZXQiOiJtQlVOZGtaQnNDRlZrZFhyIn0.LXaEkfoBlYZ5eYKeqLwnNW6wMrXjQd4EXCAx2kJeKQ8" 
def Log(stack, level, package, message):
    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }
    print("LOG PAYLOAD:", payload)
    test_server_url = "http://20.244.56.144/evaluation-service/logs" 
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        requests.post(test_server_url, json=payload, headers=headers, timeout=2)
    except Exception:
        pass

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        Log("backend", "info", "middleware", f"Request started: {request.method} {request.path}")

    def process_response(self, request, response):
        Log("backend", "info", "middleware", f"Response: {response.status_code} for {request.method} {request.path}")
        return response

    def process_exception(self, request, exception):
        Log("backend", "error", "middleware", f"Exception: {str(exception)} at {request.path}")