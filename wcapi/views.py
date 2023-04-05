import os
import datetime

import pytz
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ResumeForm, ResumeFormIcons, ResumeFormWallpapers, ResumeFormThemesSlug, ResumeFormThemesSlugPremium, \
    ResumeFormThemesSlugPremium, ResumeFormIconSlug, ResumeFormIconPremium, ResumeFormWallpaperPremium, \
    ResumeFormWallpaperSlug, ResumeWidgetsHome, ResumeWidgetsLock, ResumeWidgetsLockSlugPremium, ResumeWidgetsLockSlug, \
    ResumeWidgetsHomeSlug, ResumeWidgetsHomeSlugPremium
from .models import Themes, Icons, Wallpapers, Theme, Icon, Wallpaper, WidgetsLock, WidgetsHome, WidgetsLockS, \
    WidgetsHomeH, MobileConfig
from .serializers import WcapiSerializer, IconSerializer, ThemeSerializer, MobileConfigSerializer
from django.http import FileResponse


@login_required(login_url='/admin/')
def index(request):  # HttpRequest
    context = Themes.objects.all()
    context = {'contact': context}
    return render(request, 'wcapi/index.html', context)


@login_required(login_url='/admin/')
def index_add_category(request):  # HttpRequest
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    return render(request, 'wcapi/index_add_category.html')


@login_required(login_url='/admin/')
def index_del_category(request, cat_slug):  # HttpRequest
    Themes.objects.filter(id_themes=int(cat_slug)).delete()
    context = Themes.objects.all()
    context = {'contact': context}

    return render(request, 'wcapi/index.html', context)


@login_required(login_url='/admin/')
def del_p_index_cat_slug(request, cat_slug, pwev_slug):
    Theme.objects.filter(cat_slug=int(cat_slug), id_theme=int(pwev_slug)).delete()
    context = {'cat_slug': cat_slug}
    context['posts'] = Theme.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/index_cat_slug.html', context)


@login_required(login_url='/admin/')
def del_p_icons_cat_slug(request, cat_slug, pwev_slug):
    Icon.objects.filter(cat_slug=int(cat_slug), id_icon=int(pwev_slug)).delete()
    context = {'cat_slug': cat_slug}
    context['posts'] = Icon.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/icons_cat_slug.html', context)


@login_required(login_url='/admin/')
def del_p_wallpapers_cat_slug(request, cat_slug, pwev_slug):
    Wallpaper.objects.filter(cat_slug=int(cat_slug), id_wallpapers=int(pwev_slug)).delete()
    context = {'cat_slug': cat_slug}
    context['posts'] = Wallpaper.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/wallpapers_cat_slug.html', context)


@login_required(login_url='/admin/')
def icons_del_category(request, cat_slug):  # HttpRequest
    Icons.objects.filter(id_icons=int(cat_slug)).delete()
    context = Icons.objects.all()
    context = {'contact': context}

    return render(request, 'wcapi/icons.html', context)


@login_required(login_url='/admin/')
def wallpapers_del_category(request, cat_slug):  # HttpRequest
    Wallpapers.objects.filter(id_wallpapers=int(cat_slug)).delete()
    context = Wallpapers.objects.all()
    context = {'contact': context}

    return render(request, 'wcapi/wallpapers.html', context)


@login_required(login_url='/admin/')
def index_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}
    context['posts'] = Theme.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/index_cat_slug.html', context)


@login_required(login_url='/admin/')
def p_index_cat_slug(request, cat_slug, pwev_slug):
    if request.method == 'POST':
        data = Theme.objects.get(cat_slug=str(cat_slug), id_theme=int(pwev_slug))

        if data.is_publish == 'on':
            data.is_publish = 'off'
        else:
            data.is_publish = 'on'
        if 'premium' in request.POST:
            data.premium = 'on'
        else:
            data.premium = 'off'
        data.save()

    context = {'cat_slug': cat_slug, 'pwev_slug': pwev_slug}
    context['posts'] = Theme.objects.get(cat_slug=str(cat_slug), id_theme=int(pwev_slug))
    return render(request, 'wcapi/p_index_cat_slug.html', context)


