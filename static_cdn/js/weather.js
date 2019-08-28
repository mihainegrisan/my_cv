const notificationElement = document.querySelector(".notification");
const iconElement = document.querySelector(".weather-icon");
const tempElement = document.querySelector(".temperature-value p");
const descElement = document.querySelector(".temperature-description p");
const locationElement = document.querySelector(".location p");

// App data
const weather = {};

weather.temperature = {
    unit : "celsius"
}

const key = '5b0518f89c86ea27c70d5fc6a1a45e3c'
// http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=5b0518f89c86ea27c70d5fc6a1a45e3c'
// api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}

// SET USER'S POSITION
const setPosition = position => {
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;

    getWeather(latitude, longitude);
}

// SHOW ERROR WHEN THERE IS AN ISSUE WITH GEOLOCATION SERVICE
const showError = error => {
    notificationElement.style.display = "block";
    notificationElement.innerHTML = `<p> ${error.message} </p>`;
}

// CHECK IF BROWSER SUPPORTS GEOLOCATION
if("geolocation" in navigator){
    navigator.geolocation.getCurrentPosition(setPosition, showError)
}else{
    notificationElement.style.display = "block"; // to make it visible first then show it
    notificationElement.innerHTML = "<p>Browser Doesn't Support Geolocation.</p>";
}


// GET WEATHER FROM API PROVIDER
const getWeather = (latitude, longitude) => {
    let api = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=${key}`;

    // sent the request then you'll get a response
    fetch(api)
        .then( function(response){
            let data = response.json();
            return data;
        })
            .then( function(data){
                weather.temperature.value = Math.floor(data.main.temp)
                weather.description = data.weather[0].description;
                weather.iconId = data.weather[0].icon;
                weather.city = data.name;
                weather.country = data.sys.country;
            })
                .then( function(){
                    displayWeather();
                });

};


// DISPLAY WEATHER TO UI
function displayWeather(){
    iconElement.innerHTML = `<img src="${img_path}/${weather.iconId}.png" />`;
    tempElement.innerHTML = `${weather.temperature.value} ° <span>C</span>`;
    descElement.innerHTML = weather.description;
    locationElement.innerHTML    = `${weather.city}, ${weather.country}`;
}


// C to F conversion
const celsiusToFahrenheit = temperature => (temperature * 9/5) + 32;


// WHEN THE USER CLICKS ON THE TEMPERATURE ELEMENET
tempElement.addEventListener("click", function(){
    if(weather.temperature.value === undefined) return;
    if(weather.temperature.unit === "celsius" ){
        let fahrenheit = celsiusToFahrenheit(weather.temperature.value);
        fahrenheit = Math.floor(fahrenheit);
        tempElement.innerHTML = `${fahrenheit} ° <span>F</span>`;
        weather.temperature.unit = "fahrenheit";
    }else{
        tempElement.innerHTML = `${weather.temperature.value} ° <span>C</span>`;
        weather.temperature.unit = "celsius";

    }
});
