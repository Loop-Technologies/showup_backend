const form = document.getElementById('form');
const fullname = document.getElementById('fullname');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});
 
const setError = (element, message) => {
     const inputControl = element.parentElement;
     const errorDisplay = inputControl.querySelector('.error');

     errorDisplay.innerText = message;
     inputControl.classList.add('error');
     inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValidEmail = email => {
const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
     const fullnameValue = fullname.value.trim();
     const emailValue = email.value.trim();
     const phoneValue = phone.value.trim();
     const passwordValue = password.value.trim();
     const password2Value = password2.value.trim();

     let isValid = true;

    if(fullnameValue === '') {
          setError(fullname, 'Fullname is required');
          isValid = false;
     } else {
           setSuccess(fullname);
     }

     if(emailValue === '') {
        setError(email, 'Email is required');
     } else if (!isValidEmail(emailValue)) {
        setError(email, 'provide a vallide email address');
        isValid = false;
     } else {
     setSuccess(email);
   }

   if(phoneValue === '') {
    setError(phone, 'phone number is required');
    isValid = false;
      } 
    else {
     setSuccess(phone);
      }


   if(passwordValue === '') {
    setError(password, 'Password is required');
     } else if(passwordValue.length < 5 ) {
       setError(password, 'Password must be at least 8 character.')
       isValid = false;
     }else {  
       setSuccess(password);
   }

   if(password2Value === '') {
    setError(password2, 'Please confirm your password');
} else if(password2Value !== passwordValue) {
    setError(password2, "Password doesn't match");
    isValid = false;
     }
     else {  
     setSuccess(password2);
}

if (isValid) {
  form.submit();
}


};

function closeMessage(button) {
  const messageElement = button.previousElementSibling;
  const listItem = button.parentNode;
  listItem.remove();
}
