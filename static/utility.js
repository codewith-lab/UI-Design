export function add_warning(selector, message) {
    selector.append(`<div class = "warning"">${message}</div>`)
}

export function add_word_cnt_warning(text_length, low_limit = 10, high_limit = 500){
    if(text_length < low_limit || text_length > high_limit){
        add_warning($("#description").closest(".add-form"), `Description must be between ${low_limit} to ${high_limit}  words.`);
        return true;
    }
    return false
}

export function get_word_cnt(){
    $("#description").on("input", function () {
        let text = $(this).val().trim(); 
        let text_length = text === "" ? 0 : text.split(/\s+/).length;
        $("#word-count").text(text_length); 

        $("#description").closest(".add-form").find(".warning").remove();
        add_word_cnt_warning(text_length);
    })
}

export function is_valid_url(url) {
    try {
        new URL(url);
        //let response = await fetch(url, { method: "HEAD", mode: "no-cors" });
        return true; 
    } 
    catch (error) {
        console.log("Error");
        console.log(error);
        return false; 
    }
}

export function validate_data() {

    $(".warning").remove();

    let name = $("#name").val().trim();
    let season = $("#season").val() || []; 
    let location = $("#location").val() || []; 
    let description = $("#description").val().trim();
    let word_cnt = description === "" ? 0 : description.split(/\s+/).length;
    let image_url = $("#image-url").val().trim();
    let size = $("#size").val().trim();
    let fragrance = $("#fragrance").val().trim();
    let color = $("#color").val().trim();
    let family = $("#family").val().trim();
    let genus = $("#genus").val().trim();
    let species = $("#species").val().trim();
    let origin = $("#origin").val().trim();
    let attribute = $("#attribute").val() || []; 

    let is_valid = true;
    let first_invalid = null;

    if (!name) {
        add_warning($("#name").closest(".add-form"), "Name is required.");
        $("#name").val("");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#name");
    }
    if (season.length === 0) {
        add_warning($("#season").closest(".add-form"), "Select at least one season.");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#season");
    }
    if (location.length === 0) {
        add_warning($("#location").closest(".add-form"), "Select at least one location.");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#location");
    }
    if (add_word_cnt_warning(word_cnt)) {
    
        if (word_cnt == 0){
            $("#description").val("");
        }

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#description");
    }
    if (!image_url) {
        add_warning($("#image-url").closest(".add-form"), "Image URL is required.");
        $("#image-url").val("");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#image-url");
    }
    else if (!is_valid_url(image_url)){
        add_warning($("#image-url").closest(".add-form"), "Image URL is not valid.");
        is_valid = false;
        if (!first_invalid) first_invalid = $("#image-url");
        console.log(is_valid, first_invalid);
    }
    if (!size) {
        add_warning($("#size").closest(".add-form"), "Size is required.");
        $("#size").val("");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#size");
    }
    if (!fragrance) {
        add_warning($("#fragrance").closest(".add-form"), "Fragrance is required.");
        $("#fragrance").val("");
        
        is_valid = false;
        if(!first_invalid) first_invalid =  $("#fragrance");
    }
    if (!color) {
        add_warning($("#color").closest(".add-form"), "Color is required.");
        $("#color").val("");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#color");
    }
    if (!family) {
        add_warning($("#family").closest(".add-form"), "Family is required.");
        $("#family").val("");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#family");
    }
    if (!genus) {
        add_warning($("#genus").closest(".add-form"), "Genus is required.");
        $("#genus").val("");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#genus");
    }
    if (!species) {
        add_warning($("#species").closest(".add-form"), "Species is required.");
        $("#species").val("");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#species");
    }
    if (!origin) {
        add_warning($("#origin").closest(".add-form"), "Origin is required.");
        $("#origin").val("");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#origin");
    }
    if (attribute.length === 0) {
        add_warning($("#attribute").closest(".add-form"), "Select at least one attribute.");

        is_valid = false;
        if(!first_invalid) first_invalid =  $("#attribute");
    }

    let new_data = null;
    if (is_valid) {
        new_data = {
            "name": name,
            "image": image_url,
            "summary": description,
            "location": location,
            "bloom dates": season,
            "plant size": size,
            "fragrance": fragrance,
            "color": color,
            "origin": origin,
            "family": family,
            "genus": genus,
            "species": species, 
            "attribute": attribute,
        };
    }
    return { first_invalid, new_data };
}

export function ajax_error_message(request, status, error){

    console.log("Error");
    console.log(request);
    console.log(status);
    console.log(error);
    $(".add-status").html("An error occurred while saving the data. Please try again.");
    $("html, body").animate({scrollTop: $(".add-status").offset().top - 250}, 5);

}