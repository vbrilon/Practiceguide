$("document").ready(function() {
	$('*[data-modal]').click(function(e) {
		e.preventDefault();
		var href = $(e.target).attr('href');
		if (href.indexOf('#') == 0) {
			$(href).modal('show');
		} else {
			$('<iframe class="modal" src="' + href + '"></iframe>').modal('show').appendTo('body');
		}
	});
});

/*
$("document").ready(function() {
	$('*[data-modal]').click(function(e) {
		e.preventDefault();
		var href = $(e.target).attr('href');
		if (href.indexOf('#') == 0) {
			$(href).modal('show');
		} else {
			$.get(href, function(data) {
				$('<div class="modal">' + data + '</div>').modal('show').appendTo('body');
			});
		}
	});
});
*/
