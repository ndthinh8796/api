from django.shortcuts import render
from django.views import generic
from .scripts import rest_api


def index(request):
    return render(request, 'getapi/index.html')


def detail(request):
    url = request.GET['url']
    method = request.GET['method']
    get_values = request.GET.getlist
    params = rest_api.pair_keyvalue(get_values('key'),
                                    get_values('value')
                                    )
    headers = rest_api.pair_keyvalue(get_values('header_key'),
                                     get_values('header_value')
                                     )
    data = rest_api.pair_keyvalue(get_values('body_key'),
                                  get_values('body_value')
                                  )
    response = rest_api.get_response(url,
                                     method=method,
                                     params=params,
                                     data=data,
                                     headers=headers
                                     )
    return render(request,
                  'getapi/detail.html',
                  {'response': response}
                  )
