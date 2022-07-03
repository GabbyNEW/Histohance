function toggleMethodOptions($active, $inactive) {
   $active.addClass('active');
   $inactive.removeClass('active');
}

$(function() {
   $('#methodDHE').on('click', function(e) { toggleMethodOptions($('#methodDHE'), $('#methodHE')) })
   $('#methodHE').on('click', function(e) { toggleMethodOptions($('#methodHE'), $('#methodDHE')) })
});