google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawSeriesChart);

    function drawSeriesChart() {

      var data = google.visualization.arrayToDataTable([
        ['Name', 'Position', 'coordinate', 'Type',     'Radius, km'],
        ['Mercury', 1,          3,      'solid surface',  2440**2*3.14],
        ['Venus',   2,          3,      'solid surface',  6052**2*3.14],
        ['Earth',   3,          3,      'solid surface',  6371**2*3.14],
        ['Moon',    3,          2,      'solid surface',  1737**2*3.14],
        ['Mars',    4,          3,      'solid surface',  3390**2*3.14],
        ['Phobos',  4,          2,      'solid surface',  11**2*3.14],
        ['Deimos',  4,          1,      'solid surface',  6**2*3.14],
        ['Jupiter', 5,          3,      'gas surface',    69911**2*3.14],
        ['Saturn',  6,          3,      'gas surface',    58232**2*3.14],
        ['Uranus',  7,          3,      'gas surface',    25362**2*3.14],
        ['Neptune', 8,          3,      'gas surface',    24622**2*3.14],
        ['Pluto',   9,          3,      'solid surface',  1188**2*3.14],
      ]);

      var options = {
        title: 'Sizes of planets',
        titleTextStyle: {color: 'OrangeRed', fontName: 'Harmattan', fontSize: 25},
        backgroundColor: 'black',
        bubble: {textStyle: {color: 'yellow', fontName: 'Harmattan', fontSize: 20},
                 stroke: 'yellow'},
        chartArea: {left:30, top:30, bottom:60, right:30,
                    width: '10%', height: '10%', backgroundColor: '#2F4F4F'},
        sizeAxis: {minSize: 2,  maxSize: 80},
        colorAxis: {legend: {position: 'bottom'}},
        enableInteractivity: true,
        explorer: {axis: ['vertical', 'horizontal'],
                   actions: ['dragToZoom', 'rightClickToReset'], keepInBounds: true,
                   maxZoomIn: .5, maxZoomOut: 10},
        legend: {position: 'bottom', textStyle: {color: 'OrangeRed', fontSize: 16}},
        vAxis: {maxValue: 4},

      };

      var chart = new google.visualization.BubbleChart(document.getElementById('series_chart_div'));
      chart.draw(data, options);
    }