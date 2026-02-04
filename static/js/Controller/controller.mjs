var presenterRef = null;
export function setPresenter(p) {
    presenterRef = p;
}
;
// send data to the 'screen presenter' through the `DataPort` interface.
export function portData(data) {
    if (!presenterRef)
        throw new Error("controller not provided");
    presenterRef.port(data);
}
;


async function fetchData(url, requestData, action) {
    try {
        console.log(action, url, requestData)
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                "Cache-Control": "no-cache",
                // type to send
                "Content-Type": "application/json",
                // type allowed back
                "Accept": "application/json",
            },
            body: JSON.stringify({
                action: action,
                payload: requestData
            })
        })
    console.log(response);
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // If the response is ok, proceed to parse the JSON and return
    const responseData = await response.json();
    return responseData

    } catch (error) {
        // Handle any errors that occurred during the fetch operation or in the if block
        console.error('Fetch error:', error.message);
        return null
    }
};


/* depeneding on action attribute of button, determine which api gets called */
const API_URLS = {
    submit: '/api/insert-row/',
    update: '/api/update-row/',
    delete: '/api/delete-row/',
};



document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.shortcut-btn').forEach(input => {
    input.addEventListener('click', async event => {
        event.preventDefault();

        const action = event.currentTarget.dataset.shortcut;
        const url = API_URLS[action];

        const requestData = {};

        const parseValue = (val) => {
            if (val === 'true') return true;
            if (val === 'false') return false;
            if (val !== '' && !isNaN(val)) return Number(val);
            return val;
        };

        if (!url) {
            return console.error(`Unknown action: ${action}`);
        }

        document.querySelectorAll('#ormlabs-submission input, #ormlabs-submission select')
            .forEach(input => {

                console.log(action)
                
                switch (action) {
                    case 'submit':
                        if (input.type !== 'checkbox') {
                            requestData[input.name] = parseValue(input.value);
                        }
                        break;
                    
                    case 'update':
                        console.log(`Looping: name=${input.name}, value=${input.value}, action=${action}`);

                        if (input.type === 'checkbox') {
                            if (input.checked) {
                                requestData[input.name] = parseValue(input.value);
                            }
                        } else {
                            requestData[input.name] = parseValue(input.value);
                        }
                        break;

                    case 'delete':
                        if (input.type === 'checkbox' && input.checked) {
                            requestData.ids = requestData.ids || [];
                            requestData.ids.push(parseValue(input.value));
                        }
                        break;
                }

/*
                if (action === 'submit') {
                    // checkbox input(row id) is not needed for row inserts.
                    if (input.type !== 'checkbox') {
                        requestData[input.name] = parseValue(input.value);
                    }

                } else if (action === 'update') {
                    console.log(`Looping: name=${input.name},value=${input.checked} ,value=${input.value}, action=${action}`);
                    // check to see if checkbox is checked
                    if (input.type === 'checkbox' && input.checked) {
                        console.log(input.checked)
                        // sets the request data input name 'ormlabs-check'
                        // as the value of the checkbox(row id) for database lookup.
                        requestData[input.name] = parseValue(input.value);
                    } else {
                        // if not a checkbox, simply add the other input values
                        // to the request data.
                        requestData[input.name] = parseValue(input.value);
                    }

                } else if (action === 'delete') {
                    console.log(`Looping: name=${input.name}, value=${input.value}, action=${action}`);
                    // only sending the checkbox value. cookies get used
                    // by flask directly after the request comes through 
                    // to the api.
                    if (input.type === 'checkbox') {
                        requestData[input.name] = parseValue(input.value);
                    }

                } else {
                    console.log('HTML button submit action not recognized.')
                }
*/
        });


        console.log('Request submitted: ');
        const responseData = await fetchData(url, requestData, action);
        console.log('Response recieved: ');
        console.log(responseData);

        if (responseData !== null) {
            portData(responseData);
        }

    });
})});
