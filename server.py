from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import copy
from datetime import datetime

app = Flask(__name__)

map_coordinates = {
    "Shakespeare Garden": {
        "x": 40.7787,
        "y": -73.9686,
    },
    
    "Conservatory Garden": {
        "x": 40.7936,
        "y": -73.9532,
    },

    "North Woods": {
        "x": 40.7945,
        "y": -73.9568,
    },

    "The Ramble": {
        "x": 40.7775,
        "y": -73.9695,
    },
     
    "Reservoir": {
        "x": 40.7831,
        "y": -73.9592,
    },

    "Hallett Nature Sanctuary": {
        "x": 40.7695,
        "y": -73.9755,
    }
}

data = {
"1": { 
    "id": "1",
    "name": "Huldine Clematis",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/huldine_clematis_c_l_2020-11-11-202839.jpg",
    "summary": "This perennial vine requires a support structure to grow properly. Its pearly white flowers feature six non-overlapping petals, with dramatic reddish details on the petals' undersurface. In Conservatory Garden, it can be seen in the South Garden.",
    "location": ["Conservatory Garden"],
    "bloom dates": ["May", "June"],
    "bloom season": ["Spring", "Summer"],
    "plant size": "10-15 feet tall",
    "fragrance": "Mild",
    "color": "White with pale lavender streaks",
    "origin": "Europe (cultivated in France)",
    "family": "Ranunculaceae",
    "genus": "Clematis",
    "species": "Clematis 'Huldine'",
    "attribute": ["Perennial", "Vine"],
    "nearby plants": ["3", "4", "5", "7", "8", "10"],
    "similar plants": ["4"],
    },

"2": { 
    "id": "2",
    "name": "Montauk Daisy",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/montauk-daisy-l_2020-11-11-202819.jpg",
    "summary": "The Montauk daisy originated in Japan but today it can be found around the world. This plant grows well in many conditions, though it prefers highly acidic soil with full sun. The daisy opens in the morning and closes at night.",
    "location": ["Shakespeare Garden"],
    "bloom dates": ["October"],
    "bloom season": ["Fall"],
    "plant size": "1-2 feet tall",
    "fragrance": "Mild, fresh",
    "color": "White with yellow center",
    "origin": "Japan",
    "family": "Asteraceae",
    "genus": "Nipponanthemum",
    "species": "Nipponanthemum nipponicum",
    "attribute": ["Perennial"],
    "nearby plants": ["12"],
    "similar plants": ["6"],
    },

"3": { 
    "id": "3",
    "name": "Virginia Bluebells",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/blooms-virginia-bluebell-l_2020-08-10-131049.jpg",
    "summary": "The Virginia bluebell has pendulous, sky-blue flowers opening from pink buds, both of which can be seen on the plant simultaneously. Its leaves are rounded and gray-green, on stems of up to two feet in height. It's a spring ephemeral; after blooming, its leaves will yellow and die back, and disappear from the landscape until it comes up again next year. In the Conservatory Garden, you can spot this bloom in the South Garden and Woodland Slope.",
    "location": ["Conservatory Garden", "North Woods", "The Ramble"], 
    "bloom dates": ["March", "April", "May", "June"],
    "bloom season": ["Spring", "Sumner"],
    "plant size": "up to 2 feet tall",
    "fragrance": "Mild, sweet",
    "color": "Sky blue (flowers), pink (buds)",
    "origin": "Eastern North America",
    "family": "Boraginaceae",
    "genus": "Mertensia",
    "species": "Mertensia virginica",
    "attribute": ["Perennial"],
    "nearby plants": ["1", "4", "5", "7", "8", "10"],
    "similar plants": [],
    },

"4": { 
    "id": "4",
    "name": "Christmas Rose",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/blooms-lenten-rose-l_2020-11-11-202829.jpg",
    "summary": "The lenten rose does not actually belong to the rose family; it's a hellebore. It received the name 'rose' because its flowers somewhat resemble a small, single rose. Its evergreen leaves are divided into leathery leaflets with coarsely cut or spiny margins. The nodding flowers, up to two inches across, are usually found in shades of white, rose, green or purple. Take a closer look to see a dark speckled pattern on the inside of its petals. In Conservatory Garden, you can spot this bloom in the South Garden or Woodland Slope.",
    "location": ["Conservatory Garden"], 
    "bloom dates": ["February", "March", "April", "May"],
    "bloom season": ["Spring", "Winter"],
    "plant size": "up to 18 inches tall",
    "fragrance": "None",
    "color": "White, rose, green, or purple",
    "origin": "Europe (Central and Southern)",
    "family": "Ranunculaceae",
    "genus": "Helleborus",
    "species": "Helleborus niger",
    "attribute": ["Perennial", "Evergreen"],
    "nearby plants": ["1", "3", "5", "7", "8", "10"],
    "similar plants": ["1"],
    },

"5": {
    "id": "5",
    "name": "Arkansas Bluestar",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/arkansas-bluestar-l_2020-11-11-202932.jpg",
    "summary": "The Arkansas bluestar is known for its powdery blue flowers and feathery, soft-textured leaves. This native plant is especially remarkable in the fall, when the foliage turns a stunning apricot-yellow. In Conservatory Garden, it can be viewed in the South Garden.",
    "location": ["Conservatory Garden"],
    "bloom dates": ["May"],
    "bloom season": ["Spring"],
    "plant size": "Up to 3 feet tall",
    "fragrance": "Mild, sweet",
    "color": "Powdery blue",
    "origin": "North America",
    "family": "Apocynaceae",
    "genus": "Amsonia",
    "species": "Amsonia hubrichtii",
    "attribute": ["Perennial"],
    "nearby plants": ["1", "3", "4", "7", "8", "10"],
    "similar plants": [],
    },

"6": { 
    "id": "6",
    "name": "New England Aster",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/new-england-aster-l_2020-11-11-202817.jpg",
    "summary": "This hairy perennial grows in clumps with short rhizomes and thick stems, bearing lance-shaped leaves. Violet-purple, flowerheads, with yellow disk florets, bloom to about two inches in diameter.",
    "location": ["Reservoir"],
    "bloom dates": ["November"],
    "bloom season": ["Fall"],
    "plant size": "3-6 feet tall",
    "fragrance": "Mild, earthy",
    "color": "Violet-purple with yellow centers",
    "origin": "North America",
    "family": "Asteraceae",
    "genus": "Symphyotrichum",
    "species": "Symphyotrichum novae-angliae",
    "attribute": ["Perennial"],
    "nearby plants": ["11"],
    "similar plants": ["2"],
    },

"7": {  
    "id": "7",
    "name": "Witch Hazel",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/witch-hazel-l_2020-11-11-202719.jpg",
    "summary": "Witch hazel is a small tree or shrub that is native to England and other parts of western Europe; it can flourish in a wide range of environments. Its fragrant blooms are a pale yellow, and extracts from the plant's bark are used to make facial astringents found in drugstores worldwide.",
    "location": ["Conservatory Garden", "Hallett Nature Sanctuary", "The Ramble", "North Woods"],
    "bloom dates": ["October", "November", "December"],
    "bloom season": ["Fall", "Winter"],
    "plant size": "10-25 feet tall",
    "fragrance": "Sweet, spicy",
    "color": "Pale yellow",
    "origin": "Western Europe, North America",
    "family": "Hamamelidaceae",
    "genus": "Hamamelis",
    "species": "Hamamelis virginiana",
    "attribute": ["Shrub"],
    "nearby plants": ["1", "3", "4", "5", "8", "10"],
    "similar plants": ["8"],
    },

"8": {  
    "id": "8",
    "name": "Buttercup Winterhazel",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/blooms-buttercup-winterhazel-l_2020-11-11-202920.jpg",
    "summary": "Buttercup winterhazel is native to Japan and Taiwan. It gained the English name 'buttercup' for the fragrant buttery-yellow blossoms that herald spring. This plant offers a subtler, softer appearance than the ubiquitous forsythia, which blooms at the same time. At the Conservatory Garden, you can spot the Buttercup winterhazel in the Woodland Slope.",
    "location": ["Conservatory Garden"],
    "bloom dates": ["March", "April"],
    "bloom season": ["Spring"],
    "plant size": "Up to 5 feet tall",
    "fragrance": "Sweet, buttery",
    "color": "Buttery yellow",
    "origin": "Japan, Taiwan",
    "family": "Hamamelidaceae",
    "genus": "Corylopsis",
    "species": "Corylopsis pauciflora",
    "attribute": ["Shrub"],
    "nearby plants": ["1", "3", "4", "5", "7", "10"],
    "similar plants": ["7"],
    },

"9": {  
    "id": "9",
    "name": "Pickerelweed",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/pickerelweed-l_2020-11-11-202941.jpg",
    "summary": "The pickerelweed is native to the eastern United States and the Caribbean. It prefers full to partial sun, and shallow water to wet soil. Its blooms are pale purple and the flowers typically last one to two days.",
    "location": ["North Woods"],
    "bloom dates": ["June", "July", "August", "September"],
    "bloom season": ["Summer", "Fall"],
    "plant size": "1-3 feet tall",
    "fragrance": "Mild, fresh",
    "color": "Pale purple",
    "origin": "Eastern United States, Caribbean",
    "family": "Pontederiaceae",
    "genus": "Pontederia",
    "species": "Pontederia cordata",
    "attribute": ["Perennial"],
    "nearby plants": ["3", "7"],
    "similar plants": [],
    },

"10": {  
    "id": "10",
    "name": "Blue Lacecap Hydrangea",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/blue_lacecap_hydrangea_m_l_2020-11-11-202923.jpg",
    "summary": "This deciduous, rounded shrub is hardy; its lacecap features inner flowers of deep blue and outer ray flowers of either blue or white. The flowers around the outside edge create an enchanting bloom. In Conservatory Garden, it can be found in the North Garden at Mumford Gate.",
    "location": ["Conservatory Garden"],
    "bloom dates": ["May", "June"],
    "bloom season": ["Spring", "Summer"],
    "plant size": "3-6 feet tall",
    "fragrance": "Mild, floral",
    "color": "Deep blue with white or blue outer flowers",
    "origin": "Asia",
    "family": "Hydrangeaceae",
    "genus": "Hydrangea",
    "species": "Hydrangea macrophylla",
    "attribute": ["Shrub"],
    "nearby plants": ["1", "3", "4", "5", "7", "8"],
    "similar plants": [],
    },

"10": {  
    "id": "10",
    "name": "Blue Lacecap Hydrangea",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/blue_lacecap_hydrangea_m_l_2020-11-11-202923.jpg",
    "summary": "This deciduous, rounded shrub is hardy; its lacecap features inner flowers of deep blue and outer ray flowers of either blue or white. The flowers around the outside edge create an enchanting bloom. In Conservatory Garden, it can be found in the North Garden at Mumford Gate.",
    "location": ["Conservatory Garden"],
    "bloom dates": ["May", "June"],
    "bloom season": ["Spring", "Summer"],
    "plant size": "3-6 feet tall",
    "fragrance": "Mild, floral",
    "color": "Deep blue with white or blue outer flowers",
    "origin": "Asia",
    "family": "Hydrangeaceae",
    "genus": "Hydrangea",
    "species": "Hydrangea macrophylla",
    "attribute": ["Shrub"],
    "nearby plants": ["1", "3", "4", "5", "7", "8"],
    "similar plants": [],
    },

"11": {  
    "id": "11",
    "name": "Doublefile Viburnum",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/blooms-doublefile-viburnum-l_2020-11-11-202900.jpg",
    "summary": "The doublefile viburnum is a deciduous shrub native to China, Korea, Japan and Taiwan. A popular ornamental plant, the doublefile viburnum is one of the most striking shrubs in Central Park with its horizontal branches covered in white flowers. When in full, May bloom, its flat-top flower clusters are unforgettable, presenting a beautiful display long after magnolias, cherry trees and crabapples have bloomed.",
    "location": ["Reservoir"],
    "bloom dates": ["April", "May"],
    "bloom season": ["Spring"],
    "plant size": "Up to 10 feet tall",
    "fragrance": "Mild, sweet fragrance",
    "color": "White",
    "origin": "China, Korea, Japan, Taiwan",
    "family": "Adoxaceae",
    "genus": "Viburnum",
    "species": "Viburnum plicatum",
    "attribute": ["Shrub"],
    "nearby plants": ["6"],
    "similar plants": [],
    },

"12": {  
    "id": "12",
    "name": "Pink Shell Azalea",
    "image": "https://s3.amazonaws.com/assets.centralparknyc.org/media/images/_500xAUTO_crop_center-center_none/pink_shell_azalea_c_l_2020-11-11-202811.jpg",
    "summary": "The pink shell azalea is one of the first plants to bloom in the spring; its blooms are deliciously fragrant. Its flowers are soft pink to white, with orange freckles before the shrub's leaves emerge.",
    "location": ["Shakespeare Garden"],
    "bloom dates": ["April"],
    "bloom season": ["Spring"],
    "plant size": "Up to 4 feet tall",
    "fragrance": "Deliciously fragrant",
    "color": "Soft pink to white with orange freckles",
    "origin": "Eastern United States",
    "family": "Ericaceae",
    "genus": "Rhododendron",
    "species": "Rhododendron canescens",
    "attribute": ["Shrub"],
    "nearby plants": ["2"],
    "similar plants": [],
    },
}  

