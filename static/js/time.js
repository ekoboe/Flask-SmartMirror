/*
file: time.js
main time display on mirror homepage, live updating
*/

// Small function to convert military time to 12 hour time
function hours12(date) {return (date.getHours() + 24) % 12 || 12;}

function update_time() {

	var d = new Date();  // Javascript date object to fetch updated date

	// Ternary to add leading zero to date
	var hour = (hours12(d) < 10 ? '0' : '') + hours12(d);  // Returns normal 12 hour hour (not military)
	var minute = (d.getMinutes() < 10 ? '0' : '') + d.getMinutes();  // minute count
	var day = d.getDate();  // Get full month day number

	// Convert day and month int to string representation
	var day_name = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][d.getDay()];
	var month_name = ["January", "February", "March", "April", "May", "June",
	"July", "August", "September", "October", "November", "December"][d.getMonth()];
	
	// Set the updated time to the clock
	$('#time-top').text(hour + ":" + minute);
	$('#time-mid').text(day_name);
	$('#time-bottom').text(month_name + ' ' + day);	

}

setInterval(update_time, 1000);  // Update the time every second