import { get_word_cnt, validate_data, ajax_error_message } from './utility.js';

function edit_data(new_data){
    $.ajax({
        type: "POST",
        url: "/edit_data",                
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(new_data),
        success: function(result){
            let edited_data = result["data_to_edit"];
            let edit_status = result["status"];
            let countdown = 3;

            $("#redirectModal").modal("show");
            document.querySelector(".dialog-btn-l").classList.add("d-none");
            $(".dialog-btn-l").off("click");
            $(".dialog-btn-r").off("click");

            if (edit_status == false) {
               $(".dialog-status").html("Edit Failed")
               $(".dialog-message").html("Nothing has changed, are you sure?")
               $(".dialog-btn-r").html("Go Back");
            }
            else {
                $(".dialog-status").html("Edit Successful")
                $(".dialog-message").html(
                    `You will be redirected to the view in <span id = "countdown">${countdown}</span> seconds.`
                );
                $(".dialog-btn-r").html("Stay").click(function() {
                    window.location.href = `/edit/${edited_data.id}`; 
                });

                let countdownInterval = setInterval(() => {
                    countdown--;
                    $("#countdown").text(countdown);

                    if (countdown <= 0) {
                        clearInterval(countdownInterval);
                        window.location.href = `/view/${edited_data.id}`; 
                    }
                }, 1000); 
            }
        },
         error: function(request, status, error){
            ajax_error_message(request, status, error);
        }
    });
}

function get_page_id() {
    let path = window.location.pathname.split('/');
    let id = path[path.length - 1];
    return id;
}

function submit_data() {
    $("#edit-data").on("click", function (event) {

        event.preventDefault(); 

        let { first_invalid, new_data } =  validate_data();

        if (first_invalid) {
            $("html, body").animate(
                {scrollTop: first_invalid.offset().top - 250}, 5
            );

            first_invalid.focus();
            return;
        }
        new_data["id"] =  get_page_id();
        edit_data(new_data);

    });
}

function discard_change() {
    $("#discard-data").on("click", function (event) {

        event.preventDefault(); 

        $("#redirectModal").modal("show");
        document.querySelector(".dialog-btn-l").classList.remove("d-none");
        $(".dialog-btn-l").off("click");
        $(".dialog-btn-r").off("click");

        $(".dialog-status").html("Edit Failed")
        $(".dialog-message").html("Are you sure to discard the change?");

        let id = get_page_id();
        $(".dialog-btn-l").html("Yes").click(function() {
            window.location.href = `/view/${id}`; 
        });
        $(".dialog-btn-r").html("No");

    });
}

function prepopulate(){

    $("#name").val(detail["name"]);
    $("#season").val(detail["bloom dates"] || []);
    $("#location").val(detail["location"] || []);
    $("#description").val(detail["summary"]);
    $("#image-url").val(detail["image"]);
    $("#size").val(detail["plant size"]);
    $("#fragrance").val(detail["fragrance"]);
    $("#color").val(detail["color"]);
    $("#family").val(detail["family"]);
    $("#genus").val(detail["genus"]);
    $("#species").val(detail["species"]);
    $("#origin").val(detail["origin"]);
    $("#attribute").val(detail["attribute"] || []); //note case sensitive 
    $("#word-count").text($("#description").val().split(/\s+/).length);

}

$(document).ready(function() {

    prepopulate();
    get_word_cnt();
    submit_data();
    discard_change();

})