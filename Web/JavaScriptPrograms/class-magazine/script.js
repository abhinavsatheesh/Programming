var x = document.getElementById("myAudio");
$("#flipbook").turn({
		width: 400,
		height: 300,
		autoCenter: true
});

$("#pageFld").val($("#flipbook").turn("page"));

$("#flipbook").bind("turned", function(event, page, view) {
		$("#pageFld").val(page);
});

$("#pageFld").change(function() {
		var value_entered = parseInt($(this).val())
		if (value_entered%2 == 0) {
			$("#flipbook").turn("page", $(this).val());
			x.play()
		}
		else {
			value_entered = value_entered++
			$("#flipbook").turn("page", value_entered);
			x.play()
		}
});

$("#prevBtn").click(function() {
		$("#flipbook").turn("previous");
		x.play()
});

$("#nextBtn").click(function() {
		$("#flipbook").turn("next");
		x.play()
});