# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from mysite import models, forms
from django.contrib import messages, auth
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
# Create your views here.


def index(request):
    HOME = True
    if request.user.is_authenticated:
        username = request.user.username

    messages.get_messages(request)
    polls = models.Poll.objects.filter(
        enabled=True).order_by('-created_at')[0:6]
    if len(polls) < 6:
        complement = [1]*(6-len(polls))
    return HttpResponse(render(request, '../templates/index.html', locals()))


def add_poll(request):
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        try:
            poll_title = request.POST.get("poll_title", None)
            poll_exp = request.POST.get("poll_explanation", None)
            # this makes file upload success
            poll_logo = request.FILES.get("poll_logo", None)
            if poll_title and poll_exp:
                usr = User.objects.get(username=username)
                new_poll = models.Poll.objects.create(user=usr, name=poll_title,
                                                      explination=poll_exp, poll_logo=poll_logo)
                new_poll.save()
                print(poll_title, poll_exp, 11)
                return redirect('add_poll_item', id = new_poll.id)
            else:
                print('lack something')

        except Exception as e:
            print(e)
            print('Fail to get post')
    return HttpResponse(render(request, '../templates/add_poll.html', locals()))

    messages.get_messages(request)
    polls = models.Poll.objects.all()
    return HttpResponse(render(request, '../templates/index.html', locals()))


def add_poll_item(request, id):

    # add a auto removing unenabled polls function
    unenabled_polls = models.Poll.objects.order_by(
        '-created_at').filter(enabled=False)
    for p in unenabled_polls:
        if (datetime.date.today() - p.created_at).days >= 2:
            p.delete()
            print('{} is deleted!'.format(p.name))
            print('**************')

    # handling variables
    if request.user.is_authenticated:
        username = request.user.username

    poll = models.Poll.objects.get(pk=id)

    if request.method == 'POST':
        poll_items = []
        for i in range(4):
            if request.POST.get("poll_item_{0}".format(i), None):
                poll_items.append(request.POST.get(
                    "poll_item_{0}".format(i), None))

        if len(poll_items) >= 2:
            for item in poll_items:
                new_item = models.PollItem.objects.create(poll=poll, name=item)
                new_item.save()

            poll.enabled = True
            poll.save()

            return redirect('show_poll', id = poll.id)

        else:
            message = '請至少填寫兩項投票項目！'
            return HttpResponse(render(request, '../templates/add_poll_item.html', locals()))

    return HttpResponse(render(request, '../templates/add_poll_item.html', locals()))


def show_poll(request, id):

    if request.user.is_authenticated:
        username = request.user.username
    poll = models.Poll.objects.get(pk=id)
    pollitems = models.PollItem.objects.filter(poll=poll)

    return HttpResponse(render(request, '../templates/show_poll.html', locals()))


def vote(request, pollid, pollitemid):

    if request.user.is_authenticated:
        username = request.user.username
    try:
        pollitem = models.PollItem.objects.get(id = pollitemid)
    except Exception as e:
        print(e)
        pollitem = None

    poll = models.Poll.objects.get(pk=pollid)
    VH = models.VoteHistory.objects.filter(poll=poll,voter=str(username)).order_by('vote_time')

    '''
    Each poll can only be voted for single user per day!
    '''
    if not VH or (datetime.date.today() - VH[0].vote_time).days > 0:
        if pollitem:
            pollitem.vote += 1
            v_history = models.VoteHistory.objects.create(poll=poll,pollitem = str(pollitem), voter=str(username))
            v_history.save()
            pollitem.save()
    else:
        print('You have voted for this poll!')

    target_url = '/show_poll/' + str(pollid)
    return HttpResponseRedirect(target_url)
