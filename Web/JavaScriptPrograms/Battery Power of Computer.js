const battery = require("battery");
 
(async () => {
    const { level, charging } = await battery();
 
    if (level === 1) {
		console.log("You are using a Desktop")
	}
    
	else {
        console.log("Battery Percentage is " + level)
	} 
})();