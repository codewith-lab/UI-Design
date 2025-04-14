function get_start_end_month(months){
    if (months.length == 1) return months[0];
    return `${months[0]} - ${months[months.length-1]}`;
}

function get_most_popular(top = 5) { 

    const month_names = [
        "January", 
        "February", 
        "March", 
        "April", 
        "May", 
        "June",
        "July", 
        "August", 
        "September", 
        "October", 
        "November", 
        "December"
    ];
    let cur_date = new Date();
    let month = month_names[cur_date.getMonth()];
    let nxt_month = month_names[(cur_date.getMonth() + 1) % 12];
    
    let filter_data = [];
    for(key in data) {
        record = data[key];
        if(record["bloom dates"].includes(month) || record["bloom dates"].includes(nxt_month))
            filter_data.push(record);
    };
    filter_data = filter_data.slice(0, top);

    $.each(filter_data, function(index, record){
        let data_entry = $(
            `<a href = "/view/${record.id}">
                <div class = "home-image">
                    <img src = ${record.image} class = "img-fluid" alt = "${record.name}" title = "${record.name}">
                <div>
            </a>
            <div class>
                <span class = "text-minor">${get_start_end_month(record["bloom dates"])}</span>
                <br>
                ${record.name} 
                <br>
                <span class = "text-minor">Locations:</span> <span class = "text-medium">${record.location.join(' / ')}</span>
            </div>`);
        $(`#image-${index + 1}`).append(data_entry);
    });
}

$(document).ready(function() {

    get_most_popular();
    
});