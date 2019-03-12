from django.shortcuts import redirect

def hello(request):
    return(HttpResponse('<h1>Hello world</h1>'))


def redirect_blog(request):
    return redirect('post_list_url', permanent=True)
