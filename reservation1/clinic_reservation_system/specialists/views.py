from django.shortcuts import render, redirect
from .forms import SpecialistSignUpForm
from clinics.models import Review

def register_specialist(request):
    if request.method == 'POST':
        form = SpecialistSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_specialist = True
            user.save()
            # Logowanie użytkownika po rejestracji i przekierowanie do strony profilu
            return redirect('index')  # Zakładamy, że 'index' to strona główna
    else:
        form = SpecialistSignUpForm()
    return render(request, 'specialist/register.html', {'form': form})
def reviews_list(request):
    reviews = Review.objects.filter(specialist=request.user.specialist).order_by('-created_at')
    return render(request, 'specialists/reviews_list.html', {'reviews': reviews})
