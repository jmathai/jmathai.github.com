(function() {
  var headerImg = 'assets/home/img/header-medium.jpg'
      , imgEl = document.createElement("IMG");

  if(window.innerWidth >= 1170) {
    headerImg = 'assets/home/img/header-large.jpg';
  }
  
  imgEl.onload = function(e) {
    document.getElementsByTagName('header')[0].className = 'crisp';
  };
  imgEl.src = headerImg;
  return;
  var poll = function() {
    var thisNumber = this.number;
    console.log(thisNumber);
    $.get('https://api.joule.run/jmathai/joule-byot/number?number='+thisNumber, function(response) {
      if(response['name']) {
        $('h2.name').html('Hello, ' + response['name']).show();
        $('h3.name').show();
      }
      setTimeout(poll.bind({number: thisNumber}), '5000');
    });

  };

  var headerFromIp = function() {
    $.get('https://api.joule.run/jmathai/joule-byot/iplookup', function(ipResponse) {
      $.get('https://api.joule.run/jmathai/joule-byot/photobycity?cityName='+ipResponse['city'], function(cityResponse) {
        setHeader(cityResponse, false);
      });
    });
  };

  var setHeader = function(response, $form) {
    var styleSheet = document.styleSheets[document.styleSheets.length-1];
    styleSheet.addRule('header', 'background-image: url("'+response['imageUrl']+'")');
    $('header h1').html(response['cityName']+'<small>'+response['imageTitle']+'</small>').show();
    $form && $form.hide();
  };

  var init = function() {
    var styleSheet = document.styleSheets[document.styleSheets.length-1];
    styleSheet.addRule('header', 'background-image: url("../img/teamwork.jpg")');
    /*headerFromIp();
    $('input[type="tel"]').mask('(999) 999-9999');
    $('form.number').on('submit', function(ev) {
      ev.preventDefault();
      var $form = $(ev.currentTarget)
          , $input = $('input', $form)
          , phoneNumber = $input.val()
          , areaCode = phoneNumber.substr(0, 3);

      if(areaCode.length !== 3) {
        // not a number
      } else {
        $.get('https://api.joule.run/jmathai/joule-byot/lookup?number='+areaCode, function(response) {
            setHeader(response, $form);
        });

        $.get('https://api.joule.run/jmathai/joule-byot/register?number='+phoneNumber, function(response) {
          console.log(response);
          if(response['status']) {
            poll.bind({number: response['number']})();
          }
        });
      }
    });*/
  };

  init();
})();
