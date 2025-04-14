$(document).ready(function() {    

    $("#search-form").on("submit", function(event) {
        event.preventDefault(); 
        event.stopPropagation();

        let query = $("#search-form input").val().trim();
        if (query === "") 
            $("#search-form input").val("").focus();
        else
            window.location.href = `/search-results?q=${encodeURIComponent((query))}`;
    });
    
});