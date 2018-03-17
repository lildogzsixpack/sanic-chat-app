var ws = null;

$(document).ready(function() {
    $("#nickForm").on('submit', function(e) {
        e.preventDefault();
        $("#msgBox").removeClass('hide');
        $("#nickForm").hide('swing');
        ws = new WebSocket("ws://" + location.host + "/chat?nickname=" + $("#nickField").val());
        ws.onmessage = function (event) {
            var data = JSON.parse(event.data);

            var node = [
                '<div class="row message-bubble">',
                '<p id="nick" class="text-muted">' + data['nickname'] + '</p>',
                '<span id="msg">' + data['message'] + '</span>',
                '</div>'
            ].join('');

            $("#newMsg").append(node);
            $("#btn-input").val("");

            $("#msgContainer").scrollTop($("#msgContainer")[0].scrollHeight);
        };
    });
});

$("#form").on('submit', function (e) {
    e.preventDefault();

    var data = $("#btn-input").val();
    ws.send(data);
});
