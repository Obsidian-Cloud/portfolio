// web_view.mjs
import { viewData } from "../Presenter/screen_view_model.mjs";

export var webView = {
    port: function () {
        console.log("WebView Reached!");
        console.log(viewData)
        
        updateTable();
    }
};


function updateTable() {
    const tableBody = document.querySelector('#ormlabs-table-body'); 
    const action = viewData.action
    const data = viewData.payload
    console.log('UpdateTable: Action');

    if (action === 'submit') {

        const tr = document.createElement('tr');
        tr.className = "ormlabs-tr";
        tr.id = `row-${data.id}`;
        console.log(tr.id)
        const createCell = (content) => {
            const td = document.createElement('td');
            td.className = "ormlabs-td";
            td.textContent = content;
            return td;
        };

        const checkCell = document.createElement('td');
        checkCell.className = "ormlabs-td";
        // used a radio instead of checkbox to explicitly limit one selection for now
        checkCell.innerHTML = `<input name="ormlabs-check" type="checkbox" class="ormlabs-delete-checkbox" value="${data.id}">`;
        tr.appendChild(checkCell);

        tr.appendChild(createCell(data.id));
        tr.appendChild(createCell(data.name));
        tr.appendChild(createCell(data.note));
        tr.appendChild(createCell(data.level));
        tr.appendChild(createCell(data.active ? "True" : "False"));
        tr.appendChild(createCell(data.updated));

        tableBody.prepend(tr);

    } else if (action === 'update') {
        // find the existing row using the id from the database
        const existingRow = document.querySelector(`#row-${data.id}`);

        if (existingRow) {
            // get all cells within the row
            const cells = existingRow.querySelectorAll('.ormlabs-td');

            // update text in each cell to new values
            cells[1].textContent = data.id;
            cells[2].textContent = data.name;
            cells[3].textContent = data.note;
            cells[4].textContent = data.level;
            cells[5].textContent = data.active ? "True" : "False";
            cells[6].textContent = data.updated;
        }

    } else if (action === 'delete') {
        console.log('DATA IDS')
        console.log(data.ids)
        // if more than 1 id
        if (data.ids.length > 1) {
            for (let step = 0; step < data.ids.length; step++)
                document.querySelector(`#row-${data.ids[step]}`).remove();
        }
        // else if 1 id
        document.querySelector(`#row-${data.ids[0]}`).remove();

    } else {
        console.log('Action received from database response does not exist.')
    }



};