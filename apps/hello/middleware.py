from apps.hello.models import Request


class SaveRequestMiddleware(object):
    def process_request(self, request):
        if request.is_ajax():
            return
        request_data = Request(request=request)
        request_data.save()
