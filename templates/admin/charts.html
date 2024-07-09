<!DOCTYPE html>
<html :class="{ 'theme-dark': dark }" x-data="data()" lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Windmill Dashboard</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="{{url_for('static', filename='css/tailwind.output.css')}}" />
    <script
      src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"
      defer
    ></script>
    <script src="{{url_for('static', filename='js/init-alpine.js')}}"></script>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.css"
    />

    <link rel="stylesheet" href="{{url_for('static', filename='nuevoup.css')}}">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<script src="{{url_for('static', filename='script3.js')}}"></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"
      defer
    ></script>
    <script src="{{url_for('static', filename='js/charts-lines.js')}}" defer></script>
    <script src="{{url_for('static', filename='js/charts-pie.js')}}" defer></script>
    <!-- Estilos de DataTables -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.css">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/select/1.3.3/css/select.dataTables.min.css">
    
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    
    <!-- DataTables -->
    <script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.js">
    </script>
    
    <!-- DataTables Select (para selección de filas) -->
    <script src="https://cdn.datatables.net/select/1.3.3/js/dataTables.select.min.js">
    </script>
<style>
  /* Estilos para la tabla */
  .custom-table {
    border-collapse: collapse;
    width: 100%;
  }

  table.dataTable thead th, table.dataTable thead td {
    padding: 10px 18px;
    border-bottom: 0px solid rgb(17, 17, 17);
}
table.dataTable.no-footer {
    border-bottom: 0px solid #111;
}
  
  .custom-table th,
  .custom-table td {
    padding: 8px;
    text-align: left;
    border-bottom: none; /* Elimina el borde inferior */
  }
  
  .custom-table th {
    background-color: #f2f2f2;
    font-weight: bold;
  }
