function displayErrorMessage(fieldName, message) {
    var errorContainer = document.getElementById("errorContainer-" + fieldName);
    var errorMessageElement = errorContainer.querySelector('.error-message');

    if (errorMessageElement) {
        // If an error message already exists
        if (message === null) {
            // If message is null, remove the error message
            errorContainer.removeChild(errorMessageElement);
        } else {
            // Update the content of the existing error message
            errorMessageElement.textContent = message;
        }
    } else {
        // If no error message exists, create a new one
        if (message !== null) {
            errorMessageElement = document.createElement('p');
            errorMessageElement.className = 'error-message';
            errorMessageElement.textContent = message;
            errorContainer.appendChild(errorMessageElement);
        }
    }
}

function validateFirstName(firstName) {

        if (firstName === null) {
            // Handle if the user clicks cancel or closes the prompt
            console.log('Cancelled or no input provided');
            displayErrorMessage('firstname','Cancelled or no input provided');
            return false;
        }

        if (firstName.trim() === '') {
            console.log('Please enter your First Name');
            displayErrorMessage('firstname','Please enter your First Name');
            return false;
        } else if (firstName.length < 2 || firstName.length > 50) {
            console.log('First Name must be between 2 and 50 characters');
            displayErrorMessage('firstname','First Name must be between 2 and 50 characters');
            return false;
        } else if (!/^[A-Za-zÀ-ÿ-']+$/u.test(firstName)) {
            console.log('First Name can only contain letters, apostrophes, or hyphens.');
            displayErrorMessage('firstname','First Name can only contain letters, apostrophes, or hyphens.');
            return false;
        } else {
            console.log(`Valid name: ${firstName}`);
            displayErrorMessage('firstname',null);
            return true;
        }
    }

    function validateLastName(lastName){

        if (lastName === null) {
            // Handle if the user clicks cancel or closes the prompt
            console.log('Cancelled or no input provided');
            displayErrorMessage('Cancelled or no input provided');
            return false;
        }

        if (lastName.trim() === '') {
            console.log('Please enter your Last Name');
            displayErrorMessage('lastname','Please enter your Last Name');
            return false;
        } else if (lastName.length < 2 || lastName.length > 70) {
            console.log('Lastname must be between 2 and 70 characters');
            displayErrorMessage('lastname','Last Name must be between 2 and 70 characters');
            return false;
        } else if (!/^[A-Za-zÀ-ÿ-']+$/u.test(lastName)) {
            console.log('Last Name can only contain letters, apostrophes, or hyphens.');
            displayErrorMessage('lastname','Last Name can only contain letters, apostrophes, or hyphens.');
            return false;
        } else {
            console.log(`Valid name: ${lastName}`);
            displayErrorMessage('lastname',null);
            return true;
        }
    }

    function validateEmail(email){
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

        if (email === null){

            console.log('Cancelled or no input provided');
            displayErrorMessage('email','Please enter your email');
            return false;
        }

        if (email.trim() === '') {
            console.log('Please enter your email');
            displayErrorMessage('email','Please enter your email');
            return false;
        }
        if (emailRegex.test(email)) {
            console.log("Valid email address");
            return true;
        } else {
            console.log("Invalid email address");
            displayErrorMessage('email','Please enter a valid email format');
            return false;
    
        }
    }

    async function validateUserName(userName){

        if (userName === null) {
            
            console.log('Cancelled or no input provided');
            return false;
        }

        if (userName.trim() === '') {
            console.log('Please enter your Username');
            displayErrorMessage('username','Please enter your Username');
            return false;
        } else if (userName.length < 2 || userName.length > 50) {
            console.log('Username must be between 2 and 50 characters');
            displayErrorMessage('username','Username must be between 2 and 50 characters');
            return false;
        } else if (!/^[a-zA-Z0-9]+$/u.test(userName)) {
            console.log('Username can only contain letters or numbers.');
            displayErrorMessage('username','Username can only contain letters or numbers.');
            return false;
        } else {
            console.log(`Valid name: ${userName}`);
            displayErrorMessage('username',null);

            const form = document.getElementById('signup-form');
            const formData = new FormData(form);

            const response = await fetch('/signup', {
                method: 'POST',
                body: formData
            });
            const data = await response.text();
            const usernameExists = data.exists;
    
            if (usernameExists) {
                console.log('Username already exists');
                displayErrorMessage('username', 'Username already exists');
                return false;
            }
            return true;
        }
    }

    function validatePassword(password) {
        let spaceCount = 0;
    
        for (let i = 0; i < password.length; i++) {
            if (password[i] === ' ') {
                spaceCount++;
            }
        }
    
        if (password === '') {
            console.log('Please enter a password');
            displayErrorMessage('password','Please enter a password');
            return false;
        } else if (password.length < 10) {
            console.log(`Password must be at least 10 characters long. You entered ${password.length}.`);
            displayErrorMessage('password',`Password must be at least 10 characters long. You entered ${password.length}.`);
            return false;
        } else if (spaceCount > 0) {
            console.log(`You cannot use spaces in your password. You used ${spaceCount}.`);
            displayErrorMessage('password',`You cannot use spaces in your password. You used ${spaceCount}.`);
            return false;
        } else {
            let numCount = 0;
            let upperCount = 0;
    
            for (let i = 0; i < password.length; i++) {
                if (!isNaN(parseInt(password[i]))) {
                    numCount++;
                } else if (password[i] === password[i].toUpperCase()) {
                    upperCount++;
                }
            }
    
            if (numCount >= 2 && upperCount >= 2) {
                displayErrorMessage('password',null);
                console.log(password)
                return true;
            } else {
                console.log(`Your password must contain at least two numbers and two uppercase characters. You currently have ${numCount} numbers and ${upperCount} uppercase characters.`);
                displayErrorMessage('password',`Your password must contain at least two numbers and two uppercase characters. You currently have ${numCount} numbers and ${upperCount} uppercase characters.`);
                return false;
            }
        }
    }

    function validateRePassword(password, rePassword){
        if (rePassword !== password){
            displayErrorMessage('re-password','Please enter matching passwords');
            return false;
        }

        else{
            return true;
        }
    }
  
document.getElementById('signup-form').addEventListener('submit',function(event){

    const firstNameInput = document.getElementById('firstname')
    const firstName = firstNameInput.value
    const validatedFirstName = validateFirstName(firstName)

    const lastNameInput = document.getElementById('lastname')
    const lastName = lastNameInput.value
    const validatedLastName = validateLastName(lastName)

    const userNameInput = document.getElementById('username')
    const userName = userNameInput.value
    const validatedUserName = validateUserName(userName)

    const emailInput = document.getElementById('email')
    const email = emailInput.value
    const validatedEmail = validateEmail(email)

    const passwordInput = document.getElementById('password')
    const password = passwordInput.value
    const validatedPassword = validatePassword(password)

    const rePasswordInput = document.getElementById('re-password')
    const rePassword = rePasswordInput.value
    const validatedRePassword = validateRePassword(password, rePassword)


    if (validatedUserName && validatedFirstName && validatedLastName && validatedPassword && validatedEmail && validatedRePassword){
        document.getElementById('signup-form').submit();
        document.getElementById('submit-button').disabled = true;
        console.log('Button disabled')
        console.log('It worked!')
        
    }

    else{
        console.log('Please enter valid credentials')
        event.preventDefault()
    }

})



