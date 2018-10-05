window.onload = function () {

var chart = new CanvasJS.Chart("chartSpeed", {
	animationEnabled: true,
	theme: "dark1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Average orbital speed of planets"
	},
	axisY: {
		title: "km/s"
	},
	data: [{
		type: "column",
		showInLegend: true,
		legendMarkerColor: "grey",
		legendText: "Planets",
		dataPoints: [
			{ y: 47.36,  label: 'Mercury' },
			{ y: 35.02,  label: "Venus" },
			{ y: 29.78,  label: "Earth" },
			{ y: 24.00,  label: "Mars" },
			{ y: 13.07,  label: "Jupiter" },
			{ y: 9.68,  label: "Saturn" },
			{ y: 6.80,  label: "Uranus" },
			{ y: 5.43,  label: "Neptune" },
			{ y: 4.67,  label: "Pluto" },
			{ y: 2, label: 'Unknown'}
		]
	}]
});
chart.render();

}