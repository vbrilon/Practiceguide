$("document").ready( function() {
	if ((window.location.hash) && (window.location.hash.substring(1) == 'login')) {
		window.parent.location = "/";
	}
});