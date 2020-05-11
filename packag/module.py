def listchanger(changer1):
    changer1[1] = 33
    changer1.pop()
    changer1.append(10)
    changer1.sort()
    return

#Читает язык
def languagepicker(lang, remember):
    str(remember)
    print('На каком языке ты разговариваешь? What language do you speak? ')
    while lang == "":
        try:
            str(input(lang))
            if lang.lower() == "руский" or "russian":
                print("You speak russian. Ты говоришт по-русски. :)")
                remember == "russian"
            elif lang.lower() == "english":
                print("You speak english. :)")
                remember == "english"
            elif lang.lower() == "deutsch" or "german":
                print("You speak german. Sie sprechen Deutsch. :)")
                remember == "german"
            else:
                print("I don't understand the language you are speaking! :(")
        except ValueError:
            lang == ""
            print("Something did not work, I am sorry!")




