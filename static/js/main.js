
$(document).ready(function() {
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

    // redirectToForum function definition
    function redirectTo(category) {
        window.location.href = "{% url 'to_forum' '' %}".slice(0, -1) + category;
    }
});