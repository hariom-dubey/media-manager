from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    # Now add the HTTP status code to the response.
    response = exception_handler(exc, context)

    if response is not None:
        if 'message' in response.data and response.data['message']:
            response.data = {
                "success" : False,
                "status_code" : response.status_code,
                "message" : response.data['message'],
                "data":  (
                    response.data['data'] if 'data' in response.data
                    else None
                )
            }
        else:
            response.data = {
                "success" : False,
                "status_code" : response.status_code,
                "message" : response.data['detail'],
                "data":  (
                    response.data['data'] if 'data' in response.data
                    else None
                )
            }

    return response