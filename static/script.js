
const show_data = function() {             
  var xhttp = new XMLHttpRequest();  
  
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      var text = document.getElementById("btn").innerHTML =
      xhttp.responseText;
      console.log("text2:",text);
    }
  };     
  
  xhttp.open("GET", "/show_data/")   
   
      
  xhttp.send();
}


function get_result(){
 var input_text=document.getElementById('result');  
  console.log(input_text); 
    let xml = new XMLHttpRequest();
    xml.onreadystatechange = function() {
        if (xml.readyState == 4 && xml.status == 200) {
          result = input_text;

          console.log(result);
        }
      };
    xml.open("GET", '/result', true)
    xml.send()
}

// const show_result = function() {             
//   var xhttp = new XMLHttpRequest();  
//   
//   xhttp.onreadystatechange = function() {
//     if (xhttp.readyState == 4 && xhttp.status == 200) {
//       var text = document.getElementById("result").innerHTML =
//       xhttp.responseText;
//       // console.log("result:",text);
//     }
//   };     
  
//   xhttp.open("GET", "/")   
//    
//       
//   xhttp.send();
// }


function add_data(){
         
  var xhttp = new XMLHttpRequest();            
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {

    }
  };    
  xhttp.open("POST", "/")
      
    xhttp.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');        
    xhttp.send("input_text=" + document.getElementById('input_text').value);
}

window.onload = function() {
  // let add_btn = document.getElementById('add_data'); 
  //add_btn.addEventListener('click', add_data, this);
   show_data();
  //  show_result();
  //  add_data();
  }