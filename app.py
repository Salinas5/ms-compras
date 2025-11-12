import flask
import random 
import time      
import logging

app = flask.Flask(__name__)


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simular_latencia():
    
    time.sleep(random.uniform(0.1, 0.4))

@app.route('/api/compras/transaccion', methods=['POST'])
def compra_transaccion():
    
    logging.info("Recibida solicitud de TRANSACCIÓN de compra")
    simular_latencia()
    
    
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
    
    logging.info("Recibida solicitud de COMPENSACIÓN de compra (Eliminar)")
    simular_latencia()
    
    
    logging.info("Compensación de compra (eliminar) REALIZADA (Status 200)")
    return flask.jsonify({"mensaje": "Compensación de compra (eliminación) realizada"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)