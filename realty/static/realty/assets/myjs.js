//header
function myHeaderfix() {
    let scroll = window.scrollY;
    let scrollStart = 100;
    let myheader = document.querySelector('#myheader');
    let mybody = document.querySelector('body');
    const changeHeader = () =>  myheader.classList.add('fixhead');
    const changeBody = () => mybody.classList.add('mtbody');
    const removeHeader = () =>  myheader.classList.remove('fixhead');
    const removeBody = () => mybody.classList.remove('mtbody');

    window.addEventListener('scroll' , () =>{
        scroll = window.scrollY;
        if (scroll >= scrollStart) { changeHeader(), changeBody() }
        else{ removeHeader(), removeBody() }
    })
}
myHeaderfix();
//realry string



    
    
    
    
    
    
    

    
    
    
    
    
    
    
    