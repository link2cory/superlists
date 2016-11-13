from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_to_view = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_to_view})


def new_list(request):
    list_to_add = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_to_add)
    return redirect('/lists/%d/' % (list_to_add.id,))


def add_item(request, list_id):
    list_to_add_item_to = List.objects.get(id=list_id)
    Item.objects.create(
        text=request.POST['item_text'],
        list=list_to_add_item_to
    )
    return redirect('/lists/%d/' % (list_to_add_item_to.id,))