@login_required(login_url='/admin/')
def p_wallpapers_cat_slug(request, cat_slug, pwev_slug):
    if request.method == 'POST':
        data = Wallpaper.objects.get(cat_slug=str(cat_slug), id_wallpapers=int(pwev_slug))
        if data.is_publish == 'on':
            data.is_publish = 'off'
        else:
            data.is_publish = 'on'
        if 'premium' in request.POST:
            data.premium = 'on'
        else:
            data.premium = 'off'

        data.save()
    context = {'cat_slug': cat_slug, 'pwev_slug': pwev_slug}
    context['posts'] = Wallpaper.objects.get(cat_slug=str(cat_slug), id_wallpapers=int(pwev_slug))
    return render(request, 'wcapi/p_wallpapers_cat_slug.html', context)


@login_required(login_url='/admin/')
def index_add_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}

    if request.method == 'POST':
        if 'premium' in request.POST:
            form = ResumeFormThemesSlugPremium(request.POST, request.FILES)
            if form.is_valid():
                new_contact = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_contact.id_theme}
                context['posts'] = Theme.objects.get(cat_slug=str(cat_slug), id_theme=int(new_contact.id_theme))
                return render(request, 'wcapi/p_index_cat_slug.html', context)

        else:
            form = ResumeFormThemesSlug(request.POST, request.FILES)
            if form.is_valid():
                new_contact = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_contact.id_theme}
                context['posts'] = Theme.objects.get(cat_slug=str(cat_slug), id_theme=int(new_contact.id_theme))
                return render(request, 'wcapi/p_index_cat_slug.html', context)

    return render(request, 'wcapi/index_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def edit_icons_cat_slug(request, cat_slug, pwev_slug):
    context = {'cat_slug': cat_slug}
    if request.method == 'POST':
        print(request.POST)
        if 'premium' in request.POST:
            print('зашло')
            form = ResumeFormIconPremium(request.POST, request.FILES)
            if form.is_valid():
                Icon.objects.filter(cat_slug=int(cat_slug), id_icon=int(pwev_slug)).delete()
                form.save()
        else:
            form = ResumeFormIconSlug(request.POST, request.FILES)
            if form.is_valid():
                Icon.objects.filter(cat_slug=int(cat_slug), id_icon=int(pwev_slug)).delete()
                form.save()

    return render(request, 'wcapi/icons_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def edit_wallpapers_cat_slug(request, cat_slug, pwev_slug):
    context = {'cat_slug': cat_slug}
    if request.method == 'POST':
        if 'premium' in request.POST:
            form = ResumeFormWallpaperPremium(request.POST, request.FILES)
            if form.is_valid():
                Wallpaper.objects.filter(cat_slug=int(cat_slug), id_wallpapers=int(pwev_slug)).delete()
                form.save()
        else:
            form = ResumeFormWallpaperSlug(request.POST, request.FILES)
            if form.is_valid():
                Wallpaper.objects.filter(cat_slug=int(cat_slug), id_wallpapers=int(pwev_slug)).delete()
                form.save()

    return render(request, 'wcapi/wallpapers_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def edit_index_cat_slug(request, cat_slug, pwev_slug):
    context = {'cat_slug': cat_slug}

    if request.method == 'POST':
        if 'premium' in request.POST:
            form = ResumeFormThemesSlugPremium(request.POST, request.FILES)
            if form.is_valid():
                Theme.objects.filter(cat_slug=int(cat_slug), id_theme=int(pwev_slug)).delete()
                form.save()
        else:
            form = ResumeFormThemesSlug(request.POST, request.FILES)
            if form.is_valid():
                Theme.objects.filter(cat_slug=int(cat_slug), id_theme=int(pwev_slug)).delete()
                form.save()

    return render(request, 'wcapi/index_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def icon_add_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}
    if request.method == 'POST':
        print(request.POST)
        if 'premium' in request.POST:
            print('зашло')
            form = ResumeFormIconPremium(request.POST, request.FILES)
            if form.is_valid():
                new_con = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_con.id_icon}
                context['posts'] = Icon.objects.get(cat_slug=str(cat_slug), id_icon=int(new_con.id_icon))
                return render(request, 'wcapi/p_icons_cat_slug.html', context)
        else:
            form = ResumeFormIconSlug(request.POST, request.FILES)
            if form.is_valid():
                new_con = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_con.id_icon}
                context['posts'] = Icon.objects.get(cat_slug=str(cat_slug), id_icon=int(new_con.id_icon))
                return render(request, 'wcapi/p_icons_cat_slug.html', context)

    return render(request, 'wcapi/icons_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def wallpapers_add_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}
    if request.method == 'POST':
        if 'premium' in request.POST:
            form = ResumeFormWallpaperPremium(request.POST, request.FILES)
            if form.is_valid():
                new_con = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_con.id_wallpapers}
                context['posts'] = Wallpaper.objects.get(cat_slug=str(cat_slug),
                                                         id_wallpapers=int(new_con.id_wallpapers))
                return render(request, 'wcapi/p_wallpapers_cat_slug.html', context)
        else:
            form = ResumeFormWallpaperSlug(request.POST, request.FILES)
            if form.is_valid():
                new_con = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_con.id_wallpapers}
                context['posts'] = Wallpaper.objects.get(cat_slug=str(cat_slug),
                                                         id_wallpapers=int(new_con.id_wallpapers))
                return render(request, 'wcapi/p_wallpapers_cat_slug.html', context)

    return render(request, 'wcapi/wallpapers_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def wallpapers_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}
    context['posts'] = Wallpaper.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/wallpapers_cat_slug.html', context)


@login_required(login_url='/admin/')
def icons_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}
    context['posts'] = Icon.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/icons_cat_slug.html', context)


@login_required(login_url='/admin/')
def p_icons_cat_slug(request, cat_slug, pwev_slug):
    if request.method == 'POST':
        data = Icon.objects.get(cat_slug=str(cat_slug), id_icon=int(pwev_slug))
        if data.is_publish == 'on':
            data.is_publish = 'off'
        else:
            data.is_publish = 'on'
        if 'premium' in request.POST:
            data.premium = 'on'
        else:
            data.premium = 'off'
        data.save()
    context = {'cat_slug': cat_slug, 'pwev_slug': pwev_slug}
    context['posts'] = Icon.objects.get(cat_slug=str(cat_slug), id_icon=int(pwev_slug))
    return render(request, 'wcapi/p_icons_cat_slug.html', context)


@login_required(login_url='/admin/')
def icons_add_category(request):  # HttpRequest
    if request.method == 'POST':

        form = ResumeFormIcons(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = Icons.objects.all()
            context = {'contact': context}
            return render(request, 'wcapi/icons.html', context)

    return render(request, 'wcapi/icons_add_category.html')


@login_required(login_url='/admin/')
def icons(request):  # HttpRequest
    context = Icons.objects.all()
    context = {'contact': context}
    return render(request, 'wcapi/icons.html', context)


@login_required(login_url='/admin/')
def wallpapers_add_category(request):  # HttpRequest
    if request.method == 'POST':

        form = ResumeFormWallpapers(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = Wallpapers.objects.all()
            context = {'contact': context}
            return render(request, 'wcapi/wallpapers.html', context)

    return render(request, 'wcapi/wallpapers_add_category.html')


@login_required(login_url='/admin/')
def wallpapers(request):  # HttpRequest
    context = Wallpapers.objects.all()
    context = {'contact': context}
    return render(request, 'wcapi/wallpapers.html', context)


@login_required(login_url='/admin/')
def widgetslock(request):  # HttpRequest
    context = WidgetsLock.objects.all()
    context = {'contact': context}
    return render(request, 'wcapi/widgetslock.html', context)


@login_required(login_url='/admin/')
def widgetshome(request):  # HttpRequest
    context = WidgetsHome.objects.all()
    context = {'contact': context}
    return render(request, 'wcapi/widgetshome.html', context)


@login_required(login_url='/admin/')
def widgetslock_add_category(request):  # HttpRequest
    if request.method == 'POST':

        form = ResumeWidgetsLock(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = WidgetsLock.objects.all()
            context = {'contact': context}
            return render(request, 'wcapi/widgetslock.html', context)

    return render(request, 'wcapi/widgetslock_add_category.html')


@login_required(login_url='/admin/')
def widgetslock_del_category(request, cat_slug):  # HttpRequest
    WidgetsLock.objects.filter(id_Widgets=int(cat_slug)).delete()
    context = WidgetsLock.objects.all()
    context = {'contact': context}

    return render(request, 'wcapi/widgetslock.html', context)


@login_required(login_url='/admin/')
def widgetshome_del_category(request, cat_slug):  # HttpRequest
    WidgetsHome.objects.filter(id_Widgets=int(cat_slug)).delete()
    context = WidgetsHome.objects.all()
    context = {'contact': context}

    return render(request, 'wcapi/widgetshome.html', context)


@login_required(login_url='/admin/')
def widgetslock_add_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}

    if request.method == 'POST':
        if 'premium' in request.POST:
            form = ResumeWidgetsLockSlugPremium(request.POST, request.FILES)
            if form.is_valid():
                new_con = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_con.id_Widgets}
                context['posts'] = WidgetsLockS.objects.get(cat_slug=str(cat_slug), id_Widgets=int(new_con.id_Widgets))
                return render(request, 'wcapi/p_widgetslock_cat_slug.html', context)
        else:
            form = ResumeWidgetsLockSlug(request.POST, request.FILES)
            if form.is_valid():
                new_con = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_con.id_Widgets}
                context['posts'] = WidgetsLockS.objects.get(cat_slug=str(cat_slug), id_Widgets=int(new_con.id_Widgets))
                return render(request, 'wcapi/p_widgetslock_cat_slug.html', context)

    return render(request, 'wcapi/widgetslock_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def edit_widgetslock_cat_slug(request, cat_slug, pwev_slug):
    context = {'cat_slug': cat_slug}

    if request.method == 'POST':
        if 'premium' in request.POST:
            form = ResumeWidgetsLockSlugPremium(request.POST, request.FILES)
            if form.is_valid():
                WidgetsLockS.objects.filter(cat_slug=int(cat_slug), id_Widgets=int(pwev_slug)).delete()
                form.save()
        else:
            form = ResumeWidgetsLockSlug(request.POST, request.FILES)
            if form.is_valid():
                WidgetsLockS.objects.filter(cat_slug=int(cat_slug), id_Widgets=int(pwev_slug)).delete()
                form.save()

    return render(request, 'wcapi/widgetslock_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def edit_widgetshomep_cat_slug(request, cat_slug, pwev_slug):
    context = {'cat_slug': cat_slug}

    if request.method == 'POST':
        if 'premium' in request.POST:
            form = ResumeWidgetsHomeSlugPremium(request.POST, request.FILES)
            if form.is_valid():
                WidgetsHomeH.objects.filter(cat_slug=int(cat_slug), id_Widgets=int(pwev_slug)).delete()
                form.save()
        else:
            form = ResumeWidgetsHomeSlug(request.POST, request.FILES)
            if form.is_valid():
                WidgetsHomeH.objects.filter(cat_slug=int(cat_slug), id_Widgets=int(pwev_slug)).delete()
                form.save()

    return render(request, 'wcapi/widgetshome_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def del_p_widgetslock_cat_slug(request, cat_slug, pwev_slug):
    WidgetsLockS.objects.filter(cat_slug=int(cat_slug), id_Widgets=int(pwev_slug)).delete()
    context = {'cat_slug': cat_slug}
    context['posts'] = WidgetsLockS.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/widgetslock_cat_slug.html', context)


@login_required(login_url='/admin/')
def p_widgetslock_cat_slug(request, cat_slug, pwev_slug):
    if request.method == 'POST':
        data = WidgetsLockS.objects.get(cat_slug=str(cat_slug), id_Widgets=int(pwev_slug))
        if data.is_publish == 'on':
            data.is_publish = 'off'
        else:
            data.is_publish = 'on'
        if 'premium' in request.POST:
            data.premium = 'on'
        else:
            data.premium = 'off'
        data.save()
    context = {'cat_slug': cat_slug, 'pwev_slug': pwev_slug}
    context['posts'] = WidgetsLockS.objects.get(cat_slug=str(cat_slug), id_Widgets=int(pwev_slug))
    return render(request, 'wcapi/p_widgetslock_cat_slug.html', context)


@login_required(login_url='/admin/')
def p_widgetshomep_cat_slug(request, cat_slug, pwev_slug):
    if request.method == 'POST':
        data = WidgetsHomeH.objects.get(cat_slug=str(cat_slug), id_Widgets=int(pwev_slug))
        if data.is_publish == 'on':
            data.is_publish = 'off'
        else:
            data.is_publish = 'on'
        if 'premium' in request.POST:
            data.premium = 'on'
        else:
            data.premium = 'off'
        data.save()
    context = {'cat_slug': cat_slug, 'pwev_slug': pwev_slug}
    context['posts'] = WidgetsHomeH.objects.get(cat_slug=str(cat_slug), id_Widgets=int(pwev_slug))
    return render(request, 'wcapi/p_widgetshomep_cat_slug.html', context)


@login_required(login_url='/admin/')
def del_p_widgetshome_cat_slug(request, cat_slug, pwev_slug):
    WidgetsHomeH.objects.filter(cat_slug=int(cat_slug), id_Widgets=int(pwev_slug)).delete()
    context = {'cat_slug': cat_slug}
    context['posts'] = WidgetsHomeH.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/widgetshome_cat_slug.html', context)


@login_required(login_url='/admin/')
def widgetshome_add_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}

    if request.method == 'POST':
        if 'premium' in request.POST:
            form = ResumeWidgetsHomeSlugPremium(request.POST, request.FILES)
            if form.is_valid():
                new_con = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_con.id_Widgets}
                context['posts'] = WidgetsHomeH.objects.get(cat_slug=str(cat_slug), id_Widgets=int(new_con.id_Widgets))
                return render(request, 'wcapi/p_widgetshomep_cat_slug.html', context)
        else:
            form = ResumeWidgetsHomeSlug(request.POST, request.FILES)
            if form.is_valid():
                new_con = form.save()
                context = {'cat_slug': cat_slug, 'pwev_slug': new_con.id_Widgets}
                context['posts'] = WidgetsHomeH.objects.get(cat_slug=str(cat_slug), id_Widgets=int(new_con.id_Widgets))
                return render(request, 'wcapi/p_widgetshomep_cat_slug.html', context)

    return render(request, 'wcapi/widgetshome_add_cat_slug.html', context)


@login_required(login_url='/admin/')
def widgetslock_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}
    context['posts'] = WidgetsLockS.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/widgetslock_cat_slug.html', context)


@login_required(login_url='/admin/')
def widgetshome_add_category(request):  # HttpRequest
    if request.method == 'POST':

        form = ResumeWidgetsHome(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = WidgetsHome.objects.all()
            context = {'contact': context}
            return render(request, 'wcapi/widgetshome.html', context)

    return render(request, 'wcapi/widgetshome_add_category.html')


@login_required(login_url='/admin/')
def widgetshome_cat_slug(request, cat_slug):
    context = {'cat_slug': cat_slug}
    context['posts'] = WidgetsHomeH.objects.filter(cat_slug=str(cat_slug))
    return render(request, 'wcapi/widgetshome_cat_slug.html', context)


# widgetslock_add_cat_slug

class ThemesAPIView(APIView):
    def get(self, request):
        context = Theme.objects.all()
        serializer = ThemeSerializer(context, many=True)
        context = {'contact': serializer.data}
        return Response({'themes': context})


class ThemesAddCategoryAPIView(APIView):
    def post(self, request):
        post_new = Themes.objects.create(
            category=request.data['category'],
            amount=request.data['amount'],
            file=request.data['file'],
        )
        return Response({'comp': model_to_dict(post_new)})


class ThemesDelCategoryAPIView(APIView):
    def post(self, request):
        Themes.objects.filter(id_themes=int(request.data['id_themes'])).delete()
        return Response({'comp': 'del'})


class ThemesCatSlugAPIView(APIView):
    def post(self, request):
        context = Themes.objects.filter(cat_slug=str(request.data['id_themes'])).values()
        context = {'contact': context}
        return Response({'themes': context})


class ThemesAddCatSlugAPIView(APIView):
    def post(self, request):
        post_new = Theme.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            icons=request.data['icons'],
            wallpaper=request.data['wallpaper'],
            widgets=request.data['widgets'],
            cat_slug=request.data['cat_slug'],
        )
        return Response({'comp': model_to_dict(post_new)})


class ThemespDelCatPweAPIView(APIView):
    def post(self, request):
        Theme.objects.filter(id_theme=int(request.data['id_theme']), cat_slug=str(request.data['cat_slug'])).delete()
        return Response({'comp': 'del'})


class ThemespCatPweAPIView(APIView):
    def post(self, request):
        context = Theme.objects.filter(id_theme=int(request.data['id_theme']),
                                       cat_slug=str(request.data['cat_slug'])).values()
        context = {'contact': context}
        return Response({'comp': context})


class ThemespEditCatPweAPIView(APIView):

    def post(self, request):
        post_new = Theme.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            icons=request.data['icons'],
            wallpaper=request.data['wallpaper'],
            widgets=request.data['widgets'],
            cat_slug=request.data['cat_slug'],
        )
        Theme.objects.filter(id_theme=int(request.data['id_theme']), cat_slug=str(request.data['cat_slug'])).delete()

        return Response({'comp': model_to_dict(post_new)})


