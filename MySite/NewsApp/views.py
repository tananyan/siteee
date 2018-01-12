from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from NewsApp.models import Articles, Comments
from NewsApp.forms import CommentForm


# для вывода всех постов
class postsView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "NewsApp/posts.html"

    # В случае успеха перенаправим на главную.
    success_url = "../news"

    def get(self, request):
        form1 = AuthenticationForm(request.POST)

        return render(request, 'NewsApp/posts.html',
                      {'object_list': Articles.objects.all().order_by("-date")[:20], 'form': form1,
                       'user': request.user})

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(postsView, self).form_valid(form)


# Для вывода одного поста
class postView(FormView):
    form_class = AuthenticationForm
    model = Articles
    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "NewsApp/post.html"

    # В случае успеха перенаправим на главную.
    success_url = "/news/"

    def get(self, request, pk):
        form1 = AuthenticationForm(request.POST)
        a = dict(atr=self.model.objects.filter(id=pk))
        b = {'form': form1}
        a.update(b)
        c = {'user': request.user}
        a.update(c)

        comments = Comments.objects.filter(comments_article=pk)
        d = {'commets': comments}
        a.update(d)

        form = {'form_comments': CommentForm}
        a.update(form)

        return render(request, 'NewsApp/post.html', a)

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(postView, self).form_valid(form)


# Для добавления комментария
def addcomment(request, article_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Articles.objects.get(id=article_id)
            comment.comments_author = request.user
            form.save()
            return HttpResponseRedirect('/news/%s' % article_id)
        return HttpResponseRedirect('/news/%s' % article_id)
