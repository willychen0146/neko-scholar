
// Theme switch function
function swapStyles(theme) {
    console.log('switch triger')
    document.documentElement.setAttribute('data-theme', theme);
    console.log('data set to', theme)
    localStorage.setItem('theme', theme);
}

// Immediately invoked function to set the theme before the page is fully rendered
(function() {
    console.log('initiate loading theme')
    var savedTheme = localStorage.getItem('theme') || 'light';
    swapStyles(savedTheme);
})();

$(document).ready(function() {
    // Listener for theme bottun switch
    $('#theme-switch-icon').click(function() {
        console.log('bottun click')
        var currentTheme = localStorage.getItem('theme') || 'light';
        var newTheme = (currentTheme === 'dark') ? 'light' : 'dark';
        swapStyles(newTheme);
    });

    // Searching functionality: date
    $('input[name="date_range"]').daterangepicker({
        opens: 'left',
        autoUpdateInput: false,
        locale: {
            cancelLabel: 'Clear',
            format: 'YYYY-MM-DD'
        }
    }).on('apply.daterangepicker', function(ev, picker) {
        // Updates the input with selected dates only when the user applies the selection
        $(this).val(picker.startDate.format('YYYY-MM-DD') + ' to ' + picker.endDate.format('YYYY-MM-DD'));
    }).on('cancel.daterangepicker', function(ev, picker) {
        // Clears the input field when the user cancels the selection
        $(this).val('');
    });
});