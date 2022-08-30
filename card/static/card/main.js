// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {

        // Get the modal
        let modal = document.getElementById("rsvp_modal");
        if (event.target == modal) {
          modal.style.display = "none";
        }

}

function submitConfirmation(id_modal,confirmation){
    document.getElementById("confirm").value = confirmation;

    //alert(document.getElementById("name").value)
    if (document.getElementById("name").value!="")
        document.getElementById("frmConfirm").submit();
    else {
        //document.getElementById(id_modal).style.display = "none";
        alert("Vui lòng nhập Tên quý khách vào khung xác nhận");
    }
}
