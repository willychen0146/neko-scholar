// header.js

$(document).ready(function() {
    console.log("DOM loaded");

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
});