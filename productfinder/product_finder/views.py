# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from product_finder.models import Category,Request

def index(request):
	context = RequestContext(request)
	categories = Category.objects.order_by('type')
	context_dict = {'categories': categories}
	
	for category in categories:
		category.url = category.type.replace(' ', '_')
	
	return render_to_response('product_finder/index.html',context_dict,context)

	
def category(request,category_type_url):
	context = RequestContext(request)
	category_type = category_type_url.replace('_', ' ')
	context_dict = {'category_type': category_type}
	try:
		category = Category.objects.get(type = category_type)
		requests = Request.objects.filter(category = category)
		context_dict['requests'] = requests
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
	for request in requests:
		request.url = request.product_brand.replace(' ','_').replace('-','_ff_')+'_123_'+request.product_name.replace(' ','_').replace('-','_ff_')
		
	return render_to_response('product_finder/category.html',context_dict,context)
	
def request(request,category_type_url,request_productName_url):
	context = RequestContext(request)
	pbrand = request_productName_url.split('_123_')
	pB = pbrand[0].replace('_ff_','-').replace('_',' ')
	pName = pbrand[1].replace('_ff_','-').replace('_',' ')
	category_type = category_type_url.replace('_', ' ')
	context_dict = {'category_type': category_type}
	try:
		category = Category.objects.get(type = category_type)
		request = Request.objects.filter(category = category, product_name = pName, product_brand = pB)
		context_dict['requester'] = request[0].requester
		context_dict['name'] = request[0].product_name
		context_dict['brand'] = request[0].product_brand
		context_dict['quantity'] = request[0].product_quantity
		context_dict['local'] = request[0].area_local
		context_dict['online'] = request[0].area_online
		context_dict['category'] = category
	except Request.DoesNotExist:
		pass
	return render_to_response('product_finder/request.html',context_dict,context)
