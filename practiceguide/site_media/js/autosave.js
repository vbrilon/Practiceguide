var inputs;

$("document").ready(function() { 
	inputs = $('[autosave="true"]') ;
});

function send_ajax(obj) {
	$.ajax({data: 'name=' + obj.name +'&value=' + escape(obj.value),
	type: 'POST',
	beforeSend: function () { $.autoSave.saving[ obj ] = true; },
	success: function () { 
		$.autoSave._oldObjString[ obj.name ] =  obj.value; 
		if ( typeof callback == 'function' ) 
		callback( eval( obj ) );
		$.autoSave.saving[ obj ] = false;
	},
	url: '/edit/',
	error: function () { $.autoSave.intervalId = window.clearInterval( $.autoSave.intervalId ); console.log("Error " + e); } });
}

(function($) {	
	// setup the interval function as singleton via document.ready.
	$(function () { 
		$.autoSave.intervalId = $.autoSave.intervalId || window.setInterval( function () { 
			if (typeof $.autoSave == 'function') 
			$.autoSave( $.autoSave.callback ); 
		}, 5000 );
	});
	$.autoSave = function ( callback ) {
		// update timer
		$.autoSave._oldObjString = $.autoSave._oldObjString || {};
		$.autoSave.saving = $.autoSave.saving || {};
		// loop through each autoSave obj, detect changes and save if so - through closures of $.each()
		$.each(inputs, function (index, obj) {
			// only if the object has changed value in any way - this is a semi-expensive operation
			if ( obj.value.length > 0 &&  obj.value != $.autoSave._oldObjString[ obj.name ] && !$.autoSave.saving[ obj ] ) {	
				console.log("Index:" + index + " Value: " + obj.value);
				send_ajax(obj);
				
			}
		});
	}
})(jQuery);