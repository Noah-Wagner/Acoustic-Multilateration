/**
 * Created by noah on 3/12/17.
 */


var data = new vis.DataSet();
var counter = 0;
var steps = 50;
var axisMax = 314;
var axisStep = axisMax / steps;
for (var x = 0; x < axisMax; x+=axisStep) {
    for (var y = 0; y < axisMax; y+=axisStep) {
        var value = (Math.sin(x/50) * Math.cos(y/50) * 50 + 50);
        data.add({id:counter++,x:x,y:y,z:value,style:value});
    }
}

var options = {
    width:  '500px',
    height: '552px',
    style: 'surface',
    showPerspective: true,
    showGrid: true,
    showShadow: false,
    keepAspectRatio: true,
    verticalRatio: 0.5

};

var container = document.getElementById('visualization');
var graph3d = new vis.Graph3d(container, data, options);

