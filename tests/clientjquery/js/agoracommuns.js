Modernizr.load({
    'jquery'    :   'jquery-1.6.2.min.js',
    'jqueryui'  :   'jquery-ui-1.8.16.custom.min.js'
});

function doAjaxCall(type, url, data, callback) {
    $.ajax({
        type: type,
        url: url,
        dataType: "json",
        data: data,
        success: callback
    });
}