</style>

  </head>
  <body>
    <div
      class="flex h-screen bg-gray-50 dark:bg-gray-900"
      :class="{ 'overflow-hidden': isSideMenuOpen }"
    >
      <!-- Desktop sidebar -->
      <aside
        class="z-20 hidden w-64 overflow-y-auto bg-white dark:bg-gray-800 md:block flex-shrink-0"
      >
        <div class="py-4 text-gray-500 dark:text-gray-400">
          <a
            class="ml-6 text-lg font-bold text-gray-800 dark:text-gray-200"
            href="#"
          >
            Dashboard
          </a>
          <ul class="mt-6">
            <li class="relative px-6 py-3">
              
              <a
                class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
                href="{{ url_for('admin_home') }}"
              >
                <svg
                  class="w-5 h-5"
                  aria-hidden="true"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                  ></path>
                </svg>
                <span class="ml-4">Dashboard</span>
              </a>
            </li>
          </ul>
          <ul>
            <li class="relative px-6 py-3">
              <span
                class="absolute inset-y-0 left-0 w-1 bg-purple-600 rounded-tr-lg rounded-br-lg"
                aria-hidden="true"
              ></span>
              <a
                
                class="inline-flex items-center w-full text-sm font-semibold text-gray-800 transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200 dark:text-gray-100"
                href="{{ url_for('admin_RegistroPacientes') }}"
                
              >
                <svg
                  class="w-5 h-5"
                  aria-hidden="true"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
                  ></path>
                </svg>
                <span class="ml-4">Analisis</span>
              </a>
            </li>
            
            
            
           
          </ul>

          
        </div>
      </aside>
      <!-- Mobile sidebar -->
      <!-- Backdrop -->
      <div
        x-show="isSideMenuOpen"
        x-transition:enter="transition ease-in-out duration-150"
        x-transition:enter-start="opacity-0"
        x-transition:enter-end="opacity-100"
        x-transition:leave="transition ease-in-out duration-150"
        x-transition:leave-start="opacity-100"
        x-transition:leave-end="opacity-0"
        class="fixed inset-0 z-10 flex items-end bg-black bg-opacity-50 sm:items-center sm:justify-center"
      ></div>
      <aside
        class="fixed inset-y-0 z-20 flex-shrink-0 w-64 mt-16 overflow-y-auto bg-white dark:bg-gray-800 md:hidden"
        x-show="isSideMenuOpen"
        x-transition:enter="transition ease-in-out duration-150"
        x-transition:enter-start="opacity-0 transform -translate-x-20"
        x-transition:enter-end="opacity-100"
        x-transition:leave="transition ease-in-out duration-150"
        x-transition:leave-start="opacity-100"
        x-transition:leave-end="opacity-0 transform -translate-x-20"
        @click.away="closeSideMenu"
        @keydown.escape="closeSideMenu"
      >
        <div class="py-4 text-gray-500 dark:text-gray-400">
          <a
            class="ml-6 text-lg font-bold text-gray-800 dark:text-gray-200"
            href="#"
          >
            Dashboard
          </a>
          <ul class="mt-6">
            <li class="relative px-6 py-3">
              <span
                class="absolute inset-y-0 left-0 w-1 bg-purple-600 rounded-tr-lg rounded-br-lg"
                aria-hidden="true"
              ></span>
              <a
                class="inline-flex items-center w-full text-sm font-semibold text-gray-800 transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200 dark:text-gray-100"
                href="index.html"
              >
                <svg
                  class="w-5 h-5"
                  aria-hidden="true"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                  ></path>
                </svg>
                <span class="ml-4">Dashboard</span>
              </a>
            </li>
          </ul>
          <ul>
            <li class="relative px-6 py-3">
              <a
                class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
                href="{{ url_for('admin_RegistroPacientes') }}"
              >
                <svg
                  class="w-5 h-5"
                  aria-hidden="true"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
                  ></path>
                </svg>
                <span class="ml-4">Analisis de Datos</span>
              </a>
            </li>
            
            
            
            
            <li class="relative px-6 py-3">
              <a
                class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
                href="{{ url_for('admin_GestionarPacientes') }}"
              >
                <svg
                  class="w-5 h-5"
                  aria-hidden="true"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path d="M4 6h16M4 10h16M4 14h16M4 18h16"></path>
                </svg>
                <span class="ml-4">Gestionar Pacientes</span>
              </a>
            </li>
            
          </ul>
          <div class="px-6 my-6">
            <button
              class="flex items-center justify-between px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple"
            >
              Create account
              <span class="ml-2" aria-hidden="true">+</span>
            </button>
          </div>
        </div>
      </aside>
      <div class="flex flex-col flex-1 w-full">
        <header class="z-10 py-4 bg-white shadow-md dark:bg-gray-800">
          <div
            class="container flex items-center justify-between h-full px-6 mx-auto text-purple-600 dark:text-purple-300"
          >
            <!-- Mobile hamburger -->
            <button
              class="p-1 mr-5 -ml-1 rounded-md md:hidden focus:outline-none focus:shadow-outline-purple"
              @click="toggleSideMenu"
              aria-label="Menu"
            >
              <svg
                class="w-6 h-6"
                aria-hidden="true"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fill-rule="evenodd"
                  d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </button>
            <div class="flex justify-center flex-1 lg:mr-32">
              <div
                class="relative w-full max-w-xl mr-6 focus-within:text-purple-500"
              >
                <div class="absolute inset-y-0 flex items-center pl-2">
                  <svg
                    class="w-4 h-4"
                    aria-hidden="true"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                </div>
                <input
                  class="w-full pl-8 pr-2 text-sm text-gray-700 placeholder-gray-600 bg-gray-100 border-0 rounded-md dark:placeholder-gray-500 dark:focus:shadow-outline-gray dark:focus:placeholder-gray-600 dark:bg-gray-700 dark:text-gray-200 focus:placeholder-gray-500 focus:bg-white focus:border-purple-300 focus:outline-none focus:shadow-outline-purple form-input"
                  type="text"
                  placeholder="Buscar Elemento"
                  aria-label="Search"
                />
              </div>
            </div>
            <ul class="flex items-center flex-shrink-0 space-x-6">
              <!-- Theme toggler -->
              <li class="flex">
                <button
                  class="rounded-md focus:outline-none focus:shadow-outline-purple"
                  @click="toggleTheme"
                  aria-label="Toggle color mode"
                >
                  <template x-if="!dark">
                    <svg
                      class="w-5 h-5"
                      aria-hidden="true"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path
                        d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"
                      ></path>
                    </svg>
                  </template>
                  <template x-if="dark">
                    <svg
                      class="w-5 h-5"
                      aria-hidden="true"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                  </template>
                </button>
              </li>
              <!-- Notifications menu -->
              <li class="relative">
                <button
                  class="relative align-middle rounded-md focus:outline-none focus:shadow-outline-purple"
                  @click="toggleNotificationsMenu"
                  @keydown.escape="closeNotificationsMenu"
                  aria-label="Notifications"
                  aria-haspopup="true"
                >
                  <svg
                    class="w-5 h-5"
                    aria-hidden="true"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z"
                    ></path>
                  </svg>
                  <!-- Notification badge -->
                  <span
                    aria-hidden="true"
                    class="absolute top-0 right-0 inline-block w-3 h-3 transform translate-x-1 -translate-y-1 bg-red-600 border-2 border-white rounded-full dark:border-gray-800"
                  ></span>
                </button>
                <template x-if="isNotificationsMenuOpen">
                  <ul
                    x-transition:leave="transition ease-in duration-150"
                    x-transition:leave-start="opacity-100"
                    x-transition:leave-end="opacity-0"
                    @click.away="closeNotificationsMenu"
                    @keydown.escape="closeNotificationsMenu"
                    class="absolute right-0 w-56 p-2 mt-2 space-y-2 text-gray-600 bg-white border border-gray-100 rounded-md shadow-md dark:text-gray-300 dark:border-gray-700 dark:bg-gray-700"
                  >
                    <li class="flex">
                      <a
                        class="inline-flex items-center justify-between w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
                        href="#"
                      >
                        <span>Mensajes</span>
                        <span
                          class="inline-flex items-center justify-center px-2 py-1 text-xs font-bold leading-none text-red-600 bg-red-100 rounded-full dark:text-red-100 dark:bg-red-600"
                        >
                          10
                        </span>
                      </a>
                    </li>
                    
                    <li class="flex">
                      <a
                        class="inline-flex items-center justify-between w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
                        href="#"
                      >
                        <span>Alertas</span>
                      </a>
                    </li>
                  </ul>
                </template>
              </li>
              <!-- Profile menu -->
              <li class="relative">
                <button
                  class="align-middle rounded-full focus:shadow-outline-purple focus:outline-none"
                  @click="toggleProfileMenu"
                  @keydown.escape="closeProfileMenu"
                  aria-label="Account"
                  aria-haspopup="true"
                >
                  <img
                    class="object-cover w-8 h-8 rounded-full"
                    src="https://images.unsplash.com/photo-1502378735452-bc7d86632805?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=aa3a807e1bbdfd4364d1f449eaa96d82"
                    alt=""
                    aria-hidden="true"
                  />
                </button>
                <template x-if="isProfileMenuOpen">
                  <ul
                    x-transition:leave="transition ease-in duration-150"
                    x-transition:leave-start="opacity-100"
                    x-transition:leave-end="opacity-0"
                    @click.away="closeProfileMenu"
                    @keydown.escape="closeProfileMenu"
                    class="absolute right-0 w-56 p-2 mt-2 space-y-2 text-gray-600 bg-white border border-gray-100 rounded-md shadow-md dark:border-gray-700 dark:text-gray-300 dark:bg-gray-700"
                    aria-label="submenu"
                  >
                    <li class="flex">
                      <a
                        class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
                        href="#"
                      >
                        <svg
                          class="w-4 h-4 mr-3"
                          aria-hidden="true"
                          fill="none"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path
                            d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                          ></path>
                        </svg>
                        <span>Perfil</span>
                      </a>
                    </li>
                    <li class="flex">
                      <a
                        class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
                        href="#"
                      >
                        <svg
                          class="w-4 h-4 mr-3"
                          aria-hidden="true"
                          fill="none"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path
                            d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
                          ></path>
                          <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                        </svg>
                        <span>Settings</span>
                      </a>
                    </li>
                    <li class="flex">
                      <a
                        class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
                        href="/logout"
                      >
                        <svg
                          class="w-4 h-4 mr-3"
                          aria-hidden="true"
                          fill="none"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path
                            d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
                          ></path>
                        </svg>
                        <span>Cerrar Sesion</span>
                      </a>
                    </li>
                  </ul>
                </template>
              </li>
            </ul>
          </div>
        </header>
        <main class="h-full overflow-y-auto">
          <div class="container px-6 mx-auto grid">
            <h2
              class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200"
            >
              Dashboard
            </h2>
            
            <!-- Cards -->
            <div class="grid gap-6 mb-8 md:grid-cols-2 xl:grid-cols-4">
              
              <!-- Card -->
              <div
                class="flex items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800"
              >
                <div
                  class="p-3 mr-4 text-green-500 bg-green-100 rounded-full dark:text-green-100 dark:bg-green-500"
                >
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                    <path
                      fill-rule="evenodd"
                      d="M4 4a2 2 0 00-2 2v4a2 2 0 002 2V6h10a2 2 0 00-2-2H4zm2 6a2 2 0 012-2h8a2 2 0 012 2v4a2 2 0 01-2 2H8a2 2 0 01-2-2v-4zm6 4a2 2 0 100-4 2 2 0 000 4z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                </div>
                <div>
                  <p
                    class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400"
                  >
                    Anomalias
                  </p>
                  <p
                    class="text-lg font-semibold text-gray-700 dark:text-gray-200"
                  >
                  <p id="total-anomalias"></p>

