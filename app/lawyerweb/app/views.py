from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import BannerContactInfo, Services, FooterSocialMedya, Blog
from .Mail import MailSend
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(message)
        MailSend(name,subject,email,message)
        return redirect('index')
    else:
        Banner_All = BannerContactInfo.objects.all()
        Service_All = Services.objects.all()
        FooterSocialMedya_All = FooterSocialMedya.objects.all()
        return render(request, 'index.html', {'Banner_All': Banner_All, 'Service_All': Service_All, 'FooterSocialMedya_All': FooterSocialMedya_All})

def contact(request):
    Banner_All = BannerContactInfo.objects.all()
    FooterSocialMedya_All = FooterSocialMedya.objects.all()
    return render(request, 'contact.html', {'Banner_All': Banner_All, 'FooterSocialMedya_All': FooterSocialMedya_All})


def about(request):
    Banner_All = BannerContactInfo.objects.all()
    FooterSocialMedya_All = FooterSocialMedya.objects.all()
    return render(request, 'about.html', {'Banner_All': Banner_All, 'FooterSocialMedya_All': FooterSocialMedya_All})

def blog(request):
    Blogs = Blog.objects.all()
    Total_Blog = Blog.objects.count()
    Banner_All = BannerContactInfo.objects.all()
    FooterSocialMedya_All = FooterSocialMedya.objects.all()
    Blogs__all = Blog.objects.all().order_by('id')
    Blogs_Reverse = Blogs__all.reverse()
    categories = Services.objects.all()
    category_count = {}
    for category in categories:
        count = Blog.objects.filter(Category=category).count()
        category_count[category] = count

    ### Other için
    total_blogs = Blog.objects.count()  # Tüm blogların sayısını hesapla
    categories = Services.objects.all()[:4]  # İlk dört kategoriyi al
    category_count = {}
    for category in categories:
         count = Blog.objects.filter(Category=category).count()
         category_count[category] = count

    # # Diğer kategorilere ait blog sayısını hesapla
    count_for_listed_categories = sum(category_count.values())
    others_count = total_blogs - count_for_listed_categories
    print(others_count)
    return render(request, 'blog.html', {'Banner_All': Banner_All, 'FooterSocialMedya_All': FooterSocialMedya_All, 'Blogs':Blogs, 'category_count': category_count, 'Blogs_Reverse': Blogs_Reverse, 'Total_Blog':Total_Blog, 'others_count':others_count})

# def blog_details(request):
#     Banner_All = BannerContactInfo.objects.all()
#     FooterSocialMedya_All = FooterSocialMedya.objects.all()
#     Blogs = Blog.objects.all()
#     return render(request, 'blog-details.html', {'Banner_All': Banner_All, 'FooterSocialMedya_All': FooterSocialMedya_All, 'Blogs':Blogs})


def detail(request, question_id):
    Blogs = Blog.objects.all()
    Total_Blog = Blog.objects.count()
    Banner_All = BannerContactInfo.objects.all()
    FooterSocialMedya_All = FooterSocialMedya.objects.all()
    Blogs__all = Blog.objects.all().order_by('id')
    Blogs_Reverse = Blogs__all.reverse()
    categories = Services.objects.all()
    category_count = {}
    for category in categories:
        count = Blog.objects.filter(Category=category).count()
        category_count[category] = count

    ### Other için
    total_blogs = Blog.objects.count()  # Tüm blogların sayısını hesapla
    categories = Services.objects.all()[:4]  # İlk dört kategoriyi al
    category_count = {}
    for category in categories:
         count = Blog.objects.filter(Category=category).count()
         category_count[category] = count

    # # Diğer kategorilere ait blog sayısını hesapla
    count_for_listed_categories = sum(category_count.values())
    others_count = total_blogs - count_for_listed_categories
    print(others_count)
    blog = get_object_or_404(Blog, pk=question_id)
    categori = blog.Category
    Related_Posts = Blog.objects.filter(Category=categori)
    Related_Posts.reverse()
    Related = Related_Posts[:2]
    return render(request, 'blog-details.html', {'blog': blog,'Banner_All': Banner_All, 'FooterSocialMedya_All': FooterSocialMedya_All, 'Blogs':Blogs, 'category_count': category_count, 'Blogs_Reverse': Blogs_Reverse, 'Total_Blog':Total_Blog, 'others_count':others_count, 'Related':Related})

def detail_categori(request, categori):
    category = get_object_or_404(Services, headers=categori)
    Blogs = Blog.objects.filter(Category=category).order_by('-date_posted')
    print(Blogs)

   # Blogs = Blog.objects.all()
    Total_Blog = Blog.objects.count()
    Banner_All = BannerContactInfo.objects.all()
    FooterSocialMedya_All = FooterSocialMedya.objects.all()
    Blogs__all = Blog.objects.all().order_by('id')
    Blogs_Reverse = Blogs__all.reverse()
    categories = Services.objects.all()
    category_count = {}
    for category in categories:
        count = Blog.objects.filter(Category=category).count()
        category_count[category] = count

    ### Other için
    total_blogs = Blog.objects.count()  # Tüm blogların sayısını hesapla
    categories = Services.objects.all()[:4]  # İlk dört kategoriyi al
    category_count = {}
    for category in categories:
         count = Blog.objects.filter(Category=category).count()
         category_count[category] = count

    # # Diğer kategorilere ait blog sayısını hesapla
    count_for_listed_categories = sum(category_count.values())
    others_count = total_blogs - count_for_listed_categories
    print(others_count)

    
    return render(request, 'blog.html',{'Banner_All': Banner_All, 'FooterSocialMedya_All': FooterSocialMedya_All, 'Blogs':Blogs, 'category_count': category_count, 'Blogs_Reverse': Blogs_Reverse, 'Total_Blog':Total_Blog, 'others_count':others_count})
