// some scripts

// jquery ready start
$(document).ready(function () {
  // jQuery code

  /* ///////////////////////////////////////

    THESE FOLLOWING SCRIPTS ONLY FOR BASIC USAGE, 
    For sliders, interactions and other

    */ ///////////////////////////////////////

  //////////////////////// Prevent closing from click inside dropdown
  $(document).on("click", ".dropdown-menu", function (e) {
    e.stopPropagation();
  });

  $(".js-check :radio").change(function () {
    var check_attr_name = $(this).attr("name");
    if ($(this).is(":checked")) {
      $("input[name=" + check_attr_name + "]")
        .closest(".js-check")
        .removeClass("active");
      $(this).closest(".js-check").addClass("active");
      // item.find('.radio').find('span').text('Add');
    } else {
      item.removeClass("active");
      // item.find('.radio').find('span').text('Unselect');
    }
  });

  $(".js-check :checkbox").change(function () {
    var check_attr_name = $(this).attr("name");
    if ($(this).is(":checked")) {
      $(this).closest(".js-check").addClass("active");
      // item.find('.radio').find('span').text('Add');
    } else {
      $(this).closest(".js-check").removeClass("active");
      // item.find('.radio').find('span').text('Unselect');
    }
  });

  //////////////////////// Bootstrap tooltip
  if ($('[data-toggle="tooltip"]').length > 0) {
    // check if element exists
    $('[data-toggle="tooltip"]').tooltip();
  } // end if
});
// jquery end

// <!-- Optional: JavaScript for auto-dismiss functionality -->
document.addEventListener("DOMContentLoaded", function () {
  // Auto-dismiss alerts after 5 seconds
  const alerts = document.querySelectorAll(".alert.auto-dismiss");
  alerts.forEach(function (alert) {
    setTimeout(function () {
      if (alert && alert.parentNode) {
        alert.classList.remove("show");
        setTimeout(function () {
          if (alert && alert.parentNode) {
            alert.remove();
          }
        }, 300);
      }
    }, 5000);
  });

  // Add smooth removal animation when close button is clicked
  const closeButtons = document.querySelectorAll(".alert .btn-close");
  closeButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      const alert = this.closest(".alert");
      alert.style.animation = "slideOutRight 0.3s ease-in forwards";
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach(function (alert) {
    setTimeout(function () {
      // Bootstrap native way to close alert
      bootstrap.Alert.getOrCreateInstance(alert).close();
    }, 5000); // auto-hide after 5 seconds
  });
});

// Profile image preview functionality
document.addEventListener("DOMContentLoaded", function () {
  const profileInput = document.getElementById("id_profile_picture");
  const profilePreview = document.getElementById("profilePreview");

  if (profileInput) {
    profileInput.addEventListener("change", function (e) {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          profilePreview.src = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    });
  }
});


document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.getElementById('id_images');
    const imagePreview = document.getElementById('image-preview');
    
    if (imageInput) {
        imageInput.addEventListener('change', function(e) {
            imagePreview.innerHTML = '';
            const files = e.target.files;
            
            if (files.length > 0) {
                const previewContainer = document.createElement('div');
                previewContainer.className = 'row g-2';
                
                Array.from(files).forEach(function(file) {
                    if (file.type.startsWith('image/')) {
                        const reader = new FileReader();
                        reader.onload = function(e) {
                            const col = document.createElement('div');
                            col.className = 'col-md-3 col-sm-4 col-6';
                            col.innerHTML = `
                                <div class="image-preview-item">
                                    <img src="${e.target.result}" alt="Preview" class="img-fluid rounded">
                                    <div class="image-name">${file.name}</div>
                                </div>
                            `;
                            previewContainer.appendChild(col);
                        };
                        reader.readAsDataURL(file);
                    }
                });
                
                imagePreview.appendChild(previewContainer);
            }
        });
    }
});


// Add loading animation to payment button
document.addEventListener('DOMContentLoaded', function() {
  const paymentButton = document.querySelector('.payment-page .btn-primary');
  
  if (paymentButton) {
    paymentButton.addEventListener('click', function() {
      this.classList.add('loading');
      this.innerHTML = 'Processing Payment...';
    });
  }
  
  // Add success animation to cards on load
  const cards = document.querySelectorAll('.payment-page .card');
  cards.forEach((card, index) => {
    setTimeout(() => {
      card.classList.add('success-pulse');
    }, index * 100);
  });
});


// Add loading animation to payment button
document.addEventListener('DOMContentLoaded', function() {
  const paymentButton = document.querySelector('.payment-page .btn-primary');
  const paymentSelect = document.getElementById('paymentMethod');
  
  if (paymentButton) {
    paymentButton.addEventListener('click', function(e) {
      if (paymentSelect.value === '') {
        e.preventDefault();
        alert('Please select a payment method first!');
        paymentSelect.focus();
        return;
      }
      this.classList.add('loading');
      this.innerHTML = 'Processing Payment...';
    });
  }
  
  // Add success animation to cards on load
  const cards = document.querySelectorAll('.payment-page .card');
  cards.forEach((card, index) => {
    setTimeout(() => {
      card.classList.add('success-pulse');
    }, index * 100);
  });
  
  // Update button text based on selected payment method
  if (paymentSelect) {
    paymentSelect.addEventListener('change', function() {
      if (paymentButton) {
        switch(this.value) {
          case 'esewa':
            paymentButton.innerHTML = 'Pay With eSewa';
            break;
          case 'qr':
            paymentButton.innerHTML = 'Pay With QR Code';
            break;
          case 'cod':
            paymentButton.innerHTML = 'Confirm Cash on Delivery';
            break;
          default:
            paymentButton.innerHTML = 'Select Payment Method';
        }
      }
    });
  }
});