<!-- Tu código para mostrar el mapa de calor aquí -->

<script>
    var data_json_str = {{ data_json | safe }};
    var dataJSON = JSON.parse(data_json_str);
    console.log(dataJSON)

    // Calcular la cantidad total de anomalías
    var totalAnomalias = dataJSON.data.reduce(function (total, row) {
        var index = dataJSON.columns.indexOf('anomalia_etiqueta');
        var anomalia = parseInt(row[index]);
        return total + (anomalia === 1 ? 1 : 0);
    }, 0);

    // Mostrar el total en el elemento HTML
    document.getElementById('total-anomalias').textContent = totalAnomalias;
</script>
                  </p>
                </div>
              </div>
              
              
            </div>

            <h2
              class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200"
            >
              Tabla de Anomalias
            </h2>
            <div class="results w-full overflow-hidden rounded-lg shadow-xs w-full overflow-x-auto dataTables_wrapper no-footer" id="myTable_wrapper">
              <!-- Aquí se mostrará la tabla -->
              <div class="w-full overflow-hidden rounded-lg shadow-xs">
                  <div class="w-full overflow-x-auto">
                      <table class="table" id="myTable">
                          <thead>
                              <tr>
                                  <!-- Cabeceras de columna se agregarán dinámicamente aquí -->
                              </tr>
                          </thead>
                          <tbody>
                              <!-- Agrega las filas y celdas aquí -->
                          </tbody>
                      </table>
                  </div>
              </div>
          </div>
      
          <!-- Incluye las bibliotecas de DataTables y jQuery aquí -->
      
          <script>
            // Supongamos que data_json_str es la cadena JSON que obtienes desde el servidor
            // Supongamos que data_json_str es la cadena JSON que obtienes desde el servidor
