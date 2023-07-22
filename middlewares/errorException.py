import traceback
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from fastapi import status

def custom_exception_handler(request, exc):
    """Custom exception handler."""

    response = {
        "success": False,
        "message": str(exc.detail),
    }

    if isinstance(exc, StarletteHTTPException):
        response["status_code"] = exc.status_code

    if hasattr(exc, "errors"):
        response["data"] = exc.errors

    if exc.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
     response["message"] = "Internal Server Error"
     response["data"] = {
        "error": "Something went wrong on our end. Please try again later.",
        "call_stack": traceback.format_stack()
     }
    
    return JSONResponse(response)