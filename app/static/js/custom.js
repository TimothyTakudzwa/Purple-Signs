$(document).ready(function() {
  $("#basic1").click(function() {
    $("#classes").fadeIn("slow");
    $("#jumbotron").hide();
    $("#carouselimages").hide();
    $("#dictionary_div").hide();
    $("#constitution").hide();
    $("#videos").hide();
    $("#courses").hide();
    $("#basic").hide();
    $("#homepage").removeClass("active");
    $("#learning").removeClass("active");
    $("#constitution_tab").removeClass("active");
    $("#courses_tab").removeClass("active");
    $("#greetings").addClass("active");
  });
});


// Play Video 
$(document).ready(function() {
  var t = $('#example').DataTable();
  
  var counter = 1;
  $(".play_video").click(function() {
    t.clear();
    id = $(this).data("id")
    $("#back_button").attr("data-id", id);
    $.ajax({

      type: "GET",
      dataType: "json",

      url: "http://purple-sign.herokuapp.com/api/phrase/" + id
    }).done(function (response) {
      if (response.error) {
      } else {
        if (response.message == "failed") {
          console.log("error");
        } else {
          console.log(response);
          $.each(response, function (i, item) {
            $("#classes").hide();
            $("#basic").show();
            var node = item.file_name;
            t.row.add([
              '<a style="cursor: pointer;" onClick="gotoNode(\''+node+'\')">'+item.phrase+'</a>',
              '<span>View Image </span>',
              '<span>Play Vide </span>'

            ]).draw(false);

            console.log(item.id)
          });
        }
      }
    });


    // $("#classes").fadeIn('slow');
    // $("#jumbotron").hide();
    // $("#carouselimages").hide();
    // $("#videos").hide();
    // $("#dictionary_div").hide();
    // $("#constitution").hide();
    // $("#courses").hide();

    // $("#homepage").removeClass("active");
    // $("#learning").removeClass("active");
    // $("#constitution_tab").removeClass("active");
    // $("#courses_tab").removeClass("active");
    // $("#greetings").addClass("active");
  });
});
// <? Play Video ?> 



$(document).ready(function() {
  $("#greetings").click(function() {
    $("#classes").fadeIn('slow');
    $("#jumbotron").hide();
    $("#carouselimages").hide();
    $("#videos").hide();
    $("#dictionary_div").hide();
    $("#constitution").hide();
    $("#courses").hide();
    $("#basic").hide();
    $("#homepage").removeClass("active");
    $("#learning").removeClass("active");
    $("#constitution_tab").removeClass("active");
    $("#courses_tab").removeClass("active");
    $("#greetings").addClass("active");
  });
});

$(document).ready(function() {
  $("#constitution_tab").click(function() {
    $("#constitution").fadeIn('slow');
    $("#jumbotron").hide();
    $("#carouselimages").hide();
    $("#dictionary_div").hide();
    $("#classes").hide();
    $("#videos").hide();
    $("#courses").hide();
    $("#basic").hide();
    $("#homepage").removeClass("active");
    $("#greetings").removeClass("active");
    $("#courses_tab").removeClass("active");
    $("#learning").removeClass("active");
    $("#constitution_tab").addClass("active");
  });
});

$(document).ready(function() {
  $("#constitution_tab1").click(function() {
    $("#constitution").fadeIn('slow');
    $("#jumbotron").hide();
    $("#carouselimages").hide();
    $("#dictionary_div").hide();
    $("#videos").hide();
    $("#classes").hide();
    $("#courses").hide();
    $("#basic").hide();
    $("#homepage").removeClass("active");
    $("#greetings").removeClass("active");
    $("#courses_tab").removeClass("active");
    $("#learning").removeClass("active");
    $("#constitution_tab").addClass("active");
  });
});

$(document).ready(function() {
  $("#homepage").click(function() {
    $("#videos").fadeIn('slow');
    $("#classes").hide();
    $("#carouselimages").fadeIn('slow');
    $("#dictionary_div").hide();
    $("#videos").hide();
    $("#constitution").hide();
    $("#courses").hide();
    $("#basic").hide();
    $("#learning").removeClass("active");
    $("#constitution_tab").removeClass("active");
    $("#greetings").removeClass("active");
    $("#courses_tab").removeClass("active");
    $("#homepage").addClass("active");
  });
});

