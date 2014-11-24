import os

def populate():
    food = add_category(type = "Food and Drinks",icon="icon-glass",image="none")
    health = add_category(type = "Health and Beauty",icon="icon-eye-open",image="none")
    entertainment = add_category (type = "Home and Entertainment",icon="icon-headphones",image="none")
    pet = add_category (type = "Pets",icon="icon-leaf",image="none")
    other = add_category (type = "Other",icon="icon-certificate",image="none")

    user1 = add_requester(username = "BilboLOTR69",name = "Regina George",phone = 123456,city = "Glasgow", country = "United Kingdom")
    luckycharms = add_request(requester = user1, category = food, product_name = "Lucky Charms", product_brand = "General Mills", product_quantity = 2,description="Corn flakes")
    makeup = add_request(requester = user1, category = health, product_name = "Waterproof eye-liner", product_brand = "MAC", product_quantity = 1,description=" MAC Cosmetics Pro ")
    petFood = add_request(requester = user1, category = pet, product_name = "Dog dried food", product_brand = "Any", product_quantity = 1,description="Beef flavoured")
    entertainmentConsole = add_request(requester = user1, category = entertainment, product_name = "PS4", product_brand = "Sony", product_quantity = 1,description=" Playstation 4")
    otherProduct = add_request(requester = user1, category = other, product_name = "Band t-shirt", product_brand = "Any", product_quantity = 1,description=" Black colour")

    add_response(text = "Can be found at Tesco or American Candy Stores", helpful = True, request = luckycharms)
    add_response(text = "Why do you need this?", helpful = False, request = luckycharms)

def add_category(type,icon,image):
	cat = Category.objects.get_or_create(type=type,icon=icon,image=image)[0]
	return cat
def add_requester(username,name,phone,city,country):
    usr = User.objects.get_or_create(username=username)[0]
    usrprofile = UserProfile.objects.get_or_create(user = usr,name=name,phone=phone,city=city,country=country)[0]
    return usrprofile
def add_request(requester,category,product_name,product_brand,product_quantity,description):
	rqst = Request.objects.get_or_create(requester=requester,category=category,product_name=product_name,product_brand=product_brand,product_quantity=product_quantity,description=description)[0]
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
    populate()
