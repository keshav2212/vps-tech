from django.shortcuts import render,redirect
from .models import Member
from django.contrib import messages
from django.http import HttpResponse
def per(mem):
	permission=[]
	if mem.add_member==True:
		permission.append("Add Member")
	if mem.delete_member==True:
		permission.append("Delete Member")
	if mem.all_member==True:
		permission.append("All Members")
	if mem.edit_user==True:
		permission.append("Edit Member")
	if mem.statics==True:
		permission.append("Statstics")
	return permission
def login(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['password']
		try:
			vuser=Member.objects.get(Email=email,Password=password)
			request.session['login']=True
			request.session['userid']=vuser.id
			request.session['Name']=vuser.Name
			return redirect('/')
		except:
			messages.error(request,"Invalid Credentials")
			return redirect('/')
	elif request.session.has_key('login'):  
		if request.session['login']==True: # it is to to check whether the admin is logged in or not. if he already loged in with in 24 hrs then go to the admin dashboard instead of login page 
			return redirect('/dashboard')
		else:
			return render(request,'home.html')
	else:
		return render(request,'home.html')
# Create your views here.
def logout(request):
	del request.session['login']
	request.session['login']=False
	request.session.set_expiry(0)
	return redirect('/')


def dashboard(request):
	if request.session.has_key('login'):
		if request.session['login']==True:
			name=request.session['Name']
			id1=request.session['userid']
			try:
				mem=Member.objects.get(pk=id1)
			except:
				logout(request)
				return redirect('/')
			permission=per(mem)
			image=mem.Profilepic;
			return render(request,"dashboard.html",{'name':name,'permission':permission,'image':image})
		else:
			return redirect('/')
	else:
		return redirect('/')

def add_member(request):
	permission=per(Member.objects.get(id=request.session['userid']))
	if request.method=="POST":
		name=request.POST['name']
		mobile=request.POST['mobile']
		email=request.POST['email']
		password=request.POST['password']
		department=request.POST['department']
		image=request.FILES['image']
		age=request.POST['age']
		address=request.POST['address']
		add = request.POST.get('add_member',False)
		delete = request.POST.get('delete_member',False)
		allm = request.POST.get('all_member',False)
		edit = request.POST.get('edit_member',False)
		statstics = request.POST.get('statstics',False)	
		mem=Member(Name=name,MobileNo=mobile,Email=email,Password=password,Department=department,Profilepic=image,Age=age,Address=address,add_member=add,delete_member=delete,all_member=allm,edit_user=edit,statics=statstics)
		mem.save()
		messages.success(request,"%s has been Registered Successfully"%name)
		return redirect('/')
	if request.session.has_key('login'):
		if request.session['login']==True:
			return render(request,'add_member.html',{"permission":permission,'name':request.session['Name']})
		else:
			return redirect('/')
	else:
		return redirect('/')



def delete_member(request):
	if request.session.has_key('login'):
		if request.session['login']==True:
			name=request.session['Name']
			id1=request.session['userid']
			mem=Member.objects.get(pk=id1)
			permission=per(mem)
			image=mem.Profilepic;
			mem1=Member.objects.all()
			return render(request,'delete_member.html',{'name':name,'permission':permission,'image':image,'mem':mem1})
		else:
			return redirect('/')
	else:
		return redirect('/')


def all_member(request):
	if request.session.has_key('login'):
		if request.session['login']==True:
			mem=Member.objects.all()
			permission=per(Member.objects.get(id=request.session['userid']))
			return render(request,'all_members.html',{'mem':mem,'name':request.session['Name'],'permission':permission})
		else:
			return redirect('/')
	else:
		return redirect('/')

def edit_member(request):
	if request.session.has_key('login'):
		if request.session['login']==True:
			mem=Member.objects.all()
			permission=per(Member.objects.get(id=request.session['userid']))
			return render(request,'edit_member.html',{'mem':mem,'permission':permission,'name':request.session['Name']})
		else:
			return redirect('/')
	else:
		return redirect('/')

def statics(request):
	if request.session.has_key('login'):
		if request.session['login']==True:
			n=Member.objects.all()
			count1=0
			for t in n:
				if (t.add_member==True) and (t.delete_member==True) and (t.all_member==True) and (t.edit_user==True) and (t.statics==True):
					count1=count1+1
			permission=per(Member.objects.get(id=request.session['userid']))
			return render(request,'statstics.html',{'name':request.session['Name'],'permission':permission,'len':count1,'len1':len(n)-count1,'mem':n})

		else:
			return redirect('/')
	else:
		return redirect('/')


def deletewithid(request,id1):
	mem=Member.objects.get(id=id1)
	name=mem.Name
	mem.delete()		
	messages.success(request,"%s Has been deleted Successfully."%name)
	return redirect('/dashboard')


def editwithid(request,id1):
	mem=Member.objects.filter(id=id1)
	if request.method=="POST":
		name=request.POST['name']
		mobile=request.POST['mobile']
		email=request.POST['email']
		password=request.POST.get('password',mem[0].Password)
		department=request.POST['department']
		age=request.POST['age']
		address=request.POST['address']
		add = request.POST.get('add_member',False)
		delete = request.POST.get('delete_member',False)
		allm = request.POST.get('all_member',False)
		edit = request.POST.get('edit_member',False)
		statstics = request.POST.get('statstics',False)	
		mem.update(Name=name,MobileNo=mobile,Email=email,Password=password,Department=department,Age=age,Address=address,add_member=add,delete_member=delete,all_member=allm,edit_user=edit,statics=statstics)
		return redirect('/dashboard')
	else:	
		return render(request,'edit_member_details.html',{'name':request.session['Name'],'mem':mem[0]})