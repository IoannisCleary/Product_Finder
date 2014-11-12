# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context= RequestContext(request)
	context_dict ={}
	return render_to_response('product_finder/index.html',context_dict,context)
def request_page(request):
	context= RequestContext(request)
	context_dict ={}
	return render_to_response('product_finder/request_page.html',context_dict,context)
