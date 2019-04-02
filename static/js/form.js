$(document).ready(function() {

	$('form').on('submit', function(event) {
//        AJAX CALL TO RECEIVE DATA
		$.ajax({
			data : {
//			VARIABLE : $ (NAME OF HTML INPUT). TEXT VALUE(),
				county : $('#county').val(),
			},
//			Specify Type of request
			type : 'POST',
//			Flask Route
			url : '/addresses'
		})
//		AFTER AJAX CALL
		.done(function(data) {

			if (data.county) {
//			 GET THE DIV --> SHOW THE ERROR MSG FROM DICT
				$('#county_choice').text(data.county).show();
//			HIDE THE OTHER OBJECT
//				$('#successAlert').hide();
			}
			else {
//				$('#successAlert').text(data.name).show();
//				$('#errorAlert').hide();
			}

		});
//        PREVENT DEFAULT FORM BEHAVIOR
		event.preventDefault();

	});

});