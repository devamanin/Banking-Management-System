let loginButton = document.getElementsByClassName('login-button')[0];
loginButton.addEventListener("click", function(){
  document.getElementById("my-form").submit();
})



// loginButton.addEventListener("click", function(){
//     data = {customerId: "23dsf2fsd", password: "23dasd"}
//     fetch("http://127.0.0.1:5000/login",{
//         method: 'POST',
//         headers: {
//           'Accept': 'application/json, text/plain, */*',
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({customerId: "2343dfsd", password: "asdfsafds3"})
//     })
//     .then(function(res){ return res.json(); })
//     .then(function(data){ alert( JSON.stringify( data ) ) })
// })