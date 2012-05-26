$(document).ready(function() {
    $("#metronome_bpm_slider").slider({
            min: 60,
            max: 240,
            value: ( $("#metronome_bpm_readout").text() )
        });
    $("#metronome_beats_slider").slider({
            min: 1,
            max: 24,
            value: ( $("#metronome_beats_readout").text() )
        });
    $("#metronome_note_value_slider").slider({
            min: 1,
            max: 24,
            value: ( $("#metronome_note_value_readout").text() )
        });
});