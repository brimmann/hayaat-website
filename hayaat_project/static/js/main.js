let state = 0;
jQuery('#menu-icon').on('click', function () {
    if (state === 0) {
        jQuery('#close').css('display', 'none')
        jQuery('#open').css('display', 'block')
        jQuery('#drop-menu').css('display', 'flex');
        state = 1;
    } else {
        jQuery('#close').css('display', 'block')
        jQuery('#open').css('display', 'none')
        jQuery('#drop-menu').css('display', 'none');
        state = 0;
        
    }
})





