
var n=prompt("Enter the upper bound");

let randomNum=Math.round(Math.random()*n);
console.log(randomNum);
document.querySelector("h2").append(" "+n);
document.querySelector("p").innerText=randomNum;
