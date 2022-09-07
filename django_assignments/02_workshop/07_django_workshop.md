1.

```python
def user_list(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/user_list.html', context)

```

![](C:\Users\LG\Desktop\ssafy\HWS_PRACTICE\django_assignments\02_workshop\07_django_workshop.assets\화면 캡처 2022-09-07 230242.png)



2.

```python
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

```

![](C:\Users\LG\Desktop\ssafy\HWS_PRACTICE\django_assignments\02_workshop\07_django_workshop.assets\화면 캡처 2022-09-07 230308-1662559784203-3.png)