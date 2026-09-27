document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('grafico-emociones');
    if (!canvas) {
        console.error('No se encontró el canvas con id "grafico-emociones"');
        return;
    }

    let registros;
    try {
        registros = JSON.parse(document.getElementById('datos-registros').textContent);
    } catch (error) {
        console.error('Error al parsear los datos JSON de registros:', error);
        return;
    }

    if (!registros.length) {
        console.warn('No hay registros disponibles para mostrar.');
        return;
    }

    const emociones = registros.map(r => r.emocion);
    const totales = registros.map(r => r.total);

    new Chart(canvas, {
        type: 'bar',
        data: {
            labels: emociones,
            datasets: [{
                label: 'Total de Detecciones',
                data: totales,
                backgroundColor: 'rgba(54, 162, 235, 0.5)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
});
