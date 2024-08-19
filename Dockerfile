# Gunakan image Python sebagai base
FROM python:3.10-slim

# Menyimpan variable untuk bekerja di dalam container
WORKDIR /app

# Salin file requirements.txt dan instal dependensi
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file ke dalam container
COPY . .

# Menjalankan script saat container di jalankan
CMD ["python", "cek_domain.py"]
