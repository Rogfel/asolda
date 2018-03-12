# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import logout

###########
# User


def my_logout(request):
    logout(request)
    return render(request,'login')
