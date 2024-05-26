from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # register and login
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    # home page for admin, user, and guest
    path('', views.adminHome, name="home"),
    path('user/', views.home, name="userHome"),

    # account settings for user
    path('account/', views.accountSettings, name="account"),

    # posts 
    path('posts/', views.posts, name='posts'),
    path('guest/<str:pk_test>/', views.guest, name="guest"),

    # create, update, delete posts
    path('create_post/<str:pk>/', views.createPost, name="create_post"),
    path('update_post/<str:pk>/', views.updatePost, name="update_post"),
    path('delete_post/<str:pk>/', views.deletePost, name="delete_post"),

    # reset password
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

    # about page
    path('about/', views.about, name="about"),

    # sent email
    path('send_email/', views.send_email, name='send_email'),
    path('email_sent/', views.email_sent, name='email_sent'),

    # dark/light mode
    path('user_settings/', views.userSettings, name="user_settings"),
	path('update_theme/', views.updateTheme, name="update_theme"),

    # messages
    path('send_message/', views.send_message, name='send_message'),
    path('inbox', views.inbox, name='inbox'),

    # contact
    path('contact/', views.contact, name='contact'),

    # user profile
    path('profile/<str:user_id>/', views.user_profile, name='user_profile'),
]

'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''