class IconsAPIView(APIView):
    def get(self, request):
        context = Icon.objects.all()
        serializer = IconSerializer(context, many=True)
        context = {'contact': serializer.data}
        return Response({'icons': context})


class IconsAddCategoryAPIView(APIView):
    def post(self, request):
        post_new = Icons.objects.create(
            category=request.data['category'],
            amount=request.data['amount'],
            file=request.data['file'],
        )
        return Response({'comp': model_to_dict(post_new)})


class IconsDelCategoryAPIView(APIView):
    def post(self, request):
        Icons.objects.filter(id_icons=int(request.data['id_icons'])).delete()
        return Response({'comp': 'del'})


class IconsCatSlugAPIView(APIView):
    def post(self, request):
        context = Icons.objects.filter(cat_slug=str(request.data['id_icons'])).values()
        context = {'contact': context}
        return Response({'icons': context})


class IconsAddCatSlugAPIView(APIView):
    def post(self, request):
        post_new = Icon.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            icons=request.data['icons'],
            wallpaper=request.data['wallpaper'],
            cat_slug=request.data['cat_slug'],
        )
        return Response({'comp': model_to_dict(post_new)})


class IconspDelCatPweAPIView(APIView):
    def post(self, request):
        Icon.objects.filter(id_icon=int(request.data['id_icon']), cat_slug=str(request.data['cat_slug'])).delete()
        return Response({'comp': 'del'})


