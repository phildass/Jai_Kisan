// (J)ai Kisan - Main JavaScript

// Auto-close flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });
});

// Form validation helper
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    const inputs = form.querySelectorAll('[required]');
    let isValid = true;
    
    inputs.forEach(function(input) {
        if (!input.value.trim()) {
            input.style.borderColor = '#F44336';
            isValid = false;
        } else {
            input.style.borderColor = '#E0E0E0';
        }
    });
    
    return isValid;
}

// Mobile number validation
function validateMobile(mobile) {
    const regex = /^[0-9]{10}$/;
    return regex.test(mobile);
}

// OTP input auto-format
const otpInput = document.getElementById('otp');
if (otpInput) {
    otpInput.addEventListener('input', function(e) {
        e.target.value = e.target.value.replace(/[^0-9]/g, '').slice(0, 6);
    });
}

// Prevent form resubmission on page refresh
if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}
