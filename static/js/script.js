function setActive($object, isActive) {
   if (isActive) {
      $object.addClass('active');
      $object.removeClass('inactive');
   } else {
      $object.addClass('inactive');
      $object.removeClass('active');
   }
}

function toggleMethodOptions($active, $inactive) {
   if ($active.hasClass('active')) {
      setActive($active, false);
      setActive($inactive, false);
   } else {
      setActive($active, true);
      setActive($inactive, false);
   }
}

$(function() {
   $('#methodDHE').on('click', function(e) { toggleMethodOptions($('#methodDHE'), $('#methodHE')) })
   $('#methodHE').on('click', function(e) { toggleMethodOptions($('#methodHE'), $('#methodDHE')) })
});