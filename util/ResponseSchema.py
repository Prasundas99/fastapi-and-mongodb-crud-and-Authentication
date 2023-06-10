def responseSchema(isSuccess: bool, message: str, data: dict = None):
    return {
        "success": isSuccess,
        "message": message,
        "data": data
    }

def successResponse(message: str, data: dict = None):
    return responseSchema(True, message, data)

def errorResponse(message: str, data: dict = None):
    return responseSchema(False, message, data)