from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CoverForm
from PIL import Image, ImageFont, ImageDraw


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            form.cleaned_data  # 이미지를 생성할 데이터는 여기 있다.
    else:
        form = CoverForm()
    return render(request, "cover/index.html", {
        'form': form,
    })


def image_generator(request):
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']

    im = Image.new('RGB', (256, 256), 'white')

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    # 여기서 데이터를 받아서 그리겠습니다.
    fnt = ImageFont.truetype(ttf_path, 40)
    d = ImageDraw.Draw(im)

    d.text((10, 10), title, font=fnt, fill=(0, 255, 0, 128))
    d.text((10, 60), top_text, font=fnt, fill=(0, 255, 0, 255))
    d.text((10, 100), author, font=fnt, fill=(0, 255, 0, 255))


    response = HttpResponse(content_type='image/png')  # file-like
    im.save(response, format='png')
    return response
