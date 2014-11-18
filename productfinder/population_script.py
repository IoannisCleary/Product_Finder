import os

def populate():
    food = add_category(type = "Food and Drinks")
    health = add_category(type = "Health and Beauty")
    entertainment = add_category (type = "Home and Entertainment")
    pet = add_category (type = "Pets")
    other = add_category (type = "Other")

    user1 = add_requester(username = "BilboLOTR69",name = "Regina George",phone = 123456,city = "Glasgow", country = "United Kingdom")
    luckycharms = add_request(requester = user1, category = food, product_name = "Lucky Charms 125gr", product_brand = "General Mills", product_quantity = 2)
    makeup = add_request(requester = user1, category = health, product_name = "Waterproof eye-liner", product_brand = "MAC", product_quantity = 1)
    petFood = add_request(requester = user1, category = pet, product_name = "Dog dried food", product_brand = "Any", product_quantity = 1)
    entertainmentConsole = add_request(requester = user1, category = entertainment, product_name = "PS4", product_brand = "Sony", product_quantity = 1)
    otherProduct = add_request(requester = user1, category = other, product_name = "Band t-shirt", product_brand = "Any", product_quantity = 1)

    add_response(text = "Can be found at Tesco or American Candy Stores", helpful = True, request = luckycharms)
    add_response(text = "Why do you need this?", helpful = False, request = luckycharms)

def add_category(type):
	cat = Category.objects.get_or_create(type=type)[0]
	return cat
def add_requester(username,name,phone,city,country):
    usr = User.objects.get_or_create(username=username)[0]
    usrprofile = UserProfile.objects.get_or_create(user = usr,name=name,phone=phone,city=city,country=country)[0]
    return usrprofile
def add_request(requester,category,product_name,product_brand,product_quantity):
	rqst = Request.objects.get_or_create(requester=requester,category=category,product_name=product_name,product_brand=product_brand,product_quantity=product_quantity)[0]
	return rqst
def add_response(text,helpful,request):
	resp = Response.objects.get_or_create(text=text,helpful=helpful,request=request)[0]
	return resp

# Start execution here!
if __name__ == '__main__':
    print "Starting Product Finder population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productfinder.settings')
    from django.contrib.auth.models import User
    from product_finder.models import Request,Response,UserProfile,Category
    import django
    django.setup()
    populate()
