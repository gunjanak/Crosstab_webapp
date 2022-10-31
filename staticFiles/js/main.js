let input = document.querySelector("#myFile");
let button = document.querySelector("#myFileSubmit");
console.log('fuck')

button.disabled = true; //setting button state to disabled

input.addEventListener("change", stateHandle);

function stateHandle() {
    if (document.querySelector("#myFile").value === "") {
        button.disabled = true; //button remains disabled
    } else {
        button.disabled = false; //button is enabled
    }
}