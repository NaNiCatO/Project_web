async function checkpassword(){

    var name = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    
    const response = fetch('/login/' + name + '/' + password)
    const data = response.json()
    alert(data['message']);
    if (data['message'] == "Login successfully") {
        window.location.href = '/process_login/' + name; 
    } else if (data['message'] == "Login failed") {
        alert("Either username or password is incorrect");
        window.location.assign('/login');   
    }
}





