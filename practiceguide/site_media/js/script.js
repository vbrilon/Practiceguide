$("document").ready(function() {
	alert(window.location);
	if ((window.location.hash) && (window.location.hash.substring(1) == 'login')) {
		window.parent.location = "/";
	}
	$('*[data-modal]').click(function(e) {
		e.preventDefault();
		var href = $(e.target).attr('href');
		$('<iframe class="modal" src="' + href + '"></iframe>').modal({
			backdrop: "static",
			keyboard: true,
			show: true
		}).appendTo('body');
	});
});
