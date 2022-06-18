let getWinApps = require('get-win-apps');
 
getWinApps
    .getApps()
    .then(apps => console.log(apps))
    .catch(err => console.log(err));
 
    // OUTPUT: [{ displayName: string, displayIcon: string, installLocation: string }]