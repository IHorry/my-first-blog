from django.shortcuts import render, get_object_or_404
from .models import Post,CV,Skill,Work,Qual
from django.utils import timezone
from .forms import PostForm, CVForm, SkillForm,WorkForm,QualForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	skills  = Skill.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	workExp = Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	qualEd = Qual.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	my_CV = CV.objects.first()
	return render(request, 'blog/post_list.html', {'posts': posts, 'CV':my_CV, 'skills':skills,'workExp': workExp,'qualifications':qualEd})

@login_required
def post_remove(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		post.delete()
		return redirect('post_list')
	else:
		return redirect('post_list')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

@login_required
def CV_new(request):
    if request.method == "POST":
        form = CVForm(request.POST,request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.author = request.user
            cv.published_date = timezone.now()
            cv.save()
            return redirect('post_list')
    else:
        form = CVForm()
    return render(request, 'blog/cv_edit.html', {'form': form})

@login_required
def CV_edit(request):
    cv = CV.objects.first()
    skills  = Skill.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    workExp = Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    qualEd = Qual.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = CVForm(request.POST,request.FILES,instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.author = request.user
            cv.published_date = timezone.now()
            cv.save()
            return redirect('post_list')
    else:
        form = CVForm(instance=cv)
    return render(request, 'blog/cv_edit.html', {'form': form, 'skills':skills , 'workExp':workExp, 'qualifications':qualEd })

@login_required
def skills_new(request):
    cv= CV.objects.first()
    form = CVForm(request.POST,request.FILES,instance=cv)
    skills  = Skill.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    if request.method == "POST":
        skill_form = SkillForm(request.POST,request.FILES)
        if skill_form.is_valid():
            skill_form = skill_form.save(commit=False)
            skill_form.author = request.user
            skill_form.published_date = timezone.now()
            skill_form.save()
            return redirect('CV_edit')
    else:
        skill_form = SkillForm()
    return render(request, 'blog/skill_edit.html', {'form': form, 'skill_form': skill_form, "skills": skills,})

@login_required
def skill_edit(request,pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = SkillForm(request.POST,request.FILES,instance=skill)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.author = request.user
            skill.published_date = timezone.now()
            skill.save()
            return redirect('CV_edit')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'blog/skill_edit.html', {'skill_form': form})

@login_required
def skill_remove(request,pk):
	skill = get_object_or_404(Skill, pk=pk)
	if request.method == "POST":
		skill.delete()
		return redirect('CV_edit')
	else:
		return redirect('CV_edit')

@login_required
def work_new(request):
    cv= CV.objects.first()
    form = CVForm(request.POST,request.FILES,instance=cv)
    if request.method == "POST":
        work_form = WorkForm(request.POST,request.FILES)
        if work_form.is_valid():
            work_form = work_form.save(commit=False)
            work_form.author = request.user
            work_form.published_date = timezone.now()
            work_form.save()
            return redirect('CV_edit')
    else:
        work_form = WorkForm()
    return render(request, 'blog/work_edit.html', {'form': form, 'work_form': work_form})

@login_required
def work_edit(request,pk):
    work = get_object_or_404(Work, pk=pk)
    if request.method == "POST":
        form = WorkForm(request.POST,request.FILES,instance=work)
        if form.is_valid():
            work = form.save(commit=False)
            work.author = request.user
            work.published_date = timezone.now()
            work.save()
            return redirect('CV_edit')
    else:
        form = WorkForm(instance=work)
    return render(request, 'blog/work_edit.html', {'work_form': form})

@login_required
def work_remove(request,pk):
	work = get_object_or_404(Work, pk=pk)
	if request.method == "POST":
		work.delete()
		return redirect('CV_edit')
	else:
		return redirect('CV_edit')

@login_required
def qual_new(request):
    cv= CV.objects.first()
    form = CVForm(request.POST,request.FILES,instance=cv)
    if request.method == "POST":
        qual_form = QualForm(request.POST,request.FILES)
        if qual_form.is_valid():
            qual_form = qual_form.save(commit=False)
            qual_form.author = request.user
            qual_form.published_date = timezone.now()
            qual_form.save()
            return redirect('CV_edit')
    else:
        qual_form = QualForm()
    return render(request, 'blog/qual_edit.html', {'form': form, 'qual_form': qual_form})

@login_required
def qual_edit(request,pk):
    qual = get_object_or_404(Qual, pk=pk)
    if request.method == "POST":
        form = QualForm(request.POST,request.FILES,instance=qual)
        if form.is_valid():
            qual = form.save(commit=False)
            qual.author = request.user
            qual.published_date = timezone.now()
            qual.save()
            return redirect('CV_edit')
    else:
        form = QualForm(instance=qual)
    return render(request, 'blog/qual_edit.html', {'qual_form': form})

@login_required
def qual_remove(request,pk):
	qual = get_object_or_404(Qual, pk=pk)
	if request.method == "POST":
		qual.delete()
		return redirect('CV_edit')
	else:
		return redirect('CV_edit')