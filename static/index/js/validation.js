// Email Validation
function validateEmail(){

  let emailInput = document.getElementById("email-Input");
  let emailError = document.getElementById("email-Error");
  let emailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

  if(emailInput.value.match(emailFormat)){
    emailError.innerHTML = "";
    return true;
  }else{
    emailError.innerHTML = "Please enter a valid email";
    return false;
  }
}
// Password Strong Check
let pswdInput = document.getElementById("pswd-Input");
let letter = document.getElementById("letter");
let capital = document.getElementById("capital");
let number = document.getElementById("number");
let length = document.getElementById("length");
let messages = document.getElementById("messages");

// When the user clicks on the password field, show the message box
pswdInput.onfocus = function() {
  messages.style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
pswdInput.onblur = function() {
  messages.style.display = "none";
}

// When the user starts to type something inside the password field
pswdInput.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(pswdInput.value.match(lowerCaseLetters)) {  
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }
  
  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(pswdInput.value.match(upperCaseLetters)) {  
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(pswdInput.value.match(numbers)) {  
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }
  
  // Validate length
  if(pswdInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}