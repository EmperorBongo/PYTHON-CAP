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
    <div class="response-option">
        <span>A:</span>
        <div class="response-bar" data-percent="A" style="width: ${responseJson['a']}%">
            ${responseJson['a']}%
        </div>
    </div>
    <div class="response-option">
        <span>B:</span>
        <div class="response-bar" data-percent="B" style="width: ${responseJson['b']}%">
            ${responseJson['b']}%
        </div>
    </div>
    <div class="response-option">
        <span>C:</span>
        <div class="response-bar" data-percent="C" style="width: ${responseJson['c']}%">
            ${responseJson['c']}%
        </div>
    </div>
    <div class="response-option">
        <span>D:</span>
        <div class="response-bar" data-percent="D" style="width: ${responseJson['d']}%">
            ${responseJson['d']}%
        </div>
    </div>
</div>
<p class="total-response">Total: ${responseJson['total']}</p>

            
                `;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });
}
