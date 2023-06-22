function updateEmotionScreen(){
    fetch('result.txt')
        .then(response => response.text())
        .then(data => {
            const emotionContainer = document.getElementById('emotion-container');
            emotionContainer.innerText = data;
         })
         .catch(error => {
            console.error('Fehler beim Laden der Datei:', error);
         });
}

setInterval(updateEmotionScreen, 3000); // repeat evry 3 sec