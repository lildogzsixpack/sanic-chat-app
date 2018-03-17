$(document).ready(function() {
    $("#nickForm").on('submit', function(e) {
        e.preventDefault();
        $("#msgBox").removeClass('hide');
        $("#nickForm").hide('swing');
    });
});

$("#form").on('submit', function (e) {
    e.preventDefault();

    var data = $("#btn-input").val();
    console.log(data);
    $("#btn-input").val("");
});