async function checkpassword(e) {
  e.preventDefault();
  var name = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  fetch("/login_1/" + name + "/" + password)
    .then((response) => response.json())
    .then((data) => {
      console.log("Data: ", data);
      if (data["message"] == "Login successfully") {
        alert("Login successfully");
        window.location.href = "/process_login/" + name;
      } else if (data["message"] == "Login failed") {
        alert("Either username or password is incorrect");
        window.location.assign("/login");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const loginButton = document.getElementById("loginButton");
  loginButton.addEventListener("click", checkpassword);
});
