document.addEventListener("DOMContentLoaded", function () {
  const loaderContainer = document.querySelector('.loader-container');
  const mostrarLoaderButton = document.getElementById('mostrar-loader');

  // Agrega un manejador de eventos al botón para mostrar el loader
  mostrarLoaderButton.addEventListener('click', () => {
      mostrarLoader();
  });

  // Función para mostrar el loader durante 10 segundos
  function mostrarLoader() {
      loaderContainer.style.display = 'flex';
      setTimeout(() => {
          ocultarLoader();
          window.location.href = '/admin/ResultadosAnalisis';
      }, 5000); // 10000 milisegundos = 10 segundos
  }

  // Función para ocultar el loader y mostrar el contenido normal
  function ocultarLoader() {
      loaderContainer.style.display = 'none';
  }





  const form = document.querySelector("form"),
    fileInput = document.querySelector(".file-input"),
    progressArea = document.querySelector(".progress-area"),
    uploadedArea = document.querySelector(".uploaded-area"),
    resultsArea = document.querySelector(".results");

  form.addEventListener("click", () => {
    fileInput.click();
  });

  fileInput.onchange = ({ target }) => {
    let file = target.files[0];
    if (file) {
      let fileName = file.name;
      if (fileName.length >= 12) {
        let splitName = fileName.split('.');
        fileName = splitName[0].substring(0, 13) + "... ." + splitName[1];
      }
      uploadFile(fileName);
    }
  };

  function createTable(data) {
    // Parsea la cadena JSON en un objeto JavaScript
    let parsedData = JSON.parse(data);

    // Verifica si el objeto contiene las propiedades esperadas
    if (!parsedData.columns || !parsedData.data) {
      return "<p>Error: Los datos no tienen el formato esperado.</p>";
    }

    // Extrae las columnas y los datos del objeto
    let columns = parsedData.columns;
    let tableData = parsedData.data;

    // Crea la tabla y agrega clases de estilo
    let table = document.createElement("table");
    table.className = "w-full whitespace-no-wrap datatable dataTable no-footer";
    table.id = "myTable"; // Agrega el atributo id

    // Crea el encabezado de la tabla (thead)
    let thead = document.createElement("thead");
    let headerRow = document.createElement("tr");

    for (let column of columns) {
      let th = document.createElement("th");
      th.textContent = column;
      headerRow.appendChild(th);
    }

    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Crea el cuerpo de la tabla (tbody)
    let tbody = document.createElement("tbody");

    for (let rowData of tableData) {
      let row = document.createElement("tr");

      for (let cellData of rowData) {
        let td = document.createElement("td");
        td.textContent = cellData;
        row.appendChild(td);
      }

      tbody.appendChild(row);
    }

    table.appendChild(tbody);

    // Convierte la tabla HTML generada en una cadena HTML
    let tableHTML = table.outerHTML;

    return tableHTML;
  }

  function uploadFile(name) {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/upload");
    xhr.upload.addEventListener("progress", ({ loaded, total }) => {
      let fileLoaded = Math.floor((loaded / total) * 100);
      let fileTotal = Math.floor(total / 1000);
      let fileSize;
      fileTotal < 1024
        ? (fileSize = fileTotal + " KB")
        : (fileSize = (loaded / (1024 * 1024)).toFixed(2) + " MB");
      let progressHTML = `<li class="row">
                            <i class="fas fa-file-alt"></i>
                            <div class="content">
                              <div class="details">
                                <span class="name">${name} • Uploading</span>
                                <span class="percent">${fileLoaded}%</span>
                              </div>
                              <div class="progress-bar">
                                <div class="progress" style="width: ${fileLoaded}%"></div>
                              </div>
                            </div>
                          </li>`;
      uploadedArea.classList.add("onprogress");
      progressArea.innerHTML = progressHTML;
      if (loaded == total) {
        progressArea.innerHTML = "";
        let uploadedHTML = `<li class="row">
                              <div class="content upload">
                                <i class="fas fa-file-alt"></i>
                                <div class="details">
                                  <span class="name">${name} • Uploaded</span>
                                  <span class="size">${fileSize}</span>
                                </div>
                              </div>
                              <i class="fas fa-check"></i>
                            </li>`;
        uploadedArea.classList.remove("onprogress");
        uploadedArea.insertAdjacentHTML("afterbegin", uploadedHTML);
      }
    });

    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          // Procesa la respuesta JSON y muestra los datos en una tabla HTML
          let response = JSON.parse(xhr.responseText);
          console.log(response); // Agrega esto para verificar la estructura de la respuesta
          if (response.data) {
            let tableHTML = createTable(response.data);
            resultsArea.innerHTML = tableHTML;
    
            // Inicializar DataTables en la tabla recién creada
            $('#myTable').DataTable({
              lengthChange: false,
              lengthMenu: [ [10, 25, 50, -1], [10, 25, 50, "Todos"] ], // Define las opciones de cantidad de filas por página
              pageLength: 25,
              searching: false,
              language: {
                info: "Mostrando _END_ de _TOTAL_ registros",
                infoEmpty: "Mostrando 0 registros",
                infoFiltered: "(filtrados de _MAX_ registros en total)",
                paginate: {
                  first: "Primero",
                  last: "Último",
                  next: "Siguiente",
                  previous: "Anterior"
                }
              }
            });
          } else {
            // Mostrar mensaje de error si no se encontraron datos
            resultsArea.innerHTML = "<p>Error: " + response.error + "</p>";
          }
        } else {
          // Manejar errores de solicitud si es necesario
          resultsArea.innerHTML = "<p>Error de solicitud: " + xhr.statusText + "</p>";
        }
      }
    };
    

    let data = new FormData(form);
    xhr.send(data);
  }
});



