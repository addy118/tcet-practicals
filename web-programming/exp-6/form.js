function validateText(textid){
    var textid = document.getElementById(textid);
    if(textid.value == ""){
        textid.style.border = '1px solid red';
        textid.placeholder = "Enter value here!";
        return false;
    }
    else{
        return true;
    }
}

function validatePassword(){
    var password = document.getElementById('password');
    var confirm = document.getElementById('confirm');
    if(password.value != "" && password.value == confirm.value){
        return true;
    }
    else{
        var check = document.getElementById('check');
        check.innerHTML = "The passwords do not match. Please try again.";
        check.style.display = "block";
        check.style.color = "red";
        return false;
    }
}

function validateEmail(){
    var email = document.getElementById("email");
    var invalid3 = document.getElementById("invalid3");
    var val = email.value;
    
    if(val != "" && val.substring(val.length-4) == ".com" && val.includes("@") && (val.length - val.indexOf("@") -1) - (val.length - val.lastIndexOf(".") -1) >= 3 && val.substring(0, val.indexOf('@')).length >= 1){
        return true;
    }
    else{
        invalid3.innerHTML = "Please enter a valid email id.";
        invalid3.style.color = "red";
        invalid3.style.display = "block"
        return false;
    }
}

function validateNumber(){
    var number = document.getElementById("number");
    var number_value = number.value;
    console.log(number_value)
    console.log(number_value.length)
    if(number_value.length < 10 || number_value.length > 10){
        var invalid1 = document.getElementById("invalid1");
        invalid1.style.display = "block";
        invalid1.style.color = "red";
        invalid1.innerHTML = "Invalid phone number.";
        return false;
    }
    else{
        return true;
    }
}

function validateBldg(){
    var bldg = document.getElementById("bldg")
    var bldg_val = bldg.value
    if(bldg_val < 1 || bldg_val > 1999){
        var invalid2 = document.getElementById("invalid2")
        invalid2.style.display = "block";
        invalid2.style.color = "red";
        invalid2.innerHTML = "Please enter a value between 1 and 1999.";
        return false;
    }
    else{
        return true;
    }
}

function validateCity(){
    var city = document.getElementById("city");
    var cities = document.getElementById("cities");
    if(cities.selectedIndex == 0){
        city.innerHTML = "Please select a city.";
        city.style.display = "block";
        city.style.color = "red";
        return false;
    }
    else{
        return true;
    }
}

function validateRadio(){
    var phone = document.getElementById("phone");
    var emailid = document.getElementById("emailid");
    var message = document.getElementById("message");
    var radio = document.getElementById("radio");
    if(phone.checked || emailid.checked || message.checked){
        return true;
    }
    else{
        radio.innerHTML = "Please select an option.";
        radio.style.display = "block";
        radio.style.color = "red";
        return false;
    }
}

function validateForm(){
    var UserName = validateText('user_name');
    var StreetName = validateText('street');
    var Password = validatePassword();
    var Number1 = validateNumber();
    var Building = validateBldg();
    var City = validateCity();
    var Contact = validateRadio();
    var Email = validateEmail();

    if(UserName && StreetName && Password && Number1 && Building && Contact && City && Email){
        return true;
    }
    else{
        return false;
    }
}