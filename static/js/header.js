// header.js

$(document).ready(function() {
    console.log("DOM loaded");

    // Ensure the menu is hidden when the page loads
    $('#menuList').hide();

    // menu button
    $('#menuButton').click(function() {
        $('#menuList').css('display', 'flex') // Ensure the display is set to flex
                       .hide()
                       .slideDown(500);
    });

    $('.menu-close-btn').click(function() {
        $('#menuList').slideUp(500, function() {
            $(this).css('display', 'none');
        });
    });

    // Ensure the menu is hidden when navigating back to the page
    $(window).on('pageshow', function(event) {
        if (event.originalEvent.persisted) {
            $('#menuList').hide();
        }
    });
});