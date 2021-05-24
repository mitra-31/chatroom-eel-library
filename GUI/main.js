function login(){
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    eel.login(username,password)(function(ret) {console.log(ret)})
}

function register(){
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    eel.register(username,password)(function(ret) {console.log(ret)})
}

