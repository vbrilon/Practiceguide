$("document").ready(function() {
	//create the error displays
	$('.edit-view [error^="err:"]').each( function(index) {
		$(this).after('<br><span class="error-message">' + $(this).attr('error').substring(4) + '</span>');
	});
	var tags = $('.edit-view .tagcloud');
	tags.tagit({
		removeConfirmation: true,
		allowSpaces: true,
		placeholderText: "Tags for this exercise",
		onTagAdded: function(event, tag) { addTag(tags.tagit('tagLabel',tag)) },
		onTagRemoved: function(event, tag) { removeTag(tags.tagit('tagLabel',tag))}
	});
	
	function timestamp() {
		timechanged.text($.format.date(jQuery.now(), 'h:mm:ss a'));
	}
	
	function addTag(tag) {
		Dajaxice.practice.tag(my_callback, {'tag':tag, 'method':'ADD'} );
		timestamp();
	}
	function removeTag(tag) {
		Dajaxice.practice.tag(my_callback, {'tag':tag, 'method':'REMOVE'} );
		timestamp();
	}
	
	function my_callback(data){
		if (data==Dajaxice.EXCEPTION){
			console.debug('Error! Something bad happened!' + data);
		}
	}
});


