# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from product_finder.models import Category,Request,UserProfile
from product_finder.forms import RequestForm, UserForm, UserProfileForm

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
	context_dict = {'category_type': category_type,'category_type_url': category_type_url}
	try:
		category = Category.objects.get(type = category_type)
		requests = Request.objects.filter(category = category)
		context_dict['requests'] = requests
		context_dict['category'] = category
		context_dict['icon'] = category.icon
		context_dict['cat_image'] = category.image
	except Category.DoesNotExist:
		pass
	for request in requests:
		request.url = request.product_brand.replace(' ','_').replace('-','_ff_')+'_123_'+request.product_name.replace(' ','_').replace('-','_ff_')

	return render_to_response('product_finder/category.html',context_dict,context)
def add_request(request, category_type_url):
	context = RequestContext(request)
	category_type = category_type_url.replace('_', ' ')
	back = "/product_finder/category/" + category_type_url + "/"
	print back
	if request.method == 'POST':
		form = RequestForm(request.POST)

		if form.is_valid():
			rqst = form.save(commit=False)
			try:
				cat = Category.objects.get(type = category_type)
				rqst.category = cat
			except Category.DoesNotExist:
				pass
			usr = User.objects.get( username = request.user.username)
			rqst.requester= UserProfile.objects.get( user = usr)
			rqst.save()
			return index(request)
		else:
			print form.errors
	else:
		form = RequestForm()
	return render_to_response('product_finder/add_request.html', {'category_type_url': category_type_url,'category_type': category_type,'form': form,'goback':back}, context)

def request(request,category_type_url,request_productName_url):
	context = RequestContext(request)
	pbrand = request_productName_url.split('_123_')
	pB = pbrand[0].replace('_ff_','-').replace('_',' ')
	pName = pbrand[1].replace('_ff_','-').replace('_',' ')
	category_type = category_type_url.replace('_', ' ')
	print category_type_url
	url = "/product_finder/category/" + category_type_url + "/" + request_productName_url 
	back = "/product_finder/category/" + category_type_url + "/"
	context_dict = {'category_type': category_type, 'url':url,'goback':back}
	
	try:
		category = Category.objects.get(type = category_type)
		request = Request.objects.filter(category = category, product_name = pName, product_brand = pB)
		userprofile = request[0].requester
		context_dict['country'] = userprofile.country
		context_dict['city'] = userprofile.city
		context_dict['request'] = request[0]
		context_dict['requester'] = request[0].requester
		context_dict['description'] = request[0].description
		context_dict['name'] = request[0].product_name
		context_dict['brand'] = request[0].product_brand
		context_dict['quantity'] = request[0].product_quantity
		context_dict['local'] = request[0].area_local
		context_dict['online'] = request[0].area_online
		context_dict['category'] = category
	except Request.DoesNotExist:
		pass
	return render_to_response('product_finder/request.html',context_dict,context)

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile = profile_form.save()

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'product_finder/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):

    context = RequestContext(request)


    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)


        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/product_finder/')
            else:

                return HttpResponse("Your account is disabled.")
        else:

            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")


    else:

        return render_to_response('product_finder/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/product_finder/')