class IconspCatPweAPIView(APIView):
    def post(self, request):
        context = Icon.objects.filter(id_icon=int(request.data['id_icon']),
                                      cat_slug=str(request.data['cat_slug'])).values()
        context = {'contact': context}
        return Response({'comp': context})


class IconspEditCatPweAPIView(APIView):
    def post(self, request):
        post_new = Icon.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            icons=request.data['icons'],
            wallpaper=request.data['wallpaper'],
            cat_slug=request.data['cat_slug'],
        )
        Icon.objects.filter(id_icon=int(request.data['id_icon']), cat_slug=str(request.data['cat_slug'])).delete()

        return Response({'comp': model_to_dict(post_new)})


class WidgetsLockAPIView(APIView):
    def get(self, request):
        context = WidgetsLockS.objects.all().values()
        context = {'contact': context}
        return Response({'widgetslock': context})


class WidgetsLockAddCategoryAPIView(APIView):
    def post(self, request):
        post_new = WidgetsLock.objects.create(
            category=request.data['category'],
            amount=request.data['amount'],
            file=request.data['file'],
        )
        return Response({'comp': model_to_dict(post_new)})


class WidgetsLockDelCategoryAPIView(APIView):
    def post(self, request):
        WidgetsLock.objects.filter(id_Widgets=int(request.data['id_Widgets'])).delete()
        return Response({'comp': 'del'})


