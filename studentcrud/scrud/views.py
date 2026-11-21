from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from scrud.models import Student

# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        # return HttpResponse("Hello")
        return render(request,'index.html')

class AddStudentView(View):
    def get(self,request):
        # return HttpResponse("<h1>Add Student Details</h1>")
        return render(request,'add.html')
    def post(self,request):
        print(request.POST)
        print(request.FILES)
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        batch=request.POST.get('batch')
        em=request.POST.get('email')
        pic=request.FILES.get('picture')
        Student.objects.create(name=name,dob=dob,batch=batch,email=em,photo=pic)
        # return HttpResponse("POST hit")
        # return render(request,'studentlist.html')
        return redirect('list')

class ListStudentView(View):
    def get(self,request):
        # return HttpResponse("<h1>Add Student Details</h1>")
        student_list=Student.objects.all()
        contex={"data":student_list}
        # contex={"data":[]}
        return render(request,'studentlist.html',contex)

class StudentDeleteView(View):
    def get(self,request,**kwargs):
        sid=self.kwargs.get('sid')
        Student.objects.get(id=sid).delete()
        return redirect('list')