
let personal_details=document.querySelector('#contact-info')
let submit_form=document.querySelector('#submit-info');
let payment_btn=document.getElementById('make-payment');
let form_input=document.querySelectorAll('.form input');
let Total=document.querySelector('#total');
let form =document.querySelector('form');

if(customer!='AnonymousUser'){
    personal_details.innerHTML='';
}

submit_form.addEventListener('click',(event)=>{
event.preventDefault();
payment_btn.style.display='block';
submit_form.style.display='none';

form_input.forEach(input=>{
    input.setAttribute('readonly','true');
})
})


//payment_btn.addEventListener('click',submitValues);
let submit_paypal = document.querySelector('#payment-heading');
submit_paypal.addEventListener('click',submitValues);

function submitValues(){

var ContactInfo ={
'Name':null,
'Email':null,
'Total':'{{orders.total_order_value}}'
};

var ShippingInfo ={
'address':form.address.value,
'city':form.city.value,
'state':form.state.value,
'zipcode':form.zipcode.value
};

if(customer=='AnonymousUser'){
    ContactInfo.Name=form.name.value;
    ContactInfo.Email=form.email.value;
}
else{
    ContactInfo.Name=customer;
    ContactInfo.Email='{{request.user.email}}';
}

let url='/processdata/'

fetch(url,{
    method:"POST",
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'shippinginfo':ShippingInfo,'contactinfo':ContactInfo})
})
.then(
    function(response){
        alert('Transaction Completed by '+ customer);
        location.href='http://127.0.0.1:8000/';
        return response.json;
    }
)
.then((data) => {
    console.log(data);

})

}

//register-form