class WidgetsLockCatSlugAPIView(APIView):
    def post(self, request):
        context = WidgetsLock.objects.filter(cat_slug=str(request.data['id_Widgets'])).values()
        context = {'contact': context}
        return Response({'widgetslock': context})


class WidgetsLockAddCatSlugAPIView(APIView):
    def post(self, request):
        post_new = WidgetsLockS.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            widgets=request.data['widgets'],
            cat_slug=request.data['cat_slug'],
        )
        return Response({'comp': model_to_dict(post_new)})


class WidgetsLockDelCatPweAPIView(APIView):
    def post(self, request):
        WidgetsLockS.objects.filter(id_Widgets=int(request.data['id_Widgets']),
                                    cat_slug=str(request.data['cat_slug'])).delete()
        return Response({'comp': 'del'})


class WidgetsLockCatPweAPIView(APIView):
    def post(self, request):
        context = WidgetsLockS.objects.filter(id_Widgets=int(request.data['id_Widgets']),
                                              cat_slug=str(request.data['cat_slug'])).values()
        context = {'contact': context}
        return Response({'comp': context})


class WidgetsLockEditCatPweAPIView(APIView):
    def post(self, request):
        post_new = WidgetsLockS.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            widgets=request.data['widgets'],
            cat_slug=request.data['cat_slug'],
        )
        WidgetsLockS.objects.filter(id_Widgets=int(request.data['id_Widgets']),
                                    cat_slug=str(request.data['cat_slug'])).delete()

        return Response({'comp': model_to_dict(post_new)})


