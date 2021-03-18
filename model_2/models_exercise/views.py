from django.shortcuts import render
from models_exercise.forms import NewUserForm


# Create your views here.
def index(request):
    return render(request, 'models_exercise/index.html')


# def users(request):
#     users_list = User.objects.order_by('last_name')
#     user_dictionary ={'user_records': users_list}
#     return render(request, 'models_exercise/users.html', context=user_dictionary)

def users(request):
    form = NewUserForm()
    if request.method == 'POST':  # this means if someone hit submit
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)  # commit data to the database
            return index(request)
        else:
            print('Error, form invalid')

    return render(request, 'models_exercise/users.html', {'form': form})
