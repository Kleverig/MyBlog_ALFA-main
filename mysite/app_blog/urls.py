from django.urls import path, include
from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticleList.as_view(), name='articles-list'),
    path('articles/category/<slug:slug>/', ArticleCategoryList.as_view(), name='articles-category-list'),
    path('articles/<int:year>/<int:month>/<int:day>/<slug:slug>/', ArticleDetail.as_view(), name='news-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)


