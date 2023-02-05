$(document).ready(function(e) {
  $('button').click(function(e){
    console.log('this is the click');
    e.preventDefault();
    alert("HI");
    // ("#loadPage").load(("stats.html");
  });
});