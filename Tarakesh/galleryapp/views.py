import os
from django.conf import settings
from django.shortcuts import render,redirect

def gallery(request):
    image_dir = os.path.join(
        settings.BASE_DIR,
        'galleryapp',
        'static',
        'figure'
    )
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded = request.FILES['image']

        if uploaded.content_type =="image/png":
            existing = [
                int(os.path.splitext(f)[0])
                for f in os.listdir(image_dir)
                if f.endswith('.png') and os.path.splitext(f)[0].isdigit()
            ]

            next_index = max(existing) + 1 if existing else 0
            file_path = os.path.join(image_dir, f"{next_index}.png")

            with open(file_path, 'wb+') as destination:
                for chunk in uploaded.chunks():
                    destination.write(chunk)

        return redirect('gallery')


    # Collect only numeric jpg filenames
    images = []
    for f in os.listdir(image_dir):
        name, ext = os.path.splitext(f)
        if ext.lower() == '.png' and name.isdigit():
            images.append(f)

    # Sort numerically (0.jpg, 1.jpg, 2.jpg...)
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))

    total = len(images)

    # Default index
    index = request.GET.get('index', 0)
    try:
        index = int(index)
    except ValueError:
        index = 0

    # Navigation logic (Django if / elif)
    action = request.GET.get('action')

    if action == 'prev':
        index -= 1
    elif action == 'next':
        index += 1

    # Clamp index safely
    index = max(0, min(index, total - 1))

    context = {
        'image': images[index] if images else None,
        'index': index,
        'total': total,
    }

    return render(request, 'gallery.html', context)
