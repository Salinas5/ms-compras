import flask
import random  # Para simular el fallo aleatorio
import time      
import logging

app = flask.Flask(_name_)

# Configurar un logger simple para ver los pasos en la terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simular_latencia():
    """Simula un retraso de red, como pide el TP.""" [cite: 41]
    time.sleep(random.uniform(0.1, 0.4))

@app.route('/api/compras/transaccion', methods=['POST'])
def compra_transaccion():
    """
    Endpoint de transacción.
    Retornará aleatoriamente un status 200 (OK) o 409 (Conflicto/Fallo).
    """ [cite: 46, 47]
    logging.info("Recibida solicitud de TRANSACCIÓN de compra")
    simular_latencia()
    
    # Decidimos aleatoriamente si la transacción es exitosa o falla
    if random.choice([True, False]):
        # Éxito
        logging.info("Compra guardada EXITOSAMENTE (Status 200)")
        return flask.jsonify({"mensaje": "Compra guardada exitosamente"}), 200
    else:
        # Fallo
        logging.warning("Fallo al guardar la compra (Status 409)")
        return flask.jsonify({"mensaje": "Error al persistir la compra"}), 409

@app.route('/api/compras/compensacion', methods=['POST'])
def compra_compensacion():
    """
    Endpoint de compensación.
    El TP dice que este siempre retorna 200.
    """ [cite: 48]
    logging.info("Recibida solicitud de COMPENSACIÓN de compra (Eliminar)")
    simular_latencia()
    
    # La compensación (ej. eliminar el registro de compra) siempre es exitosa
    logging.info("Compensación de compra (eliminar) REALIZADA (Status 200)")
    return flask.jsonify({"mensaje": "Compensación de compra (eliminación) realizada"}), 200

if _name_ == '_main_':
    # Corremos en el puerto 5004 (como definimos en el orquestador)
    app.run(port=5004, debug=True)