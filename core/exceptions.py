from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from core.methods import standardResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
    	if response.status_code == 429:
    		error_message = "Too many attempts. Please try again later after {}".format(response.data["detail"][-14:])
    		return Response(standardResponse(errors=error_message), status=status.HTTP_429_TOO_MANY_REQUESTS)

    return response
