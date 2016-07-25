# -*- coding: utf-8 -*-
"""Modul for Views of RMS."""

# Externe Imports
import os
from PIL import Image
# Django Imports
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponseRedirect
# Eigene Imports
from RMS import settings
from rms_app.forms import GerichtsFormular
from rms_app.models import Gericht, Kategorie


@login_required(login_url='/login_user/')
def bearbeite_gericht(request, gericht_id):
    """
    Ermoeglicht es das Gericht zu bearbeiten.
    :param request:
    :param gericht_id:
    :return:
    """
    gewaehltes_gericht = Gericht.objects.get(pk=gericht_id)
    if request.method == 'POST':
        photo_wurde_geaendert = False
        if wurde_neues_bild_hochgeladen(request) is not False:
            photo_wurde_geaendert = True
            form = GerichtsFormular(request.POST, request.FILES, instance=gewaehltes_gericht)
        else:
            path = gib_pfad('rms_app/static/rms_app/photos/{0}.jpg'.format(gericht_id))
            form = GerichtsFormular(request.POST, instance=gewaehltes_gericht, initial={'photo': Image.open(path)})
        if form.is_valid():
            form.save()
            if photo_wurde_geaendert:
                loesche_bild(gericht_id)
                lade_photo_hoch(request.FILES['photo'], gericht_id)
        else:
            return render(request, 'gericht_erstellen.html', {'form': form, 'bearbeiten': gewaehltes_gericht.pk})
        return HttpResponseRedirect(reverse('controll_center'))
    elif request.method == 'GET':
        form = GerichtsFormular(instance=gewaehltes_gericht)
        return render(request, 'gericht_erstellen.html', {'form': form, 'bearbeiten': gewaehltes_gericht.pk})


@login_required(login_url='/login_user/')
def controll_center(request):
    """
    Zeigt die Seite Controll-Center an.
    :param request:
    :return:
    """
    gerichte = Gericht.objects.all()
    return render(request, 'controll_center.html', {'gerichte': gerichte})


def uebersicht(request):
    """
    Zeigt eine Übersicht aller eingetragenen Rezepte/Gerichte.
    :param request:
    :return:
    """
    try:
        Gericht.objects.get(pk=1)
        Gericht.objects.get(pk=2)
        Gericht.objects.get(pk=3)

    except:
        try:
            # Erstelle Kategorie
            vorspeise = Kategorie(kategorie_name="Vorspeise")
            vorspeise.save()
            hauptgericht = Kategorie(kategorie_name="Hauptgericht")
            hauptgericht.save()

            # Erstelle Gruppen
            g_editor = Group(name="editor")
            g_editor.save()
            g_benutzer = Group(name="benutzer")
            g_benutzer.save()

            # Erstelle Admin
            superuser = User.objects.create_superuser(username='superuser',
                                                      first_name="vorname_superuser",
                                                      last_name="nachname_superusert",
                                                      password='12345',
                                                      email="test@web.de")
            superuser.save()

            # Erstellung eines Editors
            editor = User.objects.create_user(username='editor',
                                            first_name="vorname_superuser",
                                            last_name="nachname_superusert",
                                            password='12345',
                                            email="test@web.de")
            editor.save()

            # Weise Gruppe zu
            g_editor.user_set.add(editor)

            # Erstelle initial 3 Gerichte
            gericht = Gericht.objects.create(kategorie=hauptgericht, gericht_name="Spaghetti",
                                             beschreibung=" hier kann vieel blalabla stehen Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel auguuris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam. Pellentesque ut neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. In ac felis quis tortor malesuada pretium. Pellentesque auctor neque nec urna. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Aenean viverra rhoncus pede. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut non enim eleifend felis pretium feugiat. Vivamus quis mi. Phasellus a est. Phasellus magna. In hac habitasse platea dictumst. Curabitur at lacus ac velit ornare lobortis. Curabitur a felis in nunc fringilla tristique. Morbi mattis ullamcorper velit. Phasellus gravida semper nisi. Nullam vel sem. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Sed hendrerit. Morbi ac felis.")
            gericht.save()
            gericht = Gericht.objects.create(kategorie=vorspeise, gericht_name="Pizzaaaa",
                                             beschreibung=" hier kann vieel pizza blalabla stehen Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. s. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. In ac felis quis tortor malesuada pretium. Pellentesque auctor neque nec urna. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Aenean viverra rhoncus pede. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut non enim eleifend felis pretium feugiat. Vivamus quis mi. Phasellus a est. Phasellus magna. In hac habitasse platea dictumst. Curabitur at lacus ac velit ornare lobortis. Curabitur a felis in nunc fringilla tristique. Morbi mattis ullamcorper velit. Phasellus gravida semper nisi. Nullam vel sem. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Sed hendrerit. Morbi ac felis.")
            gericht.save()
            gericht = Gericht.objects.create(gericht_name="Fisch mit Spinat", kategorie=vorspeise,
                                             beschreibung=" hier Fisch kochen und fertig blalabla stehen Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et . Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdie feugiat. Vivamus quis mi. Phasellus a est. Phasellus magna. In hac habitasse platea dictumst. Curabitur at lacus ac velit ornare lobortis. Curabitur a felis in nunc fringilla tristique. Morbi mattis ullamcorper velit. Phasellus gravida semper nisi. Nullam vel sem. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Sed hendrerit. Morbi ac felis.")
            gericht.save()
        except:
            pass

    gerichte = Gericht.objects.all()
    return render(request, 'main.html', {'gerichte': gerichte})


