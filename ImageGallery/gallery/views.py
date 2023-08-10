from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm


def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery')
    return render(request, 'confirm_delete.html', {'image': image})
