from django.shortcuts import render, redirect
from . import models, forms
from mahasiswa.models import Pkl
from mitra.models import Mitra
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/')
def mahasiswa(req):
    staf = models.Pkl.objects.all()
    return render(req, 'staf/index.html',{
        'data': staf,
    })

@login_required(login_url='/accounts/')
def mitra(req):
    staf = models.Mitra.objects.all()
    return render(req, 'staf/mitra.html',{
        'data': staf,
    })