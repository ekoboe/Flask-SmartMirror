/*
file: weather.js
main weather display on mirror homepage, current temperature and forcast for day
*/

//Function to fetch updated weather from flask server
function update_weather() {

	// Send an ajax post request to get updated weather from flask
	req = $.ajax({
		url : '/update_weather',
		type : 'POST',
		data : {}
	});

	req.done(function(data) {

		// Split the data from the updated weather json
		var desc = data.currentWeather.desc;
		var icon = data.currentWeather.icon;
		var temperature = data.currentWeather.temperature;
		var title = data.currentWeather.title;
		
		// Update the html elements with the data
		$('.weather-current-temp').text(temperature + String.fromCharCode(176));
		$('#weather-current-img').attr('src', '/static/' + icon);
		$('.weather-current-title').text(title);
		$('.weather-current-desc').text(desc);

	});

}

update_weather();  // Update the weather on the boot up

setInterval(update_weather, 600000);  // Update the time every 10 minutes