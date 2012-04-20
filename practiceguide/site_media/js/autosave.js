var inputs;
var virgin = $('.edit-view .virgin');
var saving = $('.edit-view .exercise-save-in-progress');
var saved = $('.edit-view .exercise-saved');
var timechanged = $('.edit-view .exercise-saved-time');

$("document").ready(function() { 
	inputs = $('[autosave="true"]') ;
	Dajaxice.setup({'default_exception_callback': function(){ console.log('Error!'); }});
});

function timestamp() {
	timechanged.text($.format.date(jQuery.now(), 'h:mm:ss a'));
}
function send_ajax(obj) {
//		console.debug("GOT: " + obj.id);	
	virgin.addClass('hidden'); saving.removeClass('hidden'); saved.addClass('hidden');
	$.autoSave.saving[ obj ] = true;
	Dajaxice.practice.exedit(my_callback, {'key':obj.id, 'val':obj.value} );
	$.autoSave._oldObjString[ obj.name ] =  obj.value; 
	//if ( typeof callback == 'function' ) callback( eval( obj ) );
	$.autoSave.saving[ obj ] = false;
	saving.addClass('hidden'); virgin.addClass('hidden'); saved.removeClass('hidden');
	timestamp();
}

function my_callback(data){
    if (data==Dajaxice.EXCEPTION){
       console.debug('Error! Something bad happened!' + data);
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
				//console.debug(obj.value + "--" + $.autoSave._oldObjString[ obj.name ] );	
				send_ajax(obj);
				
			}
		});
	}
})(jQuery);