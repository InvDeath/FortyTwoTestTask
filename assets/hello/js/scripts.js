/**
 * Created by ideath on 07.10.2015.
 */
var isActive, maxRequest, newCount, docTitle;

function getMaxRequestNumber() {
    var max = 0;
    $('#requests li').each(function (key, value) {
        if ($(value).data('request-id') > max) {
            max = $(value).data('request-id');
        }
    });
    return max;
}

function updateTabCounter(count) {
    document.title = count + ' new requests - ' + docTitle;
}

window.onfocus = function () {
    isActive = true;
    document.title = docTitle;
};

window.onblur = function () {
    isActive = false;
};

function executeUpdate() {
    $.ajax({
        url: "/requests/"
    }).done(function (records) {
        records.reverse();
        $('#requests').html('');
        records.forEach(function (rec) {
            $('#requests').append(
                '<li data-request-id="' + rec.pk +
                '">' + rec.fields.title + '<br>' + rec.fields.time +
                '<pre style="border: dotted;">' + rec.fields.request + '</pre></li>'
            );
        });
        if (isActive) {
            newCount = 0;
            document.title = docTitle;
            maxRequest = records[records.length - 1].pk;
        } else {
            newCount = records[records.length - 1].pk - maxRequest;
            updateTabCounter(newCount);
        }
    });
    setTimeout(executeUpdate, 3000); // you could choose not to continue on failure...
}

$(document).ready(function () {
    docTitle = document.title;
    maxRequest = getMaxRequestNumber();
    setTimeout(executeUpdate, 3000);
});