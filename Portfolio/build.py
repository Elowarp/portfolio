from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import dotenv
import os
import json

dotenv.load_dotenv()

# Url to rebuild the project
@csrf_exempt
def build(request):
    if request.method != "POST": return HttpResponse(status=404)

    BUILDING_KEY = os.getenv("BUILDING_KEY")
    key = json.loads(request.body)["hook"]["config"]["secret"]

    if (BUILDING_KEY != key): return HttpResponse(status=403)

    print("Building portfolio")
    process = subprocess.run(["bash", "build.sh"])
    if (process.returncode != 0):
        print("Issue while building ! (Error {})".format(process.returncode))
        return HttpResponse(status=500)


    print("Building completed !")
    return HttpResponse(status=200)