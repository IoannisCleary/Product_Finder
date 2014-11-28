import os

def populate():
	food = add_category(type = "Food and Drinks",icon="icon-glass",image="food.png")
	health = add_category(type = "Health and Beauty",icon="icon-eye-open",image="xv.png")
	entertainment = add_category (type = "Home and Entertainment",icon="icon-headphones",image="random_grey_variations.png")
	pet = add_category (type = "Pets",icon="icon-leaf",image="pool_table.png")
	other = add_category (type = "Other",icon="icon-certificate",image="washi.png")
	admin = add_requester(username = "Administrator",name = "Leader",phone = 999666,city = "Unknown city", country = "Unknown country")
	user1 = add_requester(username = "BilboLOTR69",name = "Regina George",phone = 123456,city = "Glasgow", country = "United Kingdom")
	luckycharms = add_request(requester = user1, category = food, product_name = "Lucky Charms", product_brand = "General Mills", product_quantity = 2,description="Corn flakes")
	cola = add_request(requester = user1, category = food, product_name = "Cherry cola", product_brand = "Coca cola", product_quantity = 6,description="Soft drink")
	crisps = add_request(requester = user1, category = food, product_name = "Pickled onion crisps", product_brand = "Walkers", product_quantity = 5,description="Potato crisps packet of 32.5 gr")
	peanutbutter = add_request(requester = user1, category = food, product_name = "Peanut butter cups", product_brand = "Reeses", product_quantity = 4,description="Chocolates with peanut butter filling")
	pumpkins = add_request(requester = user1, category = food, product_name = "Pumpkins", product_brand = "any", product_quantity = 4,description="Orange pumpkins")
	candycorn = add_request(requester = user1, category = food, product_name = "Candy corn", product_brand = "Brachs", product_quantity = 1,description="Candy")
	makeup = add_request(requester = user1, category = health, product_name = "Waterproof eye-liner", product_brand = "MAC", product_quantity = 1,description=" MAC Cosmetics Pro ")
	lipstick = add_request(requester = user1, category = health, product_name = "Matte lip tar", product_brand = "Obsessive compulsive cosmetics", product_quantity = 10,description=" Make-up ")
	bronzer = add_request(requester = user1, category = health, product_name = "Bronzer", product_brand = "Sunkissed", product_quantity = 1,description=" Make-up ")
	dogFood = add_request(requester = user1, category = pet, product_name = "Dog dry food", product_brand = "Any", product_quantity = 1,description="Beef flavoured")
	catFood = add_request(requester = user1, category = pet, product_name = "Dry food", product_brand = "Whiskas", product_quantity = 3,description="Beef flavoured")
	entertainmentConsole = add_request(requester = user1, category = entertainment, product_name = "PS4", product_brand = "Sony", product_quantity = 1,description=" Playstation 4")
	otherProduct = add_request(requester = user1, category = other, product_name = "Band t-shirt", product_brand = "Any", product_quantity = 1,description=" Black colour")

def add_category(type,icon,image):
	cat = Category.objects.get_or_create(type=type,icon=icon,image=image)[0]
	return cat
def add_profile(username,name,phone,city,country):
    usrprofile = UserProfile.objects.get_or_create(user = usr,name=name,phone=phone,city=city,country=country)[0]
    return usrprofile
def add_requester(username,name,phone,city,country):
    usr = User.objects.get_or_create(username=username)[0]
    usrprofile = UserProfile.objects.get_or_create(user = usr,name=name,phone=phone,city=city,country=country)[0]
    return usrprofile
def add_request(requester,category,product_name,product_brand,product_quantity,description):
	rqst = Request.objects.get_or_create(requester=requester,category=category,product_name=product_name,product_brand=product_brand,product_quantity=product_quantity,description=description)[0]
	return rqst

# References:
# This script was created with the help of a Tango with Django book chapter 
# Chapter 5. Models and Databases 
# http://www.tangowithdjango.com/book/chapters/models.html#creating-a-population-script

if __name__ == '__main__':
    print "Starting Product Finder population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productfinder.settings')
    from django.contrib.auth.models import User
    from product_finder.models import Request,UserProfile,Category
    populate()