current_id = 12

# ROUTES
@app.route("/")
def home():
   return render_template("home.html", data = data)   

@app.route("/view/<id>")
def view(id = None):
    detail = next((item for item in data.values() if item['id'] == str(id)), None)
    return render_template('view.html', detail = detail, data = data, map_coordinates = map_coordinates)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/edit/<id>")
def edit(id = None):
    detail = next((item for item in data.values() if item['id'] == str(id)), None)
    return render_template("edit.html", detail = detail)

@app.route("/search-results", methods = ["GET"])
def search_results():
    query = request.args.get('q').lower()

    results = []
    data_copy = copy.deepcopy(data) 
    for item in data_copy.values():
        if (query.lower() in item.get("name", "").lower() or
            query.lower() in item.get("summary", "").lower() or
            query.lower() in "".join([i.lower() for i in item.get("location", [])]) or
            query.lower() in "".join([i.lower() for i in item.get("bloom dates", [])]) and 
            item not in results):
            item["location"] = ' / '.join([i for i in item.get("location", [])])
            item["bloom_dates"] = ' / '.join([i for i in item.get("bloom dates", [])])
            results.append(item)

    return render_template("search.html", query = query, results = results, max = max, min = min)

# Auxiliary
def get_season_from_month(month_id):
    season = []
    if 3 in month_id or 4 in month_id or 5 in month_id:
        season.append("Spring")
    if 6 in month_id or 7 in month_id or 8 in month_id:
        season.append("Summer")
    if 9 in month_id or 10 in month_id or 11 in month_id:
        season.append("Fall")
    if 12 in month_id or 1 in month_id or 2 in month_id:
        season.append("Winter")
    return season

