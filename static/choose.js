let checkboxs = document.getElementsByClassName('checkbox_order');
let action_buttom = document.getElementsByClassName('del_rest');
let show_buttom = function(check) {
  dispalyArg = check ? 'block': 'none';
  for (let i=0; i<action_buttom.length; i++) {
    action_buttom[i].style.display = dispalyArg;
  } 
}
let check_checked = function() {
  for (let i=0; i<checkboxs.length; i++) {
    if (checkboxs[i].checked) {
      return 1;
    }
  }
  return 0;
}
let all_checked = function() {
  for (let i=0; i<checkboxs.length; i++) {
    if (!checkboxs[i].checked) {
      return 0;
    }
  }
  return 1;
}
select_all.onclick = function(event) {
  show_buttom(select_all.checked);
  for (let i=0; i<checkboxs.length; i++) {
    checkboxs[i].checked = select_all.checked;
  }
}

for (let i=0; i<checkboxs.length; i++) {
    checkboxs[i].onclick = function(event) {
      if (check_checked()) {
        show_buttom(1);
        if (all_checked()) {
          select_all.checked = 1;
        }
      } else {
        show_buttom(0);
        select_all.checked = 0;
      }     
    }
 }

