
/**
 * Created by noah on 3/12/17.
 */


var graph = null;
var data = null;
// var SERVER_IP = "https://senior-design-project-155422.appspot.com/"
var SERVER_IP = "http://127.0.0.1:5000/"

$(document).ready(function() {

    initGraph();


    $("#multiLateration").click(function() {
        $.ajax({
            type: "GET",
            url: SERVER_IP + "getsourceloc/?arrivaltimes=.01881666883, .0152187926, .016691024503997, .04124619838260953, .01688116904970476",
            success: function(data) {
                addSourceLoc(JSON.parse(data));
            },
            failure: function(data) {
                console.log(data);
            }
        })
    });
    $("#loadSensors").click(function() {
        $.ajax({
            type: "GET",
            url: SERVER_IP + "getsensorloc/",
            success: function(data) {
                console.log(data);

                updateSensorLocations(JSON.parse(data));

            },
            error: function(data) {
                console.log("failure");
                console.log(data);
            }
        });
    });
    $("#defaultSensors").click(function() {
        console.log("lol");
        $.ajax({
            type: "POST",
            url: SERVER_IP + "updatesensorloc/",
            data: "[[0,0,0],[-2.1,3.1,10],[-1,-3.1,4.5],[3,-5,-6],[5,3,2]]",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(data) {
                console.log(data);

                alert("DEBUG: Default sensor locations sent to server");
            },
            failure: function(data) {
                console.log(data);
            }

        })
    });
    $("#testXD").click(function() {
        console.log("lol");
        console.log(JSON.stringify($('#testlol').serializeArray()));
    });
    $("#submitSensors").click(function() {
        $.ajax({
            type: "POST",
            url: SERVER_IP + "updatesensorloc/",
            data: $('#sensorPos').serialize(),
            success: function(data) {
                console.log(data);
                console.log(JSON.stringify($('#sensorPos').serializeArray()));

                // updateSensorLocations(JSON.parse(data));

            },
            error: function(data) {
                console.log("failure");
                console.log($('#sensorPos').serializeArray());
                console.log(data);
            }
        });
    });
});

function updateSensorLocations(data) {
    addSensorLocations(data)
}


function addSourceLoc(parse) {

    data.add({x: parse[0], y: parse[1], z: parse[2], style:4});

}



function initGraph() {
    data = new vis.DataSet();

    data.add({x: 0, y: 0, z: 0, style:3});

    // specify options
    var options = {
        width: '700px',
        height: '700px',
        style: 'dot-color',
        showPerspective: true,
        showGrid: true,
        keepAspectRatio: true,
        verticalRatio: .2,
        cameraPosition: {
            horizontal: 2.7,
            vertical: 0.0,
            distance: 1.65
        }
    };

    // create our graph
    var container = document.getElementById('mygraph');
    graph = new vis.Graph3d(container, data, options);
}


function addSensorLocations(d) {
    // create th

    // data = new vis.DataSet();
    for (var i = 1; i < 4; i++) {
        data.add({x: d[i + "_x"], y: d[i + "_y"], z: d[i + "_z"], style:3});

    }


}

