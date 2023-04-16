# These views are not useful, when we use django auth url,
# from django.contrib.auth import login, logout
# from django.contrib.auth.forms import AuthenticationForm
#
# from django.views.generic import FormView, RedirectView
#
#
# class LoginView(FormView):
#     template_name = 'accounts/login.html'
#     form_class = AuthenticationForm
#
#     def get_success_url(self):
#         return self.request.GET.get('next')
#
#     def form_valid(self, form):
#         login(self.request, form.get_user())
#         return super().form_valid(form)
#
#
# class LogoutView(RedirectView):
#     url = '/feedbacks/'
#
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return super().get(request, *args, **kwargs)


# from accounts.model_forms import LoginForm
# from django.shortcuts import redirect

# if inheritance from FormView and using LoginForm, then use these rows
# class LoginView(FormView):
#     template_name = 'accounts/login.html'
#     form_class = LoginForm
#
#     def get_success_url(self):
#         return self.request.GET.get('next')
#
#     def form_valid(self, form):
#         login(self.request, form.user)
#         return super().form_valid(form)

# if inheritance from TemplateView, then use these rows

# class LoginView(TemplateView):
#     template_name = 'accounts/login.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({'form': LoginForm()})
#         return context
#
#     def post(self, request, *args, **kwargs):
#         _next = request.GET.get('next')
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             login(request, form.user)
#             return redirect(_next)
#         return self.get(request, *args, **kwargs)
