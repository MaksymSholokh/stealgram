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


        //pagination post page
        let page = 1;
        
        document.querySelector('.pagination').addEventListener('click', event => { 
            page += 1 
            let url = `${window.location.pathname}?page=${page}`;  
            console.log(url)
            
            fetch(url, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())   
            .then(data => {
                let cont = document.querySelector('.post-list'); 
                cont.insertAdjacentHTML('beforeend', data.new_page)

            })

            //cont.innerHTML = data.new_page })

        }); 

        //comment 

       


        document.querySelectorAll('.modal_comment').forEach(comment_block => { 
            let page_comment = 1 
            let object_id = comment_block.id; 
              
            let next_page = true;

            const req_new_page_comment = () => { 
                let url_comment = `/post/comment/${object_id}/?page=${page_comment}`
                if (next_page){

                    fetch(url_comment) 
                    .then(response => response.json()) 
                    .then(data => {
                        if(data.has_next_page === false){
                            next_page = false;
                        }
                        //comment_block.insertAdjacentHTML('beforeend', data.new_page_comment) 
                        document.getElementsByClassName('modal_comment')[0].innerHTML += data.new_page_comment
                        page_comment += 1 
                        });
            }};

            req_new_page_comment(); 


            comment_block.addEventListener('scroll', () => {
                const scrollY = window.scrollY || document.documentElement.scrollTop; 
                req_new_page_comment(); 
                alert(123)
                if(scrollY > 100){
                    
                }
                }
            
        ); 
    });

        
    window.addEventListener('scroll', function () {
    const scrollY = window.scrollY || document.documentElement.scrollTop; 
        alert('hi')
        //req_new_page_comment();
    // Тут ваша логіка
    if (scrollY > 100) { 
        //alert('Сторінка прокручена вниз на 100px або більше')
        console.log('Сторінка прокручена вниз на 100px або більше');
        }
    });


        //share 
        document.querySelectorAll('.share').forEach(shareBlock => { 
            const contentId = shareBlock.id;
            const shareButton =   shareBlock.querySelector('button');
            const chats = shareBlock.querySelector('a');
            const classShare = chats.className; 
            

            const data = {'action': 'share', 'content': classShare, 'id': contentId}; 



            chats.addEventListener('click', event => {  
                sessionStorage.setItem('share', JSON.stringify(data));  
                console.log(sessionStorage.getItem('share'))

            });

        });



       
        




        // like/dislike
        document.querySelectorAll('.like,  .dislike  ').forEach(block => { 
            const button = block.querySelector('button') 
            const p = block.querySelector('p')  

            //console.log('123', block.parentNode.className, block.parentNode.id)

            const url = `/post/${block.id}/`  
            const action = block.className 

            //  more abstract like
            const content_class = String(block.parentNode.className); 
            const content_id = String(block.parentNode.id); 

            //console.log(content_class, content_id)
            //block.id = content_type.id; 


            //content_type


            const data = {'action': action,  'type': content_class, 'id': content_id}
            
            button.addEventListener('click', (event) => { 
                sendData(url, data)

                const svg = event.target;  
                let countr = Number(p.textContent);

                if(svg.style.fill === 'red') {
                    svg.style.fill = 'black'; 
                    p.textContent = String(countr - 1);
                    
                } else{
                    svg.style.fill = 'red';
                    p.textContent = String(countr + 1);
                } 
            });
            
        });    

        function sendData(url, data){ 
            //console.log(data)
            fetch(url, {
                method: 'POST', 
                headers: {
                'Content-Type': 'application/json', 
                'X-CSRFToken': getCookie('csrftoken') 

                            
                        
                }, 
                body:  JSON.stringify(data)
                })
                .then(response => response.json());
        }