var data_json_str = {{ data_json | safe }};
var idDataJson = JSON.parse('{{ id_datajson|tojson }}');
    console.log(idDataJson)

try {
    // Intenta analizar la cadena JSON
    var data_json = JSON.parse(data_json_str);
    console.log(data_json);

    var table = $('#myTable');

    // Agregar las cabeceras de columna basadas en las claves del objeto "columns"
    var columns = data_json.columns;
    for (var i = 0; i < columns.length; i++) {
        table.find('thead tr').append('<th>' + columns[i] + '</th>');
    }

    // Agregar filas y celdas basadas en los datos JSON
    var rows = data_json.index;
    for (var i = 0; i < rows.length; i++) {
        var rowData = data_json.data[rows[i]];
        var rowHtml = '<tr>';

        for (var key in rowData) {
            if (rowData.hasOwnProperty(key)) {
                rowHtml += '<td>' + rowData[key] + '</td>';
            }
        }

        rowHtml += '</tr>';
        table.find('tbody').append(rowHtml);
    }

    // Inicializar la tabla DataTable
    var dataTable = table.DataTable({
        select: true  // Habilita la selección de filas
    });

    // Agregar el controlador de eventos para el doble clic en una fila
    table.on('dblclick', 'tr', function () {
    var data = dataTable.row(this).data(); // Obtén los datos de la fila

    var idDataJson = JSON.parse('{{ id_datajson|tojson }}');
    console.log(idDataJson)

    
    

    // Agregar la fila seleccionada al conjunto completo de datos
    var combinedData = {
        selectedRow: data,
        allData: data_json,
        idDataJson:idDataJson
    };

    // Realiza una solicitud POST al servidor para enviar los datos combinados
    $.ajax({
    url: '/admin/destino',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(combinedData),
    success: function(response) {
        // Imprime la respuesta para verificar si se recibe correctamente
        console.log(response);

        // Redirige directamente a la función destino después de completar la solicitud
        window.location.href = '/admin/destino';
    },
    error: function(error) {
        console.error("Error al enviar datos por POST:", error);
    }
});
});


} catch (error) {
    console.error("Error al analizar la cadena JSON:", error);
}

        </script>
        
              <!-- Card -->
              
