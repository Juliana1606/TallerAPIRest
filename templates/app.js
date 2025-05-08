document.addEventListener('DOMContentLoaded', async function() {
    // URL de tu API donde están las tarjetas
    const url = 'http://127.0.0.1:5000/tu_endpoint_aqui'; // Cambia esto por la URL real de tu API

    try {
        // Realizamos la solicitud GET para obtener las tarjetas
        const response = await fetch(url);
        const data = await response.json(); // Convertimos la respuesta a formato JSON

        const contenedor = document.getElementById('contenedor-tarjetas');

        // Recorremos los datos y generamos las tarjetas
        data.forEach(item => {
            const tarjeta = document.createElement('div');
            tarjeta.classList.add('tarjeta');

            tarjeta.innerHTML = `
    <img src="${item.imagen}" alt="${item.titulo}">
    <h2>${item.titulo}</h2>
    <p>${item.descripcion}</p>
    <a href="#" class="boton">Ver más</a>
`;

            // Añadimos la tarjeta al contenedor
            contenedor.appendChild(tarjeta);
        });

    } catch (error) {
        console.error('Error al cargar las tarjetas:', error);
    }
});
