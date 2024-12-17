from flask import Flask, render_template, request
import hashlib
import platform
import socket
import time

app = Flask(__name__)

@app.route('/')
def home():
    # Collecting possible data for fingerprint creation
    user_data = {
        #"user_id": "user123",  # Example user ID
        #"age": 25,
        #"gender": "Male",
        "device": platform.machine(),  # e.g., 'x86_64'
        "operating_system": platform.system(),  # e.g., 'Linux'
        "os_version": platform.version(),
        "browser": request.user_agent.browser,  # Browser (e.g., 'chrome')
        "browser_version": request.user_agent.version,  # Browser version
        "ip_address": request.remote_addr,  # User's IP address
        #"screen_resolution": "1280x720",  # Example screen resolution (this can be dynamically captured in JS)
        "timezone": time.tzname[0],  # Current timezone
        "language": request.accept_languages.best,  # User language preference
        "hostname": socket.gethostname(),  # Hostname of the server
        #"geolocation": "37.7749° N, 122.4194° W",  # Example geolocation (could be fetched with JavaScript)
        #"session_id": "abcd1234xyz",  # Example session ID
        #"last_login": "2024-12-16 15:30:00",  # Example login timestamp
    }
    
    # Combine these fields into a string and create a hash
    fingerprint_data = "".join(str(value) for value in user_data.values())
    user_fingerprint = hashlib.sha256(fingerprint_data.encode()).hexdigest()

    return render_template('index.html', user_data=user_data, fingerprint=user_fingerprint)

if __name__ == '__main__':
    app.run(debug=True)