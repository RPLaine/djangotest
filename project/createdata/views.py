from django.shortcuts import render
from .models import SimpleData
from .forms import SimpleDataForm

def index(request):
    form = SimpleDataForm()

    context = {}
    context['title'] = 'Datalist'
    context['page'] = 0
    context['pagination'] = True if (SimpleData.objects.count() > 10) else False
    
    
    if (context['pagination']):
        context['data'] = SimpleData.objects.all().order_by('id')[(context['page'] * 10) : (context['page'] * 10 + 10)]
        context['pages'] = int(SimpleData.objects.count() / 10)
    else: context['data'] = SimpleData.objects.all()

    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = SimpleDataForm(request.POST)
            else:
                data = SimpleData.objects.get(id=pk)
                form = SimpleDataForm(request.POST, instance=data)
            form.save()
            form = SimpleDataForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = SimpleData.objects.get(id=pk)
            item.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = SimpleData.objects.get(id=pk)
            form = SimpleDataForm(instance=item)

    context['form'] = form

    return render(request, 'createdata/index.html', context)