# django 
# can upload 2 images to the server (or The specified path)
# our project is to test the face alignmenet 
# here i didn't upload the matlab program
# and you must use the key to call the api 
# here i just list the keys in the views.py 
# so this method of using key to call the api may be different with the so-called api_key or api_secret
# just a test

# want to use the api you should have
# django urllib 
# and if you want to call the matlab just like "import matlab.engine"
# you should do something else
# just look at the documents of matlab


############################################

# call the api
# python
import requests
files=[
	('image1',open('/home/fengyushu/test/11111.jpg','rb')),
	('image2',open('/home/fengyushu/test/22222.jpg','rb')),
]
values={
	'api_auth':'fengyushu',
}
r=requests.post('http://localhost:8000/face_alignment/',files=files,data=values)
print r.text

# you need to post the api_auth
# and once you post and i will check the api_auth firstly 
# if it is available and read the image and call the matlab

#############################################
