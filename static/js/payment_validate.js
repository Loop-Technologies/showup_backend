// // Get the form element
// const form = document.getElementById("paymentForm");
// form.addEventListener("submit", function(event) {
//   event.preventDefault();
//   if (validateForm()) {
//     form.submit();
//   }
// });

// // Function to validate the form fields
// function validateForm() {
//   // Get the input fields from the form
//   const nameInput = document.getElementById("name");
//   const emailInput = document.getElementById("email");
//   const amountInput = document.getElementById("amount");
//   const ccnumInput = document.getElementById("ccnum");
//   const expdateInput = document.getElementById("expdate");
//   const ticketIdInput = document.getElementById("ticket_id");

//   // Validate each field
//   let isValid = true;

//   if (nameInput.value.trim() === "") {
//     nameInput.classList.add("is-invalid");
//     isValid = false;
//   } else {
//     nameInput.classList.remove("is-invalid");
//     nameInput.classList.add("is-valid");
//   }

//   if (emailInput.value.trim() === "" || !isValidEmail(emailInput.value)) {
//     emailInput.classList.add("is-invalid");
//     isValid = false;
//   } else {
//     emailInput.classList.remove("is-invalid");
//     emailInput.classList.add("is-valid");
//   }

//   if (amountInput.value.trim() === "" || isNaN(parseInt(amountInput.value))) {
//     amountInput.classList.add("is-invalid");
//     isValid = false;
//   } else {
//     amountInput.classList.remove("is-invalid");
//     amountInput.classList.add("is-valid");
//   }

//   if (ccnumInput.value.trim() === "" || !isValidCreditCard(ccnumInput.value)) {
//     ccnumInput.classList.add("is-invalid");
//     isValid = false;
//   } else {
//     ccnumInput.classList.remove("is-invalid");
//     ccnumInput.classList.add("is-valid");
//   }

//   if (expdateInput.value.trim() === "") {
//     expdateInput.classList.add("is-invalid");
//     isValid = false;
//   } else {
//     expdateInput.classList.remove("is-invalid");
//     expdateInput.classList.add("is-valid");
//   }
// }
// function isCardExpired(expirationDate) {
//     // Get the current date
//     const currentDate = new Date(); 
//     const [month, year] = expirationDate.split('/').map(Number);
  
//     // Get the current month and year
//     const expiration = new Date(year, month - 1);
//     return currentDate > expiration;
//   }
  
//   // Example usage
//   const expirationDate = '12/2022'; // Replace with the actual expiration date
//   const isExpired = isCardExpired(expirationDate);
//   console.log(isExpired); // Output: false (if the current date is before December 2022)

// // Function to validate email address
// function isValidEmail(email) {
//   const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//   return emailRegex.test(email);
// }

// // Function to validate credit card number
// function isValidCreditCard(ccnum) {
//   const ccnumRegex = /^\d{4}-\d{4}-\d{4}-\d{4}$/;
//   return ccnumRegex.test(ccnum);
// }

// function getCardType(cardNumber) {
//     // Remove any non-digit characters from the card number
//     const cleanedCardNumber = cardNumber.replace(/\D/g, '');
  
//     // Regular expressions for each card type
//     const visaRegex = /^4[0-9]{12}(?:[0-9]{3})?$/;  //removing none-space characters from thee fiels and puthing them correctly
//     const amexRegex = /^3[47][0-9]{13}$/;
//     const mastercardRegex = /^5[1-5][0-9]{14}$/;
  
//     // Check if the card number matches the patterns
//     if (visaRegex.test(cleanedCardNumber)) {
//       return 'Visa';
//     } else if (amexRegex.test(cleanedCardNumber)) {
//       return 'Amex';
//     } else if (mastercardRegex.test(cleanedCardNumber)) {
//       return 'Mastercard';
//     } else {
//       return 'Unknown';
//     }
//   }
  
//   // Example usage
//   const cardNumber = '4111-1111-1111-1111'; 
//   const cardType = getCardType(cardNumber);
//   console.log(cardType); // Output: Visa