from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Категории
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    # Отзывы на странице фильма
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Аниме
    list_display = ("title", "category", "url")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", "poster")
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Актеры и режиссеры", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        ("Параметры", {
            "fields": (("budget", 'url'),)
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    # Отзывы
    list_display = ("id", "name", "email", "parent", "movie")
    readonly_fields = ("name", "email")
    list_display_links = ("id", "name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Жанры
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # Персонажи и режиссеры
    list_display = ("name", "age")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    # Кадры из фильма
    list_display = ("title", "movie")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    # Рейтинг
    list_display = ("ip", )


admin.site.register(RatingStar)
