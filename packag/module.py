def listchanger(changer1):
    changer1[1] = 33
    changer1.pop()
    changer1.append(10)
    changer1.sort()
    return

#Считает кольчество char в string.
def lettercounter(text):
    let = 0
    for txt in let:
        if txt.ischar():
            let =+ 1
    print()
    print(f"There are {let} characters in this text.")

#Читает язык
def languagepicker(lang):
    a = str()
    print('What language do you speak? ')
    while a == "":
        try:
            a = input()
            a.lower()
            if a == "russian":
                print("You speak russian. Ты говоришь по-русски. :)")
            elif a == "english":
                print("You speak english. :)")
            elif a == "deutsch":
                print("You speak german. Sie sprechen Deutsch. :)")
            else:
                print("I don't understand the language you are speaking! :(")
        except ValueError:
            a == ""
            print("Something did not work, I am sorry!")

#hello-bot
def greeter(name):
    a = str()
    print("Hello, " + name + ". Good morning! Tell us how you are today!")
    while a == "":
        try:
            a = input("I feel ")
            a.lower()
            if a == "good":
                print("That is great! Let's get to business.")
            elif a == "fine":
                print("Alright! Let us continue.")
            elif a == "bad":
                print('What happened buddy?')
            else:
                print("I am a computer. I don't know emotions :(")
        except ValueError:
            print('No, just no. Try again.')
            a == ''


