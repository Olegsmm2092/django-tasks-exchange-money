from django.shortcuts import render

def exchange(request):
    name = "Olegsmm2092"
    context = {
        'name': name,
    }
    return render(
        request=request,
        template_name='exchange_money/index.html',
        context=context,
    )