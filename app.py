# Menggunakan Flask RESTful API
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


# Menggunakan perantara MQTT

# from app.controller.mqtt.main import mqtt_loop
# import threading

# mqtt_thread = threading.Thread(target=mqtt_loop)
# mqtt_thread.start()