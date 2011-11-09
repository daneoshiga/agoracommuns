Modernizr.load({
    'jquery'    :   'jquery-1.6.2.min.js',
    'jqueryui'  :   'jquery-ui-1.8.16.custom.min.js'
});

baseUrl = "http://127.0.0.1:8000/";


function doAjaxCall(type, url, data, callback) {
    $.ajax({
        type: type,
        url: url,
        dataType: "json",
        data: data,
        success: callback
    });
}
