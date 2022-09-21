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