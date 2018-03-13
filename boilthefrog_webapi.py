function fetchPath(source, dest) {
    ga_track('frog', 'fetchPath',  source + ' ==== ' + dest);
    var url = "http://labs2.echonest.com/ArtistGraphServer/find_path";
    var url = "http://smarterplaylists.playlistmachinery.com/frog/path";

    $("#xbuttons").hide();
    info("Creating path between " + source + " and " + dest);
    setURL(source, dest, skipList);
    $.getJSON(url, {src : source, dest : dest, skips:skipList.join(",")}, function(data) {
            var list = $("#list");
            list.empty();
            if (data.status == 'ok' && data.path.length >= 2) {
                info("");
                curArtistPath = data.path;
                var msg = 'Found a path from ' + data.path[0].name + ' to ' + data.path[data.path.length -1].name + ' in ' 
                    + data.path.length + ' tracks. '  
                info(msg);
                showPath(curArtistPath);
                let firstArtist = curArtistPath[0].name;
                let lastArtist = curArtistPath[curArtistPath.length - 1].name;
                $("#source").val(firstArtist);
                $("#dest").val(lastArtist);
                $("#time-info").show();
                $("#path-time").text(Math.round(data.pdelta));
                $("#total-time").text(Math.round(data.fdelta));
            } else {
                error("Sorry, "  + data.reason);
            }
        }
    );
}