$(document).ready(function () {

    let map = L.map('map', {
        scrollWheelZoom: false 
    }).setView([48.7936, -70.9532], 14); // Central Park coordinates

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors",
    }).addTo(map);

    let markerBounds = [];
    
    // Add markers for each location
    for (let [name, coords] of Object.entries(map_coordinates)) {
        if (coords.x && coords.y && detail["location"].includes(name)) { 
            let circleMarker = L.circleMarker([coords.x, coords.y], {
                radius: 9,
                fillColor: "#9A7F70", 
                color: "white", 
                weight: 4,
                opacity: 1,
                fillOpacity: 1
            }).addTo(map);
            
            circleMarker._path.setAttribute("aria-label", `Location: ${name}`);
            circleMarker._path.setAttribute("role", "button"); 

            circleMarker.bindPopup(`<b>${name}</b>`).openPopup();
            markerBounds.push([coords.x, coords.y]);
        } 
    }

    // Fit bound 
    if (markerBounds.length > 0) {
        const bounds = L.latLngBounds(markerBounds); 
        map.fitBounds(bounds, {
            padding: [50, 50], 
            maxZoom: 15 
        });
    }

    $(".edit-button").on("click", function (event) {
        window.location.href = `/edit/${detail.id}`;
    })

});