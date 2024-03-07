const button_id = ["a", "b", "c", "d"];

for (let id of button_id) {
    const button = document.querySelector(`#${id}`);
    button.addEventListener('click', (evt) => {
        evt.preventDefault();
        const answer = {
            response: id
        };

        fetch('/log-response', {
            method: 'POST',
            body: JSON.stringify(answer),
            headers: { 'Content-Type': 'application/json' },
        })
            .then((response) => response.json())
            .then((responseJson) => {
                const responseContainer = document.querySelector('#response');
                responseContainer.innerHTML = `
                    <div class="response-summary">
                        <p class="response-option">A: ${responseJson['a']}</p>
                        <p class="response-option">B: ${responseJson['b']}</p>
                        <p class="response-option">C: ${responseJson['c']}</p>
                        <p class="response-option">D: ${responseJson['d']}</p>
                    </div>
                    <p class="total-response">Total: ${responseJson['total']}</p>
                `;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });
}
