
// Simple SPA-like navigation
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const target = e.target.dataset.section;
    document.querySelectorAll('main .card').forEach(card => card.classList.remove('active'));
    document.getElementById(target).classList.add('active');
  });
});

// Helper: fetch with JWT from localStorage (set by your login page)
async function apiGet(url) {
  const token = localStorage.getItem('access_token');
  const res = await fetch(url, {
    headers: { 'Authorization': token ? `Bearer ${token}` : '' }
  });
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}

function renderAttendanceChart(data) {
  const present = data.filter(r => r.present).length;
  const absent = data.length - present;
  const ctx = document.getElementById('attendanceChart').getContext('2d');
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Present', 'Absent'],
      datasets: [{ data: [present, absent] }]
    }
  });
}

function renderGradesChart(data) {
  const bySubject = {};
  data.forEach(g => { bySubject[g.subject_name] = (bySubject[g.subject_name] || []).concat([parseFloat(g.score)]) });
  const labels = Object.keys(bySubject);
  const avgs = labels.map(k => {
    const arr = bySubject[k];
    return arr.reduce((a,b)=>a+b,0)/arr.length;
  });
  const ctx = document.getElementById('gradesChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [{ label: 'Average', data: avgs }]
    },
    options: { scales: { y: { beginAtZero: true, max: 100 } } }
  });
}

function renderFeesSummary(invoices) {
  const ul = document.getElementById('feesSummary');
  ul.innerHTML = '';
  let total = 0, paid = 0, due = 0, overdue = 0;
  invoices.forEach(inv => {
    total += parseFloat(inv.amount);
    if (inv.status === 'PAID') paid += parseFloat(inv.amount);
    if (inv.status === 'PENDING') due += parseFloat(inv.amount);
    if (inv.status === 'OVERDUE') overdue += parseFloat(inv.amount);
  });
  const li1 = document.createElement('li'); li1.textContent = `Total: ${total.toFixed(2)}`;
  const li2 = document.createElement('li'); li2.innerHTML = `<span class="status-paid">Paid: ${paid.toFixed(2)}</span>`;
  const li3 = document.createElement('li'); li3.innerHTML = `<span class="status-pending">Pending: ${due.toFixed(2)}</span>`;
  const li4 = document.createElement('li'); li4.innerHTML = `<span class="status-overdue">Overdue: ${overdue.toFixed(2)}</span>`;
  [li1, li2, li3, li4].forEach(li => ul.appendChild(li));
}

// Table renderers
function fillTable(id, rows, cols) {
  const tbody = document.getElementById(id);
  tbody.innerHTML = '';
  rows.forEach(r => {
    const tr = document.createElement('tr');
    cols.forEach(key => {
      const td = document.createElement('td');
      td.textContent = r[key];
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
}

async function loadPortal() {
  try {
    const base = '/api/guardian';
    const [attendance, grades, invoices] = await Promise.all([
      apiGet(`${base}/attendance/`),
      apiGet(`${base}/grades/`),
      apiGet(`${base}/fees/`)
    ]);

    renderAttendanceChart(attendance);
    renderGradesChart(grades);
    renderFeesSummary(invoices);

    fillTable('attendanceTable', attendance, ['date', 'status']);
    const gradeRows = grades.map(g => ({
      subject: g.subject_name, score: g.score, exam_date: g.exam_date
    }));
    fillTable('gradesTable', gradeRows, ['subject', 'score', 'exam_date']);
    const feeRows = invoices.map(i => ({
      invoice: i.invoice_no, item: i.item_name, amount: i.amount, status: i.status, due: i.due_date
    }));
    fillTable('feesTable', feeRows, ['invoice', 'item', 'amount', 'status', 'due']);
  } catch (e) {
    console.error(e);
    alert('Failed to load portal data. Are you logged in?');
  }
}

document.addEventListener('DOMContentLoaded', loadPortal);