<br>


<h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
  Mapa de Calor
</h2>
<div class="min-w-0 p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800">
  <h4 class="mb-4 font-semibold text-gray-800 dark:text-gray-300">
    Mapa de Calor de Anomalías en Departamentos
  </h4>

  <div class="flex">
    <div id="table-container" style="margin-right: 9.5rem;" class="table dataTable no-footer">
      <!-- La tabla generada por JavaScript se insertará aquí -->
    </div>

    <script>
      var data_json_str = {{ data_json | safe }};
      var dataJSON = JSON.parse(data_json_str);
      var anomaliasPorDepartamento = {};

      dataJSON.data.forEach(function (row) {
        var departamento = row[dataJSON.columns.indexOf('DEPARTAMENTO')];
        var anomalia = row[dataJSON.columns.indexOf('anomalia_etiqueta')];

        if (anomaliasPorDepartamento[departamento] === undefined) {
          anomaliasPorDepartamento[departamento] = 0;
        }

        if (anomalia === 1) {
          anomaliasPorDepartamento[departamento]++;
        }
      });

      var table = document.createElement('table');
      var thead = document.createElement('thead');
      var headerRow = thead.insertRow(0);
      headerRow.insertCell(0).textContent = 'DEPARTAMENTO';
      headerRow.insertCell(1).textContent = 'Anomalias';
      table.appendChild(thead);

      var tbody = document.createElement('tbody');
      for (var departamento in anomaliasPorDepartamento) {
        if (anomaliasPorDepartamento.hasOwnProperty(departamento)) {
          var newRow = tbody.insertRow();
          newRow.insertCell(0).textContent = departamento;
          newRow.insertCell(1).textContent = anomaliasPorDepartamento[departamento];
        }
      }

      table.appendChild(tbody);

      var container = document.getElementById('table-container');
      container.appendChild(table);
    </script>

    <div id="heatmap_div" style="height: 500px;"></div>

    <script type="text/javascript">
      var data_json_str = {{ data_json | safe }};
      var dataJSON = JSON.parse(data_json_str);
      var recuentoAnomaliasPorDepartamento = {};

      dataJSON.data.forEach(function (row) {
        var departamento = row[dataJSON.columns.indexOf('DEPARTAMENTO')];
        var anomalia = row[dataJSON.columns.indexOf('anomalia_etiqueta')];

        if (recuentoAnomaliasPorDepartamento[departamento] === undefined) {
          recuentoAnomaliasPorDepartamento[departamento] = 0;
        }

        if (anomalia === 1) {
          recuentoAnomaliasPorDepartamento[departamento]++;
        }
      });

      var datosDepartamento = [];

      for (var departamento in recuentoAnomaliasPorDepartamento) {
        if (recuentoAnomaliasPorDepartamento.hasOwnProperty(departamento)) {
          datosDepartamento.push([departamento, recuentoAnomaliasPorDepartamento[departamento]]);
        }
      }

      // Asegurémonos de que 'CUSCO' se encuentre dentro de los datos de departamentos
      if (!recuentoAnomaliasPorDepartamento['CUSCO']) {
        recuentoAnomaliasPorDepartamento['CUSCO'] = 0;
      }

      google.charts.load('current', { 'packages': ['geochart'] });
      google.charts.setOnLoadCallback(drawHeatmap);

      function drawHeatmap() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'DEPARTAMENTO');
        data.addColumn('number', 'Anomalias');
        data.addRows(datosDepartamento);

        var options = {
          title: 'Mapa de Calor de Anomalías por Departamento',
          width: 600,
          height: 400,
          region: 'PE',
          displayMode: 'regions',
          resolution: 'provinces'
        };

        var chart = new google.visualization.GeoChart(document.getElementById('heatmap_div'));
        chart.draw(data, options);
      }
    </script>
  </div>
