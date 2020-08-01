from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import render, redirect

from .models import Inventory, Items, Orders


def login_user(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("/items/")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        """
            check if the user is authenticated or not
        """
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/items/")
        else:
            context = {
                "error": "Invalid login!"
            }
    return render(request, "main/home.html", context)


def logout_user(request):
    logout(request)
    return redirect("/")

""" 
    display all the items list present in the inventory 
"""

def items(request):
    if request.user.is_authenticated:
        inventories = Inventory.objects.all()
        context = {
            "inventories": inventories
        }
        return render(request, "main/items.html", context)
    else:
        return redirect("/")

""" 
    order a particular item using it's order id
"""

def make_order(request, inventory_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            """
                making the transaction atomic so that no one can
                interfare during that transaction
                this is done to avoid the race condition
            """
            with transaction.atomic():
                try:
                    inventory = Inventory.objects.get(id=inventory_id)
                except Inventory.DoesNotExist:
                    error = "Inventory with id {} doesn not exist".format(inventory_id)
                    context = {"error": error}
                    return render(request, "main/items.html", context)

                order_count = int(request.POST["order_count"])
                inventory_item_count = inventory.item_count

                """ 
                    if order_count is number of items present in the inventory
                    then only place the order, other wise return the error message 
                """

                if order_count <= inventory.item_count:
                    order = Orders.objects.create(
                        user=request.user,
                        item=inventory.item,
                        order_count=order_count
                    )
                    item_name = inventory.item.item_name
                    order_id = item_name.replace(" ", "").lower() + str(order.id) + str(order_count)
                    context = {
                        "item_name": item_name,
                        "item_price": inventory.item.item_price,
                        "total_price": inventory.item.item_price*order_count,
                        "order_count": order_count,
                        "order_id": order_id,
                        "picture_url": inventory.item.picture.url
                    }
                    """
                        if all the items have been ordered by any user, delete that item from the inventory
                    """     
                    if order_count == inventory.item_count:
                        inventory.delete()
                    else:
                        inventory.item_count = inventory_item_count - order_count
                        inventory.save()
                    return render(request, "main/order_summary.html", context)
                else:
                    error = "You cannot order more than the stock count"
                    context = {"error": error}
                    return render(request, "main/items.html", context)
        else:
            return redirect("/")
            
            
