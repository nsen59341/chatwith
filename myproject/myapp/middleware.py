from auth import AuthenticationMiddleware

class userMiddleware(AuthenticationMiddleware):
    def __call__(self, request):
        print('request', request)