</div>


              



          
              
    
            <!-- Charts -->
            <h2
              class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200"
            >
              Informes Graficos
            </h2>
            <div class="grid gap-6 mb-8 md:grid-cols-2">
              <div
                class="min-w-0 p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800"
              >
                <h4 class="mb-4 font-semibold text-gray-800 dark:text-gray-300">
                  5 Primeras Marcas con mas anomalias
                </h4>
                
                <div
                  class="flex justify-center mt-4 space-x-3 text-sm text-gray-600 dark:text-gray-400"
                >
                  <!-- Agrega un elemento canvas para el gráfico -->
                  <div style="width: 350px; height: 350px;">
                    <canvas id="anomaliasPorMarcaChart"></canvas>
                  </div>

<script>
  // Obtener el JSON de los datos (asegúrate de que esto esté definido en tu HTML)
  var data_json_str = {{ data_json | safe }};
  var datosJSON = JSON.parse(data_json_str);

  // Crear un objeto para almacenar los conteos de anomalías por marca
  var anomaliasPorMarca = {};

  // Iterar a través de tus datos y contar anomalías basadas en 'Marca'
  datosJSON.data.forEach(function (row) {
    var marca = row[datosJSON.columns.indexOf('MARCA')];
    var anomaliaEtiqueta = row[datosJSON.columns.indexOf('anomalia_etiqueta')];

    // Verificar si la marca está definida en anomaliasPorMarca
    if (!anomaliasPorMarca[marca]) {
      anomaliasPorMarca[marca] = 0;
    }

    // Contar la anomalía si es 1
    if (anomaliaEtiqueta === 1) {
      anomaliasPorMarca[marca]++;
    }
  });

  // Filtrar las 5 primeras marcas con más anomalías
  var marcasConAnomalias = Object.keys(anomaliasPorMarca).filter(function(marca) {
    return anomaliasPorMarca[marca] > 0;
  }).sort(function(a, b) {
    return anomaliasPorMarca[b] - anomaliasPorMarca[a];
  }).slice(0, 5); // Filtrar las primeras 5 marcas

  // Obtener los datos y etiquetas correspondientes
  var datosFiltrados = marcasConAnomalias.map(function(marca) {
    return anomaliasPorMarca[marca];
  });
  var etiquetasFiltradas = marcasConAnomalias;

  // Define colores para el gráfico
  var colores = [
    'rgba(255, 99, 132, 0.6)',
    'rgba(54, 162, 235, 0.6)',
    'rgba(255, 206, 86, 0.6)',
    'rgba(75, 192, 192, 0.6)',
    'rgba(153, 102, 255, 0.6)',
    // Agrega más colores aquí
  ];

  // Obtener el contexto del canvas
  var ctx = document.getElementById("anomaliasPorMarcaChart").getContext("2d");

  // Crear el gráfico circular
  var chart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: etiquetasFiltradas, // Marcas como etiquetas
      datasets: [
        {
          data: datosFiltrados, // Datos de conteo
          backgroundColor: colores
        }
      ]
    }
  });
</script>


                </div>
              </div>

              

              
              

              <div
                class="min-w-0 p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800"
              >
                <h4 class="mb-4 font-semibold text-gray-800 dark:text-gray-300">
                  Estado Orden
                </h4>
                
                <div
                  class="flex justify-center mt-4 space-x-3 text-sm text-gray-600 dark:text-gray-400"
                >
                  <!-- Chart legend -->
                  <div id="piechart" style="height: 400px;"></div>
                </div>
              </div>

             
              

              <script>
                // Obtener el JSON de los datos (asegúrate de que esto esté definido en tu HTML)
                var data_json_str = {{ data_json | safe }};
                var datosJSON = JSON.parse(data_json_str);

                // Verificar si datosJSON está definido y tiene datos
                var anomaliasPorEstado = {};

                // Iterar a través de tus datos y contar anomalías basadas en 'ESTADO_ORDEN'
                datosJSON.data.forEach(function (row) {
                  var estadoOrden = row[datosJSON.columns.indexOf('ESTADO_ORDEN')];
                  var anomaliaEtiqueta = row[datosJSON.columns.indexOf('anomalia_etiqueta')];

                  // Verificar si el estado de orden está definido en anomaliasPorEstado
                  if (!anomaliasPorEstado[estadoOrden]) {
                    anomaliasPorEstado[estadoOrden] = 0;
                  }

                  // Contar la anomalía si es 1
                  if (anomaliaEtiqueta === 1) {
                    anomaliasPorEstado[estadoOrden]++;
                  }
                });

                // Crear una tabla HTML con los resultados
                var tableHTML = '<table class="table">';
                tableHTML += '<thead><tr><th>Estado Orden</th><th>Contador</th></tr></thead>';
                tableHTML += '<tbody>';

                // Iterar sobre los resultados y agregar filas a la tabla
                for (var estado in anomaliasPorEstado) {
                  if (anomaliasPorEstado.hasOwnProperty(estado)) {
                    tableHTML += `<tr><td>${estado}</td><td>${anomaliasPorEstado[estado]}</td></tr>`;
                    xValues.push(estado);
                    yValues.push(anomaliasPorEstado[estado]);
                  }
                }

                tableHTML += '</tbody></table>';

                // Mostrar la tabla en el contenedor especificado
                var tableContainer = document.getElementById('anomalias-table');
                tableContainer.innerHTML = tableHTML;



              </script>



