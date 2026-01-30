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
    console.log(url, requestData, action)
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

        if (!url) {
            console.error(`Unknown action: ${action}`);
            return;
        }

        const requestData = {};
        document.querySelectorAll('#ormlabs-submission input, #ormlabs-submission select')
            .forEach(input => {
            if (input.type === 'checkbox') {
                requestData[input.name] = input.checked; 
            } else {
                requestData[input.name] = input.value;
            }
        });
        console.log('Request submitted: ');
        console.log(action, requestData);
        console.log(url)
        const responseData = await fetchData(url, requestData, action);

        console.log('Response recieved: ');
        console.log(responseData);

        if (responseData !== null) {
            portData(responseData);
        }
        
    });
})});
