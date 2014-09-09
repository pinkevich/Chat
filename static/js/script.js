function show() {
    $.ajax({
        url: "/chat/",
        cache: false,
        contentType: 'application/json; charset=utf-8',
        success: function(json){
            var val = $.parseJSON(json);
            var data = [];
            function result() {
                for (var i = 0; i < val['date'].length; i++) {
                    data += val['date'][i] + '\n' +
                        val['name'][i] + ': ' + val['text'][i] + '\n\n'
                }
            }
            result();
            $("#chat").html(data).scrollTop(9999);
        }
    });
}
$(document).ready(function(){
    show();
    setInterval('show()', 3000);
});