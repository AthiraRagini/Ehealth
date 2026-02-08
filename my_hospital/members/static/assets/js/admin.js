console.log('admin.js loaded');
document.addEventListener('DOMContentLoaded', function () {
    var sidebar = document.getElementById('adminSidebar');
    var btn = document.getElementById('sidebarToggle');
    var main = document.querySelector('.main-content');
    if (!sidebar || !btn || !main) return;

    btn.addEventListener('click', function () {
        sidebar.classList.toggle('collapsed');
        main.classList.toggle('collapsed');
        try { localStorage.setItem('adminSidebarCollapsed', sidebar.classList.contains('collapsed') ? '1' : '0'); } catch (e) { }
    });

    try {
        var state = localStorage.getItem('adminSidebarCollapsed');
        if (state === '1') {
            sidebar.classList.add('collapsed');
            main.classList.add('collapsed');
        }
    } catch (e) { }

    var openBtn = document.getElementById('sidebarOpenBtn');
    if (openBtn) {
        openBtn.addEventListener('click', function () {
            sidebar.classList.remove('collapsed');
            main.classList.remove('collapsed');
            try { localStorage.setItem('adminSidebarCollapsed', '0'); } catch (e) { }
        });
    }
});

    console.log('admin.js DOMContentLoaded');
    // Chart and counter enhancements for admin dashboard
document.addEventListener('DOMContentLoaded', function () {
    // Animated counters
    function animateCounts() {
        document.querySelectorAll('.count').forEach(el => {
            var target = parseFloat(el.dataset.target) || 0;
            var duration = 1400;
            var start = 0;
            var startTime = null;
            function step(timestamp) {
                if (!startTime) startTime = timestamp;
                var progress = Math.min((timestamp - startTime) / duration, 1);
                var value = Math.floor(progress * (target - start) + start);
                el.textContent = value;
                if (progress < 1) {
                    window.requestAnimationFrame(step);
                } else {
                    el.textContent = target;
                }
            }
            window.requestAnimationFrame(step);
        });
    }
    animateCounts();
    console.log('admin.js: counters animated');

    // Chart - render if Chart.js loaded and data available
    try {
        if (typeof Chart !== 'undefined') {
            const labelsEl = document.getElementById('adminRevenueLabels');
            const dataEl = document.getElementById('adminRevenueData');
            if (labelsEl && dataEl) {
                const labels = JSON.parse(labelsEl.textContent);
                const data = JSON.parse(dataEl.textContent);
                var ctx = document.getElementById('revenueChart');
                if (ctx) {
                    var c = ctx.getContext('2d');
                    // gradient
                    var gradient = c.createLinearGradient(0, 0, 0, 150);
                    gradient.addColorStop(0, 'rgba(255, 99, 132, 0.25)');
                    gradient.addColorStop(1, 'rgba(255, 99, 132, 0)');
                    new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: labels,
                            datasets: [{
                                label: 'Revenue',
                                data: data,
                                backgroundColor: gradient,
                                borderColor: 'rgba(255,99,132,1)',
                                fill: true,
                                tension: 0.4,
                                pointRadius: 3,
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    ticks: { callback: function (value) { return '₹' + value; } }
                                }
                            },
                            plugins: {
                                legend: { display: false }
                            }
                        }
                    });
                }
            }
        }
    } catch (e) { console.error('Error rendering admin chart', e); }
});
