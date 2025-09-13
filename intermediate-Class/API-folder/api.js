function displayTemperature(response) {
  console.log(response);

  let currentTemperature = Math.round(response.data.temperature.current);
  console.log(currentTemperature);

  let city = response.data.city;
  let country = response.data.country;
  //   let description = response.data.condition.description;

  let h1 = document.querySelector("h1");
  h1.innerHTML = `It is ${currentTemperature} degrees in ${city}, ${country}`;
}

let city = "Abuja";
let apiKey = "8abadf7ae1834fobb53bf70t75fb8311";
let apiUrl = `https://api.shecodes.io/weather/v1/current?query=${city}&key=${apiKey}&units=metric`;
axios.get(apiUrl).then(displayTemperature);
