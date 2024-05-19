function buscarRSS(web) {
    var texto = document.getElementsByClassName('inputBuscar')[0].value;
    if (web == "elpuntavui") { // parece que no va por el bloqueo de CORS, previamente explicado en el readme
        fetch(`http://www.elpuntavui.cat/${texto}.feed?type=rss`, { method: 'HEAD' }).then((respuesta) => {
            if (respuesta.status == 200) { 
                window.location.href = `/elpuntavui/${texto}`
            } else {
                alert(`La página ${texto} no se ha encontrado en el RSS del punt avui. Prueba con otra categoria.`)
            }
        })
    } else if (web == "lavanguardia") {
        fetch(`https://www.lavanguardia.com/rss/${texto}.xml`, { method: 'HEAD' }).then((respuesta) => {
            if (respuesta.status == 200) { 
                window.location.href = `/lavanguardia/${texto}`
            } else { // feo
                alert(`La página ${texto} no se ha encontrado en el RSS de la vanguardia. Prueba con otra categoria.`)
            }
        })
    } else {
        alert("Error! La página introducida no existe/no está disponible")
    }
    
}

function abrirImagen(url) {
    document.getElementsByClassName('fotoPopup')[0].src = url;
    document.getElementsByClassName('imagenDiv')[0].hidden = false;
}

function cerrarImagen() {
    document.getElementsByClassName('imagenDiv')[0].hidden = true;
}

