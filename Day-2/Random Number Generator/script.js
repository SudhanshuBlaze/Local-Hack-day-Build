
var n=prompt("Enter the upper bound");
function gen(n){
    let randomNum=Math.round(Math.random()*n);
    console.log(randomNum);
    document.querySelector("h2").innerText="Refresh to Generate Random Number Between 0 to "+n;
    document.querySelector("p").innerText=randomNum;
}

gen(n);