$('#waiting-btn').click(function(){
	$("#waitList").css("display", "block");
	$("#seatList").css("display", "none");
	$("#takeAwayList").css("display", "none");

	$("#waiting-btn").css("border-bottom", "5px solid #FBE74B");
	$("#seating-btn").css("border-bottom", "none");
	$("#takeAway-btn").css("border-bottom", "none");
	})
$('#seating-btn').click(function(){
	$("#waitList").css("display", "none");
	$("#seatList").css("display", "block");
	$("#takeAwayList").css("display", "none");

	$("#waiting-btn").css("border-bottom", "none");
	$("#seating-btn").css("border-bottom", "5px solid #FBE74B");
	$("#takeAway-btn").css("border-bottom", "none");
	})
$('#takeAway-btn').click(function(){
	$("#waitList").css("display", "none");
	$("#seatList").css("display", "none");
	$("#takeAwayList").css("display", "block");

	$("#waiting-btn").css("border-bottom", "none");
	$("#seating-btn").css("border-bottom", "none");
	$("#takeAway-btn").css("border-bottom", "5px solid #FBE74B");
	})

$('#waiting').click(function(){
	$("#waitingForm").css("display", "block");
	$("#seatingForm").css("display", "none");
	$("#takeAwayForm").css("display", "none");

	$("#wCheck").css("display", "inline-block");
	$("#sCheck").css("display", "none");
	$("#tCheck").css("display", "none");

	})

$('#seating').click(function(){
	$("#waitingForm").css("display", "none");
	$("#seatingForm").css("display", "block");
	$("#takeAwayForm").css("display", "none");

	$("#wCheck").css("display", "none");
	$("#sCheck").css("display", "inline-block");
	$("#tCheck").css("display", "none");

	})

$('#takeAway').click(function(){
	$("#waitingForm").css("display", "none");
	$("#seatingForm").css("display", "none");
	$("#takeAwayForm").css("display", "block");

	$("#wCheck").css("display", "none");
	$("#sCheck").css("display", "none");
	$("#tCheck").css("display", "inline-block");

	})



$( "#Sadd1" ).click(function() {
		var value = parseInt($( "#SsizeBox").val());
		$( "#SsizeBox" ).val(value+1);
  	})

$( "#Ssub1" ).click(function() {
	var value = parseInt($( "#SsizeBox").val());	
	$( "#SsizeBox" ).val(value-1);
	})

$( "#Wadd1" ).click(function() {
	var value = parseInt($( "#WsizeBox").val());
	$( "#WsizeBox" ).val(value+1);
	})

$( "#Wsub1" ).click(function() {
	var value = parseInt($( "#WsizeBox").val());		
	$( "#WsizeBox" ).val(value-1);
	})


$("#aloo").click(function() {
	alert("hi");
	console.log("o");
})
$("#doneSeating").on('click', function () {
	alert("hi");
    var checkbox_value = "";
    $(":checkbox").each(function () {
        var ischecked = $(this).is(":checked");
        if (ischecked) {
            checkbox_value += $(this).val() + "|";
        }
    });
    alert(checkbox_value);
    // your awesome code calling ajax
}); 