from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CoverForm
from PIL import Image, ImageFont, ImageDraw
from .utils import COLOR_CODES


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
    animal_code = request.GET['animal_code']
    color_idx = int(request.GET['color_code'])
    guide_text = request.GET['guide_text']
    guide_text_placement = request.GET['guide_text_placement']

    animal_path = settings.ROOT('assets', 'animal', '{}.png'.format(animal_code))
    animal_im = Image.open(animal_path)

    color = COLOR_CODES[color_idx]

    canvas_im = Image.new('RGB', (500, 700), color)
    canvas_im.paste(animal_im, (0, 0))  # left, top

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    # 여기서 데이터를 받아서 그리겠습니다.
    fnt = ImageFont.truetype(ttf_path, 40)
    d = ImageDraw.Draw(canvas_im)

    d.text((10, 10), title, font=fnt, fill=(0, 255, 0, 128))
    d.text((10, 60), top_text, font=fnt, fill=(0, 255, 0, 255))
    d.text((10, 100), author, font=fnt, fill=(0, 255, 0, 255))

    response = HttpResponse(content_type='image/png')  # file-like
    canvas_im.save(response, format='png')
    return response
