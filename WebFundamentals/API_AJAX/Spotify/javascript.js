// find template and compile it
var templateSource = document.getElementById('results-template').innerHTML
template = Handlebars.compile(templateSource),
resultsPlaceholder = document.getElementById('results'),
playingCssClass = 'playing',
audioObject = null;

//retrieve your token_type and token from your Spotify developer account
var CLIENT_ID = '896230cae67c4759977e721ddfa5c429'
var CLIENT_SECRET = '3b77df91b16f4e68bd64749f88b2bc23'

curl -X GET "https://api.spotify.com/v1/albums/0sNOF9WDwhWunNAHPD3Baj" -H "Authorization: Bearer {your access token}"

var fetchTracks = function (albumId, callback) {
$.ajax({
    url: 'https://api.spotify.com/v1/albums/' + albumId,
    success: function (response) {
        callback(response);
    }
});
};

var searchAlbums = function (query) {
$.ajax({
    url: 'https://api.spotify.com/v1/search',
    data: {
        q: query,
        type: 'album'
    },
    success: function (response) {
        resultsPlaceholder.innerHTML = template(response);
    }
});
};

results.addEventListener('click', function (e) {
var target = e.target;
if (target !== null && target.classList.contains('cover')) {
    if (target.classList.contains(playingCssClass)) {
        audioObject.pause();
    } else {
        if (audioObject) {
            audioObject.pause();
        }
        fetchTracks(target.getAttribute('data-album-id'), function (data) {
            audioObject = new Audio(data.tracks.items[0].preview_url);
            audioObject.play();
            target.classList.add(playingCssClass);
            audioObject.addEventListener('ended', function () {
                target.classList.remove(playingCssClass);
            });
            audioObject.addEventListener('pause', function () {
                target.classList.remove(playingCssClass);
            });
        });
    }
}
});

document.getElementById('search-form').addEventListener('submit', function (e) {
e.preventDefault();
searchAlbums(document.getElementById('query').value);
}, false);