<div style="width: 1200px; display: flex; flex-direction: column;">
  <div style="margin-bottom: 20px;">
    <div style="width: 1200px; padding: 20px; background-color: #fff; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);" class="dark:bg-gray-800">
      <h4 class="mb-4 font-semibold text-gray-800 dark:text-gray-300">Anomalias por Proveedores</h4>
      <div class="flex justify-center mt-4 text-sm text-gray-600 dark:text-gray-400">
        <!-- Primer gráfico de barras -->
        <canvas id="anomaliasPorProveedorChart" width="1100" height="600"></canvas>
      </div>
    </div>
  </div>

  <div style="width: 1200px; padding: 20px; background-color: #fff; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);" class="dark:bg-gray-800">
    <h4 class="mb-4 font-semibold text-gray-800 dark:text-gray-300">Anomalias por Entidades</h4>
    <div class="flex justify-center mt-4 text-sm text-gray-600 dark:text-gray-400">
      <!-- Segundo gráfico de barras -->
      <canvas id="anomaliasPorEntidadHorizontalChart" width="1100" height="600"></canvas>
    </div>
  </div>
</div>








<script>
  // Obtener el JSON de los datos (asegúrate de que esto esté definido en tu HTML)
  var data_json_str = {{ data_json | safe }};
  var datosJSON = JSON.parse(data_json_str);

 

  // Crear un objeto para almacenar los conteos de anomalías por proveedor
  var anomaliasPorProveedor = {};

  // Iterar a través de tus datos y contar anomalías basadas en 'Proveedor'
  datosJSON.data.forEach(function (row) {
    var proveedor = row[datosJSON.columns.indexOf('PROVEEDOR')];
    var anomaliaEtiqueta = row[datosJSON.columns.indexOf('anomalia_etiqueta')];

    // Verificar si el proveedor está definido en anomaliasPorProveedor
    if (!anomaliasPorProveedor[proveedor]) {
      anomaliasPorProveedor[proveedor] = 0;
    }

    // Contar la anomalía si es 1
    if (anomaliaEtiqueta === 1) {
      anomaliasPorProveedor[proveedor]++;
    }
  });

  var proveedoresConMasDeUnaAnomalia = Object.keys(anomaliasPorProveedor).filter(function(proveedor) {
    return anomaliasPorProveedor[proveedor] > 1; // Cambiado a > 1 para mostrar solo los proveedores con más de una anomalía
  });

  // Obtener los datos y etiquetas correspondientes de proveedores con más de una anomalía
  var datosFiltrados = proveedoresConMasDeUnaAnomalia.map(function(proveedor) {
    return anomaliasPorProveedor[proveedor];
  });
  var etiquetasFiltradas = proveedoresConMasDeUnaAnomalia;

  // Obtener el contexto del canvas y crear el gráfico de barras horizontal
  var ctx = document.getElementById("anomaliasPorProveedorChart").getContext("2d");
  var chart = new Chart(ctx, {
    type: "horizontalBar",
    data: {
      labels: etiquetasFiltradas, // Proveedores con más de una anomalía como etiquetas
      datasets: [
        {
          label: "Anomalías por Proveedor",
          data: datosFiltrados, // Datos de conteo para proveedores con más de una anomalía
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1
        }
      ]
    },
    options: {
      indexAxis: 'y',
      scales: {
        x: {
          beginAtZero: true
        }
      }
    }
  });
</script>








