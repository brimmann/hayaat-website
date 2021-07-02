let state = 0;
jQuery('#menu-icon').on('click', function () {
    if (state === 0) {
        jQuery('#drop-menu').css('display', 'flex');
        state = 1;
    } else {
        jQuery('#drop-menu').css('display', 'none');
        state = 0;
        
    }
})




