async function checkpassword(){
    var name = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    console.log('/login/' + name + '/' + password)

    const response = await fetch('/login/' + name + '/' + password)
    const data = await response.json()
    if (data['message'] === "Login successfully") {
        window.location.href = '/process_login/' + name;
        alert("Login successfully");
    } else if (data['message'] === "Login failed") {
        alert("Either username or password is incorrect");
    }
}