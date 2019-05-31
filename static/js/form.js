var mymap = L.map('mapid').setView([53.41, -7.92], 7);


L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWF4aW11c21pbmltdXMiLCJhIjoiY2puOHlwZ2dwMGMzNDNrb2Rsc3dndTB3NyJ9.F6YVg9QT6hfgNGvy0aUypA', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
}).addTo(mymap);


$(document).ready(function() {
    var marker =  L.marker([53.41, -7.92])
    marker.addTo(mymap);
    $('#geocodeForm').on('submit', function(event) {


            $.ajax({
                data : {
                    county: $('#county').val(),
                    locality : $('#locality').val()
                },
                type : 'POST',
                url : '/find'
            })
            .done(function(data) {
                console.log(data)
                if (data.error) {
                    $('#formError').text(data.error).show();
                    $('#formHeader').hide();
                }
                else {

                    var locality = data.Locality;
                    var longitutde = data.Y;
                    var latitude = data.X;
                    marker.setLatLng([data.Y, data.X]).update;

                    string_Locality = "<b>" + locality + "</b>"
                    string_X = "<b> Long: </b>" +  latitude.slice(0,10)
                    string_Y = "<b> Lat: </b>" +  longitutde.slice(0,10)

                    marker.bindPopup(string_Locality + "<br/>" + string_X + "<br/>" + string_Y ).openPopup();

                }

            });

            event.preventDefault();

    });


});
