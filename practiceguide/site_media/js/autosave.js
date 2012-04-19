var inputs;

$("document").ready(function() { 
	inputs = $('[autosave="true"]') ;
});

function send_ajax(obj) {
	$.autoSave.saving[ obj ] = true;
	Dajaxice.practice.myedit(my_callback, {'id':obj.id, 'val':obj.value} );
	$.autoSave._oldObjString[ obj.name ] =  obj.value; 
	//if ( typeof callback == 'function' ) callback( eval( obj ) );
	$.autoSave.saving[ obj ] = false;
}

function my_callback(data){
	//alert("Got: " + data);
} 

(function($) {	
	// setup the interval function as singleton via document.ready.
	$(function () { 
		$.autoSave.intervalId = $.autoSave.intervalId || window.setInterval( function () { 
			if (typeof $.autoSave == 'function') 
			$.autoSave( $.autoSave.callback ); 
		}, 3000 );
	});
	$.autoSave = function ( callback ) {
		$.autoSave._oldObjString = $.autoSave._oldObjString || {};
		$.autoSave.saving = $.autoSave.saving || {};
		// loop through each autoSave obj, detect changes and save if so - through closures of $.each()
		$.each(inputs, function (index, obj) {
			// only if the object has changed value in any way - this is a semi-expensive operation
			if ( obj.value.length > 0 &&  obj.value != $.autoSave._oldObjString[ obj.name ] && !$.autoSave.saving[ obj ] ) {	
				send_ajax(obj);
				
			}
		});
	}
})(jQuery);