import datetime
from django.shortcuts import render, redirect
from .models import User, Produce
from .forms import UserInputForm
from django.template.defaulttags import register
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz, Question
from .forms import QuizForm
from .functions import GetQuizes, GetResponse, fetch_playlists,fetch_videos, getRelatedNews


@register.filter
def get_range(value):
    return range(value)

@register.filter
def index(indexable, i):
    return indexable[i]

def getDetailsFromUID(id):
    obj = User.objects.get(id=id)
    return obj

def e404_page(request):
    try:
        error_message = request.session["error_message"]
        return render(request, "dash/404.html", context={
            "errormsg" : error_message
        })
    except Exception as e:
        print(e)    
        return render(request, "dash/404.html")


def home_page(request):
    # try:              
    id = request.session["member_logged_id"]
    userlogged = getDetailsFromUID(id)
    quizzes = userlogged.quizes
    news = getRelatedNews(userlogged.subjectlist[0])
   
    qp = 0
    print(quizzes)
    marks={}
    i=0
    for quiz in quizzes:
        qp+=quizzes[quiz]
        marks.update({i:quizzes[quiz]})
        i+=1
    prog = 'no'
    if len(quizzes)==0:
        
     context = {
        "user": userlogged,
        "progress": prog,
        "quiz_count": len(quizzes), 
        "last_quiz": marks,
        "quizzes": quizzes,
        "news": news,
        "points": qp,
        "avg":0
    }
    else:
         context = {
        "user": userlogged,
        "progress": prog,
        "quiz_count": len(quizzes), 
        "last_quiz": marks,
        "quizzes": quizzes,
        "news": news,
        "points": qp,
        "avg":(qp/len(quizzes))
        
    }
   
    return render(request, 'dash/home.html', context)
    
def forum(request):
    try:
        return render(request, 'dash/forum.html')
    except Exception as e:
        print(e)
        request.session["error_message"] = "Please Login to Continue"
        return redirect((f'/admin/404/'))

def study_music(request):
    try:
        return render(request, 'dash/tools/study_music.html')
    except Exception as e:
        print(e)
        request.session["error_message"] = "Please Login to Continue"
        return redirect((f'/admin/404/'))
def timer(request):
    try:
        return render(request, 'dash/tools/timer.html')
    except Exception as e:
        print(e)
        request.session["error_message"] = "Please Login to Continue"
        return redirect((f'/admin/404/'))
# def news_page(request):
#     try:
#         logged_id = request.session["member_logged_id"]
#         userlogged = getDetailsFromUID(logged_id)

#         news = getRelatedNews()
#         context = {
#             'news': news,
#             'user': userlogged,
#             'userid': userlogged.id,
#         }
#         return render(request, 'dash/news.html', context)
#     except Exception as e:
#         print(e)
#         request.session["error_message"] = "Please Login to Continue"
#         return redirect((f'/admin/404/'))

# def fertrec(request):
#     try:
#         logged_id = request.session["member_logged_id"]
#         userlogged = getDetailsFromUID(logged_id)
        
#         if request.method == 'POST':
#             form = FertilizerPredictionForm(request.POST)
#             weatherd = getWeatherDetails(userlogged.coords)
#             if form.is_valid():
#                 nitrogen = form.cleaned_data['nitrogen']
#                 phosphorus = form.cleaned_data['phosphorus']
#                 potassium = form.cleaned_data['potassium']
#                 moisture = form.cleaned_data['moisture']
#                 soil_type = form.cleaned_data['soil_type']
#                 crop = form.cleaned_data['crop']
#                 temp = weatherd[1]
#                 humidity = weatherd[2]
#                 prediction = getFertilizerRecommendation(fertilizerRecommendModel, nitrogen, phosphorus, potassium, temp, humidity, moisture, soil_type, crop)
#                 context = {
#                     'form': form,
#                     'user': userlogged,
#                     'userid': userlogged.id,
#                     'prediction': prediction
#                 }
#         else:
#             form = FertilizerPredictionForm()
#             context = {
#                 "form": form,
#                 "user": userlogged,
#                 'userid': userlogged.id,
#             }

    #     return render(request, 'dash/tools/fert_rec.html', context)
    # except Exception as e:
    print(e)
    #     request.session["error_message"] = "Please Login to Continue"
    #     return redirect((f'/admin/404/'))


def help_page(request):
    try:
        logged_id = request.session["member_logged_id"]
        userlogged = getDetailsFromUID(logged_id)

        if request.method == 'POST':
            form = UserInputForm(request.POST)
            if form.is_valid():
                try:
                    existinglog = request.session["chatlog"]
                    del request.session['chatlog']
                except Exception as e:
                    print(e)
                    pass

                query = form.cleaned_data['userinput']
                res = GetResponse(query)
                try:
                    existinglog = request.session["chatlog"]
                    existinglog['queries'].append(query)
                    existinglog['responses'].append(res)
                    request.session['chatlog'] = existinglog

                except Exception as e:
                    print(e)
                    request.session["chatlog"] = {
                        'queries': [query],
                        'responses': [res]
                    }
                
                log = request.session["chatlog"]
                context = {
                    'userid': userlogged.id,
                    'user': userlogged,
                    'log' : log,
                    'form' : form,
                }

        else:
            form = UserInputForm()
            context={
                "userid": userlogged.id,
                'form': form,
                "user": userlogged,
            }

        return render(request, 'dash/help.html', context)
    except Exception as e:
        print(e)
        request.session["error_message"] = "Please Login to Continue"
        return redirect((f'/admin/404/'))

