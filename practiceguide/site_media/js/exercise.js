$("document").ready(function() {
	//create the error displays
	$('.edit-view [error^="err:"]').each( function(index) {
		$(this).after('<br><span class="error-message">' + $(this).attr('error').substring(4) + '</span>');
	});
	
    $('.edit-view .tagcloud').tagit({
		removeConfirmation: true,
		allowSpaces: true
	});
	
	/*
	$('.edit-view .tag-close').each( function(index) {
		$(this).click( function(event) {	
			event.preventDefault();
			$(this).parent().remove() 
		});
	});
	*/
});