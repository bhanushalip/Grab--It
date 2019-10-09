from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect
from django.urls import resolve


def find_worth(function):
    def _function(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('login'))
        if request.user.is_worthy is None:
            if resolve(request.path_info).url_name != 'home':
                return redirect(reverse('home'))
        elif request.user.is_worthy:
            if resolve(request.path_info).url_name != 'worthy':
                return redirect(reverse('worthy'))
        elif not request.user.is_worthy:
            if resolve(request.path_info).url_name != 'peasant':
                return redirect(reverse('peasant'))
        return function(request, *args, **kwargs)
    return _function
