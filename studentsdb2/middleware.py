from datetime import datetime

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class RequestTimeMiddleware(MiddlewareMixin):
    """Display request time on a page"""
    #
    # def __init__(self, get_response):
    #     self.get_response = get_response
    #
    # def __call__(self, request):
    #
    #     response = self.get_response(request)
    #
    #     return response

    def process_request(self, request):
        request.start_time = datetime.now()
        return None

    def process_response(self, request, response):
        # if our process_request was canceled somewhere within
        # middleware stack, we can't calculate request time
        if not hasattr(request, 'start_time'):
            return response

        # calculate request execution time
        request.end_time = datetime.now()
        if 'text/html' in response.get('Content-Type', ''):
            response.write('<p>Request took: %s</p>' % str(request.end_time - request.start_time))

        return response

    def process_view(self, request, view, args, kwargs):
        return None

    def process_template_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        return HttpResponse('Exception found: %s' % exception)