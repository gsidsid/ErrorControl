
var elem = document.getElementById('message');
elem.addEventListener('keypress', function(e){
  if (e.keyCode == 13) {
    console.log(elem.value);
  }
});

console.log(result);
elem.value = result;

document.getElementById('paritycheck').value = res_a;