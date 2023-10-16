document.addEventListener("DOMContentLoaded", function() {
    var regis_button = document.getElementById("register2");

    regis_button.addEventListener("click", function() {
        console.log("register button clicked");

    });
});


async function checkvalidity(){
    var name = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    console.log('/register/' + name + '/' + password + '/' + email)

    fetch('/register/' + name + '/' + password + '/' + email)
    .then(response => response.json())
    .then(data => {
        console.log('Data: ', data);
        if (data['message'] == 'Username is already taken')
            alert('Username is already taken')
        else if (data['message'] == 'Email is already taken')
            alert('Email is already taken')
        else if (data['message'] == 'Register successfully'){
            window.location.href = '/login'
            alert('Register successfully')
        }
    })
}


function applyScrollReveal(selector, options) {
    const sr = new ScrollReveal(options);
    sr.reveal(selector);
}

// Usage
applyScrollReveal('.container', {
    distance: '65px',
    duration: 2600,
    delay: 100,
    reset: true,
    origin: 'top',
});