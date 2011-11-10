Modernizr.load([{
    load: {
        'jquery'    :   'js/jquery-1.6.2.min.js',
        'jqueryui'  :   'js/jquery-ui-1.8.16.custom.min.js'
        },

    complete: function () {
        onComplete();
    }
}]);

function displayPauta(data) {
    $.each(data, function(name, value){
        $("#pautas").append('<div class="pauta">');
            $.each(value, function(name, value){
                $("#pautas .pauta:last-child").append("Campo: "+name+" | ");
                $("#pautas .pauta:last-child").append(value+"<br/>");
                $("#pautas .pauta:last-child").append("<br/>");
            }); 
        $("#pautas .pauta:last-child").append('<a href="" class="linkvotar">Votar</a></br>');
        $("#pautas .pauta:last-child").append('<a href="" class="linkdeliberar">Deliberar</a></br>');
        $("#pautas .pauta:last-child").append('<a href="" class="linkcomentar">Comentar</a></br>');
        $("#pautas").append('</div>');
    });
}

function doAjaxCall(type, url, data, callback) {
    $.ajax({
        type: type,
        url: url,
        dataType: "jsonp",
        data: data,
        success: callback
    });
}

function useTemplate(template, data, container) {
    if (template) {
        container.empty();
        template.tmpl(data).appendTo(container);
    }
}

function onComplete() {
    $("#votar").dialog({
        autoOpen: false,
        buttons: {
            "Ok": function() {
                $(this).dialog("close");
            },
            "Cancel": function() {
                $(this).dialog("close");
            }
        }
    });

    $(".linkvotar").live("click", function() {
        $("#votar").dialog('open');
        return false;
    });

    baseUrl = "http://127.0.0.1:8000/";

    doAjaxCall("GET",baseUrl+"api/pautas/","",displayPauta); 
    

}