def derive_nearby(data_new):
    global data 
    nearby = []
    for item in data.values():
        if str(data_new["id"]) == str(item["id"]):
            continue
        if not set(item["location"]).isdisjoint(set(data_new["location"])):
            if not str(data_new["id"]) in item["nearby plants"]:
                item["nearby plants"].append(str(data_new["id"]))
            nearby.append(item["id"])
    return nearby

def derive_similar(data_new):
    global data
    similar = []
    for item in data.values():
        if str(data_new["id"]) == str(item["id"]):
            continue
        if (item["family"].lower() == data_new["family"].lower() or 
            item["genus"].lower() == data_new["genus"].lower() or 
            item["species"].lower() == data_new["species"].lower()):
            if not str(data_new["id"]) in item["similar plants"]:
                item["similar plants"].append(str(data_new["id"]))
            similar.append(item["id"])
    return similar

# AJAX FUNCTIONS
@app.route("/add_data", methods = ["GET", "POST"])
def add_data():
    global data, current_id

    data_to_add = request.get_json()
    current_id += 1
    data_to_add["id"] = str(current_id)

    # update derived features including season, nearby plants and similar plants
    month_id = set(datetime.strptime(i, "%B").month for i in data_to_add["bloom dates"])
    data_to_add["bloom season"] = get_season_from_month(month_id) 
    data_to_add["nearby plants"] = derive_nearby(data_to_add)
    data_to_add["similar plants"] = derive_similar(data_to_add)

    data[str(current_id)] = data_to_add

    return jsonify(data_to_add = data_to_add)

@app.route("/edit_data", methods = ["GET", "POST"])
def edit_data():
    global data

    data_to_edit = request.get_json()

    month_id = set(datetime.strptime(i, "%B").month for i in data_to_edit["bloom dates"])
    data_to_edit["bloom season"] = get_season_from_month(month_id) 
    data_to_edit["nearby plants"] = derive_nearby(data_to_edit)
    data_to_edit["similar plants"] = derive_similar(data_to_edit)

    if data_to_edit == data[str(data_to_edit["id"])]:
        status = False
    else:
        status = True 
        data[str(data_to_edit["id"])] = data_to_edit

    return jsonify(data_to_edit = data_to_edit, status = status)

if __name__ == "__main__":
   app.run(debug = True, port = 5002)

