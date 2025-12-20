from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import dotenv
import os
import json

import hashlib
import hmac

dotenv.load_dotenv()

# Url to rebuild the project
@csrf_exempt
def build(request):
    if request.method != "POST": return HttpResponse(status=404)

    # Verify that the action comes from GitHub
    BUILDING_KEY = os.getenv("BUILDING_KEY")
    hash_object = hmac.new(BUILDING_KEY.encode('utf-8'), msg=request.body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()

    if expected_signature != request.headers["X-Hub-Signature-256"]:
        return HttpResponse(status=403)

    print("Launching building !")
    process = os.system("bash build.sh&") # Launch the build script in the background
    return HttpResponse(status=200)
