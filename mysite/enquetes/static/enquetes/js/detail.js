function choice(id){
    clearChoice();
    document.querySelector("#choice"+id).checked = true;
    div = document.getElementsByClassName('choice')[id-1];
    div.setAttribute("class","choice active");

}

function clearChoice(){
    div = document.getElementsByClassName('choice')[0];
    div.setAttribute("class","choice");
    div = document.getElementsByClassName('choice')[1];
    div.setAttribute("class","choice");
    div = document.getElementsByClassName('choice')[2];
    div.setAttribute("class","choice");
}