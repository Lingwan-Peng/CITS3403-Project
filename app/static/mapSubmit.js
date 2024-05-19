$(document).ready(function(){
  $("input[type='checkbox']").on("click", function(event) {
    let id = $(this).attr("id");
    let container_id = `${id}_price_container`;
    if ($(this).is(":checked")) {
      console.log(`The checkbox ${id} is checked!`);
      $(`#${container_id}`).show();
    } else {
      console.log("The checkbox is unchecked.");
      $(`#${container_id}`).hide();
    }
  });

  $("#submission").click(function(event){
    event.preventDefault();

    let stationName = $("#station_name").val();
    let phone = $("#phone").val();
    let address = $("#address").val();
    let postcode = $("#Postcode").val();
    let waitTime = $("#wait_time").val();
    
    const checkboxObject = {
      "standard_unleaded": $("#standard_unleaded").prop("checked"),
      "premium_95_octane": $("#premium_95_octane").prop("checked"),
      "premium_98_octane": $("#premium_98_octane").prop("checked"),
      "e10": $("#e10").prop("checked"),
      "e85": $("#e85").prop("checked"),
      "diesel": $("#diesel").prop("checked")
    };

    let priceObject = {};
    for (const fuelType in checkboxObject) {
      const isChecked = checkboxObject[fuelType];
      if(isChecked == true){
        let id = $(`#${fuelType}`).attr("id");
        let container_id = `${id}_price`;
        let price_value = $(`#${container_id}`).val();
        priceObject[fuelType] = price_value;
        console.log(`${fuelType}: ${price_value}`);
      }
      
    }

    console.log(priceObject);
    const priceObject_json = JSON.stringify(priceObject);
  
    $.ajax({
        url: "/map-submit",
        type: "POST",
        dataType: "json",
        data: {
          "station_name": stationName,
          "phone_num": phone,
          "address": address,
          "postcode": postcode,
          "waiting_time": waitTime,
          "checked": priceObject_json
        }, 
        success: function(response) {
          console.log("AJAX success response:", response);
          window.location.href = "/home";
        },
    })
  });

});