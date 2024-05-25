
data_json = JSON.parse(data_json); // Convertir la cadena JSON en un objeto JavaScript

console.log(data_json);
var table = document.getElementById("myTable");
var thead = table.getElementsByTagName("thead")[0];
var tbody = table.getElementsByTagName("tbody")[0];

// Agregar las cabeceras de columna basadas en las claves del objeto "columns"
var columns = data_json.columns;
for (var i = 0; i < columns.length; i++) {
    var th = document.createElement("th");
    th.textContent = columns[i];
    thead.getElementsByTagName("tr")[0].appendChild(th);
}

// Agregar filas y celdas basadas en los datos JSON
var rows = data_json.index;
for (var i = 0; i < rows.length; i++) {
    var newRow = tbody.insertRow();
    var rowData = data_json[rows[i]];

    for (var key in rowData) {
        if (rowData.hasOwnProperty(key)) {
            var cell = newRow.insertCell();
            cell.textContent = rowData[key];
        }
    }
}