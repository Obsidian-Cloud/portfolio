// controller.js


/*
function addUserInput(value) {
    userInput['theme'] = value;
};
*/
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.shortcut-btn').forEach(input => {
    input.addEventListener('click', event => {
        event.preventDefault();
        const data = {};
        document.querySelectorAll('#ormlabs-submission input, #ormlabs-submission select').forEach(input => {
            if (input.type === 'checkbox') {
                data[input.name] = input.checked; 
                console.log("CHECKBOX");
            } else {
                data[input.name] = input.value;
                console.log("VALUE");
            }
        });
        console.log(event.target.dataset.shortcut, data);   
        fetch('/api/update-row/', {
            method: 'POST',
            headers: {
                "Cache-Control": "no-cache",
                // encoding used
                "Accept-Encoding": "gzip",
                // type to send
                "Content-Type": "application/json",
                // type allowed back
                "Accept": "application/json",
            },
            body: JSON.stringify({
                action: event.target.dataset.shortcut,
                payload: data
            })
        });
    });
})});


/*
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('#shortcut-form').addEventListener('submit',
        function(event) {
            console.log(event.submitter.dataset.shortcut);
            event.preventDefault();
})});
*/  

/*
let ormSubmitButton = document.querySelector('data-ormterminal')
document.addEventListener("DOMContentLoaded", 
    document.addEventListener("submit", )
);
*/

/*
document.addEventListener("DOMContentLoaded", 
    document.querySelector(_selector),
    
    element.addEventListener(_listener,
        function(event) {
        _function;
        event.preventDefault();
    })
);
*/




// collect some user input and populate json before fetch()
const jsonBody = {'name': 'string'};

const options = {
    method: "POST",
    headers: {
        "Cache-Control": "no-cache",
        // type to send
        "Content-Type": "application/json",
        // encoding used
        "Accept-Encoding": "gzip",
        // type can accept back
        "Accept": "application/json",
    },
    body: JSON.stringify(jsonBody)
};



let requestURL = "/api/create-table/"
const request = new Request(requestURL, options);

const response = fetch(requestURL).then((response) => {
  //
});




let data = "data"


/**
 * @interface
 * Sends any data(client or database) to `screen_presenter.js` through port.
 * @param {port} - The implicit interface to implement.
 * @param {clientResponse} - The reponse from the client.
 * @param {databaseResponse} - The response from the database.
 */
export function controller(port) {
    port.portData(data);
};