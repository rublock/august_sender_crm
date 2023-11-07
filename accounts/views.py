from django.contrib.auth.views import LoginView

from accounts.forms import LoginUserForm


class CustomLoginView(LoginView):
    form_class = LoginUserForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # Установим время истечения сеанса равным 0 секундам. Таким образом, он автоматически закроет сеанс после закрытия браузера. И обновим данные.
            self.request.session.set_expiry(3600)
            self.request.session.modified = True

        # В противном случае сеанс браузера будет таким же как время сеанса cookie "SESSION_COOKIE_AGE", определенное в settings.py
        return super(CustomLoginView, self).form_valid(form)
