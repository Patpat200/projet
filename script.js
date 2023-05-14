// 2eme methode


// const btn1 = document.getElementById("btn1")
// const btn2 = document.getElementById("btn2")
// const btn3 = document.getElementById("btn3")
// const btn4 = document.getElementById("btn4")
// const btn5 = document.getElementById("btn5")
// const btn6 = document.getElementById("btn6")
// const btn7 = document.getElementById("btn7")




let box = document.querySelector(".joli"),
  input = document.querySelector("input");

input.addEventListener("input", () => {
  box.style.borderRadius = input.value;
  box.style.background = input.value;

});


btn1.onclick = () => document.body.style.backgroundColor = "blue";
btn2.onclick = () => document.body.style.backgroundColor = "red";
btn3.onclick = () => document.body.style.backgroundColor = "green";
btn4.onclick = () => document.body.style.backgroundColor = "purple";
btn5.onclick = () => document.body.style.backgroundColor = "yellow";
btn6.onclick = () => document.body.style.backgroundColor = "white";
btn7.onclick = () => document.body.style.backgroundColor = "black";


window.onscroll = function() {stickyNavbar()};

function stickyNavbar() {
  if (window.pageYOffset >= 50) {
    document.querySelector(".animated-text").classList.add("sticky");
  } else {
    document.querySelector(".animated-text").classList.remove("sticky");
  }
}


