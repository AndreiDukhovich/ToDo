let displayValyes = ['none', 'block'];
let elements = [document.getElementById('datetime'),
                document.getElementById('onlydate'), 
                document.getElementById('onlytime')];
let classes = ['up', 'down']
let b = 1
let requiredField = [timeField, dateField]

function notRequired(elem) {
      let elemsInput = elements[elem].getElementsByTagName('input');
      requiredField = []
      for (let j = 0; j<elemsInput.length; j++) {
          requiredField.push(elemsInput[j])
        } 
    }
  

function flipFunc(elem, a) {
  let otherElement = elements[elem];
  let orientation = otherElement.getElementsByTagName('span')[1];
  orientation.className = classes[a];
  let divForm = otherElement.getElementsByClassName('flip_form')[0];
  divForm.style = 'display:'+displayValyes[a];
}


for (let i=0; i<elements.length; i++) {
  elements[i].onclick = function(event) {
    let targetClassName = event.target.className;
    if (targetClassName != 'flip' & targetClassName != 'up' & targetClassName != 'down' & targetClassName != 'flipText') {
      return
    }
    let el1 = 0
    let el2 = 0
    if (i == 0) {
      el1 = 1
      el2 = 2
      elements[i].childNodes[3].prepend(timeField)
      elements[i].childNodes[3].prepend(dateField)
    } else if (i == 1) {
      el1 = 0
      el2 = 2
      elements[i].childNodes[3].prepend(dateField)
    } else if (i == 2) {
      el1 = 1
      el2 = 0
      elements[i].childNodes[3].prepend(timeField)
    }
    flipFunc(i, b);
    flipFunc(el1, 0);
    flipFunc(el2, 0);
    notRequired(i);
  }
}

button.onclick = function() {
    for (i=0; i<requiredField.length; i++) {
        if (requiredField[i].value == '') {
            error.innerHTML = 'Заполнены не все поля.'
            error.style = 'display: block; color: red;'
            return false
        }
    }
}