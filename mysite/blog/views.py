from django.shortcuts import render


def posts_list(request):
    n = ["Oleg", "Petr", "Vasja"]
    return(render(request, 'blog/index.html', context={'names': n}))
