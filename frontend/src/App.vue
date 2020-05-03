<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 60px;
}

body {
  font-size: 1rem !important;
  font-weight: 400 !important;
  line-height: 1.5 !important;
  color: #2e2e2e !important;
  text-align: left !important;

}

body {
  background-image: repeating-linear-gradient(rgba(255,255,255,.90), rgba(255,255,255,.90)), url("assets/grafismo.png");
  background-size: cover;
}

.body-view {
  padding: 65px 0px 20px 0px;
  background-color: white;
  -webkit-box-shadow: 0px 0px 9px 8px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 0px 9px 8px rgba(0,0,0,0.1);
  box-shadow: 0px 0px 9px 8px rgba(0,0,0,0.1);
}

label {
  font-weight: bold;
}

.navbar  {
  background-color: rgb(1, 59, 67) !important;
  box-shadow: 0 0.25rem 0.25rem rgba(0,0,0,.25), inset 0 -1px 5px rgba(0,0,0,.25);
}

.nav-link {
  color: #00B3A1 !important;
}

.nav-link:hover {
  color: #CDD1CE !important;
}

.navbar-toggler-icon {
  background-color: transparent !important;
}

.page-title-holder {
  border-bottom: 1px solid #fff !important;
}

.page-title {
  margin: 16px 0 !important;
  font-size: 1.75em !important;
  font-weight: 600 !important;
  color: #2E2E2E !important;
}

.page-title-controls {
  margin-left: auto;
}

input[type='search'], input[type='select'] {
  height: 1.75em;
}

.custom-file-input ~ .custom-file-label::after {
  content: 'Abrir' !important;
}

.custom-control-input:checked ~ .custom-control-label::before {
  background-color: #118274 !important;
  border-color: #0E6B60 !important;
}

.custom-control-label:hover {
  cursor: pointer;
}

.custom-control-input:focus:not(:checked) ~ .custom-control-label::before {
  border-color: #759492 !important;
}

.custom-control-input:focus ~ .custom-control-label::before {
  box-shadow: 0 0 0 0.2rem rgba(0, 96, 88, 0.25) !important ;
}

.custom-control-input:disabled:checked ~ label::before {
  border-color: #6C757D !important;
  background-color: #6C757D !important;
}

.custom-select:focus, .form-control:focus, input:focus, a:focus {
  border-color: #759492 !important;
  box-shadow: 0 0 0 0.2rem rgba(0, 96, 88, 0.25) !important ;
}

span.sub-label {
  color: #003B42;
  display: block;
  font-size: 12px;
  font-weight: normal;
  padding-left: 0.2em;
}

button.btn-success {
  background-color: #118274;
  border-color: #0E6B60;
}

button.btn-success:focus {
  background-color: #118274 !important;
  border-color: #0E6B60 !important;
  box-shadow: 0 0 0 0.2rem rgba(0, 96, 88, 0.25) !important;
}

button.btn-success:hover {
  background-color: #0B554C !important;
  border-color: #073530 !important;
}

button.btn-outline-primary {
  border-color: #0E6B60;
  color: #0E6B60;
}

button.btn-outline-primary:hover {
  background-color: #0B554C;
  border-color: #073530;
}

button.btn-outline-primary:focus {
  border-color: #0E6B60 !important;
  box-shadow: 0 0 0 0.2rem rgba(0, 96, 88, 0.25) !important;
}

button.btn-outline-primary:not(:disabled):not(.disabled):active {
  background-color: #0B554C !important;
  border-color: #0E6B60 !important;
}

a.download-file {
  color: black !important;
}

.page-item.active .page-link {
  background-color: #118274 !important;
  border-color: #118274 !important;
  color: #FFFFFF !important;
}

.page-item.active:hover .page-link {
  box-shadow: 0px 0px 1px #118274;
}

.custom-pagination a:-webkit-any-link {
  color: #118274 !important;
}

input[type=number]::-webkit-outer-spin-button,
input[type=number]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type=number] {
  -moz-appearance: textfield;
}

.maxi-green-3 {
  background-color: #a8ba2f !important;
}

