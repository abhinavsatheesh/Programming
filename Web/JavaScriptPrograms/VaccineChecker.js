var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const Http = new XMLHttpRequest();
var fs = require('fs');
const url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=682016&date=29-06-2021';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  const object = JSON.parse(Http.responseText)
  console.table(object)
}