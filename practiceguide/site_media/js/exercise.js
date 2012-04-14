$("document").ready(function() {
	//create the error displays
	$('.edit-view [error^="err:"]').each( function(index) {
		$(this).after('<br><span class="error-message">' + $(this).attr('error').substring(4) + '</span>');
	});
});