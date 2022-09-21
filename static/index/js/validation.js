// Email Validation
// Method 1
// function validateEmail(){

  //   let emailInput = document.getElementById("email-Input");
  //   let emailError = document.getElementById("email-Error");
  //   let emailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  
  //   if(emailInput.value.match(emailFormat)){
  //     emailError.innerHTML = "";
  //     return true;
  //   }else{
  //     emailError.innerHTML = "Please enter a valid email";
  //     return false;
  //   }
  // }

// Method 2
let emailInput = document.getElementById("email-input");
let emailError = document.getElementById("email-error");
let emailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

emailInput.oninput = function(){
  if(emailInput.value.match(emailFormat)){
    emailError.innerHTML = "";
  }else{
    emailError.innerHTML = "Please enter a valid email";
  }
  // Incase a user clears the text, the badge is hidden again
  if(emailInput.value.length !== 0){
    emailError.style.display = "block";
  }
  else{
    emailError.style.display = "none";
  }
}

// Passwors strength check
let pswdInput = document.getElementById("pswd-input");
let pswdStrength = document.getElementById("pswd-strength");
let strongpswd = new RegExp('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})');
// a strong level password that has at least one lowercase letter (?=.*[a-z]), one uppercase letter (?=.*[A-Z]), one digit (?=.*[0-9]), one special character (?=.*[^A-Za-z0-9]), and is at least eight characters long(?=.{8,}).
let mediumpswd = new RegExp('((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))');
// If the password is at least six characters long and meets all the other requirements, or has no digit but meets the rest of the requirements.
//  If the password entered does not meet the strong or medium-level requirements, then it is deemed weak
let message = document.getElementById("message")

// When the user clicks on the password field, show the message box
pswdInput.onfocus = function() {
  message.style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
pswdInput.onblur = function() {
  message.style.display = "none";
}

pswdInput.onkeyup = function(){
  if(pswdInput.value.match(strongpswd)){
    pswdStrength.innerHTML = "Password is strong";
    pswdStrength.style.color = "green";
  }else if(pswdInput.value.match(mediumpswd)){
    pswdStrength.innerHTML = "password is medium";
    pswdStrength.style.color = "yellow";
  }else{
    pswdStrength.innerHTML = "password is weak";
    pswdStrength.style.color = "red";
  }
  // Incase a user clears the text, the badge is hidden again
  if(pswdInput.value.length !== 0){
    pswdStrength.style.display = "block";
  }
  else{
    pswdStrength.style.display = "none";
  }
}
// Password toggle eye icons
let eyeIcons = document.getElementById("eye-icons")
// Password inputfield is already mentioned above
let eyeIcon1 = document.getElementById("eye-icon1");
let eyeIcon2 = document.getElementById("eye-icon2")

eyeIcons.onclick = function(){
  if(pswdInput.type === "password"){
    // === is used for comparing two variables, but this operator also checks datatype and compares two values.
    // Compares equality of two operands with their types.
    pswdInput.type = "text";
    eyeIcon1.style.display = "block";
    eyeIcon2.style.display = "none";
  }else{
    pswdInput.type = "password";
    eyeIcon1.style.display = "none";
    eyeIcon2.style.display = "block";
  }
}


// Toggle eye icon
// let passwordField  = document.getElementById("pswd-input");
// let eyeIcon = document.getElementById("eye-icon")

// eyeIcon.addEventListener("click", function(){
//   this.classList.toggle("fa-eye-slash");
//   const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
//   passwordField.setAttribute("type", type);
// })
