import subprocess
from django.http import HttpResponse
import dotenv
import os

dotenv.load_dotenv()

# Url to rebuild the project
def build(request):
    BUILDING_KEY = os.getenv("BUILDING_KEY")
    key = request.GET.get('k', "")

    if (BUILDING_KEY != key): return HttpResponse(status=401)

    print("Building portfolio")
    process = subprocess.run(["bash", "build.sh"])
    if (process.returncode != 0):
        print("Issue while building ! (Error {})".format(process.returncode))
        return HttpResponse(status=500)


    print("End building !")
    return HttpResponse(status=200)