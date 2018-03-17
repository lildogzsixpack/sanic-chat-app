$(document).ready(function() {
    $("#nickForm").on('submit', function(e) {
        e.preventDefault();
        $("#msgBox").removeClass('hide');
        $("#nickForm").hide('swing');
    });
});

$("#form").on('submit', function (e) {
    e.preventDefault();
    var nickName =$("#nickField").val();
    var data = $("#btn-input").val();
    var node = [
        '<div class="row message-bubble">',
        '<p id="nick" class="text-muted">' + nickName + '</p>',
        '<span id="msg">' + data + '</span>',
        '</div>'
    ].join('');


    $("#newMsg").append(node);
    $("#btn-input").val("");
});