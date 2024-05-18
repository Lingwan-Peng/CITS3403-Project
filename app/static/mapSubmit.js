$(document).ready(function(){
    $("#submission").click(function(event){
      event.preventDefault();
      let stationName = $("#station_name").val();
      let phone = $("#phone").val();
      let address = $("#address").val();
      let postcode = $("#Postcode").val();
      let waitTime = $("#wait_time").val();
      $.ajax({
          url: "/map-submit",
          type: "POST",
          dataType: "json",
          data: {
            "station_name": stationName,
            "phone_num": phone,
            "address": address,
            "postcode": postcode,
            "waiting_time": waitTime
          }, 
          success: function(response) {
            console.log("AJAX success response:", response);
            window.location.href = "/home";
          },
      })
    });

  });