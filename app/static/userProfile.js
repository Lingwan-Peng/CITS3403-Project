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
    document.getElementById("newBio").value  = document.getElementById("Bio").textContent;
}

function saveProfile() {
    let newName = document.getElementById("newName").value;
    let newEmail = document.getElementById("newEmail").value;
    let newPhone = document.getElementById("newPhone").value;
    let newDOB  = document.getElementById("newDOB").value;
    let newBio   = document.getElementById("newBio").value;

    // Update profile data
    document.getElementById("Name").textContent = newName;
    document.getElementById("Email").textContent = newEmail;
    document.getElementById("Phone").textContent = newPhone;
    document.getElementById("DOB").textContent = newDOB;
    document.getElementById("Bio").textContent = newBio;

    // Hide editProfile div and show profile div
    document.getElementById("profile").style.display = "block";
    document.getElementById("editProfile").style.display = "none";
}