let gemini_block = document.querySelector('.gemini_assistans')
let ans_text = gemini_block.querySelector('textarea')
let ask_text = gemini_block.querySelector('input') 
let btn_send = gemini_block.querySelector('button') 

function send_ans(ans_text, ask_text){
    let url = `/ask/` 

    let data = {'promt': ask_text.value}

    fetch(url, {
        headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/json',
        },
        method: "POST",
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        ans_text.value += (ans_text.value ? '\n' : '') + data.ans; 
        ask_text.value = ''
    })
    }


btn_send.addEventListener('click',  () => send_ans(ans_text, ask_text))

function getCookie(name) {
         let cookieValue = null;
         if (document.cookie && document.cookie !== '') {
             const cookies = document.cookie.split(';');
             for (let cookie of cookies) {
                 cookie = cookie.trim();
                 if (cookie.startsWith(name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
        };  