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
    var pautaAtual;
    var counter = 1;
    $.each(data, function(name, value){
        $("#pautas").append('<h3>'+value.titulo+'</h3>');
        $("#pautas").append('<div class="pauta"><ul>');

        pautaAtual = $("#pautas .pauta:last-child");
        pautaAtual.append("<li>pauta: " + value.pauta + "</li>");
        pautaAtual.append("<li>status: "+ value.status + "</li>");
        pautaAtual.append("<li>Data de Cria&ccedil;&atilde;o: "+ value.data_criacao + "</li>");
        pautaAtual.append("<li>Data para Valida&ccedil;&atilde;o: "+ value.data_validacao + "</li>");
        pautaAtual.append("<li>Data para Vota&ccedil;&atilde;o: "+ value.data_votacao + "</li>");
        pautaAtual.append("<li>Votos para Promo&ccedil;&atilde;o a Pauta: "+ value.votos_promover + "</li>");

        pautaAtual.append('<a href="' +counter+ '" class="linkdeliberacoes">Deliberacoes</a>');
        pautaAtual.append('<a href="" class="linkcomentarios">Coment&aacute;rios</a>');

        pautaAtual.append('<a href="" class="linkvotar">Votar</a>');
        pautaAtual.append('<a href="" class="linkdeliberar">Deliberar</a>');
        pautaAtual.append('<a href="" class="linkcomentar">Comentar</a>');
        $("#pautas").append('</div>');
        counter++;
    });


    $("#pautas").accordion(); 
    $(".pauta a").button();
    $("#favor, #contra").button();
}

function displayDelibera(data) {
    var deliberacoes = $("#deliberacoes");
    deliberacoes.append("<ul>");
    $.each(data, function(name, value){
        deliberacoes.append("<li>" + value.proposta + "</li>");
    });
    deliberacoes.append("</ul>");
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
    $("#votar, #comentar, #deliberar, #deliberacoes, #comentarios").dialog({
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

    $(".linkcomentar").live("click", function() {
        $("#comentar").dialog('open');
        return false;
    });


    $(".linkdeliberar").live("click", function() {
        $("#deliberar").dialog('open');
        return false;
    });

    $(".linkdeliberacoes").live("click", function() {
        var id = $(this).attr("href");
        $("#deliberacoes").empty();
        $("#deliberacoes").dialog('open');
        doAjaxCall("GET",baseUrl + "api/pauta/" + id + "/deliberacoes/","",displayDelibera); 
        return false;
    });

    $(".linkcomentarios").live("click", function() {
        $("#comentarios").dialog('open');
        return false;
    });

    baseUrl = "http://127.0.0.1:8000/";
//    baseUrl = "http://hera.ethymos.com.br:1080/agoracommuns/";


    doAjaxCall("GET",baseUrl+"api/pautas/","",displayPauta); 
    

}
