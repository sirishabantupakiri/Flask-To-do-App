// 🌙 Dark Mode Toggle
const themeBtn = document.getElementById('toggle-theme');
const html = document.documentElement;

function setTheme(theme) {
  html.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
}

themeBtn.onclick = () => {
  const current = html.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  setTheme(next);
};

const savedTheme = localStorage.getItem('theme') || 'light';
setTheme(savedTheme);

// 🔔 Reminder Alert for tasks due today
window.onload = () => {
  const tasks = document.querySelectorAll('.task');
  tasks.forEach(task => {
    const due = task.querySelector('small:last-of-type');
    if (due && due.textContent.includes('Due')) {
      const dateStr = due.textContent.replace('Due: ', '');
      const dueDate = new Date(dateStr);
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      if (dueDate.getTime() === today.getTime()) {
        alert('📌 Reminder: You have tasks due today!');
      }
    }
  });
};
