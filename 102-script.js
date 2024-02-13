$(document).ready(function() {
  $('#btn_translate').click(function() {
    var languageCode = $('#language_code').val();
    var url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;

    $.getJSON(url, function(data) {
      var translation = data.hello;
      $('#hello').text(translation);
    });
  });
});
