from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import foundation
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageForm 
from PIL import Image 
import numpy as np
import os
import glob
import time

import base64

# Create your views here. 
from django.http import JsonResponse

def uploadimage(request): 
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        
    context = {'form': form}
    return render(request, 'home.html', context)



#upload = foundation.objects.filter(file_type='img')
	#img = Image.open(upload)
def match(request):
	this_file=os.path.abspath(__file__)
	base_dir=os.path.dirname(this_file)
	entries = os.listdir('makeup/db_images/')
	entries2= os.listdir('media/images/')
	list_of_files = glob.glob('media/images/*')
	latest = max(list_of_files, key=os.path.getctime)
	img=Image.open(latest)
	
	r, g, b = img.split()
	len(r.histogram())
	red=r.histogram()
	green=g.histogram()
	blue=b.histogram()
	mr=max(red)
	mg=max(green)
	mb=max(blue)
	nhr = [i/mr for i in red]
	nnhr  = np.multiply(nhr, 255)
	nhg = [i/mg for i in green]
	nnhg  = np.multiply(nhg, 255)
	nhb = [i/mb for i in blue]
	nnhb  = np.multiply(nhb, 255)
	n=1
	p=[fname.rsplit('_', 1)[0] for fname in entries]
	mylist = list(dict.fromkeys(p))[:-1]
	for i in range(0, len(mylist)):
		img1=mylist[i]+'_a.jpg'
		img2=mylist[i]+'_b.jpg'
		img3=mylist[i]+'_face.jpg'
		f1='makeup/db_images/'+img1
		f2='makeup/db_images/'+img2
		f3='makeup/db_images/'+img3
		db_img = Image.open(f1)
		r1, g1, b1 = db_img.split()
		red1=r1.histogram()
		green1=g1.histogram()
		blue1=b1.histogram()
		db_img2 = Image.open(f2)
		r2, g2, b2 = db_img2.split()
		red2=r2.histogram()
		green2=g2.histogram()
		blue2=b2.histogram()
		db_img3 = Image.open(f3)
		shr = red1+red2
		shg = green1+green2
		shb = blue1+blue2
		shr1=np.divide(shr, 2)
		shg1=np.divide(shg, 2)
		shb1=np.divide(shb, 2)
		smr=max(shr1)
		smg = max(shg1)
		smb = max(shb1)
		nhr1 = [i/smr for i in shr1]
		nnhr1  = np.multiply(nhr1, 255)
		nhg1 = [i/smg for i in shg1]
		nnhg1  = np.multiply(nhg1, 255)
		nhb1 = [i/smb for i in shb1]
		nnhb1  = np.multiply(nhb1, 255)
		z1=zip(nnhr, nnhr1)
		z2=zip(nnhg, nnhg1)
		z3=zip(nnhb, nnhb1)
		diff1=[abs(x - y )for x, y in z1]
		diff2=[abs(x1 - y1 )for x1,y1 in z2]
		diff3=[abs(x2 - y2 )for x2, y2 in z3]
		dr=sum(diff1)
		dg=sum(diff2)
		db=sum(diff3)
		total=dr+db+dg
		if n==1:
			mimg=db_img3
			mdd=total
		else:
			if total<mdd:
				mdd=total
				mimg=db_img3
		n=n+1
	#mimg.show()
	files = glob.glob('media/images/*')
	for f in files:
		try:
			os.remove(f)
		except OSError as e:
			print("Error: %s : %s" % (f, e.strerror))
	files2 = glob.glob('static_in_env/resultant/*')
	for f in files:
		try:
			os.remove(f)
		except OSError as e:
			print("Error: %s : %s" % (f, e.strerror))

	
	mimg.save('static_in_env/resultant/abn.jpg')

	

	context={
	'mimg':mimg
	}
	

	
	return render(request, 'home1.html', context)
	
def contact(request):
	context={}
	return render(request, 'contact.html', context)
	
