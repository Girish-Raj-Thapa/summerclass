// some scripts

// jquery ready start
$(document).ready(function() {
	// jQuery code


    /* ///////////////////////////////////////

    THESE FOLLOWING SCRIPTS ONLY FOR BASIC USAGE, 
    For sliders, interactions and other

    */ ///////////////////////////////////////
    

	//////////////////////// Prevent closing from click inside dropdown
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });


    $('.js-check :radio').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $('input[name='+ check_attr_name +']').closest('.js-check').removeClass('active');
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');

        } else {
            item.removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });


    $('.js-check :checkbox').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');
        } else {
            $(this).closest('.js-check').removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });



	//////////////////////// Bootstrap tooltip
	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} // end if




    
}); 
// jquery end


// <!-- Optional: JavaScript for auto-dismiss functionality -->
document.addEventListener('DOMContentLoaded', function() {
  // Auto-dismiss alerts after 5 seconds
  const alerts = document.querySelectorAll('.alert.auto-dismiss');
  alerts.forEach(function(alert) {
    setTimeout(function() {
      if (alert && alert.parentNode) {
        alert.classList.remove('show');
        setTimeout(function() {
          if (alert && alert.parentNode) {
            alert.remove();
          }
        }, 300);
      }
    }, 5000);
  });
  
  // Add smooth removal animation when close button is clicked
  const closeButtons = document.querySelectorAll('.alert .btn-close');
  closeButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      const alert = this.closest('.alert');
      alert.style.animation = 'slideOutRight 0.3s ease-in forwards';
    });
  });
});


document.addEventListener('DOMContentLoaded', function() {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function(alert) {
    setTimeout(function() {
      // Bootstrap native way to close alert
      bootstrap.Alert.getOrCreateInstance(alert).close();
    }, 5000); // auto-hide after 5 seconds
  });
});

