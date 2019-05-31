
$('.dropdown-trigger').dropdown();


$(".alert").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});

// DataTable internationalization
function getLanguage() {
    var lang = navigator.language || navigator.userLanguage;
    return '//cdn.datatables.net/plug-ins/1.10.7/i18n/'+langMap[lang]+'.json'
}

var langMap = {
   'en' : 'English',
   'pl' : 'Polish',
}


$(document).ready(function() {

    $('#dataTable').dataTable({
        language: {
            url: getLanguage()
        }
    });

    $('.sidenav').sidenav();

    $(document).ready(function() {
        $('select').formSelect();
    });

});