class WidgetsHomeAPIView(APIView):
    def get(self, request):
        context = WidgetsHomeH.objects.all().values()
        context = {'contact': context}
        return Response({'widgetshome': context})


class WidgetsHomeAddCategoryAPIView(APIView):
    def post(self, request):
        post_new = WidgetsHome.objects.create(
            category=request.data['category'],
            amount=request.data['amount'],
            file=request.data['file'],
        )
        return Response({'comp': model_to_dict(post_new)})


class WidgetsHomeDelCategoryAPIView(APIView):
    def post(self, request):
        WidgetsHome.objects.filter(id_Widgets=int(request.data['id_Widgets'])).delete()
        return Response({'comp': 'del'})


class WidgetsHomeCatSlugAPIView(APIView):
    def post(self, request):
        context = WidgetsHome.objects.filter(cat_slug=str(request.data['id_Widgets'])).values()
        context = {'contact': context}
        return Response({'widgetshome': context})


class WidgetsHomeAddCatSlugAPIView(APIView):
    def post(self, request):
        post_new = WidgetsHomeH.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            widgets=request.data['widgets'],
            cat_slug=request.data['cat_slug'],
        )
        return Response({'comp': model_to_dict(post_new)})


class WidgetsHomeDelCatPweAPIView(APIView):
    def post(self, request):
        WidgetsHomeH.objects.filter(id_Widgets=int(request.data['id_Widgets']),
                                    cat_slug=str(request.data['cat_slug'])).delete()
        return Response({'comp': 'del'})


