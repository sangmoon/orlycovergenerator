from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CoverForm
from PIL import Image


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            form.cleaned_data  # 이미지를 생성할 데이터는 여기 있다.
            return redirect("cover:index")
    else:
        form = CoverForm()
    return render(request, "cover/index.html", {
        'form': form,
    })


def image_generator(request):
    im = Image.new('RGB', (256,256), 'yellow')

    # 여기서 데이터를 받아서 그리겠습니다.
    response = HttpResponse(content_type='image/jpeg')
    im.save(response, format='JPEG')
    return response
