from django.shortcuts import render

# Create your views here.
def index_view(request):
    all_link=request.build_absolute_uri()
    context = {"all_link":all_link}
    return render(request, "djangoSocialShareWithNgrokApp/index.html", context)
