
**📄 system_check.py**
```python
import psutil

print(f"CPU-Auslastung: {psutil.cpu_percent()}%")
print(f"RAM-Auslastung: {psutil.virtual_memory().percent}%")
print(f"Festplatten-Auslastung: {psutil.disk_usage('/').percent}%")
