let timer;
let seconds = 0;
let laps = [];

function updateDisplay() {
    const display = document.getElementById('display');
    const loading = document.getElementById('loading');
    loading.classList.add('hidden');
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    display.innerText = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}

document.getElementById('startBtn').onclick = () => {
    clearInterval(timer);
    timer = setInterval(() => {
        seconds++;
        updateDisplay();
    }, 1000);
};

document.getElementById('stopBtn').onclick = () => {
    clearInterval(timer);
};

document.getElementById('resetBtn').onclick = () => {
    clearInterval(timer);
    seconds = 0;
    updateDisplay();
    document.getElementById('laps').innerHTML = '';
    laps = [];
};

document.getElementById('lapBtn').onclick = () => {
    const lapNote = document.getElementById('lapNote').value;
    if (lapNote.trim() === '') {
        alert('请添加有效的备注');
        return;
    }
    laps.push({ time: seconds, note: lapNote });
    const lapDisplay = document.createElement('div');
    lapDisplay.innerText = `计次: ${Math.floor(seconds / 3600)}:${Math.floor((seconds % 3600) / 60)}:${seconds % 60} - 备注: ${lapNote}`;
    document.getElementById('laps').appendChild(lapDisplay);
    document.getElementById('lapNote').value = '';
};
