import time


class RequestLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start = time.perf_counter()

        response = self.get_response(request)

        elapsed = time.perf_counter() - start

        if request.user.is_authenticated:
            user = request.user.username
        else:
            user = "Anonymous"

        print(
            f"User: {user} | "
            f"Method: {request.method} | "
            f"Path: {request.path} | "
            f"Time: {elapsed:.2f}s"
        )

        return response