def profile_page(request):
    try:
        logged_id = request.session["member_logged_id"]
        userlogged = getDetailsFromUID(logged_id)

        context = {
            "userid": userlogged.id,
            "user": userlogged,
        }

        return render(request, 'dash/profile.html', context)
    except Exception as e:
        print(e)
        request.session["error_message"] = "Please Login to Continue"
        return redirect((f'/admin/404/'))

def logout_view(request):
    if request.session["member_logged_id"] != None:
        del request.session["member_logged_id"]
        return redirect('/')
    else:
        request.session["error_message"] = "You are not logged in yet."
        return redirect((f'/admin/404/'))

def learning_page(request):
    try:
        logged_id = request.session["member_logged_id"]
        userlogged = getDetailsFromUID(logged_id)
        
        #print(pl)

        context = {
            "userid": userlogged.id,
            "user": userlogged,
            #"playlist_data":pl
        }

        if request.method == 'POST':
            form = UserInputForm(request.POST)
            if form.is_valid():
                try:
                    existinglog = request.session["chatlog"]
                    del request.session['chatlog']
                except Exception as e:
                    print(e)
                    pass

                query = form.cleaned_data['userinput']
                pl = fetch_playlists(query)
                print(pl)
                context={
                "userid": userlogged.id,
                'form': form,
                "user": userlogged,
            }

                try:
                    return render(request, 'dash/learn.html', {'playlists': pl, "userid": userlogged.id,
                'form': form,
                "user": userlogged,})

                except Exception as e:
                    print(e)
                    request.session["chatlog"] = {
                        'queries': [query],
                        'responses': ['res']
                    }
                
                log = request.session["chatlog"]
                context = {
                    'userid': userlogged.id,
                    'user': userlogged,
                    'log' : log,
                    'form' : form,
                }

        else:
            form = UserInputForm()
            context={
                "userid": userlogged.id,
                'form': form,
                "user": userlogged,
            }

      
        return render(request, 'dash/learn.html', context)
    except Exception as e:
        print(e)
        request.session["error_message"] = "Please Login to Continue"
        return redirect((f'/admin/404/'))



def quiz_page(request):
    try:
        logged_id = request.session["member_logged_id"]
        userlogged = getDetailsFromUID(logged_id)
        
        #print(pl)

        context = {
            "userid": userlogged.id,
            "user": userlogged,
            #"playlist_data":pl
        }

        if request.method == 'POST':
            form = UserInputForm(request.POST)
            if form.is_valid():
                try:
                    existinglog = request.session["chatlog"]
                    del request.session['chatlog']
                except Exception as e:
                    print(e)
                    pass

                query = form.cleaned_data['userinput']
                pl = GetQuizes(20, query,query)
                print(pl)
                try:
                    return render(request, 'dash/quizzes.html', {'questions': pl})

                except Exception as e:
                    print(e)
                    request.session["chatlog"] = {
                        'queries': [query],
                        'responses': ['res']
                    }
                
                log = request.session["chatlog"]
                context = {
                    'userid': userlogged.id,
                    'user': userlogged,
                    'log' : log,
                    'form' : form,
                }

        else:
            form = UserInputForm()
            context={
                "userid": userlogged.id,
                'form': form,
                "user": userlogged,
            }

      
        return render(request, 'dash/quizzes.html', context)
    except Exception as e:
        print(e)
        request.session["error_message"] = "Please Login to Continue"
        return redirect((f'/admin/404/'))





def podcasts(request):
    try:
                logged_id = request.session["member_logged_id"]
                userlogged = getDetailsFromUID(logged_id)
        
                print(print(userlogged.subjects))

                context = {
            "userid": userlogged.id,
            "user": userlogged,
            #"playlist_data":pl
        }

        

                query = ((userlogged).subjects).split(',')
                pl=[]
                for i in query:
                    
                    pl+=fetch_videos(i)
                
                try:
                    return render(request, 'dash/podcasts.html', {'playlists': pl})

                except Exception as e:
                    print(e)
                    request.session["chatlog"] = {
                        'queries': [query],
                        'responses': ['res']
                    }
                
                log = request.session["chatlog"]
                

       
      
        
    except Exception as e:
        print(e)
        request.session["error_message"] = "Please Login to Continue"
        return redirect((f'/admin/404/'))



def quiz_view(request, quiz_id):

    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        id = request.session["member_logged_id"]
        userlogged = getDetailsFromUID(id)
        
        if form.is_valid():
            score = 0
            for question in questions:
                answer_id = form.cleaned_data[f'question_{question.id}']
                answer = question.answer_set.get(id=answer_id)
                if answer.is_correct:
                    score += 1
            quiz.score= score
            quizzes = Quiz.objects.all() 
            userlogged.quizes.update({quiz.title:score})
            userlogged.save()
            print(userlogged.quizes)
            return render(request, 'dash/quiz_list.html', {"message":f'You scored {score}/{questions.count()}!!', "quizzes":quizzes})

    else:
        form = QuizForm(questions=questions)

    return render(request, 'dash/quiz.html', {'quiz': quiz, 'form': form})


def quizzes_view(request):
    quizzes = Quiz.objects.all()  # Fetch all quizzes from the database
    return render(request, 'dash/quiz_list.html', {'quizzes': quizzes})


def logout_view(request):
    if request.session["member_logged_id"] != None:
        del request.session["member_logged_id"]
        return redirect('/')
    else:
        request.session["error_message"] = "You are not logged in yet."
        return redirect((f'/admin/404/'))

