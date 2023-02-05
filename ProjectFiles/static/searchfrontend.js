window.onload = function() {
  $('#searchButton').click(function(e){
    e.preventDefault();
    var inputString = jQuery("#countryInput").val();
    var clickme = document.getElementById("loadPage");
    clickme.style.display = "block";
    jQuery('#country').html(inputString);

  });
};


function getNYTWordMap(country){
  let url = "/getNYTWordMap?country=" + country

  fetch(url).then(response => response.json()).then(output => displayInfo(output)).catch(error => displayError(error))
}

function displayInfo(output){
  console.log(output)
}

function displayError(error){
  console.log("Error occurred fetching url")
  console.log(error)
}