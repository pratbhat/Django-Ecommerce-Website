let product_nav = document.querySelector(' #product ')
let login_nav = document.querySelector(' #login ')
let cart_nav = document.querySelector(' #cart ')
let myorder_nav = document.querySelector(' #order ')
let item_count=document.querySelector(' #item-count-wrapper ');
let username_container=document.querySelector(' .username ');

//nav-bar-active-manipulation
if(window.location.href=="http://127.0.0.1:8000/" ){
    product_nav.classList.add('active');
    login_nav.classList.remove('active');
    myorder_nav.classList.remove('active');
}
else if((window.location.href=="http://127.0.0.1:8000/login/")||(window.location.href=="http://127.0.0.1:8000/register/")){
    product_nav.classList.remove('active');
    login_nav.classList.add('active');
    myorder_nav.classList.remove('active');
}
else if(window.location.href=="http://127.0.0.1:8000/myorders/"){
    product_nav.classList.remove('active');
    login_nav.classList.remove('active');
    myorder_nav.classList.add('active');
}
else{
    product_nav.classList.remove('active');
    login_nav.classList.remove('active');
    cart_nav.style.filter='brightness(90%)';
    item_count.style.filter='brightness(90%)';
}

//ensure it is logged-in user

if(customer!=='AnonymousUser'){
    login_nav.innerHTML='Logout';
    login_nav.href='http://127.0.0.1:8000/logout/'

}
else{
    login_nav.innerHTML='Login';
    login_nav.href='http://127.0.0.1:8000/login/'
    username_container.innerHTML='';
    cart_nav.remove(self);
    myorder_nav.remove(self);
}


//cart_update

let add_to_cart_btns=document.querySelectorAll('.update-cart');

add_to_cart_btns.forEach(btn => {
    btn.addEventListener('click',function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        
        if(customer==='AnonymousUser'){
            alert('User not logged in.We recommend you to login first...');
            location.href='http://127.0.0.1:8000/login/';
        }
        else{
            pass_data(productId,action);
        }
    }
    )    
});

function pass_data(productId,action){
console.log('passing data');
url = '/update_cart/';

fetch(url,{
    method:"POST",
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({"productId":productId,"action":action})
})
.then((request)=>{
    location.reload();
    return request.json();
})
.then((data)=>{
    console.log(data);
})

}

function getCSRFToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCSRFToken('csrftoken');