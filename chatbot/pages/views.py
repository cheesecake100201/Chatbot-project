from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from .forms import SignUpForm, QueryForm
import random
from .models import Query, Conversation
import datetime
import pymongo
import openai
from pymongo import MongoClient
client = MongoClient('db', 27017)
db = client['conversation']
question = db.question
# Create your views here.
api_key = settings.OPENAI_API_KEY
openai.api_key = api_key
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid Username or Password')
    return render(request, "registration/login.html", {})

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('chat_login')
    else:
        form = SignUpForm()
    return render(request, "register.html", {"form": form})

def dashboard_view(request):
    return render(request, 'dashboard.html', {})


def query_view(request):
    user_id = request.user.id
    thirty_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=30)
    # print(queries)
    
    
    # if queries:
    #     conversation_obj = Conversation(request.user)
    #     conversation_obj.save()
    # else:
    #     conversation_obj = Conversation(request.user)
    #     conversation_obj.save()

    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            query_obj = form.save()
            queries = question.find({'created_at':{'$gte': thirty_minutes_ago}, "user_id": user_id})
            

            conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}]

            
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages=conversation
            )
            assistant_message = response['choices'][0]['message']['content']
            question.insert_one({
                'query': query,
                'reply': assistant_message,
                'created_at': datetime.datetime.now(),
                'user_id': user_id
            })

            query_obj.reply = assistant_message
            query_obj.save()
            document = question.find({"user_id": user_id}).sort([("_id", -1)]).limit(1)[0]
            if datetime.datetime.now() - document['created_at'] <= datetime.timedelta(minutes=30):
                return render(request, 'query.html', {"query_obj": query_obj, "queries": queries, "form": QueryForm()})
            return render(request, 'query.html', {"query_obj": query_obj, "form": QueryForm()})
    else:
        form = QueryForm()
    return render(request, 'query.html', {'form': form})

def view_conversation(request):
    user_id = request.user.id
    conversations = question.find({'user_id': user_id}).sort('created_at')

    context = {
        'conversations': conversations
    }
    return render(request, 'conversation.html', context)