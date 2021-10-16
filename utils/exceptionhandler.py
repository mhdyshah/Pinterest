from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    handlers = {
        "ValidationError": _hande_generic_error,
        "Http404": _hande_generic_error,
        "PermissionDenied": _hande_generic_error,
        "NotAuthenticated": _hande_authentication_error,
    }

    response = exception_handler(exc, context)

    if response is not None:
        response.data["status_code"] = response.status_code

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _hande_authentication_error(exc, context, response):

    response.data = {
        "error": "Please login to proceed",
        "status_code": response.status_code

    }
    return response


def _hande_generic_error(exc, context, response):
    return response
