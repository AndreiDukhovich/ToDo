let g = new Date();
let calendar = document.getElementById('calendar');
let month = g.getMonth();
let year = g.getFullYear();
let monthName = {0: 'Январь', 1: 'Февраль', 2: 'Март', 3: 'Апрель', 4: 'Май',
    5: 'Июнь', 6: 'Июль', 7: 'Август', 8: 'Сентябрь', 9: 'Октябрь', 10: 'Ноябрь', 11: 'Декабрь'}
function createCalendar(elem, year, month) {
  let mon = month;
  let d = new Date(year, month);
  let table = '<table><tr><th>пн</th><th>вт</th><th>ср</th><th>чт</th><th>пт</th><th>сб</th><th>вс</th></tr><tr>';
  let dE = new Date(year, month, 0);
  for (let i = getDay(d)-1; i >= 0; i--) {
    table += `<td class='excessDay' onclick='before()'>${dE.getDate()-i}</td>`;
  }
  while (d.getMonth() == mon) {
    table += `<td id='day'>${d.getDate()}</td>`;
    if (getDay(d) % 7 == 6) {
      table += '</tr><tr>';
    }

    d.setDate(d.getDate() + 1);
  }
  let j = 1;

  function fillWeek(init) {
    for (let i = init; i < 7; i++) {
      table += `<td class='excessDay' onclick='next()'>${j}</td>`;
      j++;
    }
  }
  if (getDay(d) != 0) {
    fillWeek(getDay(d));
  } else {
    fillWeek(0);

  }
  let counTr = table.split('tr').length-1;
  if (counTr < 13) {
    table += '</tr><tr>';
    fillWeek(0);
  }
  table += '</tr></table>';
  elem.innerHTML = table;
  let p = document.getElementById('data');
  p.innerHTML = monthName[month]+' '+year;
}
function addNull(n) {
  if (n < 10) {
    return '0'+n;
  }
  return n+'';
}
function getDay(date) {
    let day = date.getDay();
    if (day == 0) day = 7;
    return day - 1;
}

createCalendar(calendar, year, month);

function next() {
    month +=1;
    if (month > 11) {
        month = 0;
        year +=1;
    }
  createCalendar(calendar,year, month);
}

function before() {
    month -= 1;
    if (month < 0) {
      month = 11;
      year -=1;
  }
  createCalendar(calendar, year, month);
}

let cal = document.getElementById('cal');
let dateField = document.getElementById('dateField');

let currentElem = null;

cal.onmouseover = function(event) {
  if (currentElem) return;
  let target = event.target.closest('td');
  if (!target) return;
  if (!cal.contains(target)) return;
  currentElem = target;
  target.classList.add('tdHover');
};

cal.onmouseout = function(event) {
  if (!currentElem) return;
  let relatedTarget = event.relatedTarget;
  while (relatedTarget) {
    if (relatedTarget == currentElem) return;
    relatedTarget = relatedTarget.parentNode;
  }
  currentElem.classList.remove('tdHover');
  currentElem = null;
}

cal.onclick = function(event) {
  if (event.target.id != 'day' ) return;
  dateField.value = `${addNull(event.target.innerHTML)}.${addNull(month+1)}.${year}`;
  cal.style.display='none';
};

dateField.onclick=function(event) {
  cal.style.display='block';
  cal.style.top=dateField.getBoundingClientRect().bottom+'px';
  cal.style.left=dateField.getBoundingClientRect().left-(cal.offsetWidth/2-dateField.offsetWidth/2)+'px';
}

document.onclick = function(event) {
  if (event.target.id == 'main') {
  cal.style.display='none';
  clock.style.display='none';
  }
}

function createClock() {
  let hours = document.getElementById('hours');
  let hoursHtml = '';
  let minutes = document.getElementById('minutes');
  let minutesHtml = '';
  for (let i=0; i <= 23; i++) {
    hoursHtml += "<li id='hours' style='scroll-snap-align: start'>"+addNull(i)+'</li>';
  }
  for (let i=0; i < 60; i++) {
    minutesHtml += "<li id='minutes' style='scroll-snap-align: start'>"+addNull(i)+'</li>';
  }
  hours.innerHTML = hoursHtml;
  minutes.innerHTML = minutesHtml;
}
createClock();
let clockField = document.getElementById('timeField');
let clock = document.getElementById('clock')

clockField.onclick=function(event) {
  clock.style.display='flex';
  clock.style.top=clockField.getBoundingClientRect().bottom+'px';
  clock.style.left=clockField.getBoundingClientRect().left-(clock.offsetWidth/2-clockField.offsetWidth/2)+'px';
}
let time = ['00', '00']
let hourLi, minuteLi;
clock.onclick = function(event) {
  let target = event.target;
  if (event.target.id == 'hours') {
    setHour(time, target)
  }
  if (event.target.id == 'minutes') {
    setMinute(time, target)
  }
  clockField.value = time.join(':');
}

function setHour(time, target) {
  if (hourLi) {
    hourLi.style = '';
  }
  hourLi = target;
  hourLi.style = 'background-color: rgba(241, 241, 241, 0.627)';
  time[0] = hourLi.innerHTML;
}
function setMinute(time, target) {
  if (minuteLi) {
    minuteLi.style = '';
  }
  minuteLi = target;
  minuteLi.style = 'background-color: rgba(241, 241, 241, 0.627)';
  time[1] = minuteLi.innerHTML;
}
function setTime() {
  clock.style.display='none';
}