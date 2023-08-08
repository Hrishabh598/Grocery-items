let searchF = document.querySelector('.search-form');
let shopCart = document.querySelector('.shopping-cart');
let login = document.querySelector('.info');
let nb = document.querySelector('.navbar');


document.querySelector('#search-btn').onclick = () =>{
    searchF.classList.toggle('active');
    shopCart.classList.remove('active');
    login.classList.remove('active');
    nb.classList.remove('active');
};

document.querySelector("#cart-btn").onclick = () =>{
    shopCart.classList.toggle('active');
    searchF.classList.remove('active');
    login.classList.remove('active');
    nb.classList.remove('active');
};


document.querySelector("#login-btn").onclick = () =>{
    login.classList.toggle('active');
    searchF.classList.remove('active');
    shopCart.classList.remove('active');
    nb.classList.remove('active');
};


document.querySelector("#menu-btn").onclick = () =>{
    nb.classList.toggle('active');
    searchF.classList.remove('active');
    shopCart.classList.remove('active');
    login.classList.remove('active');
};

window.onscroll = () =>{
    searchF.classList.remove('active');
    shopCart.classList.remove('active');
    login.classList.remove('active');
    nb.classList.remove('active');
}

var swiper = new Swiper(".product-slider", {
    loop:true,
    spaceBetween: 20,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    centeredSlides: true,
    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1020: {
            slidesPerView: 3,
        },
    },
});

var swiper = new Swiper(".review-slider", {
    loop:true,
    spaceBetween: 20,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    centeredSlides: true,
    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1020: {
            slidesPerView: 3,
        },
    },
});

if(localStorage.getItem('cart')==null){
        var cart = {};
    }
    else{
        cart = JSON.parse(localStorage.getItem('cart'));
    }
$('.ct-btn').click(function(){
    document.getElementById('cart-btn').innerHTML=JSON.parse(document.getElementById('cart-btn').innerHTML)+1;
    var idstr = this.id.toString();
    if(cart[idstr] != undefined){
        cart[idstr] = cart[idstr]+1;
    }
    else{
        cart[idstr]=1;
    }
    localStorage.setItem('cart',JSON.stringify(cart));
});

var n = 0
for(var c in cart){
    n+=(cart[c])
}
document.getElementById('cart-btn').innerHTML = n

$('.check-out').click(function(){
    localStorage.clear()
})














