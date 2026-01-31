from flask import Flask, render_template, request
import platform, psutil, time, socket
app = Flask(__name__)

@app.route('/')
def home():
    uname = platform.uname()
    system_info = {
        'System': uname.system,
        'Node Name': uname.node,
        'Release': uname.release,
        'Version': uname.version,
        'Machine': uname.machine,
        'Processor': uname.processor,
        'CPU Usage': psutil.cpu_percent(interval=1),
        'Memory Usage': psutil.virtual_memory().percent,
        'Disk Usage': psutil.disk_usage('/').percent,
        'Network': socket.gethostbyname(socket.gethostname()),
        'Uptime': time.strftime('%H:%M:%S', time.gmtime(time.time() - psutil.boot_time())),
        'Current Date and Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        'Current User': psutil.users()[0].name,
        'IP Address': socket.gethostbyname(socket.gethostname()),
        'vCPU Cores': psutil.cpu_count(logical=True),
        'CPU Cores': psutil.cpu_count(logical=False),
        'Memory': psutil.virtual_memory().total / (1024 ** 3),
        'Disk': psutil.disk_usage('/').total / (1024 ** 3)
        
    }
    return render_template('home.html', system_info=system_info)

app.run(debug=True, port=6767, host='0.0.0.0')   

