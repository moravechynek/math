c_btn = document.getElementById('c_btn');
equals_btn = document.getElementById('equals_btn');
input = document.getElementById('input');

btn_0 = document.getElementById('btn_0');
btn_1 = document.getElementById('btn_1');
btn_2 = document.getElementById('btn_2');
btn_3 = document.getElementById('btn_3');
btn_4 = document.getElementById('btn_4');
btn_5 = document.getElementById('btn_5');
btn_6 = document.getElementById('btn_6');
btn_7 = document.getElementById('btn_7');
btn_8 = document.getElementById('btn_8');
btn_9 = document.getElementById('btn_9');

btn_plus = document.getElementById('btn_plus');
btn_minus = document.getElementById('btn_minus');
btn_mult = document.getElementById('btn_mult');
btn_div = document.getElementById('btn_div');
btn_opened = document.getElementById('btn_opened');
btn_closed = document.getElementById('btn_closed');

c_btn.addEventListener("click", clear);
equals_btn.addEventListener("click", evaluate_calculation);
btn_0.addEventListener("click",function(){add_symbol(0)});
btn_1.addEventListener("click",function(){add_symbol(1)});
btn_2.addEventListener("click",function(){add_symbol(2)});
btn_3.addEventListener("click",function(){add_symbol(3)});
btn_4.addEventListener("click",function(){add_symbol(4)});
btn_5.addEventListener("click",function(){add_symbol(5)});
btn_6.addEventListener("click",function(){add_symbol(6)});
btn_7.addEventListener("click",function(){add_symbol(7)});
btn_8.addEventListener("click",function(){add_symbol(8)});
btn_9.addEventListener("click",function(){add_symbol(9)});

btn_plus.addEventListener('click',function(){add_symbol('+')});
btn_minus.addEventListener('click',function(){add_symbol('-')});
btn_mult.addEventListener('click',function(){add_symbol('*')});
btn_div.addEventListener('click',function(){add_symbol('/')});
btn_opened.addEventListener('click',function(){add_symbol('(')});
btn_closed.addEventListener('click',function(){add_symbol(')')});

function clear(){
    console.log('field cleared')
    input.value = "";}
function evaluate_calculation(){
    console.log('calculation evaluated')
    try{
        input.value = eval(input.value); // security risk
    }
    catch (error){
        input.value = error;
    }}
function add_symbol(symbol){
    console.log('1 has been written')
    input.value += symbol;}