<script>
  // Obtener el JSON de los datos (asegúrate de que esto esté definido en tu HTML)
  var data_json_str = {{ data_json | safe }};
  var datosJSON = JSON.parse(data_json_str);

  // Crear un objeto para almacenar los conteos de anomalías por entidad
  var anomaliasPorEntidad = {};

  // Iterar a través de tus datos y contar anomalías basadas en 'Entidad'
  datosJSON.data.forEach(function (row) {
    var entidad = row[datosJSON.columns.indexOf('ENTIDAD')];
    var anomaliaEtiqueta = row[datosJSON.columns.indexOf('anomalia_etiqueta')];

    // Verificar si la entidad está definida en anomaliasPorEntidad
    if (!anomaliasPorEntidad[entidad]) {
      anomaliasPorEntidad[entidad] = 0;
    }

    // Contar la anomalía si es 1
    if (anomaliaEtiqueta === 1) {
      anomaliasPorEntidad[entidad]++;
    }
  });

  // Filtrar entidades con un valor mayor a 0
  var entidadesConAnomalias = Object.keys(anomaliasPorEntidad).filter(function(entidad) {
    return anomaliasPorEntidad[entidad] > 1;
  });

  // Obtener los datos y etiquetas correspondientes
  var datosFiltrados = entidadesConAnomalias.map(function(entidad) {
    return anomaliasPorEntidad[entidad];
  });
  var etiquetasFiltradas = entidadesConAnomalias;

  // Obtener el contexto del canvas
  var ctx2 = document.getElementById("anomaliasPorEntidadHorizontalChart").getContext("2d");

  // Crear el gráfico de barras horizontal para las entidades
  var chart2 = new Chart(ctx2, {
    type: "horizontalBar", // Cambiado a tipo horizontalBar
    data: {
      labels: etiquetasFiltradas, // Entidades como etiquetas
      datasets: [
        {
          label: "Anomalías por Entidad",
          data: datosFiltrados, // Datos de conteo
          backgroundColor: "rgba(75, 192, 192, 0.2)", // Color de las barras
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1
        }
      ]
    },
    options: {
      indexAxis: 'y', // Establecer el eje horizontal
      scales: {
        x: {
          beginAtZero: true
        }
      }
    }
  });
</script>






<script type="text/javascript">
  var data_json_str = {{ data_json | safe }};
  var dataJSON = JSON.parse(data_json_str);

  // Inicializar un objeto para almacenar el recuento de anomalías por estado de orden
  var recuentoAnomaliasPorEstado = {};

  // Recorrer tus datos para calcular el recuento de anomalías por estado de orden
  dataJSON.data.forEach(function (row) {
    var estadoOrden = row[dataJSON.columns.indexOf('ESTADO_ORDEN')];
    var anomalia = row[dataJSON.columns.indexOf('anomalia_etiqueta')];

    if (recuentoAnomaliasPorEstado[estadoOrden] === undefined) {
      recuentoAnomaliasPorEstado[estadoOrden] = 0;
    }

    if (anomalia === 1) {
      recuentoAnomaliasPorEstado[estadoOrden]++;
    }
  });

  // Crear una matriz en el formato adecuado para el Pie Chart
  var datosEstado = [['Estado de Orden', 'Recuento de Anomalías']];
  for (var estado in recuentoAnomaliasPorEstado) {
    if (recuentoAnomaliasPorEstado.hasOwnProperty(estado)) {
      datosEstado.push([estado, recuentoAnomaliasPorEstado[estado]]);
    }
  }

  google.charts.load('current', { 'packages': ['corechart'] });
  google.charts.setOnLoadCallback(drawPieChart);

  function drawPieChart() {
    var data = google.visualization.arrayToDataTable(datosEstado);

    var options = {
      title: 'Recuento de Anomalías por Estado de Orden',
      width: 600,
      height: 400,
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
  }
</script>





            </div>
          </div>
        </main>
      </div>
    </div>

    <script>
      var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
      var yValues = [55, 49, 44, 24, 15];
      var barColors = ["red", "green","blue","orange","brown"];
      
      new Chart("myChart", {
        type: "bar",
        data: {
          labels: xValues,
          datasets: [{
            backgroundColor: barColors,
            data: yValues
          }]
        },
        options: {
          legend: {display: false},
          title: {
            display: true,
            text: "World Wine Production 2018"
          }
        }
      });
      </script>
  </body>
</html>
