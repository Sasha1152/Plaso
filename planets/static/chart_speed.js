google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {

      var data = google.visualization.arrayToDataTable([
        ['Planet', 'Speed', {role: 'style'}],
        ['Mercury', 47.36, 'color: gray'],
        ['Venus', 35.02, 'color: yellow'],
        ['Earth', 29.78, 'color: blue'],
        ['Mars', 24.00, 'color: red'],
        ['Jupiter', 13.07, 'color: #871B47'],
        ['Saturn', 9.68, 'color: #871B47'],
        ['Uranus', 6.80, 'color: #871B47'],
        ['Neptune', 5.43, 'color: #871B47'],
        ['Pluto', 4.67, 'color: #871B47'],
      ]);

      var options = {
        title: 'Speed of planets',
        titleTextStyle: {color: 'OrangeRed', fontName: 'Harmattan', fontSize: 25},
        backgroundColor: 'black',
        hAxis: {
          format: 'h:mm a',
          viewWindow: {
            min: [7, 30, 0],
            max: [17, 30, 0]
          }
        },
        vAxis: {
          title: 'Speed, km/s'
        }
      };

      var chart = new google.visualization.ColumnChart(
        document.getElementById('chart_div'));

      chart.draw(data, options);
    }