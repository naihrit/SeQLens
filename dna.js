//CHANGE MODE START
//_________________________________________________________________________________________
let modebtn = document.querySelector('#mode');
let body = document.querySelector('body');
let currentMode = 'light-mode';

modebtn.addEventListener('click', () => {
    if (currentMode === 'light') {
        currentMode = 'dark';
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
    } else {
        currentMode = 'light';
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
    }
});
//________________________________________________________________________________________

// INPUT
//________________________________________________________________________________________
const form = document.getElementById("dnaForm");
const dna = document.getElementById("dnaInput");
const out = document.getElementById("interpretedbox");
const subutton = document.querySelector('#suB');

subutton.addEventListener('click', async (e) =>{
    e.preventDefault();
    let seq= dna.value.trim().toUpperCase();
    if(!seq){
        alert("Please Enter the DNA sequence");
        return;
    }
    out.value = "Translating Given Sequence";

    try{
        const response = await fetch ('http://127.0.0.1:5000/translate',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({seq: seq})
        });
        const data = await response.json();
        out.value = data.output;
    } catch (error) {
        console.error("Error:", error);
        out.value = "Error connecting to Python backend.";
    }
 });
//__________________________________________________________________________________________