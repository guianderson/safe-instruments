   // If you're using a separate JavaScript file, wrap the code inside a document.ready function
document.addEventListener("DOMContentLoaded", function() {
  // Initialize the input mask
  Inputmask({ mask: "(99) 9999-9999" }).mask("#phone");
  Inputmask({ mask: "(99) 99999-9999" }).mask("#mobile");
  Inputmask({ mask: "99/9999" }).mask("#monthyear");
  Inputmask({ mask: "99:99:99" }).mask("#time");
  Inputmask({ mask: "99/99/9999 99:99:99" }).mask("#date_time");
  Inputmask({ mask: "99999-999" }).mask("#cep");
  Inputmask({ mask: "999.999.999-99" }).mask("#cpf");
  Inputmask({ mask: "99.999.999/9999-99" }).mask("#cnpj");
  Inputmask({mask: "99.99%", placeholder: "0"}).mask("#percentage");
  Inputmask({alias: 'currency', radixPoint: '.', rightAlign: false, prefix: 'R$'}).mask("#currency");
  Inputmask({alias: 'decimal', radixPoint: '.', rightAlign: false}).mask("#decimal");
  Inputmask({ mask: "999.999.999.999" }).mask("#ip-address");
});
