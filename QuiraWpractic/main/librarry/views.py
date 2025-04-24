from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,View
from .models import Author ,Library
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required ,permission_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view , APIView
from rest_framework.response import Response
import json
from rest_framework import serializers
from .serializers import LibrarySerializer


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        return super().form_valid(form)
    
#class AuthorList(ListView):
#    model = Author
#    template_name = 'author_list.html'
#    context_object_name = 'authors'


#@login_required(login_url='login/')
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['name', 'bio', 'date_of_birth', 'date_of_death']


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['name', 'bio', 'date_of_birth', 'date_of_death']


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author_list')


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {
            'form': form
        })
    def post(self,request):
        form=AuthenticationForm(data=request.POST)
        if not form.is_valid():
            return render(request,'login.html',{
                'form':form
            })
        user=form.get_user()
        login(request,user)
        return HttpResponse("you are logged in UwU")


class LogOut(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponse('You have logged out successfully.')
        else:
            return HttpResponse('You are not logged in.')


class HelloView(APIView):
    def get(self,request):
        return Response({'message':'Hello'})
    def post(self,request):
        if request.user.is_authenticated:
            return Response({'message':'you post something '})
        return Response({'message':'premison dinaide'})
    

def change_password(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first')


def user_list(requset):
    if requset.user.is_authenticated:
        authors=Author.objects.all()
        return render(requset,'author_list.html',{
            'authors':authors
        })
    return HttpResponse('your are not login')


@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if not request.user.check_password(old_password):
            return render(request, 'change_password.html', {'error': 'Wrong old password'})

        if new_password1 != new_password2:
            return render(request, 'change_password.html', {'error': 'Passwords do not match'})

        request.user.set_password(new_password1)
        request.user.save()

        return HttpResponse('pass has ben changed')
    return render(request, 'change_password.html')


@csrf_exempt
@api_view(['GET',"POST"])
def library_list_create(request):
    request.user.is_authenticated
    if request.method=="GET":
        librares=Library.objects.all()
        object_list=[]
        for library in librares:
            object_list.append({"id":library.id ,"number":library.number})
        return HttpResponse(object_list)
    if request.method=="POST":
        serializer=LibrarySerializer(data=request.data)
        #payload=json.load(request.body)
        #number=payload.get('number',None)
        #number=request.data('number',None)
        #if number is None:
        #    return HttpResponse('error number is not provided')
        if not serializer.is_valid():
            return Response(data=serializer.errors)
        #Library.objects.create(number=serializer.data['number'])
        serializer.save()
        return HttpResponse("library created")
    
    return HttpResponse('method not allowd ')


@csrf_exempt
@api_view(['GET','DELETE','PUT'])
def library_detail_update_delete(request,library_id):
    library=Library.objects.get(id=library_id)
    if request.method=='GET':
        serializer=LibrarySerializer(instance=library)
        serializer.data
        #response={'id':library.id,'number':library.number}
        #return HttpResponse(json.dump(response))
        return Response(data=serializer.data)
    if request.method=='DELETE':
        library.delete()
        return HttpResponse('library deleted')
    if request.method=='PUT':
        #payload=json.load(request.body)
        #number=payload.get('number',None)
        number=request.data.get('number',None)
        if number is None:
            return HttpResponse('error :number is not provided ')
        library.number=number
        library.save()
        return HttpResponse('library updated')
    return HttpResponse('method not allowed')

