//don't let them pay for nothing
let checkout_btn = document.querySelector('.checkout-btn');
let Quantity=document.querySelector('.item-count');

checkout_btn.addEventListener('click',()=>{
console.log(Quantity.innerHTML);
    if(Quantity.innerHTML==0){
        
        alert('Please add some items to the cart ')
        checkout_btn.href="http://127.0.0.1:8000/";
    }
    else{
        checkout_btn.href="http://127.0.0.1:8000/checkout";
    }
}

)