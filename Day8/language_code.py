def code_greeting(language_code):
    if language_code == 'en':
        return 'Hello'
    elif language_code == 'es':
        return 'Hola'
    elif language_code == 'fr':
        return 'Bonjour'
    else:
        print("Wrong language code")

print(code_greeting('en'),"Sara")
print(code_greeting('es'),"Sara")
print(code_greeting('fr'),"Sara")