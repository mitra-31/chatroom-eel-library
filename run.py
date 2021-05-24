import eel

eel.init('GUI')

@eel.expose
def login(username,password):
    cred = open('cred.txt','r')
    try:
        user,passw = cred.readline().split(":")[:-1]
        cred.close()
        if username == user and password == passw:
            print("Logged in")
        else:
            print("Falied")
    except ValueError:
        print("Not found")
        cred.close()
    


@eel.expose
def register(username,password):
    cred = open('cred.txt','w+')
    cred.write(username+":"+password+":")
    cred.close()
    print("yees")


eel.start("index.html",size=(700,500))

