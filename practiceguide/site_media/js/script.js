/*
$("document").ready(function() {
	if( $("#signin_modal").length > 0 ) {
		$("#signin_modal").modal({
			keyboard: true
		});
		
		$("#signin_link").click(function( event ) {
			$("#signin_modal").modal("show");
		});
	}
});
*/

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