.maxi-green-2 {
  background-color: #5e9435 !important;
}

.maxi-green-1 {
  background-color: #149c90 !important;
}

.maxi-green {
  background-color: #0E6B60 !important;
}

.footer-shadow {
  box-shadow: 0.25rem 0 0.50rem 0.25rem rgba(0,0,0,.25)
}

.maxi-red {
  background-color: #B3120F !important;
}

/* Chrome, Opera, Safari, Edge */
input.custom-range::-webkit-slider-thumb {
  background: #0E6B60 !important;
}

input.custom-range:focus::-webkit-slider-thumb {
  box-shadow: 0px 0px 2px 2px rgba(0, 96, 88, 0.25) !important;
}

/* Firefox */
input.custom-range::-moz-range-thumb {
  background: #0E6B60 !important;
}

input.custom-range:focus::-moz-range-thumb {
  box-shadow: 0px 0px 2px 2px rgba(0, 96, 88, 0.25) !important;
}

input.custom-range {
  box-shadow: 0px 0px 0px !important;
}

input.custom-range:hover {
  cursor: pointer;
}

#nav-collapse li > a:not(.dropdown-item):-webkit-any-link {
  padding-top: 0px;
  color: white !important;
}

#nav-collapse li > a button {
  padding-top: 0px;
}

.tabs li > a:-webkit-any-link {
  color: #494949 !important;
}

.sub-label {
  color: darkred !important;
  font-weight: bold !important;
}

input:disabled,
div.vs--disabled > div,
div.vs--disabled > div > div > span,
div.vs--disabled button,
div.vs--disabled svg {
  color: #6C757D !important;
  background-color: #E9ECEF !important;
}

div.vs--disabled > div {
  border-color: #CED4DA !important;
}

input[type='file'] ~ label,
input[type='file'] ~ label::after {
  color: #6C757D !important;
}

ul[role='tablist'] {
  margin-bottom: 1em !important;
}

.bars {
  color: white !important;
  border-color: white !important;
  outline: 0;
}

.bars:focus {
  outline: 0;
}

a[aria-selected='false'] {
  background-color: #d3d3d380 !important;
}

input[type='range']:disabled {
  background-color: transparent !important;
}

/* Chrome, Opera, Safari, Edge */
input.custom-range:disabled::-webkit-slider-thumb {
  background: #6C757D !important;
}

/* Firefox */
input.custom-range:disabled::-moz-range-thumb {
  background: #6C757D !important;
}

button.dropdown-toggle,
button.maxi-dropdown-toggle,
button.dropdown-toggle:active,
button.maxi-dropdown-toggle:active {
  background-color: transparent !important;
  border-color: transparent;
}

.show > .btn-secondary.dropdown-toggle,
button.dropdown-toggle:focus,
button.maxi-dropdown-toggle:focus {
  background-color: transparent !important;
  border-color: transparent !important;
}

button.dropdown-toggle:hover,
button.maxi-dropdown-toggle:hover {
  background-color: #004B54;
  border-color: transparent;
}

a.dropdown-item:active {
  background-color: lightgrey !important;
}

#right-click-menu {
  display: none;
  position: fixed;
  border: 1px solid #B2B2B2;
  /*width: 160px;*/
  background: #F9F9F9;
  box-shadow: 3px 3px 2px #E9E9E9;
  border-radius: 4px;
}

#right-click-menu ul {
  list-style-type: none;
  margin: 0;
  padding: 0 10px 0 10px;
}

#right-click-menu ul:hover {
  cursor: pointer;
}

/* mobile stuff only */
@media only screen and (max-width: 600px) {
  div.container, div.container-fluid, div.col {
    padding-left: 0.05em !important;
    padding-right: 0.05em !important;
  }

  div.input-group {
    padding-left: 0.5em !important;
    padding-right: 0.5em !important;
  }

  br.desktop-break-line {
    display: none;
  }

  br.desktop-break-line ~ span {
    margin-left: 8px;
  }

  #nav-collapse {
    margin-top: 20px;
  }

  .b-popover {
    display: none !important;
  }
}

</style>
