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