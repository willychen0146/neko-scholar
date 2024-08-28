
def theme_context(request):
    default_theme = 'light.css'
    if request.user.is_authenticated:
        try:
            account = request.user.account
            setting = account.setting
            user_theme = setting.theme if setting.theme else default_theme
        except AttributeError:
            user_theme = default_theme
    else:
        user_theme = default_theme
    
    return {'user_theme': user_theme}
