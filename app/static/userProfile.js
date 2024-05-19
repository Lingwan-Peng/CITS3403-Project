$(document).ready(function () {
    function toggleEditMode() {
        let profileDiv = document.getElementById("profile");
        let editProfileDiv = document.getElementById("editProfile");

        // Toggle visibility of profile and editProfile divs
        profileDiv.style.display = "none";
        editProfileDiv.style.display = "block";

        // Populate input fields with current profile data
        document.getElementById("newName").value = document.getElementById("Name").textContent;
        document.getElementById("newEmail").value = document.getElementById("Email").textContent;
        document.getElementById("newPhone").value = document.getElementById("Phone").textContent;
        document.getElementById("newDOB").valueAsDate = new Date(document.getElementById("DOB").textContent);
        document.getElementById("newBio").value = document.getElementById("Bio").textContent;
    }

    // Function to update profile
    function updateProfile() {
        let oldName = $("#Name").val();
        let newName = $("#newName").val();
        let newEmail = $("#newEmail").val();
        let newPhone = $("#newPhone").val();
        let newDOB = $("#newDOB").val();
        let newBio = $("#newBio").val();
        $.ajax({
            url: "/userProfile",  // Update the URL endpoint
            type: "POST",
            dataType: "json",
            data: {
                "oldName": oldName,
                "newName": newName,
                "newEmail": newEmail,
                "newPhone": newPhone,
                "newDOB": newDOB,
                "newBio": newBio
            },
            success: function (response) {
                console.log("AJAX request successful!");
                // Handle the response from the server
                console.log(response);
                // update the UI with the updated profile data
                document.getElementById("Name").textContent = newName;
                document.getElementById("Email").textContent = newEmail;
                document.getElementById("Phone").textContent = newPhone;
                document.getElementById("DOB").textContent = newDOB;
                document.getElementById("Bio").textContent = newBio;
                // Hide editProfile div and show profile div
                document.getElementById("profile").style.display = "block";
                document.getElementById("editProfile").style.display = "none";

            }
           
        })
    }
    // Bind click event to toggleEdit button
    $("#update").click(function(event){
        event.preventDefault();
        toggleEditMode();
    });

    // Bind click event to update button
    $("#save").click(function(event){
        event.preventDefault();
        updateProfile();
    });
});