class WidgetsHomeCatPweAPIView(APIView):
    def post(self, request):
        context = WidgetsHomeH.objects.filter(id_Widgets=int(request.data['id_Widgets']),
                                              cat_slug=str(request.data['cat_slug'])).values()
        context = {'contact': context}
        return Response({'comp': context})


class WidgetsHomeEditCatPweAPIView(APIView):
    def post(self, request):
        post_new = WidgetsHomeH.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            widgets=request.data['widgets'],
            cat_slug=request.data['cat_slug'],
        )
        WidgetsHomeH.objects.filter(id_Widgets=int(request.data['id_Widgets']),
                                    cat_slug=str(request.data['cat_slug'])).delete()

        return Response({'comp': model_to_dict(post_new)})


class WallpapersAPIView(APIView):
    def get(self, request):
        context = Wallpaper.objects.all().values()
        context = {'contact': context}
        return Response({'Wallpapers': context})


class WallpapersAddCategoryAPIView(APIView):
    def post(self, request):
        post_new = Wallpapers.objects.create(
            category=request.data['category'],
            amount=request.data['amount'],
            file=request.data['file'],
        )
        return Response({'comp': model_to_dict(post_new)})


class WallpapersDelCategoryAPIView(APIView):
    def post(self, request):
        Wallpapers.objects.filter(id_wallpapers=int(request.data['id_wallpapers'])).delete()
        return Response({'comp': 'del'})


