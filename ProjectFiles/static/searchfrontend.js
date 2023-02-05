$(document).ready(function(e) {
  $('button').click(function(e){
    console.log('this is the click');
    e.preventDefault();
    alert("HI");
    // ("#loadPage").load(("stats.html");
  });
});


function getNYTWordMap(){
  let url = "/getNYTWordMap"

  fetch(url).then(response => response.json()).then(output => displayInfo(output)).catch(error => displayError(error))
}

function displayInfo(output){
  console.log(output)
}

function displayError(error){
  console.log("Error occurred fetching url")
  console.log(error)
}