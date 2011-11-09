Modernizr.load([{
    load: {
        'jquery'    :   'js/jquery-1.6.2.min.js',
        'jqueryui'  :   'js/jquery-ui-1.8.16.custom.min.js'
        },

    complete: function () {
        onComplete();
    }
}]);


function onComplete() {
    baseUrl = "http://127.0.0.1:8000/";

    $
    function doAjaxCall(type, url, data, callback) {
        $.ajax({
            type: type,
            url: url,
            dataType: "json",
            data: data,
            success: callback
        });
    }

    function test(anyvar) {
        console.log(anyvar);
    }

    $("#pautas").click(function () {
        doAjaxCall("GET", baseurl+"api/pautas/",data,test);
    });
}