class WallpapersCatSlugAPIView(APIView):
    def post(self, request):
        context = Wallpapers.objects.filter(cat_slug=str(request.data['id_wallpapers'])).values()
        context = {'contact': context}
        return Response({'Wallpapershome': context})


class WallpapersAddCatSlugAPIView(APIView):
    def post(self, request):
        post_new = Wallpaper.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            wallpaper=request.data['wallpaper'],
            cat_slug=request.data['cat_slug'],
        )
        return Response({'comp': model_to_dict(post_new)})


class download_file(APIView):
    def post(self, request):
        # Получаем имя файла, которое мы хотим скачать, из POST запроса
        filename = request.data['filename']

        # Проверяем, существует ли файл
        if not os.path.exists(filename):
            return Response({'error': f'File {filename} not found'})

        with open(filename, 'rb') as f:
            response = FileResponse(f.read())
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response


class WallpapersDelCatPweAPIView(APIView):
    def post(self, request):
        Wallpaper.objects.filter(id_wallpapers=int(request.data['id_wallpapers']),
                                 cat_slug=str(request.data['cat_slug'])).delete()
        return Response({'comp': 'del'})


class WallpapersCatPweAPIView(APIView):
    def post(self, request):
        context = Wallpaper.objects.filter(id_wallpapers=int(request.data['id_wallpapers']),
                                           cat_slug=str(request.data['cat_slug'])).values()
        context = {'contact': context}
        return Response({'comp': context})


class WallpapersEditCatPweAPIView(APIView):
    def post(self, request):
        post_new = Wallpaper.objects.create(
            premium=request.data['premium'],
            name=request.data['name'],
            preview=request.data['preview'],
            wallpaper=request.data['wallpaper'],
            cat_slug=request.data['cat_slug'],
        )
        Wallpaper.objects.filter(id_wallpapers=int(request.data['id_wallpapers']),
                                 cat_slug=str(request.data['cat_slug'])).delete()

        return Response({'comp': model_to_dict(post_new)})


class ConfigFileAPIView(APIView):
    serializer_class = MobileConfigSerializer

    @staticmethod
    def clean_old_files():
        from datetime import timedelta
        current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
        old_files = MobileConfig.objects.filter(created_time__lt=current_time - timedelta(minutes=10))
        for old_file in old_files:
            if os.path.exists(old_file.file.path):
                os.remove(old_file.file.path)
            old_file.delete()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.clean_old_files()

            mobile_config_instance = serializer.save()
            url = reverse('get_config_file_path', kwargs={'file_uuid': mobile_config_instance.uuid})
            absolute_url = request.build_absolute_uri(url)
            return Response({'file_url': absolute_url})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetConfigFileAPIView(APIView):
    def get(self, request, file_uuid: str):
        from datetime import timedelta
        needed_file = MobileConfig.objects.get(uuid=file_uuid)
        current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
        if (needed_file.created_time + timedelta(minutes=10)) > current_time:
            return FileResponse(needed_file.file)
        else:
            if os.path.exists(needed_file.file.path):
                os.remove(needed_file.file.path)

            needed_file.delete()

            return Response(status=status.HTTP_404_NOT_FOUND)
