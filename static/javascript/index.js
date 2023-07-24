function reviewShow(){
document.getElementById("pro-img").style.opacity="100%"
document.querySelector("#hma").style.filter="brightness(0.4)"
}   function reviewHide(){
    document.getElementById("pro-img").style.opacity="0%"
    document.querySelector("#hma").style.filter="brightness(1)"
    }
   var header =document.getElementsByTagName("header")[0];
    var body =document.getElementsByTagName("body")[0];
    var mnav =document.getElementsByClassName("mnav")[0];

  function dark(){
        document.getElementById("moon").style.display = "none"
        document.getElementById("suni").style.display = "inline-flex"
    body.classList.toggle("body-dark")
    header.classList.toggle("body-dark")
    mnav.classList.toggle("body-dark")
    
}
    function light(){
        document.getElementById("suni").style.display = "none"
        document.getElementById("moon").style.display = "inline-flex"
        body.classList.toggle("body-dark")
        header.classList.toggle("body-dark")
        mnav.classList.toggle("body-dark")
 
    }
    function pr(){console.log("thank you for watching!")}
       var vidi= document.getElementById("vidi");
       vidi.addEventListener("ended", pr)
       function signup(name,lastname){
this.name=name;
this.lastname=lastname;
       }
function submitform(){
var fn=document.getElementById("name").value
var ln=document.getElementById("namee").value
var user1=new signup(fn ,ln)
var greeting="hi,"+user1.name+""+user1.lastname+"welcome";
document.getElementById("object").textContent=greeting;
}
    