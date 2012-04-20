var inputs;

$("document").ready(function() { 
	inputs = $('[autosave="true"]') ;
	Dajaxice.setup({'default_exception_callback': function(){ console.log('Error!'); }});
});


function send_ajax(obj) {
	$.autoSave.saving[ obj ] = true;
	var val;
	if (obj.id == 'id_tags') {
		var temp=[];
		$('.edit-view .tagcloud .tag').each(function() { temp.push($(this).text()) });
		temp.push(obj.value);
		val = temp.join(',');
		console.debug("GOT: " + val);	
	}
	else { val = obj.value}
	Dajaxice.practice.exedit(my_callback, {'key':obj.id, 'val':val} );
	$.autoSave._oldObjString[ obj.name ] =  obj.value; 
	//if ( typeof callback == 'function' ) callback( eval( obj ) );
	$.autoSave.saving[ obj ] = false;
}

function my_callback(data){
    if (data==Dajaxice.EXCEPTION){
       console.debug('Error! Something happens!' + data);
     }
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