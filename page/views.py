from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from page.models import Comment,Instruction,User

# Create your views here.

#GET index request
def index(request):
    return HttpResponseRedirect('/home/')

#GET homepage request
def homePage(request):
    if request.session.get('logged_in'):
        currentUser = request.session.get('username')
        return render(request,'homepage.html',{"logged_in":True,"username":currentUser})
    return render(request,'homepage.html',{'logged_in':False,'username':''})

#GET submission request
def submission(request):
    if not request.session.get("logged_in"):
        return HttpResponseRedirect('/home/')
    return render(request,'submission.html')

#POST submission request
def acceptSubmission(request):
    newText = request.POST["instructions"]
    newTitle = request.POST["title"]
    currentUsername = request.session.get('username')
    try:
        currentUser = User.objects.get(username=currentUsername)
    except User.DoesNotExist:
        return HttpResponseRedirect('/home/')
    newInstruction = Instruction(title=newTitle,instructions=newText,
                                 author=currentUser,date=timezone.now(),
                                 rating=-1,)
    newInstruction.save()
    return HttpResponseRedirect('/home/')
    
#GET signup request
def signup(request):
    return render(request,'signup.html')

#POST signup request
def acceptSignup(request):
    newusername = request.POST["username"]
    newpassword = request.POST["pass"]
    newemail = request.POST["email"]
    newUser = User(username=newusername,password=newpassword,
                   email=newemail,dateJoined=timezone.now())
    newUser.save()
    return HttpResponseRedirect('/home/')

#GET login request
def login(request):
    return render(request,'login.html')

#POST login request
def acceptLogin(request):
    try:
        loginusername = request.POST["username"]
        loginpassword = request.POST["pass"]
    except: 
        return HttpResponseRedirect('/login/')
    try:
        user = User.objects.get(username=loginusername)
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=loginusername)
        except User.DoesNotExist:
            return HttpResponseRedirect('/login/')
    if user.password == loginpassword:
        request.session['logged_in'] = True
        request.session['username'] = user.username
    else:
        return HttpResponseRedirect('/login/')
    return HttpResponseRedirect('/home/')
    
#GET userpage request
def userpage(request,providedUsername=None):
    if providedUsername == None:
        return HttpResponseRedirect('/home/')
    else:
        try:
            creator = User.objects.get(username=providedUsername)
        except User.DoesNotExist:
            return HttpResponseRedirect('/home/')
        userInstructions = Instruction.objects.filter(author=creator)
    return render(request,'userpage.html',{"instructions":userInstructions,"user":creator})

#GET lessons request
def lessons(request):
    userInstructions = Instruction.objects.all()
    return render(request,'taught.html',{"instructions":userInstructions})
    

#GET instruction request
def instruction(request):
    try:
        elemid = request.GET['howtoid']
    except:
        return HttpResponseRedirect('/lessons/')
    try:
        instruction = Instruction.objects.get(pk=elemid)
    except Instruction.DoesNotExist:
        return HttpResponseRedirect('/lessons/')
    instructionText = instruction.instructions
    instructionTitle = instruction.title
    instructionAuthor = instruction.author.username
    instructionDate = instruction.date
    instructionRating = instruction.rating
    return render(request,'instruction.html',{"title":instructionTitle,
                                              "author":instructionAuthor,
                                              "text":instructionText,
                                              "date":instructionDate,
                                              "rating":instructionRating})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/home/')
