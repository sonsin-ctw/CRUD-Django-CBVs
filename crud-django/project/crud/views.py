from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

class ItemListView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'item_list.html', {'items': items})

class ItemDetailView(View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'item_detail.html', {'item': item})

class ItemCreateView(View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'item_form.html', {'form': form})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        return render(request, 'item_form.html', {'form': form})

class ItemUpdateView(View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(instance=item)
        return render(request, 'item_form.html', {'form': form})

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        return render(request, 'item_form.html', {'form': form})

class ItemDeleteView(View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'item_confirm_delete.html', {'item': item})

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('item_list')