$(document).ready(function() {
  $("#learning").click(function() {
    $("#dictionary_div").fadeIn('slow');
    $("#carouselimages").hide();
    $("#classes").hide();
    $("#jumbotron").hide();
    $("#videos").hide();
    $("#dictionary").hide();
    $("#constitution").hide();
    $("#courses").hide();
    $("#basic").hide();
    $("#homepage").removeClass("active");
    $("#greetings").removeClass("active");
    $("#constitution_tab").removeClass("active");
    $("#courses_tab").removeClass("active");
    $("#learning").addClass("active");
  });
});
$(document).ready(function() {
  $("#dictionary1").click(function() {
    $("#dictionary_div").fadeIn('slow');
    $("#classes").hide();
    $("#carouselimages").hide();
    $("#dictionary").hide();
    $("#videos").hide();
    $("#constitution").hide();
    $("#jumbotron").hide();
    $("#courses").hide();
    $("#basic").hide();
    $("#homepage").removeClass("active");
    $("#greetings").removeClass("active");
    $("#constitution_tab").removeClass("active");
    $("#courses_tab").removeClass("active");
    $("#learning").addClass("active");
  });
});

$(document).ready(function() {
  $("#courses_tab").click(function() {
    $("#courses").fadeIn('slow');
    
    $("#classes").hide();
    $("#dictionary").hide();
    $("#carouselimages").hide();
    $("#videos").hide();
    $("#constitution").hide();
    $("#jumbotron").hide();
    $("#basic").hide();
    $("#homepage").removeClass("active");
    $("#learning").removeClass("active");
    $("#greetings").removeClass("active");
    $("#constitution_tab").removeClass("active");
    $("#courses_tab").addClass("active");
  });
});

$(document).ready(function() {
  $("#courses_tab1").click(function() {
    $("#courses").fadeIn('slow');
    $("#classes").hide();
    $("#carouselimages").hide();
    $("#dictionary").hide();
    $("#constitution").hide();
    $("#videos").hide();
    $("#jumbotron").hide();
    $("#basic").hide();
    $("#homepage").removeClass("active");
    $("#learning").removeClass("active");
    $("#greetings").removeClass("active");
    $("#constitution_tab").removeClass("active");
    $("#courses_tab").addClass("active");
  });
});

$(document).ready(function() {
  $("#owl-demo").owlCarousel({
    navigation: true
  });
});
var TxtRotate = function(el, toRotate, period) {
  this.toRotate = toRotate;
  this.el = el;
  this.loopNum = 0;
  this.period = parseInt(period, 5) || 10;
  this.txt = "";
  this.tick();
  this.isDeleting = false;
};

TxtRotate.prototype.tick = function() {
  var i = this.loopNum % this.toRotate.length;
  var fullTxt = this.toRotate[i];

  if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
  } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
  }

  this.el.innerHTML = '<span class="wrap">' + this.txt + "</span>";

  var that = this;
  var delta = 300 - Math.random() * 100;

  if (this.isDeleting) {
    delta /= 2;
  }

  if (!this.isDeleting && this.txt === fullTxt) {
    delta = this.period;
    this.isDeleting = true;
  } else if (this.isDeleting && this.txt === "") {
    this.isDeleting = false;
    this.loopNum++;
    delta = 200;
  }

  setTimeout(function() {
    that.tick();
  }, delta);
};

window.onload = function() {
  var elements = document.getElementsByClassName("txt-rotate");
  for (var i = 0; i < elements.length; i++) {
    var toRotate = elements[i].getAttribute("data-rotate");
    var period = elements[i].getAttribute("data-period");
    if (toRotate) {
      new TxtRotate(elements[i], JSON.parse(toRotate), period);
    }
  }
  // INJECT CSS
  var css = document.createElement("style");
  css.type = "text/css";
  css.innerHTML = ".txt-rotate > .wrap { border-right: 0.08em solid #666 }";
  document.body.appendChild(css);
};
