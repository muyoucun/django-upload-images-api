from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from PIL import Image
import urllib
import time
import matlab.engine



@csrf_exempt
def alignment(request):

    data = {}
    path1=None
    path2=None
    savepath1=None
    savepath2=None

    ASSET_AUTH_KEY=['fengyushu','caichengfei','maoying','chenweiliang']

    # check to see if this is a post request
    if request.method == "POST":

        if request.POST.get('api_auth') is not None:
            [temp0,temp00,auth_key] = _grab_image(api_auth=request.POST.get('api_auth'))
            if auth_key not in ASSET_AUTH_KEY:
                data.update({'result':'the key is not available'})
                return JsonResponse(data)
            else:

                if request.FILES.get("image1") is not None:
                    # grab the uploaded image
                    [path1,temp1,temp2] = _grab_image(path1=request.FILES["image1"])
                    image1=Image.open(path1)
                    savepath1 = '/home/fengyushu/0822_2/media/' + str(time.strftime('%m%d%H%M%S')) + '_' + str(path1)
                    image1.save(savepath1)
                if request.FILES.get("image2") is not None:
                    [temp3,path2,temp4]=_grab_image(path2=request.FILES["image2"])
                    image2=Image.open(path2)
                    savepath2 = '/home/fengyushu/0822_2/media/' + str(time.strftime('%m%d%H%M%S')) + '_' + str(path2)
                    image2.save(savepath2)

                eng=matlab.engine.start_matlab()
                eng.addpath(r"/home/fengyushu/0822_2/api/face_alignment")
                result=eng.centerface_rec(savepath1,savepath2)

                data.update({'result':result})

                return JsonResponse(data)
        else:
            data.update({'result':'you should post a key'})
            return JsonResponse(data)

def _grab_image(path1=None,path2=None,api_auth=None):
    return [path1,path2,api_auth]

