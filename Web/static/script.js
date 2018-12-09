
M.AutoInit();

var elem = document.getElementById('message');
elem.addEventListener('keypress', function(e){
  if (e.keyCode == 13) {
    console.log(elem.value);
  }
});

console.log(result);
elem.value = result;

var slider = document.getElementById('noise');
console.log(noisy);
slider.value = noisy*100;

document.getElementById('paritycheck').value = res_a;
document.getElementById('hadamard').value = res_b;
document.getElementById('hamming').value = res_c;