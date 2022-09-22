let conv = document.querySelector('.conv')
let patienter = document.querySelector('.patienter')
let spinnerBox = document.querySelector('.sp-box')

let audio = document.querySelector('#audio')

let spinner = document.querySelector('#status-spinner')
let btnText = document.querySelector('.btn-text')


conv.addEventListener('click', function(){
    spinner.classList.add('spinner-border')
    spinner.classList.add('spinner-border-sm')
    
    spinnerBox.classList.remove('sp-box')
    audio.hidden = true
    patienter.classList.add('spinner-border')
    patienter.classList.add('spinner-border-sm')


  sleep(500).then(() => {
    btnText.disabled=true
    });
})

function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }