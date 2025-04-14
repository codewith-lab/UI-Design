import { get_word_cnt, validate_data, ajax_error_message } from './utility.js';

function save_data(new_data){
    $.ajax({
        type: "POST",
        url: "/add_data",                
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(new_data),
        success: function(result){
            let added_data = result["data_to_add"];
            $(".add-status").html(
                `New item successfully created.
                <a class = "link" href = "/view/${added_data.id}">See it here!</a>`
            );

            $("html, body").animate(
                {scrollTop: $(".add-status").offset().top - 250}, 5
            );

            $(".add-more .add-form input[type='text'], .add-more .add-form input[type='url'], .add-more .add-form textarea").val("");
            $(".add-basic .add-form input[type='text'], .add-basic .add-form input[type='url'], .add-basic .add-form textarea").val("");
            $(".add-form select").prop("selectedIndex", 0); 
            $(".add-form select[multiple]").val([]);
            $("#name").focus();
        },
        error: function(request, status, error){
            ajax_error_message(request, status, error);
        }
    });
}

function submit_data() {
    $("#add-data").on("click", function (event) {

        event.preventDefault(); 

        let { first_invalid, new_data } =  validate_data();

        if (first_invalid) {
            $("html, body").animate(
                {scrollTop: first_invalid.offset().top - 250}, 5
            );

            first_invalid.focus();
            return;
        }
        save_data(new_data);
    });
}

$(document).ready(function () {

    get_word_cnt();
    submit_data();

});