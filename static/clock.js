let clockField = document.getElementById('timeField');
let clock = document.getElementById('clock')

function addNull(n) {
    if (n < 10) {
      return '0'+n;
    }
    return n+'';
  }

clockField.onmousedown = function() {
    return false;
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
  
  
  clockField.onclick=function(event) {
    createClock();
    clock.style.display='flex';
    clock.style.top=clockField.getBoundingClientRect().bottom+'px';
    clock.style.left=clockField.getBoundingClientRect().left-(clock.offsetWidth/2-clockField.offsetWidth/2)+'px';
    document.addEventListener('mousedown', closeTime)
  }
  let time = ['00', '00']
  let hourLi, minuteLi;
  
  let closeTime = function(event) {
    if (!(clock.contains(event.target) || event.target === timeField)) {
    clock.style.display='none';
    document.removeEventListener('mousedown', closeTime)
    }
  }
  
  clock.onclick = function(event) {
    let target = event.target;
    if (target.id == 'hours') {
      setHour(time, target)
    }
    if (target.id == 'minutes') {
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