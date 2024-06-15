import platform
import psutil

def get_cpu_info():
    """
    Retrieve CPU information.
    """
    try:
        cpu_info = platform.processor()
        return cpu_info
    except Exception as e:
        return f"Failed to retrieve CPU information: {e}"

def get_cpu_temperature():
    """
    Retrieve CPU temperature if available.
    """
    try:
        if hasattr(psutil, 'sensors_temperatures'):
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                cpu_temp = temps['coretemp'][0].current
                return f"{cpu_temp} °C"
            else:
                return "N/A"
        else:
            return "Temperature monitoring not supported"
    except Exception as e:
        return f"Failed to retrieve CPU temperature: {e}"

def get_cpu_usage():
    """
    Retrieve current CPU usage percentage.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        return f"{cpu_usage}%"
    except Exception as e:
        return f"Failed to retrieve CPU usage: {e}"

def check_cpu_health():
    """
    Check CPU health and print the results.
    """
    try:
        print("--- CPU Health Check ---")
        cpu_info = get_cpu_info()
        print(f"CPU: {cpu_info}")

        cpu_temp = get_cpu_temperature()
        print(f"CPU Temperature: {cpu_temp}")

        cpu_usage = get_cpu_usage()
        print(f"CPU Usage: {cpu_usage}")

    except Exception as e:
        print(f"Error during CPU health check: {e}")

if __name__ == "__main__":
    check_cpu_health()