@login_required(login_url='/login_user/')
def erstelle_gericht(request):
    """
    Zeigt ein Formular zur Gerichterstellung an Erstell und ermoeglicht es das neue Gericht zu speichern.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = GerichtsFormular(request.POST, request.FILES)
        if form.is_valid():
            aktuelles_gericht = form.save(commit=True)
            lade_photo_hoch(request.FILES['photo'], aktuelles_gericht.pk)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'gericht_erstellen.html', {'form': form})
    else:
        form = GerichtsFormular()
        return render(request, 'gericht_erstellen.html', {'form': form})


def gib_pfad(inner_path):
    """
    Gibt den gesamten Pfad zum uebergebenen internen Pfad.
    :param inner_path:
    :return:
    """
    return os.path.join(settings.BASE_DIR, inner_path)


def lade_photo_hoch(f, anzahl):
    """
    Laedt Photo hoch.
    :param f:
    :param anzahl:
    :return:
    """
    path = 'rms_app/static/rms_app/photos/{0}.jpg'.format(anzahl)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def loesche_bild(gericht_id):
    """
    Loescht das Bild zur uebergebenen ID.
    :param gericht_id:
    :return:
    """
    inner_path = 'rms_app/static/rms_app/photos/{0}.jpg'.format(gericht_id)
    os.remove(gib_pfad(inner_path))


@login_required(login_url='/login_user/')
def loesche_gericht(request, gericht_id):
    """
    Loescht das Gericht mit Bild.
    :param request:
    :param gericht_id:
    :return:
    """
    gewaehltes_gericht = Gericht.objects.get(pk=gericht_id)
    loesche_bild(gericht_id)
    gewaehltes_gericht.delete()
    return HttpResponseRedirect(reverse('controll_center'))


def login_user(request):
    """
    Zeigt ANmeldeform an und Ueberprueft ggf. die uebermittelten Anmeldeinformationen und loggt den Nutzer ggf. ein.
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('controll_center'))
            else:
                return render(request, 'login.html', {'error': 'Nutzer ist nicht aktiv'})
        else:
            return render(request, 'login.html', {'error': 'Die Anmeldeinformationen sind falsch'})
    elif request.method == "GET":
        return render(request, 'login.html')


def wurde_neues_bild_hochgeladen(request):
    """
    Gibt zurueck ob ein neues Bild hochgeladen wurde.
    :param request:
    :return:
    """
    return bool(request.FILES.get('photo', False))


def zeige_gericht(request, gericht_id):
    """
    Zeigt alle Informationen für ein spezielles Gericht an.
    :param request:
    :param gericht_id:
    :return:
    """
    gericht = Gericht.objects.get(pk=gericht_id)
    return render(request, 'gericht.html', {'gericht': gericht})


def zeige_kategorie(request, kategorie_id):
    """
    Zeigt alle Gerichte fuer die entsprechende Kategorie an.
    :param request:
    :param kategorie_id:
    :return:
    """
    ausgewaehlte_kategorie = Kategorie.objects.get(pk=kategorie_id)
    gerichte_in_kategorie = Gericht.objects.filter(kategorie=ausgewaehlte_kategorie)
    return render(request, 'kategorie.html', {'gerichte': gerichte_in_kategorie,
                                              'kategorie': ausgewaehlte_kategorie.kategorie_name})
