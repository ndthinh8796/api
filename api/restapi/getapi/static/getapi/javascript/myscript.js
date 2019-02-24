document.addEventListener("DOMContentLoaded", function(event){
  var add_param = document.querySelector("#param_button");
  var add_headers = document.querySelector("#headers_button");
  var add_body = document.querySelector("#body_button");
  var selections = document.querySelector("#method_selection");

  showBodyBlock(selections);

  add_param.addEventListener("click", function(){
    addInputField('key', 'value', '#params');
  });

  add_headers.addEventListener("click", function(){
    addInputField('header_key', 'header_value', '#headers');
  });

  add_body.addEventListener("click", function(){
    addInputField('body_key', 'body_value', '#body');
  });

  selections.addEventListener("change", function(){
    showBodyBlock(selections);
  });
});


function addInputField(value1, value2, field_id) {
  request_field = addLineBreak(field_id)
  const keys = [value1, value2];
  for (key of keys) {
    createInputField(key, request_field);
  };
}

function addLineBreak(id) {
  var linebreak = document.createElement("br");
  var request_field = document.querySelector(id);
  request_field.appendChild(linebreak);
  return request_field;
}

function createInputField(name, field) {
  var input = document.createElement("input");
  input.setAttribute("type", "text");
  input.setAttribute("name", name);
  input.setAttribute("placeholder", name);
  field.appendChild(input);
}

function showBodyBlock(choice){
  var body_block = document.querySelector("#body_block");
  if(choice.options[ choice.selectedIndex ].value === "get" || choice.options[ choice.selectedIndex ].value === "head"){
    body_block.style.display = "none";
  } else {
    body_block.style.display = "block";
  }
}
