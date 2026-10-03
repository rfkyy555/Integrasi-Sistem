from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API Integrasi Sistem - Tugas 1",
    description="API CRUD Data Mahasiswa menggunakan FastAPI",
    version="1.0.0"
)

# Model Data Mahasiswa sesuai soal
class Mahasiswa(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

# Simulasi Database Sederhana di Memory
mahasiswa_db = {}

# ROOT
@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Data Mahasiswa!"}

# CREATE (POST)
@app.post("/mahasiswa/{nim}", summary="Tambah Data Mahasiswa")
async def create_mahasiswa(nim: int, data: Mahasiswa):
    if nim in mahasiswa_db:
        raise HTTPException(status_code=400, detail="NIM sudah terdaftar!")
    
    mahasiswa_db[nim] = data.dict()
    return {
        "message": "Data mahasiswa berhasil ditambahkan",
        "data": mahasiswa_db[nim]
    }

# READ ALL (GET)
@app.get("/mahasiswa/", summary="Ambil Semua Data Mahasiswa")
async def get_all_mahasiswa():
    return {"total": len(mahasiswa_db), "data": mahasiswa_db}

# READ BY NIM (GET)
@app.get("/mahasiswa/{nim}", summary="Ambil Data Mahasiswa Berdasarkan NIM")
async def read_mahasiswa(nim: int):
    if nim not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan!")
    return {"nim": nim, "data": mahasiswa_db[nim]}

# UPDATE (PUT)
@app.put("/mahasiswa/{nim}", summary="Update Data Mahasiswa")
async def update_mahasiswa(nim: int, data: Mahasiswa):
    if nim not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan!")
    
    mahasiswa_db[nim] = data.dict()
    return {
        "message": "Data mahasiswa berhasil diperbarui",
        "data": mahasiswa_db[nim]
    }

# DELETE (DELETE)
@app.delete("/mahasiswa/{nim}", summary="Hapus Data Mahasiswa")
async def delete_mahasiswa(nim: int):
    if nim not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan!")
    
    deleted_data = mahasiswa_db.pop(nim)
    return {
        "message": "Data mahasiswa berhasil dihapus",
        "deleted_data": deleted_data
    }