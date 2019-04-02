
$('.dropdown-trigger').dropdown();


$(".alert").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});


$(document).ready(function() {
//  Get the lat-long cords
//    if (navigator.geolocation) {
//            var currentPosition = '';
//            navigator.geolocation.getCurrentPosition(function(position){
//                currentPosition = position;
//    //            set lat-long
//                var latitude = currentPosition.coords.latitude;
//                var longitude = currentPosition.coords.longitude;
//                console.log(currentPosition);
//        });
//
//    };
    $('.sidenav').sidenav();

    $(document).ready(function() {
        $('select').formSelect();
    });



});


