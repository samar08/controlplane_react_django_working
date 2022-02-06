from django.shortcuts import render
#import sys
sys.path.insert(1, 'app')
#from core.app.lib import list_pod_in_ns
from kubernetes import client,config
config.load_kube_config(config_file=r'core/app/k3s.yaml')
con=client.CoreV1Api()
# Create your views here.

def front(request):
    context = { }
    return render(request, "index.html", context)