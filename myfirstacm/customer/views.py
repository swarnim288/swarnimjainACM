from django.shortcuts import render
from django.views import View

class Index(View):
	def get(self, request, *args, **kwargs):
		return render(request,'customer/index.html')

 class About(View):
	def get(self, request, *args, **kwargs):
		 return(request,'customer/about.html')

class Order(View):
	def get (self,request, *args, **kwargs):
		appetizers=MenuItem.objects.filter(category_name_contains='Appetizer')
        drinks=MenuItem.objects.filter(category_name_contains='drinks') 
 		desserts=MenuItem.objects.filter(category_name_contains='desserts')


 		context= {
 		'appetizers': appetizers,
 		'drinks': drinks,
 		'desserts':drinks,
 		}

 		return render(request,'customer/order.html', context)
    def post(self,request,*args,**kwargs):
    	order_items={
    	'items':[]
    	}

    	items=request.POST.getlist('items[]')

    	for item in items:
    		menu_item= MenuItem.objects.get(pk_contains=int(item))
    		item_data={
    		'id':menu_item.pk,
    		'name':menu_item.name,
    		'price': menu_item.price
    		}

    		order_items['items'].append(item_data)

    		price=0
    		item_ids=[]

    		for item in order_items['items']:
    			price+= item['price']
    			item.ids.append(item_id)

    			context = {
    			     'items': order_items['items'],
    			     'price':price
    			}

    			return render(request, 'customer/order_confirmation.html', context)