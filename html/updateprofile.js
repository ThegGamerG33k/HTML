"use strict";

function submit(){
    let file = document.getElementById("ppic").files[0];
    if(!file){
        file = new Blob();
    }
    let R = new FileReader();
    let path = document.location.pathname;
    R.addEventListener("load", () => {
        let profilepic = btoa(R.result);    //do base64 encoding
        let fname = document.getElementById("fname").value;
        let lname = document.getElementById("lname").value;
        let dob = document.getElementById("birthdate").value;
        let J = {
            firstName: fname,
            lastName: lname,
            birthDate: dob,
            pic: profilepic
        };
        fetch( path,
            {   method: "POST",
                body: JSON.stringify(J)
            }
        ).then( (resp) => {
            //can also use text(), blob(), or arrayBuffer()
            resp.json().then( (J) => {
                console.log("Server said:",J);
            });
        }).catch( (err) => {
            console.log("Uh oh",err);
        })
    });
    R.readAsBinaryString(file);
}