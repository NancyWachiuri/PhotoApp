from django.shortcuts import render, redirect
from .models import Category, Photo, Location

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else: 
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    location = Location.objects.all()



    context = {'categories':categories, 'photos': photos, 'location': location}
    return render(request, 'photos/gallery.html',context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')



        if data['category'] != 'none':
            category =Category.objects.get(id =data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category= None

            photo = Photo.objects.create(
                category= category,
                description = data['description'],
                image= image,
            )

            return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
         search_term = request.GET.get("image")
         searched_images = Photo.search_by_category(search_term)
         message = f"{search_term}"

         return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def location(request, location_id):
    images = Photo.objects.filter(location_id=location_id)
    # get the location name
    title = location
    return render(request, 'location.html', {'images': images,'title': title})

