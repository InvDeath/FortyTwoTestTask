/**
 * Created by ideath on 10.10.2015.
 */
$(document).ready(function () {
    var formObject = $("#contacts-edit-form"),
        inputs = $("#contacts-edit-form input, #contacts-edit-form textarea");

    function block_form() {
        inputs.prop("disabled", true);
        $("#loading").show();

    }

    function unblock_form() {
        inputs.prop("disabled", false);
        $("#loading").fadeOut('fast');
    }

    var options = {
        beforeSubmit: function () {
            block_form();
        },
        success: function (resp) {
            var response = JSON.parse(resp);
            $('#id_img_photo').attr('src', response.photo);
            unblock_form();
            $("#success").show();
            setTimeout(function () {
                $("#success").fadeOut("slow");
            }, 2000);
        },
        error: function (resp) {
            unblock_form();
            $(".list-error").remove();
            var errors = JSON.parse(resp.responseText);
            for (error in errors) {
                var id = '#id_' + error;
                $(id).parent('li').append('<span class="list-error">' +
                    errors[error] + '</span>');
            }
        }
    };

    formObject.ajaxForm(options);
});
