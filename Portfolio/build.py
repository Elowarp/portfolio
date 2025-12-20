from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import dotenv
import os
import json

import hashlib
import hmac

dotenv.load_dotenv()

def verify_signature(payload_body, secret_token, signature_header):
    """Verify that the payload was sent from GitHub by validating SHA256.

    Raise and return 403 if not authorized.

    Args:
        payload_body: original request body to verify (request.body())
        secret_token: GitHub app webhook token (WEBHOOK_SECRET)
        signature_header: header received from GitHub (x-hub-signature-256)
    """
    if not signature_header:
        raise HTTPException(status_code=403, detail="x-hub-signature-256 header is missing!")

    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()

    if not hmac.compare_digest(expected_signature, signature_header):
        raise HTTPException(status_code=403, detail="Request signatures didn't match!")

# Url to rebuild the project
@csrf_exempt
def build(request):
    if request.method != "POST": return HttpResponse(status=404)

    BUILDING_KEY = os.getenv("BUILDING_KEY")

    try:
        verify_signature(body, BUILDING_KEY, request.headers["X-Hub-Signature-256"])
    except: 
        print("Signature error !")
        return HttpResponse(status_code=403)

    print("Launching building !")
    process = os.system("bash build.sh&") # Launch the build script in the background
    return HttpResponse(status=200)