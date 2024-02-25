from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.



# this is the default home page for the elecions site
def index(request):

    return render(request, "polls/index.html")

# this is for the 'about' page found on the home page
def about(request):

    return render(request, "polls/about.html")

"""
this will redirect the user to the login page before 
allowing them to enter the polls site.
"""
@login_required(login_url="/user_auth/")

# This is the welcome page once the user logs in
def poll(request):
    
    print(request.user)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, "polls/poll.html", context)

# this view shows the user all the voting options for the chosen election
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

"""
this method checks to see if the user has logged in when they voted. 
if they are logged in then their answer is recorded.
if not then they are redirected to the login page.
"""
def vote(request, question_id):
    if not request.user.is_authenticated:
        return render(request, "user_auth/login.html")
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'elections/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully
        # dealing with POST data. This prevents data from being
        # posted twice if a
        # user hits the Back button.

        # this sends the user back to the elections home page after they vote
        return HttpResponseRedirect(
            reverse('polls:poll')
        )

